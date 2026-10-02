"""Capstone Modul 6 (v2) — Jalur C: arXiv / literatur + ringkasan kuantitatif.

Alur: ambil paper (paginasi + jeda + error handling) -> DataFrame -> cleaning ->
analisis (per tahun, kata judul, penulis teratas) -> visualisasi -> insight.

Sumber data:
    python src/main.py                # live ke API arXiv; jika gagal, pakai sampel fiktif
    python src/main.py --offline      # langsung pakai data sampel fiktif (tanpa internet)

PENTING: bila API tidak dapat dijangkau, program memakai data/raw/arxiv_sample.xml
yang FIKTIF (lihat src/buat_sampel.py). Hasil dari sampel hanya demonstrasi pipeline,
bukan temuan tentang literatur sebenarnya; insight.txt akan memuat peringatan itu.
"""
import argparse
import re
import time
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import feedparser
import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROC_DIR = BASE_DIR / "data" / "processed"
FIG_DIR = BASE_DIR / "figures"
OUT_DIR = BASE_DIR / "output"
SAMPEL = RAW_DIR / "arxiv_sample.xml"

API = "http://export.arxiv.org/api/query"
QUERY = 'all:"deep learning" AND all:education'
PER_HALAMAN = 10
JUMLAH_HALAMAN = 3          # total 30 paper (>= 20 sesuai scope minimum)
JEDA_DETIK = 3              # hormati server arXiv

PERTANYAAN = [
    "1. Bagaimana jumlah paper bertopik deep learning + education berkembang dari tahun ke tahun?",
    "2. Kata/topik apa yang paling sering muncul di judul?",
    "3. Siapa penulis yang paling sering muncul dan seberapa terkonsentrasi penulisnya?",
]
STOP = {"the", "a", "an", "of", "and", "for", "in", "on", "to", "with", "from", "using", "via", "by", "at"}
sns.set_theme(style="whitegrid")


# --------------------------------------------------------------------------
# 1. Ambil data
# --------------------------------------------------------------------------
def fetch_halaman(query, start, n, timeout=20):
    """Ambil satu halaman dari API arXiv; kembalikan teks Atom, atau None jika gagal."""
    params = {"search_query": query, "start": start, "max_results": n,
              "sortBy": "submittedDate", "sortOrder": "descending"}
    try:
        r = requests.get(API, params=params, timeout=timeout)
        r.raise_for_status()
        return r.text
    except requests.exceptions.RequestException as err:
        print(f"  ! halaman start={start} gagal: {type(err).__name__}")
        return None


def parse_feed(teks):
    """Ubah teks Atom menjadi list dict metadata paper."""
    feed = feedparser.parse(teks)
    baris = []
    for e in feed.entries:
        terbit = e.get("published", "")[:10]
        baris.append({
            "title": " ".join(e.title.split()),
            "authors": "; ".join(a.name for a in e.get("authors", [])),
            "published": terbit,
            "link": e.get("link", ""),
        })
    return baris


def ambil_live():
    """Ambil JUMLAH_HALAMAN halaman dengan jeda; simpan XML mentah tiap halaman."""
    semua = []
    for i in range(JUMLAH_HALAMAN):
        print(f"Mengambil halaman {i + 1}/{JUMLAH_HALAMAN} ...")
        teks = fetch_halaman(QUERY, i * PER_HALAMAN, PER_HALAMAN)
        if teks is None:
            return None            # gagal -> biarkan pemanggil memakai cadangan
        RAW_DIR.mkdir(parents=True, exist_ok=True)
        (RAW_DIR / f"arxiv_halaman_{i + 1}.xml").write_text(teks, encoding="utf-8")
        semua.extend(parse_feed(teks))
        if i < JUMLAH_HALAMAN - 1:
            time.sleep(JEDA_DETIK)
    return semua


def ambil_sampel():
    """Baca data sampel fiktif; potong sesuai ukuran halaman agar sama dengan mode live."""
    baris = parse_feed(SAMPEL.read_text(encoding="utf-8"))
    return baris[: PER_HALAMAN * JUMLAH_HALAMAN]


def muat_data(offline):
    """Kembalikan (DataFrame, sumber) dengan sumber 'arXiv (live)' atau 'sampel fiktif'."""
    if not offline:
        data = ambil_live()
        if data:
            return pd.DataFrame(data), "arXiv (live)"
        print("API arXiv tidak dapat dijangkau -> memakai DATA SAMPEL FIKTIF.")
    return pd.DataFrame(ambil_sampel()), "sampel fiktif"


# --------------------------------------------------------------------------
# 2. Cleaning, analisis
# --------------------------------------------------------------------------
def cleaning(df):
    """Bersihkan metadata; kembalikan (df, catatan)."""
    catatan = [f"Data awal: {len(df)} baris."]
    df = df.copy()
    n_dup = int(df.duplicated(subset=["title"]).sum())
    df = df.drop_duplicates(subset=["title"])
    catatan.append(f"{n_dup} judul duplikat dibuang.")
    df["published"] = pd.to_datetime(df["published"], errors="coerce")
    n_bad = int(df["published"].isna().sum())
    df = df.dropna(subset=["published"])
    catatan.append(f"{n_bad} baris tanpa tanggal valid dibuang.")
    df["tahun"] = df["published"].dt.year
    df["n_penulis"] = df["authors"].str.count(";") + 1
    return df.reset_index(drop=True), catatan


def kata_judul(df, n=12):
    """Frekuensi kata judul (huruf, >= 3 karakter, tanpa stopword)."""
    hitung = Counter()
    for judul in df["title"]:
        for w in re.findall(r"[a-zA-Z]{3,}", judul.lower()):
            if w not in STOP:
                hitung[w] += 1
    return hitung.most_common(n)


def penulis_teratas(df, n=8):
    """Penulis dengan jumlah kemunculan terbanyak."""
    hitung = Counter(a.strip() for s in df["authors"] for a in s.split(";") if a.strip())
    return hitung.most_common(n)


def analisis(df):
    """Hitung ringkasan kuantitatif."""
    return {
        "per_tahun": df.groupby("tahun").size().rename("jumlah_paper"),
        "kata": kata_judul(df),
        "penulis": penulis_teratas(df),
        "rata_penulis": df["n_penulis"].mean(),
        "rentang": (df["published"].min().date(), df["published"].max().date()),
    }


# --------------------------------------------------------------------------
# 3. Visualisasi
# --------------------------------------------------------------------------
def visualisasi(hasil, sumber):
    """Simpan 3 figure: paper per tahun, kata judul, penulis teratas."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    cat = " (data sampel fiktif)" if sumber == "sampel fiktif" else ""

    fig, ax = plt.subplots(figsize=(8, 4.5))
    pt = hasil["per_tahun"]
    ax.bar(pt.index.astype(str), pt.values, color="steelblue")
    for i, v in enumerate(pt.values):
        ax.text(i, v + 0.1, str(v), ha="center")
    ax.set_title("Jumlah paper per tahun" + cat)
    ax.set_xlabel("Tahun terbit"); ax.set_ylabel("Jumlah paper")
    fig.tight_layout(); fig.savefig(FIG_DIR / "01_paper_per_tahun.png", dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    kata, n = zip(*hasil["kata"])
    ax.barh(list(kata)[::-1], list(n)[::-1], color="seagreen")
    ax.set_title("Kata paling sering di judul" + cat)
    ax.set_xlabel("Jumlah kemunculan")
    fig.tight_layout(); fig.savefig(FIG_DIR / "02_kata_judul.png", dpi=150); plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    nama, n = zip(*hasil["penulis"])
    ax.barh(list(nama)[::-1], list(n)[::-1], color="darkorange")
    ax.set_title("Penulis dengan paper terbanyak" + cat)
    ax.set_xlabel("Jumlah paper")
    fig.tight_layout(); fig.savefig(FIG_DIR / "03_penulis_teratas.png", dpi=150); plt.close(fig)


# --------------------------------------------------------------------------
# 4. Insight + simpan
# --------------------------------------------------------------------------
def tulis_insight(df, hasil, sumber):
    """Susun insight (>= 5 poin) + batasan; tulis ke output/insight.txt."""
    pt = hasil["per_tahun"]
    tahun_max = pt.idxmax()
    kata = dict(hasil["kata"])
    (k1, n1), (k2, n2) = hasil["kata"][0], hasil["kata"][1]
    pen = hasil["penulis"]
    total_penulis = sum(len(s.split(";")) for s in df["authors"])
    top3 = sum(n for _, n in pen[:3])
    tahun_penuh = pt[pt.index < pt.index.max()]
    naik = (tahun_penuh.iloc[-1] / tahun_penuh.iloc[0]) if len(tahun_penuh) > 1 and tahun_penuh.iloc[0] else float("nan")
    baris = [
        f"1. Korpus: {len(df)} paper, terbit {hasil['rentang'][0]} s.d. {hasil['rentang'][1]}.",
        f"2. Tahun dengan paper terbanyak: {tahun_max} ({int(pt.max())} paper); tahun {tahun_penuh.index[0]} hanya {int(tahun_penuh.iloc[0])}, "
        f"sehingga jumlah pada tahun penuh terakhir ({tahun_penuh.index[-1]}) = {int(tahun_penuh.iloc[-1])} (≈ {naik:.1f}× tahun pertama).",
        f"3. Kata judul paling sering: '{k1}' ({n1}×) dan '{k2}' ({n2}×) — menandakan fokus topik pada kata tersebut.",
        f"4. Rata-rata {hasil['rata_penulis']:.1f} penulis per paper; penulis teratas {pen[0][0]} muncul di {pen[0][1]} paper.",
        f"5. Tiga penulis teratas menyumbang {top3} dari {total_penulis} kemunculan nama penulis ({top3 / total_penulis:.0%}) "
        "— indikasi tingkat konsentrasi penulis pada korpus ini.",
    ]
    batasan = [
        "Hanya metadata (judul, penulis, tanggal) — isi paper tidak dianalisis; kata judul tidak sama dengan topik sebenarnya.",
        "Hasil bergantung pada query: query berbeda akan menghasilkan korpus berbeda (bias query).",
        "Ukuran korpus kecil (30 paper) sehingga pola per tahun dan penulis tidak stabil secara statistik.",
        "Satu nama penulis dapat ditulis berbeda antar paper (tidak ada disambiguasi penulis).",
        "Tanggal 'published' adalah tanggal submit versi pertama, bukan tanggal publikasi jurnal.",
    ]
    kepala = ""
    if sumber == "sampel fiktif":
        kepala = ("PERINGATAN: angka di bawah dihitung dari DATA SAMPEL FIKTIF (data/raw/arxiv_sample.xml), "
                  "bukan hasil pencarian arXiv sebenarnya. Gunakan untuk memahami alur pipeline saja.\n\n")
    teks = kepala + "\n".join(baris) + "\n\nBatasan:\n" + "\n".join(f"- {b}" for b in batasan) + "\n"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "insight.txt").write_text(teks, encoding="utf-8")
    return teks


def simpan(df, hasil):
    """Simpan data bersih dan ringkasan CSV."""
    PROC_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df.assign(published=df["published"].dt.strftime("%Y-%m-%d")).to_csv(PROC_DIR / "paper_bersih.csv", index=False)
    ring = hasil["per_tahun"].reset_index()
    ring["persen"] = (ring["jumlah_paper"] / ring["jumlah_paper"].sum() * 100).round(1)
    ring.to_csv(OUT_DIR / "ringkasan.csv", index=False)
    pd.DataFrame(hasil["kata"], columns=["kata", "jumlah"]).to_csv(OUT_DIR / "kata_judul.csv", index=False)
    pd.DataFrame(hasil["penulis"], columns=["penulis", "jumlah_paper"]).to_csv(OUT_DIR / "penulis_teratas.csv", index=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--offline", action="store_true", help="pakai data sampel fiktif tanpa memanggil API")
    args = parser.parse_args()

    print("PERTANYAAN ANALISIS\n" + "\n".join(PERTANYAAN) + "\n")
    print("=" * 60 + "\n1. PENGAMBILAN DATA\n" + "=" * 60)
    df_mentah, sumber = muat_data(args.offline)
    print(f"Sumber data: {sumber}; {len(df_mentah)} paper mentah")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    df_mentah.to_csv(RAW_DIR / "paper_mentah.csv", index=False)

    print("\n" + "=" * 60 + "\n2. CLEANING\n" + "=" * 60)
    df, catatan = cleaning(df_mentah)
    for c in catatan:
        print("-", c)
    print("Shape bersih:", df.shape)
    print(df[["title", "published", "n_penulis"]].head(5).to_string(index=False))

    print("\n" + "=" * 60 + "\n3. ANALISIS\n" + "=" * 60)
    hasil = analisis(df)
    print("Paper per tahun:\n" + hasil["per_tahun"].to_string())
    print("\nKata judul teratas:", hasil["kata"])
    print("\nPenulis teratas:", hasil["penulis"])

    visualisasi(hasil, sumber)
    simpan(df, hasil)
    teks = tulis_insight(df, hasil, sumber)
    print("\n" + "=" * 60 + "\n4. INSIGHT\n" + "=" * 60)
    print(teks)
    print("Selesai. Lihat data/processed/, figures/, dan output/.")


if __name__ == "__main__":
    main()
