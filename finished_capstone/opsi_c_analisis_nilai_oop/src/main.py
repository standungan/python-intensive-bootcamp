"""Capstone Opsi C — aplikasi analisis nilai akademik berbasis OOP.

Mode:
    python src/main.py              # pipeline otomatis (default)
    python src/main.py --interaktif # menu terminal (input dari keyboard)
"""
import argparse
import sys
from pathlib import Path

import pandas as pd

from analisis_nilai import MATKUL, AnalisisNilai, DataTidakValidError
from generate_data import buat_data

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_CSV = BASE_DIR / "data" / "raw" / "nilai_mahasiswa.csv"
OUT_DIR = BASE_DIR / "output"
STATE = BASE_DIR / "data" / "processed" / "state_aplikasi.json"
pd.set_option("display.width", 110)
pd.set_option("display.max_columns", 20)


def siapkan_data():
    """Buat data sintetis jika file mentah belum ada."""
    if not RAW_CSV.exists():
        RAW_CSV.parent.mkdir(parents=True, exist_ok=True)
        buat_data().to_csv(RAW_CSV, index=False)
        print(f"Data sintetis dibuat: {RAW_CSV.name}")


def pipeline():
    """Jalankan seluruh fitur secara otomatis dan simpan semua output."""
    siapkan_data()
    app = AnalisisNilai(RAW_CSV)
    print(app, "\n")
    print("=" * 60 + "\n1. STATISTIK\n" + "=" * 60)
    print(app.statistik().to_string())
    print("\nRata-rata per prodi:")
    print(app.statistik_per_prodi().to_string())
    print("\nSebaran predikat:")
    print(app.df["predikat"].value_counts().reindex(["A", "B", "C", "D"], fill_value=0).to_string())

    print("\n" + "=" * 60 + "\n2. FILTER\n" + "=" * 60)
    f1 = app.filter(prodi="Teknik Elektro", min_rata=80)
    print(f"Teknik Elektro dengan rata-rata >= 80: {len(f1)} mahasiswa")
    f2 = app.filter(predikat="A")
    print(f"Predikat A di seluruh prodi: {len(f2)} mahasiswa")
    print(f"Kelas B Sistem Informasi: {len(app.filter(prodi='Sistem Informasi', kelas='B'))} mahasiswa")

    print("\n" + "=" * 60 + "\n3. RANKING\n" + "=" * 60)
    print("Top 10 keseluruhan:")
    print(app.ranking(10).to_string())
    print("\nTop 3 per prodi:")
    for prodi in sorted(app.df["prodi"].unique()):
        print(f"\n{prodi}")
        print(app.ranking(3, prodi=prodi).to_string())

    print("\n" + "=" * 60 + "\n4. BANDINGKAN PRODI (Welch t-test)\n" + "=" * 60)
    banding = app.bandingkan_prodi("Informatika", "Teknik Elektro")
    print(banding.to_string(float_format=lambda x: f"{x:.4g}"))
    banding.to_csv(OUT_DIR / "reports" / "perbandingan_if_vs_te.csv")

    print("\n" + "=" * 60 + "\n5. VISUALISASI & EXPORT\n" + "=" * 60)
    file_gambar = app.visualisasi(OUT_DIR / "figures")
    print("Grafik:", ", ".join(file_gambar))
    app.export(OUT_DIR / "reports" / "laporan_nilai.csv", OUT_DIR / "reports" / "laporan_nilai.xlsx")
    app.df.to_csv(BASE_DIR / "data" / "processed" / "nilai_dengan_rata_rata.csv", index=False)
    print("Laporan CSV & Excel (5 sheet) disimpan di output/reports/")

    tulis_insight(app, banding)

    print("\n" + "=" * 60 + "\n7. TAMBAH DATA (dengan validasi)\n" + "=" * 60)
    nim = app.tambah_mahasiswa("Rina Kartika", "Informatika", "a",
                               dict(zip(MATKUL, [90, 85, 80, 88, 92])))
    print("Mahasiswa baru ditambahkan dengan NIM", nim)
    try:
        app.tambah_mahasiswa("Salah Input", "Informatika", "A",
                             dict(zip(MATKUL, [90, 85, 80, 88, 120])))
    except DataTidakValidError as err:
        print("Input ditolak:", err)

    print("\n" + "=" * 60 + "\n8. SIMPAN & MUAT STATE\n" + "=" * 60)
    app.simpan_state(STATE)
    app2 = AnalisisNilai.muat_state(STATE)
    sama = app2.df[["nim", "rata_rata"]].equals(app.df[["nim", "rata_rata"]])
    print(f"State disimpan ke {STATE.name}; dimuat ulang: {app2}; data identik: {sama}")



def tulis_insight(app, banding):
    """Hitung insight dari data dan simpan ke output/reports/insights.md."""
    df = app.df
    pp = app.statistik_per_prodi()
    terbaik_prodi = pp["rata_rata"].idxmax()
    korelasi = df[MATKUL].corr()
    pasangan = korelasi.where(~(korelasi.values == 1)).stack()
    kuat = pasangan.idxmax()
    lemah = pasangan.idxmin()
    sd = df[MATKUL].std()
    pred = df["predikat"].value_counts(normalize=True)
    unggul = {prodi: pp.loc[prodi, MATKUL].idxmax() for prodi in pp.index}
    sig = banding[banding["signifikan_5%"]].index.tolist()
    baris = [
        f"1. **Program studi dengan rata-rata tertinggi: {terbaik_prodi}** "
        f"({pp.loc[terbaik_prodi, 'rata_rata']:.2f}); selisih rata-rata antar prodi hanya "
        f"{pp['rata_rata'].max() - pp['rata_rata'].min():.2f} poin, sehingga perbedaan lebih terlihat "
        f"pada mata kuliah daripada rata-rata keseluruhan.",
        "2. **Setiap prodi unggul pada mata kuliah berbeda:** "
        + "; ".join(f"{p} → {m}" for p, m in unggul.items()) + ".",
        f"3. **Perbandingan Informatika vs Teknik Elektro (Welch t-test, alpha 5%):** "
        f"mata kuliah dengan beda signifikan: {', '.join(sig) if sig else 'tidak ada'}. "
        f"Selisih terbesar pada {banding['selisih'].abs().drop('rata_rata').idxmax()} "
        f"({banding.loc[banding['selisih'].abs().drop('rata_rata').idxmax(), 'selisih']:+.1f} poin).",
        f"4. **Semua korelasi antar mata kuliah positif** (r antara {pasangan[lemah]:.2f} dan "
        f"{pasangan[kuat]:.2f}): terkuat {kuat[0]}–{kuat[1]}, terlemah {lemah[0]}–{lemah[1]}; "
        f"mahasiswa yang kuat di satu mata kuliah cenderung kuat di lainnya (kemampuan umum).",
        f"5. **Mata kuliah paling bervariasi: {sd.idxmax()}** (SD {sd.max():.1f}); "
        f"paling seragam: {sd.idxmin()} (SD {sd.min():.1f}).",
        f"6. **Sebaran predikat:** A {pred.get('A', 0):.1%}, B {pred.get('B', 0):.1%}, "
        f"C {pred.get('C', 0):.1%}, D {pred.get('D', 0):.1%}.",
    ]
    teks = "# Insight — Analisis Nilai Mahasiswa\n\n" + "\n\n".join(baris) + "\n"
    (OUT_DIR / "reports").mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "reports" / "insights.md").write_text(teks, encoding="utf-8")
    print("\n" + "=" * 60 + "\n6. INSIGHT\n" + "=" * 60)
    print("\n\n".join(baris))


def tanya(prompt):
    """input() yang ikut menampilkan jawaban bila stdin bukan terminal (mis. demo/log)."""
    jawaban = input(prompt)
    if not sys.stdin.isatty():
        print(jawaban)
    return jawaban


def interaktif():
    """Menu terminal sederhana untuk mencoba fitur secara interaktif."""
    siapkan_data()
    app = AnalisisNilai.muat_state(STATE) if STATE.exists() else AnalisisNilai(RAW_CSV)
    menu = ("\n=== ANALISIS NILAI ===\n1. Statistik\n2. Ranking top 5\n3. Filter by prodi\n"
            "4. Tambah mahasiswa\n5. Simpan & keluar")
    while True:
        print(menu)
        try:
            pilih = tanya("Pilih (1-5): ").strip()
        except EOFError:
            print("\nInput habis, keluar.")
            break
        if pilih == "1":
            print(app.statistik_per_prodi().to_string())
        elif pilih == "2":
            print(app.ranking(5).to_string())
        elif pilih == "3":
            prodi = tanya("Nama prodi: ").strip()
            hasil = app.filter(prodi=prodi)
            print(f"{len(hasil)} mahasiswa ditemukan.")
            if len(hasil):
                print(hasil[["nim", "nama", "rata_rata", "predikat"]].head(5).to_string(index=False))
        elif pilih == "4":
            try:
                nama = tanya("Nama: ")
                prodi = tanya("Prodi: ")
                kelas = tanya("Kelas (A/B): ")
                nilai = {mk: float(tanya(f"  nilai {mk}: ")) for mk in MATKUL}
                print("Ditambahkan dengan NIM", app.tambah_mahasiswa(nama, prodi, kelas, nilai))
            except (ValueError, DataTidakValidError) as err:
                print("Gagal:", err)
        elif pilih == "5":
            app.simpan_state(STATE)
            print("State disimpan. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak dikenal.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--interaktif", action="store_true", help="jalankan mode menu terminal")
    args = parser.parse_args()
    interaktif() if args.interaktif else pipeline()
