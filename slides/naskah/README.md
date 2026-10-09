# Naskah Video Tutorial

Naskah narasi untuk merekam video tutorial memakai [slide web HTML](../index.html). Slide **tidak diubah**: naskah mengikuti persis slide dan langkah animasinya (tiap tekan `→`).

| Hari | Naskah | Slide | Klik | Perkiraan narasi |
|---|---|---|---|---|
| 1 | [Python Fundamentals](hari1-naskah.md) | 30 | 114 | 15 mnt 16 dtk |
| 2 | [Functions, Modules & File Handling](hari2-naskah.md) | 31 | 98 | 13 mnt 35 dtk |
| 3 | [Object-Oriented Programming](hari3-naskah.md) | 24 | 78 | 10 mnt 13 dtk |
| 4 | [NumPy & Pandas](hari4-naskah.md) | 26 | 104 | 12 mnt 47 dtk |
| 5 | [Visualisasi, API & Scraping](hari5-naskah.md) | 28 | 90 | 11 mnt 28 dtk |
| 6 | [Capstone Project](hari6-naskah.md) | 23 | 68 | 8 mnt 40 dtk |

Durasi di atas hanya narasi (±140 kata/menit); belum termasuk jeda latihan (slide *Sekarang coba!*) dan istirahat.

## Cara merekam

1. Buka deck di browser, tekan `F` (layar penuh). Mulai dari slide 1 (`#1`).
2. Baca blok **Saat slide muncul**, lalu tekan `→` setiap tertulis **Klik N →**. Teks di samping "muncul:" menunjukkan apa yang tampil pada klik itu.
3. Blok **🎬 Aksi** berisi hal yang dikerjakan di layar selain `→`: menjalankan perintah di terminal, membuka notebook, atau menjeda video untuk latihan.
4. Pada slide *Sekarang coba!*, jeda rekaman (atau potong) selama waktu latihan; timer di slide bisa dijalankan dengan tombol **Mulai**.
5. Untuk menandai bab video: setiap slide *bagian* (A, B, C, …) adalah titik bab yang natural.

## Menyusun ulang naskah

Narasi ada di `_build/n1.py … n6.py` (kunci = nomor slide; isi = narasi per langkah). Struktur slide diambil otomatis dari deck:

```bash
cd slides/naskah/_build
node extract.js     # baca struktur langkah dari deck (butuh Playwright + Chromium)
python3 gen.py      # gabungkan dengan narasi → ../hariN-naskah.md
```

`gen.py` berhenti dengan pesan jelas bila jumlah narasi suatu slide tidak sama dengan jumlah langkahnya, jadi naskah tidak bisa keluar dari sinkronisasi dengan slide tanpa disadari. Jika slide diubah, jalankan `extract.js` lalu perbaiki narasi yang dilaporkan.

## Catatan

- Slide Hari 6 (slide 5) menyebut **tiga** jalur capstone, sedangkan Modul 6 di repositori kini memuat **empat** jalur. Naskah mengikuti slide dan memberi catatan perekam pada slide tersebut.
- Beberapa slide menampilkan output baris demi baris pada klik berurutan (mis. tabel DataFrame di Hari 4); narasinya mengikuti urutan munculnya baris, sehingga sorotan kode dan baris output kadang tidak berada pada baris yang sama.
