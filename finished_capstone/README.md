# finished_capstone — Contoh Capstone Project Lengkap

Tiga contoh pengerjaan Capstone (Hari 6) yang lengkap: kode, data, output (grafik, laporan, log eksekusi), insight, README, dan dokumentasi sesuai template pada materi.

| Opsi | Folder | Topik | Data | Highlight |
|---|---|---|---|---|
| A | [opsi_a_titanic_eda](opsi_a_titanic_eda/) | EDA dataset Titanic | Nyata (seaborn-data) | Cleaning terdokumentasi, uji chi-square/Mann-Whitney, dashboard 2x3, Excel multi-sheet |
| B | [opsi_b_pypi_npm_pipeline](opsi_b_pypi_npm_pipeline/) | Ritme rilis library PyPI vs npm | Nyata, diambil live dari API PyPI & npm (2026-10-01) | Fungsi generik + cache + retry + fallback, dua sumber digabung |
| C | [opsi_c_analisis_nilai_oop](opsi_c_analisis_nilai_oop/) | Aplikasi analisis nilai berbasis OOP | Sintetis (fiktif, seed tetap) | Kelas `AnalisisNilai`, validasi, 7 unit test, mode interaktif, simpan/muat state |

Setiap folder berisi:

```text
README.md  DOCUMENTATION.md  requirements.txt
src/       kode sumber (function/class, docstring, error handling)
data/      raw/ dan processed/
output/    figures/ (PNG, dashboard) dan reports/ (CSV, Excel, insights.md, run_log.txt)
```

## Menjalankan ulang
```bash
cd opsi_a_titanic_eda        && pip install -r requirements.txt && python src/main.py
cd ../opsi_b_pypi_npm_pipeline && pip install -r requirements.txt && python src/main.py
cd ../opsi_c_analisis_nilai_oop && pip install -r requirements.txt && python src/main.py
```

## Catatan
- Insight pada tiap proyek dihitung otomatis oleh kode dari data (bukan diketik manual), lalu disalin ke README/DOKUMENTASI.
- Opsi B bergantung pada API publik; hasil dapat sedikit berbeda jika dijalankan ulang di waktu lain (`--refresh`). Data yang dipakai pada contoh ini disimpan di `data/raw/cache/`.
- Opsi C memakai data fiktif; temuannya menggambarkan cara kerja aplikasi, bukan kondisi akademik nyata.
