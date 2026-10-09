# Contoh Capstone — Modul 6

Empat contoh pengerjaan lengkap untuk empat jalur Capstone pada [Modul 6](../materi/modul06-capstone-project.md). Setiap contoh berisi kode, data, output (grafik dan laporan), insight, dan dokumentasi mengikuti template modul — dirancang sebagai **bahan belajar**: baca, jalankan, ubah, lalu kerjakan versi Anda sendiri.

| Jalur | Folder | Data | Level | Catatan |
|---|---|---|---|---|
| A — EDA dataset publik | [jalur_a_eda_titanic](jalur_a_eda_titanic/) | Nyata (Titanic, seaborn-data) | Menengah | 6 figure + dashboard, uji chi-square/Mann-Whitney, Excel multi-sheet |
| B — API → analisis → visualisasi | [jalur_b_api_pypi_npm](jalur_b_api_pypi_npm/) | Nyata, live dari API PyPI & npm (2026-10-02) | Menengah–tinggi | Cache + retry + fallback, dua sumber digabung |
| C — arXiv / literatur | [jalur_c_arxiv](jalur_c_arxiv/) | **Sampel FIKTIF** (API arXiv diblokir di lingkungan pembuatan) | Menengah–tinggi | Mode live tersedia; hasil nyata perlu dijalankan dengan internet |
| D — Aplikasi analisis nilai (OOP) | [jalur_d_analisis_nilai_oop](jalur_d_analisis_nilai_oop/) | Sintetis (fiktif, seed tetap) | Tinggi | Class `AnalisisNilai`, 7 unit test, mode interaktif, simpan/muat state |

> Contoh versi 1 (Opsi A Titanic dan Opsi B PyPI/npm) identik dengan Jalur A dan B — kode, data, dan grafiknya sama — sehingga digabung menjadi satu. Opsi C versi 1 menjadi Jalur D.

## Alur belajar yang disarankan

1. **Baca modul** — [Modul 6](../materi/modul06-capstone-project.md): pertanyaan analisis, struktur folder, template dokumentasi.
2. **Buka README contoh** — lihat bagaimana pertanyaan, metode, hasil, dan batasan ditulis.
3. **Jalankan** `src/main.py`, lalu bandingkan dengan `output/run_log.txt`.
4. **Baca kode** mengikuti urutan pada bagian *Bahan belajar* di tiap README.
5. **Kerjakan latihan lanjutan** (3 tantangan per jalur), lalu buat capstone Anda sendiri dengan [buku kerja Hari 6](../workbook/hari6-capstone-project.ipynb).

## Pemeriksaan terhadap "Scope minimum" Modul 6

| Syarat | A | B | C | D |
|---|---|---|---|---|
| Pertanyaan analisis tertulis | ✓ 3 | ✓ 3 | ✓ 3 | ✓ (di DOKUMENTASI, tidak bernomor) |
| Cleaning terdokumentasi + CSV bersih | ✓ `data_bersih.csv` | ✓ `rilis_bersih.csv` | ✓ `paper_bersih.csv` | ✓ `nilai_dengan_rata_rata.csv` |
| Minimal 3 groupby/agregasi berbeda | ✓ 6 groupby + pivot | ✓ | ✓ per tahun, kata, penulis | ✓ per prodi, ranking, perbandingan |
| Figure minimal | ✓ 6 (min. 4) | ✓ 5 (min. 3) | ✓ 3 (min. 2–3) | ✓ 6 + dashboard (min. 4) |
| Insight + batasan | ✓ 6 + 6 batasan | ✓ 7 + 5 batasan | ✓ 5 + 6 batasan | ✓ insight + 3 batasan (DOKUMENTASI) |
| Fetch dengan timeout & penanganan gagal | – | ✓ | ✓ | – |
| CSV mentah + olahan | – | ✓ | ✓ | ✓ |
| ≥ ~20 paper, paginasi + sleep | – | – | ✓ kode (30 paper; live diblokir di sini) | – |
| Class + unit test | – | – | – | ✓ (7 test) |

## Menjalankan ulang
```bash
cd jalur_a_eda_titanic && pip install -r requirements.txt && python src/main.py
cd ../jalur_b_api_pypi_npm && pip install -r requirements.txt && python src/main.py
cd ../jalur_c_arxiv && pip install -r requirements.txt && python src/main.py
cd ../jalur_d_analisis_nilai_oop && pip install -r requirements.txt && python src/main.py && python -m unittest discover -s tests
```
