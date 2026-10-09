# Naskah Video — Hari 3: Object-Oriented Programming

Deck: [`hari3-oop.html`](../hari3-oop.html) · 24 slide · 78 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 10 mnt 13 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | Object-Oriented Programming | 0 | 12 dtk |
| 2 | Agenda | 9 | 34 dtk |
| 3 | Tujuan | 6 | 26 dtk |
| 4 | A. Class & Object | 0 | 6 dtk |
| 5 | Class & object | 6 | 56 dtk |
| 6 | Class vs instance attribute | 5 | 36 dtk |
| 7 | Latihan: L1, L2, L3 | 0 | 22 dtk |
| 8 | B. Inheritance & Polimorfisme | 0 | 6 dtk |
| 9 | Inheritance | 6 | 37 dtk |
| 10 | super() | 4 | 26 dtk |
| 11 | Latihan: L4, L5 | 0 | 22 dtk |
| 12 | Rehat | 0 | 12 dtk |
| 13 | C. Encapsulation, Special Methods & Context Manager | 0 | 9 dtk |
| 14 | Encapsulation | 5 | 40 dtk |
| 15 | Special methods | 7 | 48 dtk |
| 16 | Context manager | 6 | 36 dtk |
| 17 | Latihan: L6, L7, L8, L9 | 0 | 22 dtk |
| 18 | D. Jebakan Umum | 0 | 6 dtk |
| 19 | Mutable default | 5 | 30 dtk |
| 20 | Error umum | 6 | 26 dtk |
| 21 | E. Mini Project | 0 | 6 dtk |
| 22 | Rancang class | 7 | 42 dtk |
| 23 | Latihan: P1, P2 | 0 | 22 dtk |
| 24 | Rekap | 6 | 31 dtk |

---

### Slide 1 — Object-Oriented Programming

*judul · transisi `zoom` · 0 klik · ⏱ 12 dtk*

**Saat slide muncul**

> Selamat datang di hari ketiga: Object-Oriented Programming. Hari ini kita belajar membungkus data dan perilaku dalam class, supaya program besar tetap rapi.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 9 klik · ⏱ 34 dtk*

**Saat slide muncul**

> Agenda hari ketiga, sekitar enam jam.

**Klik 1 →** — muncul: `Opening`

> Pembukaan dua puluh lima menit.

**Klik 2 →** — muncul: `Class & object`

> Class dan object, tujuh puluh menit.

**Klik 3 →** — muncul: `Inheritance`

> Inheritance, enam puluh menit.

**Klik 4 →** — muncul: `Rehat`

> Istirahat dua puluh menit.

**Klik 5 →** — muncul: `Encapsulation & special`

> Encapsulation, special methods, dan context manager, tujuh puluh menit.

**Klik 6 →** — muncul: `Jebakan`

> Jebakan umum, dua puluh menit.

**Klik 7 →** — muncul: `Mini project`

> Mini project berbasis class, delapan puluh menit.

**Klik 8 →** — muncul: `Rekap`

> Dan rekap lima belas menit.

**Klik 9 →** — muncul: `Total ±6 jam. Demo singkat → peserta coba di buku kerja.`

> Polanya sama: demo singkat, lalu latihan di buku kerja.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 6 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Tujuan hari ini ada enam.

**Klik 1 →** — muncul: `menjelaskan class vs object, attribute vs method`

> Menjelaskan perbedaan class dan object, serta attribute dan method.

**Klik 2 →** — muncul: `menulis __init__ dan memakai self`

> Menulis init dan memakai self.

**Klik 3 →** — muncul: `membedakan class attribute dan instance attribute`

> Membedakan class attribute dan instance attribute.

**Klik 4 →** — muncul: `memakai inheritance, super(), dan override`

> Memakai inheritance, super, dan override.

**Klik 5 →** — muncul: `menjaga data lewat encapsulation, @property, dan special methods (__st`

> Menjaga data dengan encapsulation, property, dan special methods seperti str dan eq.

**Klik 6 →** — muncul: `membangun mini project berbasis class`

> Dan membangun mini project berbasis class.

---

### Slide 4 — A. Class & Object

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian A: class dan object. Cetak biru dan benda nyata.

---

### Slide 5 — Class & object

*isi · transisi `slide` · 6 klik · ⏱ 56 dtk*

**Saat slide muncul**

> Class adalah cetak biru, object adalah benda yang dibuat dari cetak biru itu. Lihat bagaimana keduanya terhubung.

**Klik 1 →** — muncul: `class Mahasiswa:`

> Kita mulai dengan mendefinisikan class Mahasiswa. Di kanan, kotak putus-putus mewakili cetak biru.

**Klik 2 →** — muncul: `def __init__(self, nama, ipk):`

> Method init dijalankan otomatis saat object dibuat. Ia menerima nama dan ipk, lalu menyimpannya di self titik nama dan self titik ipk. Self adalah object yang sedang dipakai.

**Klik 3 →** — muncul: `def info(self):`

> Lalu method info mengembalikan kalimat berisi nama dan ipk. Method adalah function milik class.

**Klik 4 →** — muncul: `m1 = Mahasiswa("Ani", 3.7)`

> Sekarang kita buat object pertama: m1 sama dengan Mahasiswa Ani, ipk tiga koma tujuh. Kartu m1 muncul dengan data miliknya sendiri.

**Klik 5 →** — muncul: `m2 = Mahasiswa("Budi", 3.2)`

> Object kedua, m2, Budi dengan ipk tiga koma dua. Datanya terpisah dari m1, tapi dibuat dari cetak biru yang sama.

**Klik 6 →** — muncul: `print(m1.info())`

> Dan saat m1 titik info dipanggil, tercetak Ani, ipk tiga koma tujuh.

---

### Slide 6 — Class vs instance attribute

*isi · transisi `slide` · 5 klik · ⏱ 36 dtk*

**Saat slide muncul**

> Attribute bisa dimiliki class atau dimiliki object. Bedanya penting.

**Klik 1 →** — muncul: `sekolah = "SMA 1" # class attribute`

> Sekolah dan jumlah didefinisikan langsung di class. Itu class attribute, dibagi oleh semua object.

**Klik 2 →** — muncul: `self.nama = nama # instance attribute`

> Sedangkan self titik nama di dalam init adalah instance attribute, milik masing-masing object.

**Klik 3 →** — muncul: `Siswa.jumlah += 1`

> Dan Siswa titik jumlah ditambah satu setiap object dibuat, berfungsi sebagai penghitung bersama.

**Klik 4 →** — muncul: `print(a.nama, b.nama, a.sekolah, Siswa.jumlah)`

> Kita buat dua siswa, Ani dan Budi. Hasilnya: nama masing-masing berbeda, sekolah sama, dan jumlah dua.

**Klik 5 →** — muncul: `Class attribute: dibagi semua object (mis. penghitung). Instance attri`

> Rangkumannya: class attribute dibagi semua object, instance attribute milik object masing-masing.

---

### Slide 7 — Latihan: L1, L2, L3

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 3, bagian A, dan kerjakan latihan L1 sampai L3. Waktunya 35 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari3-oop.ipynb dan jalankan timer 35 menit (tekan Mulai).

---

### Slide 8 — B. Inheritance & Polimorfisme

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian B: inheritance dan polimorfisme. Mewarisi dan menimpa perilaku.

---

### Slide 9 — Inheritance

*isi · transisi `slide` · 6 klik · ⏱ 37 dtk*

**Saat slide muncul**

> Inheritance memungkinkan class baru mewarisi attribute dan method dari class lain.

**Klik 1 →** — muncul: `class Hewan:`

> Hewan adalah class induk. Ia punya nama dan method suara yang mengembalikan tiga titik.

**Klik 2 →** — muncul: `class Kucing(Hewan):`

> Kucing mewarisi Hewan, dan menimpa method suara menjadi meong. Itu disebut override.

**Klik 3 →** — muncul: `class Anjing(Hewan):`

> Anjing juga mewarisi Hewan, tapi menambah attribute ras, dan memanggil super titik init agar nama tetap terisi.

**Klik 4 →** — muncul: `return "guk"`

> Method suara pada Anjing di-override menjadi guk.

**Klik 5 →** — muncul: `print(h.nama, h.suara())`

> Sekarang satu loop memanggil suara pada object yang berbeda-beda. Mimi menjawab meong.

**Klik 6 →** — muncul: `Rex guk`

> Dan Rex menjawab guk. Pemanggilan sama, perilaku berbeda: itulah polimorfisme.

---

### Slide 10 — super()

*isi · transisi `slide` · 4 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Salah satu jebakan terbesar inheritance adalah lupa memanggil super.

**Klik 1 →** — muncul: `Lupa memanggil super().__init__()`

> Di sini class Anjing punya init sendiri, tetapi tidak memanggil super titik init, jadi nama tidak pernah diisi.

**Klik 2 →** — muncul: `AttributeError: 'A' object has no attribute 'nama'`

> Akibatnya AttributeError: object tidak punya attribute nama.

**Klik 3 →** — muncul: `Benar`

> Cara yang benar: panggil super titik init dengan nama terlebih dahulu, baru isi ras.

**Klik 4 →** — muncul: `Rex Husky`

> Hasilnya, Rex Husky dengan nama dan ras terisi.

---

### Slide 11 — Latihan: L4, L5

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 3, bagian B, dan kerjakan latihan L4 dan L5. Waktunya 35 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari3-oop.ipynb dan jalankan timer 35 menit (tekan Mulai).

---

### Slide 12 — Rehat

*isi · transisi `slide` · 0 klik · ⏱ 12 dtk*

**Saat slide muncul**

> Waktunya istirahat sekitar 20 menit. Setelah ini kita lanjut ke encapsulation dan special methods.

🎬 **Aksi:** Jeda video; tampilkan timer istirahat.

---

### Slide 13 — C. Encapsulation, Special Methods & Context Manager

*bagian · transisi `rise` · 0 klik · ⏱ 9 dtk*

**Saat slide muncul**

> Bagian C: encapsulation, special methods, dan context manager. Menjaga data dan membuat object berperilaku seperti Python.

---

### Slide 14 — Encapsulation

*isi · transisi `slide` · 5 klik · ⏱ 40 dtk*

**Saat slide muncul**

> Encapsulation berarti melindungi data dan memberi pintu resmi untuk mengubahnya.

**Klik 1 →** — muncul: `self._saldo = saldo`

> Saldo disimpan di attribute bernama garis bawah saldo. Awalan garis bawah artinya jangan disentuh dari luar.

**Klik 2 →** — muncul: `@property`

> Property membuat saldo bisa dibaca seperti attribute biasa, tetapi tidak bisa diubah sembarangan.

**Klik 3 →** — muncul: `def setor(self, jumlah):`

> Satu-satunya cara menambah saldo adalah method setor, yang memvalidasi: jumlah harus lebih dari nol, kalau tidak raise ValueError.

**Klik 4 →** — muncul: `r = Rekening(100)`

> Kita buat rekening dengan saldo seratus, setor lima puluh, dan saldo menjadi seratus lima puluh.

**Klik 5 →** — muncul: `r.setor(-5) → ValueError: jumlah harus > 0`

> Setor minus lima ditolak dengan ValueError: jumlah harus lebih dari nol. Data tetap aman.

---

### Slide 15 — Special methods

*isi · transisi `slide` · 7 klik · ⏱ 48 dtk*

**Saat slide muncul**

> Special methods, yang diawali dan diakhiri dua garis bawah, membuat object kita terasa alami di Python.

**Klik 1 →** — muncul: `def __str__(self):`

> Str menentukan tampilan saat object di-print. Tanpa str, yang muncul hanya alamat memori.

**Klik 2 →** — muncul: `def __repr__(self):`

> Repr menentukan tampilan untuk debugging dan untuk fungsi repr.

**Klik 3 →** — muncul: `def __eq__(self, other):`

> Eq menentukan arti dari tanda sama dengan sama dengan antar dua object.

**Klik 4 →** — muncul: `print(b1)`

> Print b1 menghasilkan Python, tahun dua ribu dua puluh empat, memakai str.

**Klik 5 →** — muncul: `print(repr(b1))`

> Repr b1 menghasilkan bentuk lengkap Buku dengan kurung dan tanda kutip.

**Klik 6 →** — muncul: `print(b1 == b2, b1 is b2)`

> Dan membandingkan b1 dengan b2 menghasilkan True lewat eq, tetapi b1 is b2 adalah False karena keduanya object yang berbeda.

**Klik 7 →** — muncul: `__str__ harus return string — bukan print.`

> Ingat: str harus mengembalikan string dengan return, bukan mencetaknya dengan print.

---

### Slide 16 — Context manager

*isi · transisi `slide` · 6 klik · ⏱ 36 dtk*

**Saat slide muncul**

> Context manager memungkinkan blok with: sesuatu disiapkan di awal dan dibereskan di akhir.

**Klik 1 →**

> Kita pakai with FileCatatan log titik txt as f.

**Klik 2 →** — muncul: `def __enter__(self):`

> Saat with dimulai, method enter dipanggil otomatis. Ia mencetak buka dan mengembalikan self.

**Klik 3 →** — muncul: `print("bekerja dengan", f.nama)`

> Lalu isi blok with dijalankan: bekerja dengan log titik txt.

**Klik 4 →** — muncul: `def __exit__(self, tipe, nilai, tb):`

> Saat blok selesai, method exit dipanggil otomatis, mencetak tutup.

**Klik 5 →** — muncul: `bekerja dengan log.txt`

> Hasilnya tiga baris: buka, bekerja dengan, tutup.

**Klik 6 →** — muncul: `tutup log.txt`

> Exit selalu dipanggil walau terjadi error di dalam blok. Itulah mengapa with open itu aman.

---

### Slide 17 — Latihan: L6, L7, L8, L9

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 3, bagian C, dan kerjakan latihan L6 sampai L9. Waktunya 35 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari3-oop.ipynb dan jalankan timer 35 menit (tekan Mulai).

---

### Slide 18 — D. Jebakan Umum

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian D: jebakan umum, yaitu kesalahan klasik dalam OOP.

---

### Slide 19 — Mutable default

*isi · transisi `slide` · 5 klik · ⏱ 30 dtk*

**Saat slide muncul**

> Jebakan pertama: mutable default argument.

**Klik 1 →** — muncul: `def __init__(self, isi=[]):`

> Parameter isi diberi default list kosong. Kelihatannya aman, tapi bermasalah.

**Klik 2 →** — muncul: `a, b = Keranjang(), Keranjang()`

> Kita buat dua keranjang, a dan b, tanpa memberi argumen.

**Klik 3 →** — muncul: `a.isi.append("apel")`

> Kita tambah apel hanya ke keranjang a.

**Klik 4 →** — muncul: `print(b.isi)`

> Tapi saat isi b dicetak, ternyata ada apel juga. Semua object berbagi list yang sama, karena default dibuat sekali saja saat function didefinisikan.

**Klik 5 →** — muncul: `def __init__(self, isi=None): self.isi = isi or []`

> Perbaikannya: default None, lalu buat list baru di dalam init.

---

### Slide 20 — Error umum

*isi · transisi `slide` · 6 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Tiga error yang paling sering di OOP.

**Klik 1 →** — muncul: `A()`

> Pertama, membuat object tanpa argumen yang dibutuhkan init.

**Klik 2 →** — muncul: `TypeError: A.__init__() missing 1 required positional argument: 'x'`

> Hasilnya TypeError: init kekurangan satu argumen posisi.

**Klik 3 →** — muncul: `def f():`

> Kedua, method yang lupa diberi parameter self.

**Klik 4 →** — muncul: `TypeError: A.f() takes 0 positional arguments but 1 was given`

> Hasilnya TypeError: method menerima nol argumen tapi satu diberikan. Python otomatis mengirim self.

**Klik 5 →** — muncul: `A().nama`

> Ketiga, mengakses attribute yang tidak ada.

**Klik 6 →** — muncul: `AttributeError: 'A' object has no attribute 'nama'`

> Hasilnya AttributeError: object tidak punya attribute nama.

---

### Slide 21 — E. Mini Project

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian E: mini project berbasis class, sistem perpustakaan atau inventaris.

---

### Slide 22 — Rancang class

*isi · transisi `slide` · 7 klik · ⏱ 42 dtk*

**Saat slide muncul**

> Sebelum menulis kode, rancang class-nya. Ini kebiasaan yang membedakan program rapi.

**Klik 1 →** — muncul: `◆Bukujudul, penulis, tersedia`

> Tanyakan: object apa yang ada, data apa yang dimilikinya, dan aksi apa yang dilakukan. Pertama kita punya Buku, dengan judul, penulis, dan status tersedia.

**Klik 2 →** — muncul: `◆Perpustakaandaftar_buku (list of Buku)`

> Lalu Perpustakaan, yang menyimpan daftar buku, yaitu list of Buku.

**Klik 3 →** — muncul: `▪tambah(buku)`

> Aksi pertama: tambah buku.

**Klik 4 →** — muncul: `▪pinjam(judul)validasi tersedia`

> Aksi kedua: pinjam berdasarkan judul, dengan validasi bahwa buku harus tersedia.

**Klik 5 →** — muncul: `▪kembalikan(judul)`

> Aksi ketiga: kembalikan buku.

**Klik 6 →** — muncul: `▪cari(kata)`

> Aksi keempat: cari berdasarkan kata kunci.

**Klik 7 →** — muncul: `Pakai __str__ agar tampilan buku rapi dan raise untuk aksi yang tidak `

> Dan tips terakhir: pakai str agar tampilan buku rapi, dan raise untuk aksi yang tidak valid.

---

### Slide 23 — Latihan: P1, P2

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 3, bagian E, dan kerjakan project P1 dan P2. Waktunya 60 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari3-oop.ipynb dan jalankan timer 60 menit (tekan Mulai).

---

### Slide 24 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 31 dtk*

**Saat slide muncul**

> Rekap Hari 3.

**Klik 1 →** — muncul: `Class, object, __init__, self; class vs instance attribute`

> Class, object, init, dan self, serta class versus instance attribute.

**Klik 2 →** — muncul: `Inheritance, super(), override, polimorfisme`

> Inheritance, super, override, dan polimorfisme.

**Klik 3 →** — muncul: `Encapsulation, @property, __str__/__repr__/__eq__, context manager`

> Encapsulation, property, str, repr, eq, dan context manager.

**Klik 4 →** — muncul: `Jebakan: mutable default, lupa self/super()`

> Jebakan: mutable default, serta lupa self atau super.

**Klik 5 →** — muncul: `Mini project berbasis class`

> Mini project berbasis class.

**Klik 6 →** — muncul: `Besok (Hari 4): NumPy & Pandas`

> Jalankan sel Rekap hasil latihan. Besok, Hari 4: NumPy dan Pandas. Sampai jumpa!

🎬 **Aksi:** Tampilkan sel rekap di notebook.

---
