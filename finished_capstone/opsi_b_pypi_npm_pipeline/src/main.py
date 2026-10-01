"""Capstone Opsi B — Pipeline data dari dua API publik: PyPI dan npm.

Pertanyaan: seperti apa ritme rilis library populer Python (PyPI) dibanding
JavaScript (npm)? Pipeline: ambil data (API + cache) -> DataFrame -> cleaning
-> analisis -> visualisasi -> simpan data mentah & bersih -> insight.

Pemakaian:
    python src/main.py             # pakai cache jika masih segar (< 24 jam)
    python src/main.py --refresh   # paksa ambil ulang dari API
"""
import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from packaging.version import InvalidVersion, Version

BASE_DIR = Path(__file__).resolve().parent.parent
CACHE_DIR = BASE_DIR / "data" / "raw" / "cache"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIG_DIR = BASE_DIR / "output" / "figures"
REPORT_DIR = BASE_DIR / "output" / "reports"

PYPI_PACKAGES = ["pandas", "numpy", "matplotlib", "seaborn", "scipy",
                 "requests", "flask", "django", "fastapi", "scikit-learn"]
NPM_PACKAGES = ["react", "vue", "express", "lodash", "axios"]
CACHE_TTL_JAM = 24
HEADERS = {"User-Agent": "capstone-bootcamp/1.0 (contoh edukasi)"}
WARNA = {"PyPI": "#3776ab", "npm": "#cb3837"}
sns.set_theme(style="whitegrid")


# --------------------------------------------------------------------------
# 1. Pengambilan data (generik + caching + error handling)
# --------------------------------------------------------------------------
def ambil_json(url, cache_file, refresh=False, retry=3, timeout=30):
    """Ambil JSON dari URL dengan cache file dan retry.

    Urutan: cache segar -> API (retry, backoff) -> cache lama (fallback) -> None.
    Mengembalikan (data, sumber) dengan sumber 'cache' | 'api' | 'cache-lama'.
    """
    if cache_file.exists() and not refresh:
        umur = time.time() - cache_file.stat().st_mtime
        if umur < CACHE_TTL_JAM * 3600:
            return json.loads(cache_file.read_text(encoding="utf-8")), "cache"

    for percobaan in range(1, retry + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=timeout)
            resp.raise_for_status()
            return resp.json(), "api"
        except (requests.exceptions.RequestException, ValueError) as err:
            print(f"  ! percobaan {percobaan}/{retry} gagal untuk {url}: "
                  f"{type(err).__name__}")
            time.sleep(1.5 * percobaan)

    if cache_file.exists():
        print("  ! API gagal, memakai cache lama.")
        return json.loads(cache_file.read_text(encoding="utf-8")), "cache-lama"
    return None, "gagal"


def _ringkas_pypi(data):
    """Ambil hanya field yang dibutuhkan dari respons PyPI (hemat ruang)."""
    info = data["info"]
    rilis = []
    for versi, files in data["releases"].items():
        if not files:
            continue
        rilis.append({
            "version": versi,
            "upload_time": min(f["upload_time_iso_8601"] for f in files),
            "n_files": len(files),
            "size_bytes": sum(f["size"] for f in files),
            "yanked": any(f.get("yanked") for f in files),
        })
    return {"name": info["name"], "latest": info["version"],
            "summary": info.get("summary"),
            "requires_python": info.get("requires_python"), "releases": rilis}


def _ringkas_npm(data):
    """Ambil hanya field yang dibutuhkan dari respons registry npm."""
    waktu = {v: t for v, t in data["time"].items()
             if v not in ("created", "modified")}
    return {"name": data["name"], "latest": data["dist-tags"]["latest"],
            "summary": data.get("description"),
            "releases": [{"version": v, "upload_time": t} for v, t in waktu.items()]}


def kumpulkan_data(refresh=False):
    """Ambil semua paket dari kedua sumber; kembalikan (list_ringkasan, log)."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    hasil, log = [], []
    sumber = ([("PyPI", p, f"https://pypi.org/pypi/{p}/json", _ringkas_pypi)
               for p in PYPI_PACKAGES]
              + [("npm", p, f"https://registry.npmjs.org/{p}", _ringkas_npm)
                 for p in NPM_PACKAGES])
    for eko, paket, url, ringkas in sumber:
        cache_file = CACHE_DIR / f"{eko.lower()}_{paket}.json"
        mentah, asal = ambil_json(url, cache_file, refresh=refresh)
        if mentah is None:
            print(f"- {eko}/{paket}: GAGAL (dilewati)")
            log.append({"ekosistem": eko, "paket": paket, "asal": "gagal"})
            continue
        if asal == "api":  # simpan versi ringkas sebagai cache
            ringkasan = ringkas(mentah)
            ringkasan["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            cache_file.write_text(json.dumps(ringkasan), encoding="utf-8")
        else:
            ringkasan = mentah  # cache sudah berbentuk ringkas
        ringkasan["ekosistem"] = eko
        hasil.append(ringkasan)
        log.append({"ekosistem": eko, "paket": paket, "asal": asal,
                    "n_rilis_mentah": len(ringkasan["releases"])})
        print(f"- {eko}/{paket}: {len(ringkasan['releases'])} rilis ({asal})")
    return hasil, pd.DataFrame(log)


# --------------------------------------------------------------------------
# 2. DataFrame + cleaning
# --------------------------------------------------------------------------
def _prerelease(versi):
    """True jika versi pre-release (alpha/beta/rc/dev, atau '-' pada semver)."""
    try:
        return Version(versi).is_prerelease
    except InvalidVersion:
        return "-" in versi


def buat_dataframe(ringkasan):
    """Gabungkan data dua sumber menjadi satu DataFrame rilis."""
    baris = []
    for p in ringkasan:
        for r in p["releases"]:
            baris.append({"ekosistem": p["ekosistem"], "paket": p["name"],
                          "version": r["version"], "upload_time": r["upload_time"],
                          "n_files": r.get("n_files"),
                          "size_bytes": r.get("size_bytes"),
                          "yanked": r.get("yanked", False)})
    return pd.DataFrame(baris)


def cleaning(df):
    """Bersihkan DataFrame rilis; kembalikan (df_bersih, catatan)."""
    catatan = [f"Data mentah: {len(df)} baris, {df['paket'].nunique()} paket."]
    df = df.copy()
    df["released_at"] = pd.to_datetime(df["upload_time"], utc=True, errors="coerce")
    n_bad = int(df["released_at"].isna().sum())
    df = df.dropna(subset=["released_at"])
    catatan.append(f"{n_bad} baris tanpa tanggal valid dibuang.")

    n_dup = int(df.duplicated(subset=["paket", "version"]).sum())
    df = df.drop_duplicates(subset=["paket", "version"])
    catatan.append(f"{n_dup} duplikat (paket, versi) dibuang.")

    df["prerelease"] = df["version"].apply(_prerelease)
    df["yanked"] = df["yanked"].fillna(False).astype(bool)
    df["size_mb"] = df["size_bytes"] / 1e6
    df["tahun"] = df["released_at"].dt.year
    catatan.append(
        f"{int(df['prerelease'].sum())} versi pre-release dan "
        f"{int(df['yanked'].sum())} versi yanked ditandai; analisis irama rilis "
        "memakai rilis stabil non-yanked saja."
    )
    df = df.sort_values(["ekosistem", "paket", "released_at"]).reset_index(drop=True)
    stabil = df[~df["prerelease"] & ~df["yanked"]]
    catatan.append(f"Rilis stabil yang dianalisis: {len(stabil)} baris.")
    return df.drop(columns=["upload_time"]), catatan


# --------------------------------------------------------------------------
# 3. Analisis
# --------------------------------------------------------------------------
def analisis(df, ringkasan):
    """Hitung metrik irama rilis per paket dan per ekosistem."""
    stabil = df[~df["prerelease"] & ~df["yanked"]].copy()
    stabil["interval_hari"] = stabil.groupby("paket")["released_at"].diff().dt.total_seconds() / 86400
    acuan = max(pd.Timestamp(p["fetched_at"]) for p in ringkasan if "fetched_at" in p)
    tahun_acuan = acuan.year

    per_paket = stabil.groupby(["ekosistem", "paket"]).agg(
        rilis_stabil=("version", "count"),
        rilis_pertama=("released_at", "min"),
        rilis_terakhir=("released_at", "max"),
        median_interval_hari=("interval_hari", "median"),
        p90_interval_hari=("interval_hari", lambda s: s.quantile(0.9)),
    ).reset_index()
    per_paket["umur_tahun"] = (acuan - per_paket["rilis_pertama"]).dt.days / 365.25
    per_paket["rilis_per_tahun"] = per_paket["rilis_stabil"] / per_paket["umur_tahun"]
    per_paket["hari_sejak_rilis_terakhir"] = (acuan - per_paket["rilis_terakhir"]).dt.days
    versi_terbaru = {p["name"]: p["latest"] for p in ringkasan}
    per_paket["versi_terbaru"] = per_paket["paket"].map(versi_terbaru)
    per_paket = per_paket.sort_values("rilis_per_tahun", ascending=False)

    per_tahun = (stabil.pivot_table(index="paket", columns="tahun", values="version",
                                    aggfunc="count", fill_value=0))
    per_eko = stabil.groupby("ekosistem").agg(
        paket=("paket", "nunique"), rilis_stabil=("version", "count"),
        median_interval_hari=("interval_hari", "median"))
    per_eko["rilis_per_paket_per_tahun"] = per_paket.groupby("ekosistem")["rilis_per_tahun"].median()

    pre = df.groupby("ekosistem")["prerelease"].mean().rename("persen_prerelease")
    pypi_ukuran = (df[(df["ekosistem"] == "PyPI") & ~df["prerelease"]]
                   .groupby(["paket", "tahun"])["size_mb"].median().reset_index())
    return {"stabil": stabil, "per_paket": per_paket, "per_tahun": per_tahun,
            "per_eko": per_eko, "pre": pre, "pypi_ukuran": pypi_ukuran,
            "acuan": acuan, "tahun_acuan": tahun_acuan}


# --------------------------------------------------------------------------
# 4. Visualisasi
# --------------------------------------------------------------------------
def _simpan(fig, nama):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{nama}.png", dpi=150, bbox_inches="tight")
    plt.close(fig)


def visualisasi(hasil):
    """Buat 5 grafik: jumlah rilis, interval, heatmap tahunan, kumulatif, ukuran."""
    pp = hasil["per_paket"]

    fig, ax = plt.subplots(figsize=(9, 6))
    d = pp.sort_values("rilis_stabil")
    ax.barh(d["paket"], d["rilis_stabil"], color=d["ekosistem"].map(WARNA))
    ax.set_title("Jumlah rilis stabil sepanjang sejarah paket")
    ax.set_xlabel("Jumlah rilis stabil")
    for i, v in enumerate(d["rilis_stabil"]):
        ax.text(v + 2, i, str(v), va="center", fontsize=9)
    ax.legend(handles=[plt.Rectangle((0, 0), 1, 1, color=c) for c in WARNA.values()],
              labels=list(WARNA), loc="lower right")
    _simpan(fig, "01_jumlah_rilis_per_paket")

    fig, ax = plt.subplots(figsize=(9, 6))
    d = pp.sort_values("median_interval_hari")
    ax.barh(d["paket"], d["median_interval_hari"], color=d["ekosistem"].map(WARNA))
    ax.set_title("Median jarak antar rilis stabil (hari)")
    ax.set_xlabel("Hari (lebih kecil = rilis lebih sering)")
    for i, v in enumerate(d["median_interval_hari"]):
        ax.text(v + 0.3, i, f"{v:.1f}", va="center", fontsize=9)
    _simpan(fig, "02_median_interval_rilis")

    fig, ax = plt.subplots(figsize=(11, 6))
    pt = hasil["per_tahun"]
    pt = pt.loc[pp["paket"]]  # urut sesuai rilis per tahun
    sns.heatmap(pt, annot=True, fmt="d", cmap="YlGnBu", cbar_kws={"label": "rilis stabil"}, ax=ax)
    ax.set_title("Rilis stabil per paket per tahun"); ax.set_xlabel("Tahun"); ax.set_ylabel("")
    _simpan(fig, "03_heatmap_rilis_per_tahun")

    fig, ax = plt.subplots(figsize=(10, 6))
    st = hasil["stabil"].copy()
    st["kumulatif"] = st.groupby("paket").cumcount() + 1
    for eko, grup in st.groupby("ekosistem"):
        for paket, g in grup.groupby("paket"):
            ax.plot(g["released_at"], g["kumulatif"], color=WARNA[eko], alpha=0.75,
                    linestyle="-" if eko == "PyPI" else "--", label=f"{paket}")
            ax.annotate(paket, (g["released_at"].iloc[-1], g["kumulatif"].iloc[-1]),
                        fontsize=8, xytext=(3, 0), textcoords="offset points")
    ax.set_title("Akumulasi rilis stabil dari waktu ke waktu (biru = PyPI, merah = npm)")
    ax.set_xlabel("Tanggal"); ax.set_ylabel("Jumlah rilis stabil kumulatif")
    _simpan(fig, "04_kumulatif_rilis")

    fig, ax = plt.subplots(figsize=(10, 6))
    uk = hasil["pypi_ukuran"]
    sns.lineplot(data=uk, x="tahun", y="size_mb", hue="paket", marker="o", ax=ax)
    ax.set_yscale("log")
    ax.set_title("Median ukuran distribusi per rilis (PyPI, skala log)")
    ax.set_xlabel("Tahun rilis"); ax.set_ylabel("Ukuran total file per rilis (MB, log)")
    ax.legend(bbox_to_anchor=(1.01, 1), loc="upper left", fontsize=8)
    _simpan(fig, "05_ukuran_distribusi_pypi")


# --------------------------------------------------------------------------
# 5. Insight + simpan
# --------------------------------------------------------------------------
def tulis_insight(hasil, df):
    """Susun insight dari angka hasil analisis."""
    pp = hasil["per_paket"].set_index("paket")
    eko = hasil["per_eko"]
    pt = hasil["per_tahun"]
    teraktif = pp["rilis_per_tahun"].idxmax()
    terjarang = pp["rilis_per_tahun"].idxmin()
    tercepat = pp["median_interval_hari"].idxmin()
    terlama = pp["median_interval_hari"].idxmax()
    terbanyak = pp["rilis_stabil"].idxmax()
    pandas_n = pp.loc["pandas", "rilis_stabil"]
    py_med = eko.loc["PyPI", "rilis_per_paket_per_tahun"]
    js_med = eko.loc["npm", "rilis_per_paket_per_tahun"]
    pre = hasil["pre"]
    tahun_penuh = hasil["tahun_acuan"] - 1
    puncak_tahun = pt.sum().idxmax()
    basi = pp["hari_sejak_rilis_terakhir"].sort_values(ascending=False)
    uk = hasil["pypi_ukuran"]
    uk_np = uk[uk["paket"] == "numpy"].set_index("tahun")["size_mb"]

    cepat_hari = hasil["stabil"].loc[hasil["stabil"]["paket"] == tercepat, "interval_hari"]
    persen_serentak = (cepat_hari < 1).mean()
    pre_paket = df.groupby("paket")["prerelease"].mean().sort_values(ascending=False)
    pre_top = pre_paket.index[0]
    pre_top_df = df[(df["paket"] == pre_top) & df["prerelease"]]
    persen_build = pre_top_df["version"].str.contains("canary|experimental|nightly|dev").mean()
    tahun_max = int(uk_np.index.max())
    files_np = df[(df["paket"] == "numpy") & ~df["prerelease"]].groupby("tahun")["n_files"].median()

    baris = [
        f"1. **{terbanyak} punya rilis stabil terbanyak ({pp.loc[terbanyak, 'rilis_stabil']}), "
        f"tetapi {teraktif} paling aktif per tahun** ({pp.loc[teraktif, 'rilis_per_tahun']:.1f} "
        f"rilis/tahun) sedangkan {terjarang} paling jarang ({pp.loc[terjarang, 'rilis_per_tahun']:.1f}/tahun). "
        f"Jumlah total dipengaruhi umur paket, sehingga rilis per tahun lebih adil untuk membandingkan.",
        f"2. **Jarak antar rilis sangat bervariasi.** Median tercepat: {tercepat} "
        f"({pp.loc[tercepat, 'median_interval_hari']:.1f} hari), terlama: {terlama} "
        f"({pp.loc[terlama, 'median_interval_hari']:.1f} hari). "
        f"Untuk {tercepat}, {persen_serentak:.0%} interval antar rilis kurang dari 1 hari karena beberapa cabang "
        f"dukungan dirilis bersamaan (rilis keamanan), sehingga mediannya mendekati nol. "
        f"Pandas memiliki {pandas_n} rilis stabil dengan median {pp.loc['pandas', 'median_interval_hari']:.1f} hari.",
        f"3. **Perbandingan ekosistem:** median rilis per paket per tahun di PyPI = {py_med:.1f} "
        f"vs npm = {js_med:.1f}; median jarak antar rilis PyPI = "
        f"{eko.loc['PyPI', 'median_interval_hari']:.1f} hari vs npm = {eko.loc['npm', 'median_interval_hari']:.1f} hari "
        f"(sampel hanya {int(eko.loc['PyPI','paket'])} paket PyPI dan {int(eko.loc['npm','paket'])} paket npm, "
        f"jadi bukan generalisasi ekosistem).",
        f"4. **Tahun {puncak_tahun} adalah tahun dengan rilis stabil terbanyak** "
        f"({int(pt.sum()[puncak_tahun])} rilis dari seluruh paket yang dipantau; "
        f"{pt[puncak_tahun].idxmax()} sendiri menyumbang {int(pt[puncak_tahun].max())}); "
        f"pada tahun penuh terakhir ({tahun_penuh}) total rilis = {int(pt.sum().get(tahun_penuh, 0))}.",
        f"5. **Proporsi pre-release berbeda jauh:** PyPI {pre['PyPI']:.1%} vs npm {pre['npm']:.1%} dari "
        f"seluruh versi terdaftar. Angka npm didominasi {pre_top}: {pre_paket[pre_top]:.0%} versinya "
        f"pre-release ({len(pre_top_df)} versi, {persen_build:.0%} di antaranya build "
        f"canary/experimental/nightly/dev).",
        f"6. **Paket dengan rilis terakhir paling lama:** {basi.index[0]} "
        f"({int(basi.iloc[0])} hari sebelum tanggal pengambilan data), "
        f"sedangkan paling baru: {basi.index[-1]} ({int(basi.iloc[-1])} hari).",
    ]
    if 2015 in uk_np.index and uk_np.index.max() > 2015:
        baris.append(
            f"7. **Ukuran distribusi NumPy** (median per rilis) berubah dari {uk_np[2015]:.2f} MB (2015) "
            f"menjadi {uk_np.iloc[-1]:.2f} MB ({tahun_max}); median jumlah file per rilis naik dari "
            f"{files_np[2015]:.0f} menjadi {files_np[tahun_max]:.0f} (makin banyak wheel per platform/versi Python)."
        )
    return "\n\n".join(baris) + "\n"


def simpan(df_mentah, df, hasil, catatan, log, insight):
    """Simpan data mentah, data bersih, ringkasan, Excel, dan insight."""
    for d in (PROCESSED_DIR, REPORT_DIR):
        d.mkdir(parents=True, exist_ok=True)
    df_mentah.to_csv(BASE_DIR / "data" / "raw" / "rilis_mentah.csv", index=False)
    df_simpan = df.copy()  # format waktu seragam agar mudah dibaca ulang pd.read_csv
    df_simpan["released_at"] = df_simpan["released_at"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    df_simpan.to_csv(PROCESSED_DIR / "rilis_bersih.csv", index=False)
    pp = hasil["per_paket"].copy()
    for k in ("rilis_pertama", "rilis_terakhir"):
        pp[k] = pp[k].dt.strftime("%Y-%m-%d")
    pp.round(2).to_csv(REPORT_DIR / "ringkasan_per_paket.csv", index=False)
    with pd.ExcelWriter(REPORT_DIR / "laporan_rilis.xlsx") as xl:
        pp.round(2).to_excel(xl, sheet_name="Per paket", index=False)
        hasil["per_tahun"].to_excel(xl, sheet_name="Rilis per tahun")
        hasil["per_eko"].round(2).to_excel(xl, sheet_name="Per ekosistem")
        log.to_excel(xl, sheet_name="Log pengambilan", index=False)
        pd.DataFrame({"catatan_cleaning": catatan}).to_excel(xl, sheet_name="Catatan cleaning", index=False)
    (REPORT_DIR / "insights.md").write_text("# Insight — Pipeline PyPI & npm\n\n" + insight, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--refresh", action="store_true", help="abaikan cache, ambil ulang dari API")
    args = parser.parse_args()

    print("=" * 60 + "\n1. PENGAMBILAN DATA\n" + "=" * 60)
    ringkasan, log = kumpulkan_data(refresh=args.refresh)
    if not ringkasan:
        raise SystemExit("Tidak ada data yang berhasil diambil dan tidak ada cache.")

    print("\n" + "=" * 60 + "\n2. CLEANING\n" + "=" * 60)
    df_mentah = buat_dataframe(ringkasan)
    print("Shape mentah:", df_mentah.shape)
    df, catatan = cleaning(df_mentah)
    for c in catatan:
        print("-", c)
    print("Shape bersih:", df.shape)

    print("\n" + "=" * 60 + "\n3. ANALISIS\n" + "=" * 60)
    hasil = analisis(df, ringkasan)
    print("Tanggal acuan (waktu pengambilan data):", hasil["acuan"].date())
    kolom = ["ekosistem", "paket", "rilis_stabil", "median_interval_hari",
             "rilis_per_tahun", "hari_sejak_rilis_terakhir", "versi_terbaru"]
    print(hasil["per_paket"][kolom].round(2).to_string(index=False))
    print("\nPer ekosistem:")
    print(hasil["per_eko"].round(2).to_string())
    print("\nProporsi pre-release:")
    print(hasil["pre"].round(3).to_string())

    visualisasi(hasil)
    insight = tulis_insight(hasil, df)
    simpan(df_mentah, df, hasil, catatan, log, insight)
    print("\n" + "=" * 60 + "\n4. INSIGHT\n" + "=" * 60)
    print(insight)
    print("Selesai. Lihat data/processed/ dan output/.")


if __name__ == "__main__":
    main()
