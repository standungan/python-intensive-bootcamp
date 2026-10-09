# Naskah Video Tutorial

Naskah narasi untuk merekam video tutorial memakai [slide web HTML](../index.html). Slide **tidak diubah**: naskah mengikuti persis slide dan langkah animasinya (tiap tekan `→`).

| Hari | Naskah | Slide | Klik | Perkiraan narasi |
|---|---|---|---|---|
{{ROWS}}

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

- Beberapa slide menampilkan output baris demi baris pada klik berurutan (mis. tabel DataFrame di Hari 4); narasinya mengikuti urutan munculnya baris, sehingga sorotan kode dan baris output kadang tidak berada pada baris yang sama.
