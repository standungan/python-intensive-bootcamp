# Contoh Capstone — Modul 6

Tiga contoh pengerjaan lengkap untuk tiga jalur Capstone pada [Modul 6](../materi/modul06-capstone-project.md). Struktur folder, deliverable, dan README mengikuti template pada modul: `README.md` (10 bagian), `requirements.txt`, `data/raw`, `data/processed`, `src/`, `figures/`, `output/ringkasan.csv`, dan `output/insight.txt`.

| Jalur | Folder | Data | Catatan |
|---|---|---|---|
| A — EDA dataset publik | [jalur_a_eda_titanic](jalur_a_eda_titanic/) | Nyata (Titanic, seaborn-data) | 6 figure + dashboard |
| B — API → analisis → visualisasi | [jalur_b_api_pypi_npm](jalur_b_api_pypi_npm/) | Nyata, live dari API PyPI & npm (2026-10-02) | Cache + retry + fallback |
| C — arXiv / literatur | [jalur_c_arxiv](jalur_c_arxiv/) | **Sampel FIKTIF** (API arXiv diblokir di lingkungan pembuatan) | Mode live tersedia; hasil nyata perlu dijalankan dengan internet |

## Pemeriksaan terhadap "Scope minimum" Modul 6

| Syarat | A | B | C |
|---|---|---|---|
| Pertanyaan analisis tertulis | ✓ 3 | ✓ 3 | ✓ 3 |
| Cleaning terdokumentasi + CSV bersih | ✓ `data_bersih.csv` | ✓ `rilis_bersih.csv` | ✓ `paper_bersih.csv` |
| Minimal 3 groupby/agregasi berbeda | ✓ 6 groupby + pivot | ✓ | ✓ per tahun, kata, penulis |
| Figure minimal | ✓ 6 (min. 4) | ✓ 5 (min. 3) | ✓ 3 (min. 2–3) |
| Insight (A: 5 poin) + batasan | ✓ 6 + 6 batasan | ✓ 7 + 5 batasan | ✓ 5 + 6 batasan |
| Fetch dengan timeout & penanganan gagal | – | ✓ | ✓ |
| CSV mentah + olahan | – | ✓ | ✓ |
| ≥ ~20 paper, paginasi + sleep | – | – | ✓ kode (30 paper; live diblokir di sini) |

Contoh dari **versi 1** (Opsi A Titanic, B PyPI/npm, C aplikasi nilai OOP — rujukan [Modul 6b](../materi/modul06b-capstone-opsi-versi1.md)) ada di [opsi-versi1/](opsi-versi1/); isinya tidak diubah.

## Menjalankan ulang
```bash
cd jalur_a_eda_titanic && pip install -r requirements.txt && python src/main.py
cd ../jalur_b_api_pypi_npm && pip install -r requirements.txt && python src/main.py
cd ../jalur_c_arxiv && pip install -r requirements.txt && python src/main.py
```
