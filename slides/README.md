# Slide Bootcamp (web HTML)

Slide berbasis web untuk **dibawakan langsung oleh instruktur** sementara peserta mencoba di [buku kerja](../workbook/README.md). Setiap deck memakai transisi antar-slide dan animasi komponen (diagram alur, grid indeks, variabel yang berubah, grafik, tabel merge, dst.). Tanpa dependensi eksternal — cukup buka file `.html` di browser, bahkan offline.

| Hari | Deck | Slide |
|---|---|---|
| — | [`index.html`](index.html) (daftar deck) | — |
| 0 | [Persiapan Lingkungan (Python, venv, Jupyter)](hari0-setup-lingkungan.html) | 28 |
| 1 | [Python Fundamentals](hari1-python-fundamentals.html) | 30 |
| 2 | [Functions, Modules & File Handling](hari2-functions-modules-file-handling.html) | 31 |
| 3 | [Object-Oriented Programming](hari3-oop.html) | 24 |
| 4 | [NumPy & Pandas](hari4-numpy-pandas.html) | 26 |
| 5 | [Visualisasi, API & Scraping](hari5-visualisasi-api-scraping.html) | 28 |
| 6 | [Capstone Project](hari6-capstone-project.html) | 23 |

## Cara memakai

| Tombol | Fungsi |
|---|---|
| `→` / `Spasi` / `PgDn` | langkah berikutnya (animasi bertahap), lalu slide berikutnya |
| `←` / `PgUp` | mundur |
| `O` | ikhtisar semua slide |
| `N` | catatan pembicara (alur mengajar + waktu) |
| `T` / `C` | timer sesi / timer latihan |
| `L` | tema gelap/terang |
| `F` | layar penuh |
| `?` | bantuan |

- Tautan langsung ke slide/langkah: `#12.3` (slide 12, langkah 3).
- **Ekspor PDF:** buka `…html?print` lalu cetak dari browser (Ctrl/Cmd+P → Save as PDF).
- Slide **"Sekarang coba!"** menunjuk ke ID latihan di buku kerja (mis. L1–L5) dan memiliki timer.
- Semua output kode pada slide berasal dari eksekusi Python sungguhan saat deck dibangun.
- `prefers-reduced-motion` dihormati (animasi dimatikan).

## Naskah video

Naskah narasi per slide dan per langkah untuk merekam video tutorial ada di [naskah/](naskah/README.md).

## Membangun ulang

```bash
cd slides/_build
python3 build.py        # semua deck (atau: python3 build.py 3 5)
```

Konten tiap hari ada di `_build/d1.py … d6.py` (DSL di `lib.py`); tampilan di `assets/deck.css`, perilaku di `assets/deck.js`.
