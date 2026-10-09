# Naskah Video — Hari 2: Functions, Modules & File Handling

Deck: [`hari2-functions-modules-file-handling.html`](../hari2-functions-modules-file-handling.html) · 31 slide · 98 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 13 mnt 35 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | Functions, Modules & File Handling | 0 | 20 dtk |
| 2 | Agenda | 10 | 37 dtk |
| 3 | Tujuan | 6 | 30 dtk |
| 4 | A. Functions | 0 | 7 dtk |
| 5 | Anatomi function | 5 | 35 dtk |
| 6 | print vs return | 6 | 41 dtk |
| 7 | args & kwargs | 4 | 34 dtk |
| 8 | Scope | 6 | 37 dtk |
| 9 | Latihan: L1, L2, L3, L4, L5, L6, L7, L8 | 0 | 22 dtk |
| 10 | B. Lambda, map, filter & Comprehension | 0 | 8 dtk |
| 11 | map & filter | 4 | 38 dtk |
| 12 | Comprehension | 4 | 32 dtk |
| 13 | Latihan: L9, L10, L11, L12, L13 | 0 | 22 dtk |
| 14 | Rehat | 0 | 12 dtk |
| 15 | C. Modules | 0 | 5 dtk |
| 16 | Module | 5 | 44 dtk |
| 17 | Gaya import | 6 | 41 dtk |
| 18 | Latihan: L14, L15 | 0 | 22 dtk |
| 19 | D. Error Handling | 0 | 6 dtk |
| 20 | try/except | 4 | 33 dtk |
| 21 | Hasil bagi_aman | 4 | 26 dtk |
| 22 | raise | 5 | 37 dtk |
| 23 | Latihan: L16, L17, L18 | 0 | 22 dtk |
| 24 | E. File Handling | 0 | 9 dtk |
| 25 | File teks | 7 | 40 dtk |
| 26 | CSV | 3 | 32 dtk |
| 27 | F. Mini Project | 0 | 6 dtk |
| 28 | Alur mini project | 6 | 30 dtk |
| 29 | Latihan: L19, L20 | 0 | 23 dtk |
| 30 | Jebakan umum | 7 | 32 dtk |
| 31 | Rekap | 6 | 32 dtk |

---

### Slide 1 — Functions, Modules & File Handling

*judul · transisi `zoom` · 0 klik · ⏱ 20 dtk*

**Saat slide muncul**

> Selamat datang di hari kedua: Functions, Modules, dan File Handling. Hari ini kita belajar menyusun kode agar bisa dipakai ulang, menangani error dengan rapi, dan menyimpan data ke file. Seperti kemarin, kita demo singkat lalu Anda mencoba sendiri di buku kerja.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 10 klik · ⏱ 37 dtk*

**Saat slide muncul**

> Ini agenda hari kedua, sekitar enam jam.

**Klik 1 →** — muncul: `Opening`

> Pembukaan lima belas menit.

**Klik 2 →** — muncul: `Functions`

> Functions, delapan puluh menit.

**Klik 3 →** — muncul: `Lambda & comp.`

> Lambda dan comprehension, empat puluh menit.

**Klik 4 →** — muncul: `Rehat`

> Istirahat dua puluh menit.

**Klik 5 →** — muncul: `Modules`

> Modules, tiga puluh lima menit.

**Klik 6 →** — muncul: `Error handling`

> Error handling, lima puluh menit.

**Klik 7 →** — muncul: `File`

> File handling, lima puluh menit.

**Klik 8 →** — muncul: `Mini project`

> Mini project pencatat kegiatan, enam puluh menit.

**Klik 9 →** — muncul: `Rekap`

> Dan rekap sepuluh menit.

**Klik 10 →** — muncul: `Total ±6 jam. Setiap blok: demo singkat → peserta coba sendiri.`

> Total enam jam, dengan pola yang sama: demo singkat lalu latihan sendiri.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 6 klik · ⏱ 30 dtk*

**Saat slide muncul**

> Setelah hari ini, ada enam kemampuan baru yang akan Anda miliki.

**Klik 1 →** — muncul: `menulis function dengan parameter, default, *args/**kwargs, dan return`

> Menulis function dengan parameter, nilai default, args, kwargs, dan return.

**Klik 2 →** — muncul: `memahami scope local vs global`

> Memahami scope, yaitu perbedaan variabel lokal dan global.

**Klik 3 →** — muncul: `memakai lambda, map/filter, dan comprehension`

> Memakai lambda, map, filter, dan comprehension.

**Klik 4 →** — muncul: `membuat module sendiri dan meng-import-nya`

> Membuat module sendiri lalu meng-import-nya.

**Klik 5 →** — muncul: `menangani error dengan try/except dan raise`

> Menangani error dengan try, except, dan raise.

**Klik 6 →** — muncul: `membaca & menulis file teks dan CSV — lalu membuat pencatat yang menyi`

> Dan membaca serta menulis file teks dan CSV, lalu menggabungkan semuanya menjadi pencatat yang menyimpan datanya.

---

### Slide 4 — A. Functions

*bagian · transisi `rise` · 0 klik · ⏱ 7 dtk*

**Saat slide muncul**

> Bagian A: functions. Kita belajar membungkus logika agar bisa dipakai berulang.

---

### Slide 5 — Anatomi function

*isi · transisi `slide` · 5 klik · ⏱ 35 dtk*

**Saat slide muncul**

> Mari bedah anatomi sebuah function sederhana.

**Klik 1 →** — muncul: `def sapa(nama, sapaan="Halo"):`

> Kata kunci def membuat function bernama sapa, dengan dua parameter: nama, dan sapaan yang punya nilai default Halo.

**Klik 2 →** — muncul: `"""Mengembalikan kalimat sapaan."""`

> Baris berikutnya adalah docstring, penjelasan singkat tentang apa yang dilakukan function ini.

**Klik 3 →** — muncul: `return f"{sapaan}, {nama}!"`

> Badan function mengembalikan kalimat sapaan dengan return. Perhatikan panah return pada diagram.

**Klik 4 →** — muncul: `pesan = sapa("Rina")`

> Saat memanggil sapa dengan argumen Rina, nilai itu masuk ke parameter nama. Bedakan: parameter ada di definisi, argumen diberikan saat memanggil.

**Klik 5 →** — muncul: `print(pesan)`

> Hasilnya disimpan di pesan dan dicetak: Halo, Rina!

---

### Slide 6 — print vs return

*isi · transisi `slide` · 6 klik · ⏱ 41 dtk*

**Saat slide muncul**

> Sekarang perbedaan yang sering membingungkan: print dan return.

**Klik 1 →** — muncul: `def kuadrat_print(x):`

> Function pertama hanya mencetak hasil kuadrat dengan print.

**Klik 2 →** — muncul: `def kuadrat_return(x):`

> Function kedua mengembalikan hasilnya dengan return.

**Klik 3 →** — muncul: `a = kuadrat_print(4)`

> Kita panggil function pertama dan simpan hasilnya di a. Angka enam belas tercetak, karena print bekerja.

**Klik 4 →** — muncul: `b = kuadrat_return(4)`

> Kita panggil function kedua dan simpan di b. Tidak ada yang tercetak, tapi b sekarang berisi enam belas.

**Klik 5 →** — muncul: `print(a, b + 1)`

> Saat a dan b ditambah satu dicetak, hasilnya None dan tujuh belas. a bernilai None karena function pertama tidak punya return.

**Klik 6 →** — muncul: `Function tanpa return mengembalikan None — hasilnya tidak bisa dipakai`

> Ingat: function tanpa return mengembalikan None, sehingga hasilnya tidak bisa dipakai untuk hitungan lanjutan.

---

### Slide 7 — args & kwargs

*isi · transisi `slide` · 4 klik · ⏱ 34 dtk*

**Saat slide muncul**

> Kadang kita tidak tahu berapa banyak argumen yang akan diberikan. Untuk itu ada args dan kwargs.

**Klik 1 →** — muncul: `def rata_rata(*angka):`

> Dengan bintang di depan parameter angka, function menerima argumen posisi sebanyak apa pun.

**Klik 2 →** — muncul: `Posisi bebas*angka → tuple(80, 90, 70)`

> Di dalam function, angka berbentuk tuple. Pada contoh delapan puluh, sembilan puluh, dan tujuh puluh, rata-ratanya delapan puluh.

**Klik 3 →** — muncul: `def profil(**data):`

> Dengan dua bintang, parameter data menampung argumen bernama sebagai dictionary.

**Klik 4 →** — muncul: `profil(nama="Ani", prodi="IF")`

> Saat dipanggil dengan nama Ani dan prodi IF, function mencetak setiap pasangan key dan value.

---

### Slide 8 — Scope

*isi · transisi `slide` · 6 klik · ⏱ 37 dtk*

**Saat slide muncul**

> Berikutnya scope, yaitu wilayah berlakunya sebuah variabel.

**Klik 1 →** — muncul: `x = 10`

> Di luar function kita punya x sama dengan sepuluh. Ini variabel global.

**Klik 2 →** — muncul: `def ubah():`

> Di dalam function ubah, ada x sama dengan sembilan puluh sembilan. Karena dibuat di dalam function, ini variabel lokal yang berbeda, bukan mengubah x global.

**Klik 3 →** — muncul: `print("dalam:", x)`

> Function mencetak x lokal-nya.

**Klik 4 →** — muncul: `ubah()`

> Saat function dipanggil, tercetak dalam: sembilan puluh sembilan.

**Klik 5 →** — muncul: `print("luar:", x)`

> Tapi x global tetap sepuluh. Tercetak luar: sepuluh.

**Klik 6 →** — muncul: `Mengubah variabel global dari dalam function? Pakai return (lebih aman`

> Kalau ingin mengubah nilai dari luar function, lebih aman memakai return daripada kata kunci global.

---

### Slide 9 — Latihan: L1, L2, L3, L4, L5, L6, L7, L8

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 2, bagian A, dan kerjakan latihan L1 sampai L8. Waktunya 25 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari2-functions-modules-file-handling.ipynb dan jalankan timer 25 menit (tekan Mulai).

---

### Slide 10 — B. Lambda, map, filter & Comprehension

*bagian · transisi `rise` · 0 klik · ⏱ 8 dtk*

**Saat slide muncul**

> Bagian B: lambda, map, filter, dan comprehension. Cara menulis kode ringkas tanpa kehilangan kejelasan.

---

### Slide 11 — map & filter

*isi · transisi `slide` · 4 klik · ⏱ 38 dtk*

**Saat slide muncul**

> Map dan filter memproses sekumpulan data dengan function pendek bernama lambda. Setiap klik memproses satu elemen.

**Klik 1 →** — muncul: `kuadrat = list(map(lambda x: x * x, [1, 2, 3, 4]))`

> Di kiri, map dengan lambda x kali x. Elemen satu menjadi satu. Di kanan, filter dengan syarat n lebih dari atau sama dengan enam puluh: delapan puluh lolos.

**Klik 2 →** — muncul: `2`

> Dua menjadi empat. Lima puluh lima ditolak, ditandai coret.

**Klik 3 →** — muncul: `3`

> Tiga menjadi sembilan. Sembilan puluh lolos, empat puluh lima ditolak.

**Klik 4 →** — muncul: `16`

> Empat menjadi enam belas. Hasil akhir map adalah satu, empat, sembilan, enam belas, dan filter menyisakan delapan puluh dan sembilan puluh.

---

### Slide 12 — Comprehension

*isi · transisi `slide` · 4 klik · ⏱ 32 dtk*

**Saat slide muncul**

> List comprehension dan sorted adalah alat yang akan sering Anda pakai. Lihat hasil empat pola ini.

**Klik 1 →** — muncul: `[80, 90, 70]`

> Pertama, comprehension dengan filter: hanya nilai yang lebih dari atau sama dengan enam puluh. Hasilnya delapan puluh, sembilan puluh, tujuh puluh.

**Klik 2 →** — muncul: `bonus = [n + 5 for n in nilai]`

> Kedua, transformasi: setiap nilai ditambah lima.

**Klik 3 →** — muncul: `{80: 'lulus', 55: 'remedi', 90: 'lulus', 45: 'remedi', 70: 'lulus'}`

> Ketiga, dictionary comprehension dengan kondisi: nilai menjadi key, dan labelnya lulus atau remedi.

**Klik 4 →** — muncul: `urut = sorted(nilai, key=lambda n: -n)`

> Keempat, sorted dengan key lambda minus n, mengurutkan dari yang terbesar.

---

### Slide 13 — Latihan: L9, L10, L11, L12, L13

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 2, bagian B, dan kerjakan latihan L9 sampai L13. Waktunya 20 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari2-functions-modules-file-handling.ipynb dan jalankan timer 20 menit (tekan Mulai).

---

### Slide 14 — Rehat

*isi · transisi `slide` · 0 klik · ⏱ 12 dtk*

**Saat slide muncul**

> Waktunya istirahat sekitar 20 menit. Setelah ini kita lanjut ke module dan error handling.

🎬 **Aksi:** Jeda video; tampilkan timer istirahat.

---

### Slide 15 — C. Modules

*bagian · transisi `rise` · 0 klik · ⏱ 5 dtk*

**Saat slide muncul**

> Bagian C: modules. Memecah program ke beberapa file.

---

### Slide 16 — Module

*isi · transisi `slide` · 5 klik · ⏱ 44 dtk*

**Saat slide muncul**

> Module adalah file Python yang bisa di-import oleh file lain.

**Klik 1 →** — muncul: `▾proyek/`

> Kita punya folder proyek.

**Klik 2 →** — muncul: `▪konversi.pymodule buatan sendiri`

> Di dalamnya ada konversi titik py, yaitu module buatan sendiri, berisi function c ke f untuk mengubah Celsius ke Fahrenheit.

**Klik 3 →** — muncul: `▪main.pyprogram utama`

> Dan main titik py, program utama yang memakai module itu: import konversi, atau from konversi import c ke f.

**Klik 4 →** — muncul: `212.0 32.0`

> Saat dijalankan, seratus derajat Celsius menjadi dua ratus dua belas Fahrenheit, dan nol menjadi tiga puluh dua.

**Klik 5 →** — muncul: `▾__pycache__/dibuat otomatis`

> Folder pycache dibuat otomatis oleh Python. Jangan khawatir, dan jangan beri nama file seperti module bawaan, misalnya random titik py, karena akan menimpa module standar.

---

### Slide 17 — Gaya import

*isi · transisi `slide` · 6 klik · ⏱ 41 dtk*

**Saat slide muncul**

> Ada beberapa gaya import. Kita lihat satu per satu.

**Klik 1 →** — muncul: `import mathmath.sqrt(9)namespace jelas — paling aman`

> Import math: dipakai dengan awalan math. Namespace jelas, paling aman.

**Klik 2 →** — muncul: `from math import sqrtsqrt(9)singkat, hindari bentrok nama`

> From math import sqrt: bisa langsung dipanggil sqrt. Lebih singkat, tapi hati-hati bentrok nama.

**Klik 3 →** — muncul: `import numpy as npnp.array([1])alias konvensional`

> Import numpy as np memakai alias. Ini konvensi yang dipakai semua orang.

**Klik 4 →** — muncul: `from m import *—hindari`

> From m import bintang sebaiknya dihindari karena mengacaukan namespace.

**Klik 5 →** — muncul: `3.141592653589793 3.0`

> Hasil contoh: nilai pi dan akar sembilan, yaitu tiga.

**Klik 6 →** — muncul: `__main__`

> Terakhir, nama file yang dijalankan langsung bernilai main. Karena itu kita sering menulis if name sama dengan main untuk kode yang hanya jalan saat file dieksekusi langsung.

---

### Slide 18 — Latihan: L14, L15

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 2, bagian C, dan kerjakan latihan L14 dan L15. Waktunya 20 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari2-functions-modules-file-handling.ipynb dan jalankan timer 20 menit (tekan Mulai).

---

### Slide 19 — D. Error Handling

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian D: error handling. Program tidak crash ketika sesuatu salah.

---

### Slide 20 — try/except

*isi · transisi `slide` · 4 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Try, except, else, dan finally mengatur apa yang terjadi saat error. Ikuti alurnya pada diagram.

**Klik 1 →** — muncul: `try:`

> Pertama kode di blok try dijalankan: a dibagi b. Lalu program menanyakan, apakah ada error?

**Klik 2 →** — muncul: `except ZeroDivisionError:`

> Jika ya, misalnya pembagian dengan nol, blok except ZeroDivisionError dijalankan dan function mengembalikan None.

**Klik 3 →** — muncul: `else:`

> Jika tidak ada error, blok else dijalankan dan hasilnya dibulatkan lalu dikembalikan.

**Klik 4 →** — muncul: `finally:`

> Terakhir, blok finally selalu jalan, apa pun yang terjadi. Cocok untuk membersihkan resource.

---

### Slide 21 — Hasil bagi_aman

*isi · transisi `slide` · 4 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Mari lihat hasil nyata function bagi aman.

**Klik 1 →** — muncul: `selesai dihitung`

> Pemanggilan pertama, sepuluh dibagi empat. Pertama tercetak selesai dihitung dari blok finally.

**Klik 2 →** — muncul: `2.5`

> Lalu hasilnya, dua koma lima.

**Klik 3 →** — muncul: `Tangkap error yang spesifik (ZeroDivisionError), jangan except: kosong`

> Satu catatan: tangkap error yang spesifik seperti ZeroDivisionError, jangan except kosong yang menelan semua error.

**Klik 4 →** — muncul: `None`

> Pemanggilan kedua, satu dibagi nol: tercetak selesai dihitung lagi, lalu None, karena error ditangani.

---

### Slide 22 — raise

*isi · transisi `slide` · 5 klik · ⏱ 37 dtk*

**Saat slide muncul**

> Selain menangkap error, kita juga bisa membuat error sendiri dengan raise, misalnya untuk validasi.

**Klik 1 →** — muncul: `raise TypeError("umur harus int")`

> Jika umur bukan angka bulat, kita raise TypeError dengan pesan umur harus int.

**Klik 2 →** — muncul: `if umur < 0:`

> Jika umur negatif, kita raise ValueError.

**Klik 3 →** — muncul: `try:`

> Di bagian pemanggil, kita coba tiga nilai: dua puluh lima, minus tiga, dan teks dua. Setiap error ditangkap dengan except dan dicetak jenisnya.

**Klik 4 →** — muncul: `ValueError -> umur tidak boleh negatif`

> Dua puluh lima valid dan langsung dicetak. Minus tiga memunculkan ValueError: umur tidak boleh negatif.

**Klik 5 →** — muncul: `TypeError -> umur harus int`

> Dan teks dua memunculkan TypeError: umur harus int.

---

### Slide 23 — Latihan: L16, L17, L18

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 2, bagian D, dan kerjakan latihan L16 sampai L18. Waktunya 25 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari2-functions-modules-file-handling.ipynb dan jalankan timer 25 menit (tekan Mulai).

---

### Slide 24 — E. File Handling

*bagian · transisi `rise` · 0 klik · ⏱ 9 dtk*

**Saat slide muncul**

> Bagian E: file handling. Menyimpan dan membaca data dari file teks dan CSV, supaya data bertahan.

---

### Slide 25 — File teks

*isi · transisi `slide` · 7 klik · ⏱ 40 dtk*

**Saat slide muncul**

> Pertama file teks, dengan pathlib dan with open.

**Klik 1 →** — muncul: `from pathlib import Path`

> Kita buat objek Path untuk catatan titik txt.

**Klik 2 →** — muncul: `p.write_text("baris 1\nbaris 2\n", encoding="utf-8")`

> write text menulis dua baris ke file, dengan encoding utf-8.

**Klik 3 →** — muncul: `f.write("baris 3\n")`

> Lalu kita buka lagi dengan mode a, artinya append: menambah baris ketiga tanpa menghapus isi lama. Blok with menutup file otomatis.

**Klik 4 →** — muncul: `print(no, baris)`

> Kita baca kembali semua isi file dan mencetaknya bernomor. Baris satu tercetak pertama.

**Klik 5 →** — muncul: `print(p.exists(), p.suffix)`

> Baris dua menyusul, dan kita juga mengecek apakah file ada serta ekstensinya.

**Klik 6 →** — muncul: `3 baris 3`

> Baris tiga tercetak. Ingat: selalu pakai with dan encoding utf-8.

**Klik 7 →** — muncul: `True .txt`

> Hasil akhirnya: file ada, True, dan ekstensinya titik txt.

---

### Slide 26 — CSV

*isi · transisi `slide` · 3 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Untuk data tabel, kita pakai CSV dengan DictWriter dan DictReader.

**Klik 1 →** — muncul: `w = csv.DictWriter(f, fieldnames=["nama", "nilai"])`

> DictWriter menulis header dan dua baris data. Tabel di kanan menunjukkan isi file setelah ditulis.

**Klik 2 →** — muncul: `for baris in csv.DictReader(f):`

> DictReader membaca baris demi baris sebagai dictionary. Setiap nilai ditambah lima: Ani menjadi sembilan puluh.

**Klik 3 →** — muncul: `Budi 75`

> Budi menjadi tujuh puluh lima. Ingat, nilai dari CSV selalu teks, jadi ubah dengan int, dan saat menulis pakai newline kosong agar tidak muncul baris kosong di Windows.

---

### Slide 27 — F. Mini Project

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian F: mini project. Pencatat kegiatan akademik yang menyimpan datanya.

---

### Slide 28 — Alur mini project

*isi · transisi `slide` · 6 klik · ⏱ 30 dtk*

**Saat slide muncul**

> Ini alur pencatat kegiatan.

**Klik 1 →**

> Saat program mulai, function muat csv membaca data lama dari file.

**Klik 2 →**

> Lalu menu tampil dengan pilihan tambah, lihat, dan filter.

**Klik 3 →**

> Jika memilih tambah, function tambah kegiatan dijalankan.

**Klik 4 →**

> Jika memilih lihat atau filter, data ditampilkan.

**Klik 5 →**

> Setelah setiap perubahan, function simpan csv menyimpan ke file.

**Klik 6 →** — muncul: `Data tersimpan di kegiatan.csv → tetap ada saat program dijalankan lag`

> Hasilnya, data tersimpan di kegiatan titik csv dan tetap ada saat program dijalankan lagi.

---

### Slide 29 — Latihan: L19, L20

*latihan · transisi `zoom` · 0 klik · ⏱ 23 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 2, bagian E dan F, dan kerjakan latihan L19 dan L20. Waktunya 40 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari2-functions-modules-file-handling.ipynb dan jalankan timer 40 menit (tekan Mulai).

---

### Slide 30 — Jebakan umum

*isi · transisi `slide` · 7 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Terakhir, tiga jebakan yang paling sering.

**Klik 1 →** — muncul: `f(1)`

> Pertama, memanggil function dengan argumen kurang.

**Klik 2 →** — muncul: `TypeError: f() missing 1 required positional argument: 'b'`

> Hasilnya TypeError: function meminta satu argumen posisi lagi, yaitu b.

**Klik 3 →** — muncul: `x += 1 # di dalam f()`

> Kedua, mengubah variabel global di dalam function.

**Klik 4 →** — muncul: `UnboundLocalError: cannot access local variable 'x' where it is not as`

> Hasilnya UnboundLocalError. Python menganggap x lokal karena ada penugasan. Solusinya pakai return.

**Klik 5 →** — muncul: `open("tidak_ada.txt")`

> Ketiga, membuka file yang belum ada.

**Klik 6 →** — muncul: `FileNotFoundError: [Errno 2] No such file or directory: 'tidak_ada.txt`

> Hasilnya FileNotFoundError.

**Klik 7 →** — muncul: `Periksa path dengan Path(...).exists(); path relatif bergantung pada f`

> Periksa path dengan Path exists. Ingat, path relatif bergantung pada folder tempat program dijalankan.

---

### Slide 31 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Rekap Hari 2.

**Klik 1 →** — muncul: `Function: parameter, default, *args/**kwargs, return vs print, scope`

> Function: parameter, default, args dan kwargs, return versus print, dan scope.

**Klik 2 →** — muncul: `Lambda, map/filter, comprehension, sorted(key=)`

> Lambda, map, filter, comprehension, dan sorted dengan key.

**Klik 3 →** — muncul: `Module & import; try/except/else/finally dan raise`

> Module dan import, try except else finally, dan raise.

**Klik 4 →** — muncul: `File teks & CSV dengan with + pathlib`

> File teks dan CSV dengan with dan pathlib.

**Klik 5 →** — muncul: `Mini project pencatat kegiatan yang persisten`

> Mini project pencatat kegiatan yang menyimpan datanya.

**Klik 6 →** — muncul: `Besok (Hari 3): Object-Oriented Programming`

> Jalankan sel Rekap hasil latihan. Besok, Hari 3: Object-Oriented Programming. Sampai jumpa!

🎬 **Aksi:** Tampilkan sel rekap di notebook.

---
