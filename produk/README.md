# Produk Digital (PDF)

**Belajar Pemrograman Python** — *Materi dasar, Data Analisis, Visualisasi data, dan Capstone Project*. Dua produk terpisah, dibangun otomatis dari isi repositori ini.

| Produk | Berkas | Isi |
|---|---|---|
| **1. Paket Materi + Buku Kerja** (ZIP) | [paket/Belajar-Pemrograman-Python-Materi-dan-Buku-Kerja.zip](paket/Belajar-Pemrograman-Python-Materi-dan-Buku-Kerja.zip) (±3,3 MB) | Buku Materi (PDF, 152 halaman) + buku kerja Jupyter Hari 1–6 + `requirements.txt` + panduan awal |
| **2. Buku Solusi** (PDF terpisah) | [Belajar-Pemrograman-Python-Buku-Solusi.pdf](Belajar-Pemrograman-Python-Buku-Solusi.pdf) (104 halaman) | Solusi **102 latihan dan mini project** (Hari 1–6): soal, pendekatan pseudocode, kode solusi, output, hasil pemeriksa — plus lampiran 4 contoh capstone utuh |

[Belajar-Pemrograman-Python-Buku-Materi.pdf](Belajar-Pemrograman-Python-Buku-Materi.pdf) adalah Buku Materi yang sama dengan yang ada di dalam ZIP (tersedia terpisah untuk dibaca langsung).

Isi PDF: sampul, halaman "tentang buku", daftar isi dengan nomor halaman dan tautan, penanda (bookmark) PDF, pembuka tiap bab, kode berwarna, kotak output/pseudocode/catatan, dan nomor halaman. Buku Materi memuat contoh output asli; Buku Solusi memuat output dan hasil pemeriksa setiap solusi.

## Isi paket ZIP

```text
Belajar-Pemrograman-Python/
├── MULAI-DI-SINI.txt          panduan awal: isi paket, urutan belajar, persiapan cepat
├── 1-Buku-Materi.pdf
├── 2-Buku-Kerja/              hari1 … hari6 (.ipynb, versi latihan tanpa solusi)
└── requirements.txt
```

Buku kerja di paket adalah versi latihan (jawaban masih kosong); rujukan "solusi lengkap" di dalam notebook diarahkan ke **Buku Solusi (PDF terpisah)**. Notebook solusi, Buku Solusi, slide, dan materi sumber **tidak** disertakan di ZIP. Keenam notebook sudah diuji berjalan mandiri di luar repositori ini. Edit isi paket di `_build/paket.py`.

## Membangun ulang

```bash
pip install -r produk/_build/requirements.txt     # mistune, pygments, pypdf
# butuh Node + Playwright + Chromium (dipakai untuk mencetak PDF)
python3 produk/_build/build.py            # keduanya
python3 produk/_build/build.py materi     # hanya Buku Materi
python3 produk/_build/build.py solusi     # hanya Buku Solusi
python3 produk/_build/paket.py            # merakit paket ZIP Materi + Buku Kerja (setelah PDF dibangun)
```

- **Buku Materi** disusun dari `materi/modul00…06-*.md` (dengan gambar di `materi/images/`).
- **Buku Solusi** disusun dari notebook solusi yang sudah dieksekusi di `workbook/solusi/` dan `contoh-capstone/`.
- Judul dan subjudul diatur di `_build/common.py` (`TITLE`, `SUBTITLE`); nama penerbit/penulis dan tahun pada halaman hak cipta di `_build/build.py` (`OWNER`, `YEAR`); warna dan gaya di `_build/common.py`.
