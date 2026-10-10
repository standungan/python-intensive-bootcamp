# python-intensive-bootcamp

Materi Python Intensive Bootcamp (6 hari): modul lengkap dengan seluruh kode sudah dijalankan dan outputnya ditampilkan, contoh capstone, buku kerja Jupyter, dan slide web interaktif.

## Struktur repositori

```text
materi/            6 modul (Markdown) + docx asli + gambar
contoh-capstone/   4 contoh capstone lengkap (Jalur A/B/C/D) sebagai bahan belajar
produk/            produk digital PDF: Buku Materi dan Buku Solusi
workbook/          buku kerja Jupyter per hari (+ solusi, + versi HTML)
slides/            slide web HTML untuk instruktur (satu deck per hari)
```

## Jalur belajar

Persiapan lingkungan ([slide Hari 0](slides/hari0-setup-lingkungan.html)) → `materi/` (baca) → `workbook/` (latihan dengan pemeriksa otomatis) → `slides/` (instruktur) → `contoh-capstone/` (studi kasus lengkap, dengan latihan lanjutan) → capstone Anda sendiri.

## Materi

| Modul | Topik | Markdown | Dokumen asli |
|---|---|---|---|
| 0 | Persiapan Lingkungan (Python, venv, Jupyter) | [modul00](materi/modul00-persiapan-lingkungan.md) | — |
| 1 | Python Fundamentals | [modul01](materi/modul01-python-fundamentals.md) | [docx](materi/docx/Modul_01_Python_Fundamentals.docx) |
| 2 | Functions, Modules & File Handling | [modul02](materi/modul02-functions-modules-file-handling.md) | [docx](materi/docx/Modul_02_Functions_Modules_FileHandling.docx) |
| 3 | Object-Oriented Programming | [modul03](materi/modul03-oop.md) | [docx](materi/docx/Modul_03_Object_Oriented_Programming.docx) |
| 4 | NumPy & Pandas | [modul04](materi/modul04-numpy-pandas.md) | [docx](materi/docx/Modul_04_NumPy_Pandas.docx) |
| 5 | Visualisasi, API & Scraping | [modul05](materi/modul05-visualisasi-api-scraping.md) | [docx](materi/docx/Modul_05_Visualisasi_API_Scraping.docx) |
| 6 | Capstone Project (Jalur A/B/C/D) | [modul06](materi/modul06-capstone-project.md) | [docx](materi/docx/Modul_06_Capstone_Project.docx) · [docx versi 1](materi/docx/Modul_06_Capstone_Project_Versi1.docx) |

Materi versi 1 dan 2 sudah digabung. Modul 1–5 identik di kedua versi (docx byte-per-byte sama), sehingga hanya ada satu salinan. Modul 6 memuat empat jalur: A–C dari versi 2 dan Jalur D (aplikasi analisis nilai berbasis OOP) dari modul Hari 6 versi 1, beserta agenda dan alokasi waktu, ekspektasi kualitas kode, dan rekomendasi dataset dari versi 1. Dokumen asli versi 1 tetap disimpan di `materi/docx/`.

## Produk digital (PDF)

*Belajar Pemrograman Python.* Dua PDF siap bagikan di [produk/](produk/README.md): **Buku Materi** (Modul 0–6 dengan contoh output asli, 152 halaman) dan **Buku Solusi** (solusi 102 latihan + contoh capstone utuh, 104 halaman).

## Contoh capstone

[contoh-capstone/](contoh-capstone/): Jalur A (EDA Titanic), B (API PyPI/npm), C (arXiv), dan D (aplikasi analisis nilai OOP) — masing-masing dengan bagian *Bahan belajar* dan tiga latihan lanjutan.

## Tentang output pada modul
- Bagian **Output** pada tiap blok kode adalah hasil eksekusi nyata (Python 3.11; pandas 3.0.6, numpy 2.4.6, matplotlib 3.11.2, seaborn 0.13.2).
- Blok yang memakai `input()` dijalankan dengan input simulasi (ditulis di samping label output).
- Grafik Modul 5 disimpan di `materi/images/modul05/`.
- Bagian "Demonstrasi error" pada Troubleshooting menjalankan kasus error nyata.
- Blok yang memanggil API yang tidak dapat diakses dari lingkungan pengujian dijalankan dengan respons tiruan dan diberi catatan.

## Buku kerja (Jupyter Notebook)
Buku kerja interaktif per hari dengan pemeriksa jawaban otomatis ada di [workbook/](workbook/) (notebook latihan dan notebook solusi yang sudah dieksekusi).

## Slide presentasi (web HTML)

Slide interaktif dengan transisi dan animasi komponen untuk instruktur ada di [slides/](slides/) — mulai dari [`slides/index.html`](slides/index.html). Satu deck per hari (Hari 0 = persiapan Python, venv, dan Jupyter; Hari 1–6 = materi), selaras dengan latihan buku kerja. Lihat [slides/README.md](slides/README.md) untuk pintasan dan cara ekspor PDF. Naskah untuk video tutorial: [slides/naskah/](slides/naskah/README.md).

Cara membuka: unduh/clone repositori lalu buka `slides/index.html` di browser (bekerja offline), atau jalankan server lokal: `python -m http.server 8000` di folder repositori lalu buka `http://localhost:8000/slides/`. (GitHub Pages tidak dipakai: repositori privat pada paket gratis.)
