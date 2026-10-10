# Produk Digital (PDF)

**Belajar Pemrograman Python** — *Materi dasar, Data Analisis, Visualisasi data, dan Capstone Project*. Dua produk PDF siap dibagikan atau dijual, dibangun otomatis dari isi repositori ini.

| Produk | Berkas | Halaman | Isi |
|---|---|---|---|
| **Buku Materi** | [Belajar-Pemrograman-Python-Buku-Materi.pdf](Belajar-Pemrograman-Python-Buku-Materi.pdf) | 152 | Modul 0–6 lengkap: pembahasan, kasus beragam, kode yang sudah dijalankan, **contoh output asli**, grafik, troubleshooting, dan capstone |
| **Buku Solusi** | [Belajar-Pemrograman-Python-Buku-Solusi.pdf](Belajar-Pemrograman-Python-Buku-Solusi.pdf) | 104 | Solusi **102 latihan dan mini project** (Hari 1–6): soal, pendekatan pseudocode, kode solusi, output, hasil pemeriksa — plus lampiran 4 contoh capstone utuh (dokumentasi, grafik, kode sumber) |

Fitur kedua buku: sampul, halaman "tentang buku", daftar isi dengan nomor halaman dan tautan yang bisa diklik, penanda (bookmark) PDF, pembuka tiap bab, kode berwarna, kotak output/pseudocode/catatan, dan nomor halaman.

## Membangun ulang

```bash
pip install -r produk/_build/requirements.txt     # mistune, pygments, pypdf
# butuh Node + Playwright + Chromium (dipakai untuk mencetak PDF)
python3 produk/_build/build.py            # keduanya
python3 produk/_build/build.py materi     # hanya Buku Materi
python3 produk/_build/build.py solusi     # hanya Buku Solusi
```

- **Buku Materi** disusun dari `materi/modul00…06-*.md` (dengan gambar di `materi/images/`).
- **Buku Solusi** disusun dari notebook solusi yang sudah dieksekusi di `workbook/solusi/` dan `contoh-capstone/`.
- Judul dan subjudul diatur di `_build/common.py` (`TITLE`, `SUBTITLE`); nama penerbit/penulis dan tahun pada halaman hak cipta di `_build/build.py` (`OWNER`, `YEAR`); warna dan gaya di `_build/common.py`.
