# Naskah Video — Hari 5: Visualisasi, API & Scraping

Deck: [`hari5-visualisasi-api-scraping.html`](../hari5-visualisasi-api-scraping.html) · 28 slide · 90 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 11 mnt 28 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | Visualisasi, API & Scraping | 0 | 18 dtk |
| 2 | Agenda | 9 | 33 dtk |
| 3 | Tujuan | 6 | 25 dtk |
| 4 | A. Matplotlib | 0 | 6 dtk |
| 5 | Anatomi grafik | 4 | 39 dtk |
| 6 | Memilih grafik | 5 | 26 dtk |
| 7 | Bar, scatter, histogram | 4 | 29 dtk |
| 8 | Subplot | 7 | 43 dtk |
| 9 | Latihan: L1, L2, L3, L4, L5 | 0 | 22 dtk |
| 10 | B. Seaborn | 0 | 5 dtk |
| 11 | Seaborn | 5 | 36 dtk |
| 12 | Latihan: L6, L7, L8 | 0 | 22 dtk |
| 13 | Rehat | 0 | 12 dtk |
| 14 | C. API & JSON | 0 | 6 dtk |
| 15 | Request-response | 5 | 40 dtk |
| 16 | JSON | 5 | 35 dtk |
| 17 | Error jaringan | 7 | 41 dtk |
| 18 | Latihan: L9, L10, L11 | 0 | 22 dtk |
| 19 | D. Scraping & arXiv | 0 | 8 dtk |
| 20 | Etika | 5 | 20 dtk |
| 21 | BeautifulSoup | 3 | 24 dtk |
| 22 | arXiv | 7 | 39 dtk |
| 23 | Latihan: L12, L13 | 0 | 22 dtk |
| 24 | E. Mini Project | 0 | 7 dtk |
| 25 | Pilih proyek | 5 | 23 dtk |
| 26 | Latihan: P1, P2, P3, P4 | 0 | 22 dtk |
| 27 | Jebakan umum | 7 | 31 dtk |
| 28 | Rekap | 6 | 32 dtk |

---

### Slide 1 — Visualisasi, API & Scraping

*judul · transisi `zoom` · 0 klik · ⏱ 18 dtk*

**Saat slide muncul**

> Selamat datang di hari kelima: Visualisasi, API, dan Scraping. Hari ini kita mengubah data menjadi grafik, dan belajar mengambil data dari web dengan cara yang etis. Kalau jaringan terbatas, buku kerja menyediakan data contoh sebagai cadangan.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 9 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Agenda hari kelima, sekitar enam jam.

**Klik 1 →** — muncul: `Opening`

> Pembukaan lima belas menit.

**Klik 2 →** — muncul: `Matplotlib`

> Matplotlib, enam puluh menit.

**Klik 3 →** — muncul: `Seaborn`

> Seaborn, empat puluh menit.

**Klik 4 →** — muncul: `Rehat`

> Istirahat dua puluh menit.

**Klik 5 →** — muncul: `API & JSON`

> API dan JSON, enam puluh menit.

**Klik 6 →** — muncul: `Scraping & arXiv`

> Scraping dan arXiv, lima puluh menit.

**Klik 7 →** — muncul: `Mini project`

> Mini project, seratus menit, blok terpanjang hari ini.

**Klik 8 →** — muncul: `Rekap`

> Dan rekap lima belas menit.

**Klik 9 →** — muncul: `Total ±6 jam. Demo singkat → peserta coba di buku kerja.`

> Polanya tetap: demo singkat lalu latihan di buku kerja.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 6 klik · ⏱ 25 dtk*

**Saat slide muncul**

> Setelah hari ini Anda bisa melakukan enam hal.

**Klik 1 →** — muncul: `membuat line, bar, scatter, histogram, dan subplot dengan Matplotlib`

> Membuat grafik line, bar, scatter, histogram, dan subplot dengan Matplotlib.

**Klik 2 →** — muncul: `memakai Seaborn untuk distribusi, relasi, dan heatmap`

> Memakai Seaborn untuk distribusi, relasi, dan heatmap.

**Klik 3 →** — muncul: `memanggil API dengan requests dan mengolah JSON`

> Memanggil API dengan requests dan mengolah JSON.

**Klik 4 →** — muncul: `menangani error jaringan (timeout, 404, 429)`

> Menangani error jaringan seperti timeout, 404, dan 429.

**Klik 5 →** — muncul: `melakukan scraping secara etis dengan BeautifulSoup & membaca feed arX`

> Melakukan scraping secara etis dengan BeautifulSoup dan membaca feed arXiv.

**Klik 6 →** — muncul: `membangun dashboard dan pipeline data mini`

> Dan membangun dashboard serta pipeline data mini.

---

### Slide 4 — A. Matplotlib

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian A: Matplotlib. Grafik dasar yang jelas dan jujur.

---

### Slide 5 — Anatomi grafik

*isi · transisi `slide` · 4 klik · ⏱ 39 dtk*

**Saat slide muncul**

> Mari bangun grafik sederhana dan pahami anatominya. Datanya suhu lima hari.

**Klik 1 →** — muncul: `fig, ax = plt.subplots()`

> Pertama, plt titik subplots membuat dua objek: fig, yaitu kanvas, dan ax, yaitu sumbu tempat kita menggambar. Di kanan muncul kerangka sumbunya.

**Klik 2 →** — muncul: `ax.plot(hari, suhu, marker="o")`

> Kedua, ax titik plot menggambar garis suhu per hari dengan penanda bulat.

**Klik 3 →** — muncul: `ax.set_title("Suhu Harian")`

> Ketiga, judul dan label sumbu. Ini penting: selalu beri judul, label sumbu, dan satuan, supaya grafik bisa dipahami tanpa penjelasan lisan.

**Klik 4 →** — muncul: `plt.show()`

> Terakhir, plt titik show menampilkan grafik. Di skrip biasa tanpa layar, kita akan pakai savefig, yang dibahas sebentar lagi.

---

### Slide 6 — Memilih grafik

*isi · transisi `slide` · 5 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Pertanyaan pertama bukan grafik apa yang cantik, tapi apa yang ingin dijawab.

**Klik 1 →** — muncul: `Bagaimana perubahan dari waktu ke waktu?Lineax.plot`

> Perubahan dari waktu ke waktu: pakai line plot.

**Klik 2 →** — muncul: `Bandingkan antar kategori?Barax.bar`

> Membandingkan antar kategori: pakai bar chart.

**Klik 3 →** — muncul: `Apakah dua variabel berhubungan?Scatterax.scatter`

> Hubungan dua variabel: pakai scatter plot.

**Klik 4 →** — muncul: `Bagaimana sebaran nilai?Histogramax.hist`

> Sebaran nilai: pakai histogram.

**Klik 5 →** — muncul: `Bagian dari keseluruhan (sedikit kategori)?Pieax.pie`

> Bagian dari keseluruhan dengan sedikit kategori: boleh pakai pie chart. Mulailah dari pertanyaan, bukan dari jenis grafik.

---

### Slide 7 — Bar, scatter, histogram

*isi · transisi `slide` · 4 klik · ⏱ 29 dtk*

**Saat slide muncul**

> Tiga jenis grafik yang paling sering dipakai.

**Klik 1 →** — muncul: `01234IFSITI3.43.73.1BarIPK`

> Bar chart membandingkan kategori. Di sini ipk rata-rata per prodi: IF, SI, dan TI.

**Klik 2 →** — muncul: `3.4`

> Scatter plot menunjukkan hubungan dua variabel. Semakin banyak jam belajar, nilai cenderung naik.

**Klik 3 →** — muncul: `BarIPK`

> Histogram menunjukkan sebaran nilai: berapa banyak data jatuh di setiap rentang.

**Klik 4 →** — muncul: `ax.bar(prodi, ipk) ax.scatter(jam, nilai) ax.hist(nilai, bins=5)`

> Kodenya singkat: ax titik bar, ax titik scatter, dan ax titik hist dengan jumlah bin.

---

### Slide 8 — Subplot

*isi · transisi `slide` · 7 klik · ⏱ 43 dtk*

**Saat slide muncul**

> Subplot memungkinkan beberapa grafik dalam satu gambar, misalnya dashboard dua kali dua.

**Klik 1 →**

> Kita buat kanvas dengan dua baris dua kolom. Variabel axes sekarang berisi empat sumbu.

**Klik 2 →** — muncul: `axes[0, 0].plot(x, y)`

> Kiri atas, indeks nol koma nol: line plot.

**Klik 3 →** — muncul: `axes[0, 1].bar(k, v)`

> Kanan atas, nol koma satu: bar chart.

**Klik 4 →** — muncul: `axes[1, 0].hist(data)`

> Kiri bawah, satu koma nol: histogram.

**Klik 5 →** — muncul: `axes[1, 1].scatter(a, b)`

> Kanan bawah, satu koma satu: scatter plot. Perhatikan bahwa pengindeksannya mirip array NumPy.

**Klik 6 →** — muncul: `fig.tight_layout()`

> Terakhir, tight layout merapikan jarak antar grafik, dan savefig menyimpan gambar ke file dengan resolusi seratus lima puluh dpi.

**Klik 7 →** — muncul: `Di skrip .py / server tanpa layar, plt.show() tidak tampil → gunakan s`

> Penting: di skrip biasa atau server tanpa layar, plt titik show tidak menampilkan apa pun. Gunakan savefig.

---

### Slide 9 — Latihan: L1, L2, L3, L4, L5

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 5, bagian A, dan kerjakan latihan L1 sampai L5. Waktunya 30 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari5-visualisasi-api-scraping.ipynb dan jalankan timer 30 menit (tekan Mulai).

---

### Slide 10 — B. Seaborn

*bagian · transisi `rise` · 0 klik · ⏱ 5 dtk*

**Saat slide muncul**

> Bagian B: Seaborn. Grafik statistik dengan sedikit kode.

---

### Slide 11 — Seaborn

*isi · transisi `slide` · 5 klik · ⏱ 36 dtk*

**Saat slide muncul**

> Seaborn bekerja langsung dari DataFrame, dengan nama kolom sebagai argumen.

**Klik 1 →** — muncul: `sns.histplot(df, x="nilai", kde=True)`

> histplot menggambar distribusi sebuah kolom, dengan garis kde untuk kurva halus.

**Klik 2 →** — muncul: `sns.boxplot(data=df, x="hari", y="tip")`

> boxplot menunjukkan sebaran dan outlier per kategori, misalnya tip per hari.

**Klik 3 →** — muncul: `scatterplotrelasi + hue`

> scatterplot menunjukkan relasi dua kolom, dan hue mewarnai berdasarkan kategori.

**Klik 4 →** — muncul: `heatmapkorelasi`

> heatmap menampilkan matriks korelasi, dengan angka di setiap sel.

**Klik 5 →** — muncul: `Seaborn bekerja di atas Matplotlib: judul/label tetap diatur dengan pl`

> Seaborn berjalan di atas Matplotlib, jadi judul dan label tetap diatur dengan plt titik title dan sejenisnya. Pastikan nama kolom persis sama, salah ketik akan menimbulkan error.

---

### Slide 12 — Latihan: L6, L7, L8

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 5, bagian B, dan kerjakan latihan L6 sampai L8. Waktunya 20 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari5-visualisasi-api-scraping.ipynb dan jalankan timer 20 menit (tekan Mulai).

---

### Slide 13 — Rehat

*isi · transisi `slide` · 0 klik · ⏱ 12 dtk*

**Saat slide muncul**

> Waktunya istirahat sekitar 20 menit. Setelah ini kita lanjut ke API dan JSON.

🎬 **Aksi:** Jeda video; tampilkan timer istirahat.

---

### Slide 14 — C. API & JSON

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian C: API dan JSON. Meminta data dari server.

---

### Slide 15 — Request-response

*isi · transisi `slide` · 5 klik · ⏱ 40 dtk*

**Saat slide muncul**

> API adalah cara program kita meminta data ke server. Alurnya request lalu response.

**Klik 1 →** — muncul: `GET /users?limit=3`

> Program kita mengirim permintaan GET ke alamat users dengan limit tiga.

**Klik 2 →** — muncul: `200 OK + JSON`

> Server membalas kode dua ratus OK, disertai data berformat JSON.

**Klik 3 →** — muncul: `GET /halaman-tidak-ada`

> Sekarang permintaan ke halaman yang tidak ada.

**Klik 4 →** — muncul: `404 Not Found`

> Server membalas empat ratus empat, tidak ditemukan. Warna merah menandakan masalah.

**Klik 5 →** — muncul: `r = requests.get(url, params={"limit": 3}, timeout=10)r.raise_for_stat`

> Di kode kita pakai requests titik get dengan parameter dan timeout, lalu raise for status agar error empat ratus atau lima ratus langsung jadi exception, dan terakhir titik json untuk membaca datanya. Selalu pakai timeout.

---

### Slide 16 — JSON

*isi · transisi `slide` · 5 klik · ⏱ 35 dtk*

**Saat slide muncul**

> Respons API biasanya berupa JSON, yang di Python menjadi dictionary dan list. Contohnya data pengguna bersarang.

**Klik 1 →** — muncul: `d = json.loads(raw)`

> json loads mengubah teks JSON menjadi dictionary Python.

**Klik 2 →** — muncul: `Bandung`

> Kita ambil kota dari pengguna pertama dengan serangkaian kurung siku: hasilnya Bandung.

**Klik 3 →** — muncul: `df = pd.json_normalize(d["data"])`

> Untuk analisis, kita ubah menjadi DataFrame dengan json normalize. Header-nya: id, nama, dan kota titik nama.

**Klik 4 →** — muncul: `0 1 Ani Bandung`

> Baris pertama: Ani dari Bandung. Perhatikan bahwa json normalize meratakan JSON bersarang jadi kolom bernama kota titik nama.

**Klik 5 →** — muncul: `1 2 Budi Medan`

> Baris kedua: Budi dari Medan.

---

### Slide 17 — Error jaringan

*isi · transisi `slide` · 7 klik · ⏱ 41 dtk*

**Saat slide muncul**

> Jaringan bisa gagal kapan saja, jadi error handling wajib.

**Klik 1 →** — muncul: `r = requests.get(url, timeout=5)`

> Kita bungkus pemanggilan dalam function dengan try, lalu raise for status dan kembalikan json.

**Klik 2 →** — muncul: `except requests.exceptions.RequestException as e:`

> Satu except untuk RequestException menangkap timeout, gagal koneksi, dan error HTTP. Kita cetak jenis errornya dan kembalikan None.

**Klik 3 →** — muncul: `200OK`

> Kode status dua ratus artinya OK.

**Klik 4 →** — muncul: `404tidak ditemukan`

> Empat ratus empat, tidak ditemukan.

**Klik 5 →** — muncul: `429terlalu sering — tunggu`

> Empat ratus dua puluh sembilan, terlalu sering: tunggu sebelum mencoba lagi.

**Klik 6 →** — muncul: `5xxserver bermasalah`

> Lima ratus dan seterusnya, server yang bermasalah.

**Klik 7 →** — muncul: `Siapkan fallback: cache lokal / data contoh agar program tetap jalan o`

> Siapkan juga fallback, misalnya cache lokal atau data contoh, supaya program tetap jalan walau API gagal.

---

### Slide 18 — Latihan: L9, L10, L11

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 5, bagian C, dan kerjakan latihan L9 sampai L11. Waktunya 25 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari5-visualisasi-api-scraping.ipynb dan jalankan timer 25 menit (tekan Mulai).

---

### Slide 19 — D. Scraping & arXiv

*bagian · transisi `rise` · 0 klik · ⏱ 8 dtk*

**Saat slide muncul**

> Bagian D: scraping dan arXiv. Mengambil data dari halaman web dan feed ilmiah.

---

### Slide 20 — Etika

*isi · transisi `slide` · 5 klik · ⏱ 20 dtk*

**Saat slide muncul**

> Sebelum teknik scraping, etikanya dulu.

**Klik 1 →** — muncul: `Baca robots.txt dan Terms of Service situs`

> Baca robots titik txt dan syarat layanan situs.

**Klik 2 →** — muncul: `Beri jeda antar request (rate limit), jangan membanjiri server`

> Beri jeda antar permintaan. Jangan membanjiri server.

**Klik 3 →** — muncul: `Utamakan API resmi bila tersedia`

> Utamakan API resmi bila tersedia.

**Klik 4 →** — muncul: `Jangan ambil data pribadi / yang dilindungi`

> Jangan mengambil data pribadi atau yang dilindungi.

**Klik 5 →** — muncul: `Cantumkan sumber data pada laporan`

> Dan cantumkan sumber data pada laporan Anda.

---

### Slide 21 — BeautifulSoup

*isi · transisi `slide` · 3 klik · ⏱ 24 dtk*

**Saat slide muncul**

> BeautifulSoup menelusuri HTML. Struktur HTML berbentuk pohon, seperti di kiri.

**Klik 1 →** — muncul: `▸<html>`

> Pohonnya: html, di dalamnya body, lalu ul, dan di dalam ul ada dua elemen li berkelas judul.

**Klik 2 →** — muncul: `print(li.get_text())`

> select dengan li titik judul memilih kedua elemen itu, dan get text mengambil isinya. Elemen pertama: Python 3.14 rilis.

**Klik 3 →** — muncul: `AI kampus`

> Elemen kedua: AI kampus.

---

### Slide 22 — arXiv

*isi · transisi `slide` · 7 klik · ⏱ 39 dtk*

**Saat slide muncul**

> arXiv menyediakan API untuk metadata paper ilmiah. Alurnya empat tahap.

**Klik 1 →**

> Pertama, query: kita mengirim pencarian, misalnya kata kunci LLM.

**Klik 2 →**

> Kedua, respons berupa feed Atom XML.

**Klik 3 →**

> Ketiga, kita parse dengan ElementTree.

**Klik 4 →**

> Keempat, hasilnya dijadikan DataFrame untuk dianalisis.

**Klik 5 →**

> Kodenya memakai namespace Atom dan mencari setiap elemen entry. Namespace diperlukan karena feed berformat Atom.

**Klik 6 →** — muncul: `Paper A 2025-01-10`

> Hasilnya: Paper A, tanggal sepuluh Januari dua ribu dua puluh lima.

**Klik 7 →** — muncul: `Paper B 2025-02-01`

> Dan Paper B, tanggal satu Februari dua ribu dua puluh lima. Buku kerja menyediakan sampel feed bila jaringan terblokir.

---

### Slide 23 — Latihan: L12, L13

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 5, bagian D, dan kerjakan latihan L12 dan L13. Waktunya 20 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari5-visualisasi-api-scraping.ipynb dan jalankan timer 20 menit (tekan Mulai).

---

### Slide 24 — E. Mini Project

*bagian · transisi `rise` · 0 klik · ⏱ 7 dtk*

**Saat slide muncul**

> Bagian E: mini project. Dashboard, API plus visualisasi, dan pipeline arXiv.

---

### Slide 25 — Pilih proyek

*isi · transisi `slide` · 5 klik · ⏱ 23 dtk*

**Saat slide muncul**

> Ada empat proyek dengan tingkat tantangan berbeda. Pilih sesuai kemampuan.

**Klik 1 →** — muncul: `P1Dashboard visualisasi nilaiDasar`

> P1, dashboard visualisasi nilai, tingkat dasar.

**Klik 2 →** — muncul: `P2API + visualisasiMenengah`

> P2, API plus visualisasi, tingkat menengah.

**Klik 3 →** — muncul: `P3Pipeline paper arXivMenengah–Tinggi`

> P3, pipeline paper arXiv, menengah sampai tinggi.

**Klik 4 →** — muncul: `P4EDA lengkap dataset nyataTinggi`

> P4, EDA lengkap dataset nyata, tingkat tinggi.

**Klik 5 →** — muncul: `Semua proyek memakai pola ambil → bersihkan → analisis → visualisasi →`

> Semua proyek memakai pola yang sama: ambil, bersihkan, analisis, visualisasi, simpan.

---

### Slide 26 — Latihan: P1, P2, P3, P4

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 5, bagian E, dan kerjakan project P1 sampai P4. Waktunya 80 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari5-visualisasi-api-scraping.ipynb dan jalankan timer 80 menit (tekan Mulai).

---

### Slide 27 — Jebakan umum

*isi · transisi `slide` · 7 klik · ⏱ 31 dtk*

**Saat slide muncul**

> Tiga jebakan yang paling sering hari ini.

**Klik 1 →** — muncul: `plt.plot(x, y)`

> Pertama, memplot x dan y dengan panjang berbeda.

**Klik 2 →** — muncul: `ValueError: x and y must have same first dimension, but have shapes (3`

> Hasilnya ValueError: x dan y harus punya dimensi pertama yang sama. Samakan panjangnya.

**Klik 3 →** — muncul: `json.loads("<html>…")`

> Kedua, membaca respons yang bukan JSON, misalnya halaman HTML.

**Klik 4 →** — muncul: `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

> Hasilnya JSONDecodeError. Pastikan respons memang JSON.

**Klik 5 →** — muncul: `d["data"]`

> Ketiga, mengakses key data padahal respons berisi error.

**Klik 6 →** — muncul: `KeyError: 'data'`

> Hasilnya KeyError.

**Klik 7 →** — muncul: `Periksa r.status_code dan key "error" sebelum membaca data; pastikan r`

> Periksa status code dan key error sebelum membaca data.

---

### Slide 28 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Rekap Hari 5.

**Klik 1 →** — muncul: `Matplotlib: line/bar/scatter/hist, subplot, savefig`

> Matplotlib: line, bar, scatter, histogram, subplot, dan savefig.

**Klik 2 →** — muncul: `Seaborn: histplot, boxplot, heatmap dari DataFrame`

> Seaborn: histplot, boxplot, dan heatmap langsung dari DataFrame.

**Klik 3 →** — muncul: `API: requests, JSON, json_normalize, error handling`

> API: requests, JSON, json normalize, dan error handling.

**Klik 4 →** — muncul: `Scraping etis: BeautifulSoup & feed arXiv`

> Scraping etis dengan BeautifulSoup dan feed arXiv.

**Klik 5 →** — muncul: `Mini project: dashboard & pipeline data`

> Mini project dashboard dan pipeline data.

**Klik 6 →** — muncul: `Besok (Hari 6): Capstone Project`

> Jalankan sel Rekap hasil latihan. Besok, Hari 6, Capstone Project: pikirkan jalur yang ingin Anda ambil. Sampai jumpa!

🎬 **Aksi:** Tampilkan sel rekap di notebook.

---
