# Naskah Video — Hari 1: Python Fundamentals

Deck: [`hari1-python-fundamentals.html`](../hari1-python-fundamentals.html) · 30 slide · 114 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 15 mnt 16 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | Python Fundamentals | 0 | 21 dtk |
| 2 | Agenda | 8 | 40 dtk |
| 3 | Tujuan | 5 | 25 dtk |
| 4 | A. Variabel, Tipe Data & I/O | 0 | 10 dtk |
| 5 | Setup environment | 5 | 59 dtk |
| 6 | Variabel | 5 | 42 dtk |
| 7 | Tipe data & casting | 6 | 38 dtk |
| 8 | Operator | 6 | 48 dtk |
| 9 | f-string & input | 5 | 37 dtk |
| 10 | Latihan: L1, L2, L3, L4, L5 | 0 | 22 dtk |
| 11 | B. Control Flow | 0 | 7 dtk |
| 12 | if / elif / else | 5 | 40 dtk |
| 13 | for loop | 5 | 32 dtk |
| 14 | while loop | 9 | 48 dtk |
| 15 | Latihan: L6, L7, L8, L9, L10 | 0 | 22 dtk |
| 16 | Rehat | 0 | 13 dtk |
| 17 | C. Struktur Data | 0 | 8 dtk |
| 18 | List | 6 | 40 dtk |
| 19 | Tuple | 4 | 31 dtk |
| 20 | Dictionary | 6 | 41 dtk |
| 21 | Set | 5 | 35 dtk |
| 22 | List of dict | 3 | 29 dtk |
| 23 | Memilih struktur | 4 | 24 dtk |
| 24 | Latihan: L11, L12, L13, L14, L15, L16 | 0 | 22 dtk |
| 25 | PEP 8 | 5 | 29 dtk |
| 26 | D. Mini Project | 0 | 9 dtk |
| 27 | Alur menu | 9 | 42 dtk |
| 28 | Latihan: P1, P2 | 0 | 22 dtk |
| 29 | Jebakan umum | 7 | 42 dtk |
| 30 | Rekap | 6 | 38 dtk |

---

### Slide 1 — Python Fundamentals

*judul · transisi `zoom` · 0 klik · ⏱ 21 dtk*

**Saat slide muncul**

> Selamat datang di Python Intensive Bootcamp, hari pertama: Python Fundamentals. Hari ini kita mulai dari nol: variabel, alur logika, sampai struktur data, dan di akhir kita bangun menu interaktif untuk data mahasiswa. Formatnya sederhana: saya demo singkat, lalu Anda langsung mencoba di buku kerja.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 8 klik · ⏱ 40 dtk*

**Saat slide muncul**

> Ini agenda hari ini. Totalnya sekitar enam jam, dibagi menjadi beberapa blok.

**Klik 1 →** — muncul: `Opening + setup`

> Dimulai dengan pembukaan dan setup lingkungan, sekitar empat puluh menit.

**Klik 2 →** — muncul: `Variabel & I/O`

> Lalu variabel dan input-output, empat puluh lima menit.

**Klik 3 →** — muncul: `Control flow`

> Berikutnya control flow, yaitu percabangan dan perulangan, satu jam.

**Klik 4 →** — muncul: `Rehat`

> Setelah itu istirahat dua puluh lima menit.

**Klik 5 →** — muncul: `Struktur data`

> Sesudah istirahat, struktur data, delapan puluh lima menit, ini blok terpanjang.

**Klik 6 →** — muncul: `Mini project`

> Lalu mini project tujuh puluh lima menit, di mana semuanya kita gabungkan.

**Klik 7 →** — muncul: `Rekap`

> Dan ditutup dengan rekap tiga puluh menit.

**Klik 8 →** — muncul: `Total ±6 jam. Setiap blok: demo singkat → peserta coba sendiri di buku`

> Pola setiap blok sama: demo singkat, lalu Anda mencoba sendiri di buku kerja.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 5 klik · ⏱ 25 dtk*

**Saat slide muncul**

> Setelah hari ini, ada lima hal yang bisa Anda lakukan.

**Klik 1 →** — muncul: `menyiapkan environment Python (venv + Jupyter)`

> Pertama, menyiapkan environment Python dengan venv dan Jupyter.

**Klik 2 →** — muncul: `memakai variabel, tipe data, operator, dan f-string`

> Kedua, memakai variabel, tipe data, operator, dan f-string.

**Klik 3 →** — muncul: `membuat logika dengan if, for, while`

> Ketiga, membuat logika program dengan if, for, dan while.

**Klik 4 →** — muncul: `memilih list / tuple / dict / set yang tepat`

> Keempat, memilih struktur data yang tepat: list, tuple, dictionary, atau set.

**Klik 5 →** — muncul: `membuat menu interaktif data mahasiswa (Mini Project)`

> Dan kelima, membuat menu interaktif data mahasiswa sebagai mini project.

---

### Slide 4 — A. Variabel, Tipe Data & I/O

*bagian · transisi `rise` · 0 klik · ⏱ 10 dtk*

**Saat slide muncul**

> Bagian A: variabel, tipe data, dan input-output. Kita akan belajar menyimpan nilai, memahami tipenya, dan membaca masukan dari pengguna.

---

### Slide 5 — Setup environment

*isi · transisi `slide` · 5 klik · ⏱ 59 dtk*

**Saat slide muncul**

> Sebelum menulis kode, kita siapkan lingkungan kerja. Ikuti langkah ini di terminal.

**Klik 1 →**

> Pertama, pastikan Python terpasang dengan perintah python --version. Harusnya muncul Python 3.11 atau lebih baru.

🎬 **Aksi:** Ketik perintah di terminal dan tunjukkan versinya.

**Klik 2 →**

> Kedua, buat virtual environment dengan python -m venv .venv. Ini membuat folder terpisah khusus untuk proyek kita.

🎬 **Aksi:** Jalankan perintah, tunjukkan folder .venv muncul.

**Klik 3 →**

> Ketiga, aktifkan environment-nya. Di Linux atau Mac pakai source, di Windows pakai skrip activate di folder Scripts.

🎬 **Aksi:** Aktifkan environment.

**Klik 4 →** — muncul: `Cek: prompt berawalan (.venv) berarti environment aktif.`

> Setelah aktif, pasang paket yang kita perlukan, lalu jalankan jupyter notebook. Perhatikan prompt terminal sekarang berawalan kurung .venv, itu tanda environment aktif.

**Klik 5 →** — muncul: `Tanpa venv, paket antar-proyek bisa bentrok.`

> Kenapa repot memakai venv? Tanpa venv, paket antar proyek bisa saling bentrok. Pastikan semua peserta berhasil sampai tahap ini sebelum lanjut.

---

### Slide 6 — Variabel

*isi · transisi `slide` · 5 klik · ⏱ 42 dtk*

**Saat slide muncul**

> Konsep pertama dan terpenting: variabel. Variabel adalah nama yang menunjuk ke sebuah nilai.

**Klik 1 →** — muncul: `nama"Siti"str`

> Baris pertama: nama sama dengan teks Siti. Di sebelah kanan muncul kotak bernama nama, isinya Siti, bertipe str.

**Klik 2 →** — muncul: `umur20int`

> Baris kedua: umur sama dengan dua puluh. Isinya angka bulat, bertipe int.

**Klik 3 →** — muncul: `ipk3.67float`

> Baris ketiga: ipk sama dengan 3,67. Angka berkoma, bertipe float.

**Klik 4 →** — muncul: `aktifTruebool`

> Baris keempat: aktif sama dengan True. Nilai benar atau salah, bertipe bool.

**Klik 5 →** — muncul: `umur = umur + 1`

> Dan nilai variabel boleh diganti. Perhatikan: umur sama dengan umur ditambah satu, dan kotak umur berubah dari dua puluh menjadi dua puluh satu. Tipe mengikuti nilainya, bukan namanya.

---

### Slide 7 — Tipe data & casting

*isi · transisi `slide` · 6 klik · ⏱ 38 dtk*

**Saat slide muncul**

> Selanjutnya tipe data dan casting, yaitu mengubah tipe suatu nilai.

**Klik 1 →** — muncul: `<class 'str'> <class 'int'> <class 'float'> <class 'bool'>`

> Fungsi type memberi tahu tipe sebuah nilai: str, int, float, dan bool.

**Klik 2 →** — muncul: `50`

> int dari teks empat puluh dua menghasilkan angka bulat, sehingga ditambah delapan hasilnya lima puluh.

**Klik 3 →** — muncul: `7.0`

> float dari teks 3,5 dikali dua menghasilkan 7,0.

**Klik 4 →** — muncul: `3`

> Hati-hati: int dari 3,9 menghasilkan tiga. Angkanya dipotong, bukan dibulatkan.

**Klik 5 →** — muncul: `False False True`

> Tentang bool: nol, teks kosong dianggap False, sedangkan teks yang berisi dianggap True.

**Klik 6 →**

> Satu catatan penting: input selalu menghasilkan teks, jadi ubah dulu dengan int atau float sebelum dihitung.

---

### Slide 8 — Operator

*isi · transisi `slide` · 6 klik · ⏱ 48 dtk*

**Saat slide muncul**

> Sekarang operator.

**Klik 1 →** — muncul: `//pembagian bulat`

> Pembagian bulat memakai dua garis miring: tujuh belas dibagi lima, hasilnya tiga. Bandingkan dengan satu garis miring yang menghasilkan 3,5.

**Klik 2 →** — muncul: `%sisa bagi`

> Persen memberi sisa bagi, dan perbandingan bisa dirantai: enam puluh sampai tujuh puluh delapan sampai sembilan puluh, hasilnya True.

**Klik 3 →** — muncul: `**pangkat`

> Dua bintang berarti pangkat: dua pangkat delapan adalah dua ratus lima puluh enam.

**Klik 4 →** — muncul: `total = 10`

> Operator penugasan seperti plus sama dengan menambah nilai variabel itu sendiri: total sepuluh ditambah lima menjadi lima belas. Operator logika and, or, dan not menggabungkan kondisi.

**Klik 5 →**

> Silakan ulangi contoh ini di notebook Anda, ubah angkanya, dan amati hasilnya.

**Klik 6 →**

> Kalau sudah paham, kita lanjut ke input dan f-string.

---

### Slide 9 — f-string & input

*isi · transisi `slide` · 5 klik · ⏱ 37 dtk*

**Saat slide muncul**

> Sekarang kita buat program yang berinteraksi dengan pengguna.

**Klik 1 →**

> Fungsi input menampilkan pertanyaan dan menunggu ketikan pengguna.

**Klik 2 →**

> Nilai dari input perlu diubah dengan float agar bisa dihitung.

**Klik 3 →** — muncul: `print(f"{nama} mendapat {nilai:.1f}")`

> Terakhir, f-string: awali teks dengan huruf f, lalu taruh variabel dalam kurung kurawal. Kode petik titik satu f berarti satu angka di belakang koma.

🎬 **Aksi:** Jalankan di notebook dan ketik input Anda sendiri.

**Klik 4 →** — muncul: `Nilai: 88.5`

> Contoh: nama Rina dan nilai delapan puluh delapan koma lima.

**Klik 5 →** — muncul: `Rina mendapat 88.5`

> Hasilnya: Rina mendapat delapan puluh delapan koma lima. Mudah dibaca dibanding menggabung teks dengan plus.

---

### Slide 10 — Latihan: L1, L2, L3, L4, L5

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 1, bagian A, dan kerjakan latihan L1 sampai L5. Waktunya 15 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari1-python-fundamentals.ipynb dan jalankan timer 15 menit (tekan Mulai).

---

### Slide 11 — B. Control Flow

*bagian · transisi `rise` · 0 klik · ⏱ 7 dtk*

**Saat slide muncul**

> Bagian B: control flow. Cara membuat program memilih jalur dan mengulang pekerjaan.

---

### Slide 12 — if / elif / else

*isi · transisi `slide` · 5 klik · ⏱ 40 dtk*

**Saat slide muncul**

> Percabangan if, elif, else: dari beberapa jalur, hanya satu yang dijalankan. Mari ikuti alurnya dengan nilai tujuh puluh delapan.

**Klik 1 →** — muncul: `nilai = 78`

> Kita mulai dengan nilai sama dengan tujuh puluh delapan.

**Klik 2 →** — muncul: `if nilai >= 85:`

> Pertama dicek: apakah nilai lebih dari atau sama dengan delapan puluh lima? Tujuh puluh delapan tidak, jadi cabang A dilewati.

**Klik 3 →** — muncul: `elif nilai >= 70:`

> Lanjut ke elif: apakah nilai lebih dari atau sama dengan tujuh puluh? Ya.

**Klik 4 →** — muncul: `grade = "B"`

> Maka grade diisi B. Cabang else tidak dijalankan sama sekali.

**Klik 5 →** — muncul: `print(grade)`

> Setelah itu program lanjut ke print grade yang menampilkan B. Ingat: cek dari batas tertinggi ke terendah.

---

### Slide 13 — for loop

*isi · transisi `slide` · 5 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Perulangan for mengulang untuk setiap elemen. Di sini range satu sampai enam menghasilkan angka satu sampai lima; angka enam tidak ikut karena batas akhirnya tidak dihitung.

**Klik 1 →** — muncul: `print(i * i)`

> Putaran pertama: i bernilai satu, dan i kali i menghasilkan satu.

**Klik 2 →** — muncul: `4`

> Putaran kedua: i bernilai dua, hasilnya empat.

**Klik 3 →** — muncul: `9`

> Putaran ketiga: i tiga, hasilnya sembilan.

**Klik 4 →** — muncul: `16`

> Putaran keempat: i empat, hasilnya enam belas.

**Klik 5 →** — muncul: `25`

> Putaran terakhir: i lima, hasilnya dua puluh lima. Setelah itu loop selesai.

---

### Slide 14 — while loop

*isi · transisi `slide` · 9 klik · ⏱ 48 dtk*

**Saat slide muncul**

> Perulangan while mengulang selama kondisi bernilai benar. Kita ikuti satu putaran demi satu.

**Klik 1 →** — muncul: `sisa = 3`

> Variabel sisa diisi tiga.

**Klik 2 →** — muncul: `while sisa > 0:`

> Program mengecek: sisa lebih dari nol?

**Klik 3 →** — muncul: `print(sisa)`

> Ya, jadi badan loop jalan: mencetak tiga, lalu sisa dikurangi satu menjadi dua.

**Klik 4 →** — muncul: `2`

> Cek lagi: dua lebih dari nol, ya. Cetak dua.

**Klik 5 →** — muncul: `sisa1int`

> Sisa menjadi satu. Cek lagi: satu lebih dari nol, ya. Cetak satu.

**Klik 6 →** — muncul: `selesai`

> Sekarang cetak satu selesai, dan sisa menjadi nol.

**Klik 7 →** — muncul: `sisa0int`

> Cek lagi: nol lebih dari nol? Tidak.

**Klik 8 →**

> Loop berhenti dan program mencetak selesai.

**Klik 9 →** — muncul: `print("selesai")`

> Peringatan: kalau baris sisa dikurangi satu terlupa, kondisi tidak pernah salah dan loop tak pernah berhenti. Kalau itu terjadi di notebook, tekan Interrupt kernel.

---

### Slide 15 — Latihan: L6, L7, L8, L9, L10

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 1, bagian B, dan kerjakan latihan L6 sampai L10. Waktunya 15 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari1-python-fundamentals.ipynb dan jalankan timer 15 menit (tekan Mulai).

---

### Slide 16 — Rehat

*isi · transisi `slide` · 0 klik · ⏱ 13 dtk*

**Saat slide muncul**

> Waktunya istirahat sekitar dua puluh lima menit. Kembali tepat waktu, karena berikutnya kita masuk ke struktur data.

🎬 **Aksi:** Jeda video; tampilkan timer istirahat.

---

### Slide 17 — C. Struktur Data

*bagian · transisi `rise` · 0 klik · ⏱ 8 dtk*

**Saat slide muncul**

> Bagian C: struktur data. Kita belajar list, tuple, dictionary, set, dan list of dict.

---

### Slide 18 — List

*isi · transisi `slide` · 6 klik · ⏱ 40 dtk*

**Saat slide muncul**

> List adalah urutan nilai yang bisa diubah. Indeks dimulai dari nol.

**Klik 1 →**

> Kita punya list berisi delapan puluh, sembilan puluh, tujuh puluh lima, dan delapan puluh delapan. Kotak di kanan menunjukkan nomor indeksnya.

**Klik 2 →** — muncul: `print(nilai[0])`

> nilai kurung siku nol mengambil elemen pertama, yaitu delapan puluh.

**Klik 3 →** — muncul: `print(nilai[-1])`

> Indeks minus satu mengambil elemen terakhir, yaitu delapan puluh delapan.

**Klik 4 →** — muncul: `print(nilai[1:3])`

> Irisan satu titik dua tiga mengambil indeks satu dan dua, yaitu sembilan puluh dan tujuh puluh lima. Batas akhir tidak ikut.

**Klik 5 →** — muncul: `nilai.append(95)`

> Method append menambahkan elemen baru di ujung: sembilan puluh lima.

**Klik 6 →** — muncul: `print(nilai)`

> Dan ketika di-print, list sudah berisi lima elemen.

---

### Slide 19 — Tuple

*isi · transisi `slide` · 4 klik · ⏱ 31 dtk*

**Saat slide muncul**

> Tuple mirip list tetapi tidak bisa diubah setelah dibuat. Cocok untuk data tetap seperti koordinat.

**Klik 1 →**

> Koordinat berisi minus enam koma dua dan seratus enam koma delapan, dua elemen dengan indeks nol dan satu.

**Klik 2 →** — muncul: `lat, lon = koordinat`

> Dengan unpacking, setiap elemen langsung masuk ke satu variabel: lat dan lon terisi sekaligus, berurutan.

**Klik 3 →** — muncul: `print(lat, lon)`

> Hasil print: minus enam koma dua, seratus enam koma delapan.

**Klik 4 →** — muncul: `Tuple tidak bisa diubah setelah dibuat — cocok untuk data yang tetap.`

> Ingat, tuple tidak bisa diubah setelah dibuat.

---

### Slide 20 — Dictionary

*isi · transisi `slide` · 6 klik · ⏱ 41 dtk*

**Saat slide muncul**

> Dictionary menyimpan pasangan key dan value. Akses datanya lewat label, bukan nomor urut.

**Klik 1 →** — muncul: `mhs = {`

> Kita buat dictionary mahasiswa dengan tiga pasang: nama, nim, dan ipk.

**Klik 2 →** — muncul: `print(mhs["nama"])`

> mhs kurung siku nama mengambil nilainya, yaitu Budi.

**Klik 3 →** — muncul: `belum diisi`

> Kalau key tidak ada, get dengan nilai default memberi belum diisi, tanpa error.

**Klik 4 →** — muncul: `mhs["prodi"] = "Informatika"`

> Menambah key baru cukup dengan menugaskan: prodi sama dengan Informatika. Baris baru muncul di tabel.

**Klik 5 →** — muncul: `mhs["ipk"] = 3.7`

> Mengubah nilai yang ada juga sama: ipk menjadi tiga koma tujuh.

**Klik 6 →** — muncul: `Akses langsung mhs["prodi"] yang belum ada → KeyError; .get(key, defau`

> Peringatan: mengakses key yang belum ada langsung dengan kurung siku menghasilkan KeyError. Pakai get agar aman.

---

### Slide 21 — Set

*isi · transisi `slide` · 5 klik · ⏱ 35 dtk*

**Saat slide muncul**

> Set adalah kumpulan nilai unik dengan operasi himpunan. Kita punya dua set hobi, a dan b.

**Klik 1 →**

> Kita definisikan dua set: a berisi baca, musik, olahraga; b berisi musik, gaming, olahraga.

**Klik 2 →** — muncul: `print(a | b) # gabungan`

> Garis tegak lurus menghasilkan gabungan: semua elemen dari keduanya, tanpa duplikat.

**Klik 3 →** — muncul: `print(a & b) # irisan`

> Tanda dan menghasilkan irisan: yang ada di kedua set, yaitu musik dan olahraga.

**Klik 4 →** — muncul: `print(a - b) # hanya di a`

> Tanda minus menghasilkan elemen yang hanya ada di a, yaitu baca.

**Klik 5 →** — muncul: `Hapus duplikat: list(set([1, 2, 2, 3])) → [1, 2, 3]`

> Kegunaan praktis: menghapus duplikat dari list dengan list dari set.

---

### Slide 22 — List of dict

*isi · transisi `slide` · 3 klik · ⏱ 29 dtk*

**Saat slide muncul**

> List of dict adalah pola data yang akan paling sering kita pakai: list sebagai kumpulan baris, dan setiap dictionary adalah satu mahasiswa.

**Klik 1 →**

> Ini tabel mahasiswa kita: Ani, Budi, dan Cici dengan ipk dan prodinya. Ini struktur utama mini project nanti.

**Klik 2 →** — muncul: `IF → Ani, Cici`

> List comprehension memfilter prodi IF, hasilnya Ani dan Cici.

**Klik 3 →** — muncul: `terbaik = max(mahasiswa, key=lambda m: m["ipk"])`

> Fungsi max dengan key lambda mencari mahasiswa dengan ipk tertinggi, yaitu Budi.

---

### Slide 23 — Memilih struktur

*isi · transisi `slide` · 4 klik · ⏱ 24 dtk*

**Saat slide muncul**

> Bagaimana memilih struktur yang tepat? Ini ringkasannya.

**Klik 1 →** — muncul: `listurutan penting, boleh berubahdaftar nilai, daftar MK`

> List: bila urutan penting dan datanya boleh berubah, misalnya daftar nilai.

**Klik 2 →** — muncul: `tupledata tetap / return beberapa nilaikoordinat, (nim, nama)`

> Tuple: untuk data tetap atau mengembalikan beberapa nilai sekaligus, misalnya koordinat.

**Klik 3 →** — muncul: `dictbutuh label / lookup cepatprofil mahasiswa, map MK→nilai`

> Dictionary: bila butuh label atau pencarian cepat, misalnya profil mahasiswa.

**Klik 4 →** — muncul: `setunik & operasi himpunanhobi, deduplikasi`

> Set: bila butuh nilai unik dan operasi himpunan, misalnya hobi atau deduplikasi.

---

### Slide 24 — Latihan: L11, L12, L13, L14, L15, L16

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 1, bagian C, dan kerjakan latihan L11 sampai L16. Waktunya 20 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari1-python-fundamentals.ipynb dan jalankan timer 20 menit (tekan Mulai).

---

### Slide 25 — PEP 8

*isi · transisi `slide` · 5 klik · ⏱ 29 dtk*

**Saat slide muncul**

> Sedikit tentang gaya penulisan kode: PEP 8.

**Klik 1 →** — muncul: `Kurang baik`

> Contoh kurang baik: nama fungsi huruf besar satu huruf, tidak ada spasi, indentasi dua spasi.

**Klik 2 →** — muncul: `Lebih baik`

> Dan ini versi yang lebih baik: nama bermakna, spasi rapi, indentasi empat spasi.

**Klik 3 →** — muncul: `indentasi 4 spasi, nama snake_case yang bermakna`

> Pakai indentasi empat spasi dan nama snake case yang bermakna.

**Klik 4 →** — muncul: `spasi di sekitar operator & setelah koma`

> Beri spasi di sekitar operator dan setelah koma.

**Klik 5 →** — muncul: `konstanta HURUF_BESAR, class PascalCase`

> Konstanta ditulis huruf besar semua, sedangkan nama class memakai PascalCase.

---

### Slide 26 — D. Mini Project

*bagian · transisi `rise` · 0 klik · ⏱ 9 dtk*

**Saat slide muncul**

> Bagian D: mini project, sistem data mahasiswa dan sistem nilai. Di sini semua yang kita pelajari digabungkan.

---

### Slide 27 — Alur menu

*isi · transisi `slide` · 9 klik · ⏱ 42 dtk*

**Saat slide muncul**

> Mini project pertama: menu interaktif. Ini alurnya.

**Klik 1 →**

> Program menampilkan menu lalu meminta pilihan dengan input.

**Klik 2 →**

> Jika memilih satu, program memanggil function tambah.

**Klik 3 →**

> Pilihan dua memanggil function tampilkan.

**Klik 4 →**

> Pilihan tiga memanggil function cari berdasarkan NIM.

**Klik 5 →**

> Pilihan empat menghapus data berdasarkan NIM.

**Klik 6 →**

> Pilihan lima menampilkan mahasiswa dengan IPK tertinggi.

**Klik 7 →**

> Setelah setiap aksi, program kembali ke menu untuk putaran berikutnya.

**Klik 8 →** — muncul: `pilih 6`

> Sampai pengguna memilih enam, dan program keluar dengan break.

**Klik 9 →** — muncul: `Function terpisah untuk tiap fitur + while True untuk menu. Validasi: `

> Kuncinya: satu function terpisah untuk setiap fitur, dan while True untuk menu. Jangan lupa validasi: IPK harus nol sampai empat, dan NIM tidak boleh ganda.

---

### Slide 28 — Latihan: P1, P2

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 1, bagian D, dan kerjakan latihan P1 dan P2. Waktunya 35 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari1-python-fundamentals.ipynb dan jalankan timer 35 menit (tekan Mulai).

---

### Slide 29 — Jebakan umum

*isi · transisi `slide` · 7 klik · ⏱ 42 dtk*

**Saat slide muncul**

> Terakhir, jebakan yang paling sering ditemui pemula. Ketiganya muncul sebagai pesan error.

**Klik 1 →** — muncul: `print(nama)`

> Pertama: mencetak variabel nama padahal belum pernah dibuat.

**Klik 2 →** — muncul: `NameError: name 'nama' is not defined`

> Hasilnya NameError: name nama is not defined. Biasanya salah ketik atau belum dibuat.

**Klik 3 →** — muncul: `print("Nilai: " + 80)`

> Kedua: menggabungkan teks dengan angka memakai plus.

**Klik 4 →** — muncul: `TypeError: can only concatenate str (not "int") to str`

> Hasilnya TypeError: bisa menggabung hanya teks dengan teks. Ubah angkanya dengan str atau pakai f-string.

**Klik 5 →** — muncul: `mhs["nim"]`

> Ketiga: mengakses key dictionary yang tidak ada.

**Klik 6 →** — muncul: `KeyError: 'nim'`

> Hasilnya KeyError. Cek key-nya atau pakai get.

**Klik 7 →** — muncul: `Baca pesan error dari baris paling bawah ke atas: jenis error → apa ya`

> Kebiasaan penting: baca pesan error dari baris paling bawah ke atas. Pertama jenis errornya, kedua apa yang salah, ketiga di baris mana.

---

### Slide 30 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 38 dtk*

**Saat slide muncul**

> Mari rekap Hari 1.

**Klik 1 →** — muncul: `Variabel & tipe: int float str bool, casting, f-string`

> Kita belajar variabel dan tipe: int, float, str, bool, plus casting dan f-string.

**Klik 2 →** — muncul: `Percabangan if/elif/else dan perulangan for / while`

> Percabangan if, elif, else dan perulangan for dan while.

**Klik 3 →** — muncul: `Struktur data: list, tuple, dict, set, list of dict`

> Struktur data: list, tuple, dictionary, set, dan list of dict.

**Klik 4 →** — muncul: `Mini project: menu data mahasiswa dengan function`

> Mini project: menu data mahasiswa yang dibangun dengan function.

**Klik 5 →** — muncul: `Semua latihan buku kerja ✅ (rekap skor di sel terakhir)`

> Jalankan sel Rekap hasil latihan di akhir notebook untuk melihat skor Anda.

🎬 **Aksi:** Tampilkan sel rekap di notebook.

**Klik 6 →** — muncul: `Besok (Hari 2): Functions, Modules & File Handling`

> Besok, Hari 2: Functions, Modules, dan File Handling. Terima kasih, sampai jumpa besok!

---
