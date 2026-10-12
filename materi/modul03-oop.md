# Modul 3 — Object-Oriented Programming

_Penjelasan lebih jelas  ·  Kasus beragam  ·  Pseudocode di latihan · Estimasi: ± 6 jam  ·  Prasyarat: Modul 1–2_

> **Catatan pengujian:** seluruh blok kode pada modul ini dijalankan (Python 3.11). Bagian **Output** adalah hasil eksekusi nyata. Blok yang memakai `input()` dijalankan dengan input simulasi yang ditulis di samping label output. Blok yang hanya berisi definisi/komentar diberi keterangan, dan "Uji pelengkap" ditambahkan agar function/class pada blok tersebut terbukti berjalan. Kasus error pada bagian Troubleshooting dijalankan nyata di "Demonstrasi error".

# 1. Apa yang Akan Anda Pelajari

- Memahami class dan object, serta cara menyimpan data dan perilaku dalam satu unit.
- Membedakan data milik satu object dengan data yang dibagi seluruh class.
- Membuat class anak yang mewarisi class induk, dan menyesuaikan perilakunya.
- Memakai __str__, encapsulation sederhana, dan menyelesaikan 2 mini project.

> [!NOTE]
> **Cara membaca modul ini**
>
> Bagian penjelasan sengaja dibuat lebih panjang agar alurnya mudah diikuti.
>
> Baca penjelasan dulu, baru ketik contoh. Ubah angka/nama agar terasa hidup.
>
> Di latihan: baca soal → ikuti pseudocode → tulis kode sendiri → baru bandingkan solusi.

# 2. Class, Object, Attribute & Method

## 2.1 Apa itu OOP, dengan bahasa sederhana

Sampai Modul 2, Anda banyak bekerja dengan function dan data terpisah. Misalnya list of dict mahasiswa di satu sisi, dan function yang mengolah list itu di sisi lain. Itu sah dan sering cukup.

Object-Oriented Programming (OOP) menawarkan cara lain: menggabungkan data dan operasi yang berkaitan ke dalam satu “benda” bernama object. Class adalah cetakannya. Object adalah hasil cetakan itu di dunia nyata program.

Analogi singkat: class Mahasiswa mirip formulir kosong “Data Mahasiswa”. Object m1 = Mahasiswa("Ani", ...) mirip formulir yang sudah diisi untuk Ani. Formulir kosong (class) bisa dipakai berkali-kali untuk orang berbeda; tiap isian (object) punya data sendiri.

Kapan OOP membantu? Saat Anda punya banyak entitas sejenis (banyak mahasiswa, banyak buku, banyak rekening) dan tiap entitas punya aturan yang sama (setor, tarik, update IPK). Kapan tidak wajib? Script pendek sekali jalan sering lebih jelas tetap memakai function biasa.

## 2.2 Bagian-bagian class

Di dalam class biasanya ada:

(1) __init__ — method khusus yang dipanggil otomatis saat object dibuat. Isinya menyiapkan data awal.

(2) Attribute — data yang “nempel” di object, misalnya self.nama. Kata self merujuk ke object yang sedang dipakai.

(3) Method — function yang hidup di dalam class. Parameter pertamanya selalu self agar method tahu object mana yang sedang dilayani.

Alur membuat object: Anda menulis Mahasiswa("Ani", "2201"). Python membuat object kosong, memanggil __init__, mengisi self.nama dan self.nim, lalu menyerahkan object itu ke variabel Anda.

## 2.3 Contoh bertahap

Contoh 1 — Mahasiswa. Perhatikan: update_ipk memeriksa rentang sebelum mengubah data. Itu pola penting: method menjaga agar data tidak menjadi tidak masuk akal.

```python
class Mahasiswa:
    def __init__(self, nama, nim, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def perkenalan(self):
        return f"{self.nama} ({self.nim}) — IPK {self.ipk}"

    def update_ipk(self, ipk_baru):
        if 0 <= ipk_baru <= 4:
            self.ipk = ipk_baru
        else:
            print("IPK tidak valid")

m1 = Mahasiswa("Ani", "2201", 3.5)
m2 = Mahasiswa("Budi", "2202")
print(m1.perkenalan())
m2.update_ipk(3.2)
print(m2.perkenalan())
```

**Output:**

```text
Ani (2201) — IPK 3.5
Budi (2202) — IPK 3.2
```

Contoh 2 — Produk toko. Method total menghitung harga belanja; kurangi_stok mengembalikan True/False agar pemanggil tahu apakah stok cukup.

```python
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def total(self, qty):
        return self.harga * qty

    def kurangi_stok(self, qty):
        if qty <= self.stok:
            self.stok -= qty
            return True
        return False

p = Produk("Buku Python", 75000, 10)
print(p.total(2))
print(p.kurangi_stok(3), p.stok)
```

**Output:**

```text
150000
True 7
```

Contoh 3 — Titik pada bidang. Method jarak_ke menerima object Titik lain. Ini menunjukkan object bisa saling berinteraksi.

```python
import math

class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def jarak_ke(self, lain):
        return math.hypot(self.x - lain.x, self.y - lain.y)

a = Titik(0, 0)
b = Titik(3, 4)
print(a.jarak_ke(b))  # 5.0
```

**Output:**

```text
5.0
```

## 2.4 Class attribute vs instance attribute

Instance attribute adalah data milik satu object: self.nama pada m1 tidak otomatis sama dengan self.nama pada m2.

Class attribute ditulis di tubuh class (sejajar dengan def), bukan di dalam __init__. Nilainya dibagi bersama. Contoh klasik: penghitung berapa object sudah dibuat.

```python
class Mahasiswa:
    jumlah = 0  # class attribute

    def __init__(self, nama):
        self.nama = nama  # instance attribute
        Mahasiswa.jumlah += 1

a = Mahasiswa("Ani")
b = Mahasiswa("Budi")
print(Mahasiswa.jumlah)  # 2
print(a.nama, b.nama)    # Ani Budi — berbeda per object
```

**Output:**

```text
2
Ani Budi
```

> [!WARNING]
> **Kesalahan yang sering muncul**
>
> Lupa menulis self di parameter method → TypeError saat method dipanggil.
>
> Lupa self. saat mengisi attribute di __init__ → variabel lokal hilang setelah __init__ selesai.
>
> Mengisi list/dict sebagai class attribute lalu mengubah isinya — perubahan bisa “bocor” ke semua instance. Untuk data per object, isi di __init__.

## 2.5 Latihan Class Dasar

Kerjakan satu per satu. Ikuti pseudocode jika masih bingung menyusun urutan.

1. Class RekeningBank: pemilik & saldo; method setor, tarik (hanya jika saldo cukup), dan info.

```text
Pseudocode:
  CLASS RekeningBank
    SAAT dibuat: simpan pemilik dan saldo awal
    setor(jumlah): jika jumlah > 0, tambahkan ke saldo
    tarik(jumlah): jika jumlah valid dan saldo cukup, kurangi saldo
                  jika tidak, tampilkan pesan gagal
    info: kembalikan teks berisi pemilik dan saldo
```

2. Class Buku: judul, penulis, tahun; method ringkas() mengembalikan satu string rapi.

```text
Pseudocode:
  CLASS Buku
    SAAT dibuat: simpan judul, penulis, tahun
    ringkas(): kembalikan "judul — penulis (tahun)"
```

3. Class Keranjang: menyimpan daftar item; method tambah, total_harga, jumlah_item.

```text
Pseudocode:
  CLASS Keranjang
    SAAT dibuat: items ← list kosong
    tambah(nama, harga): masukkan pasangan nama-harga ke items
    total_harga(): jumlahkan semua harga di items
    jumlah_item(): banyak elemen di items
```

4. Class Mahasiswa dengan class attribute yang menghitung berapa instance sudah dibuat.

```text
Pseudocode:
  CLASS Mahasiswa
    jumlah ← 0   (milik class)
    SAAT dibuat: simpan nama; jumlah bertambah 1
```

5. Class Suhu menyimpan nilai Celsius; method ke_fahrenheit() dan ke_kelvin().

```text
Pseudocode:
  CLASS Suhu
    SAAT dibuat: simpan celsius
    ke_fahrenheit(): hitung c×9/5+32
    ke_kelvin(): hitung c+273.15
```

# 3. Inheritance (Pewarisan)

## 3.1 Ide dasar

Kadang dua class hampir sama, hanya berbeda di detail. Misalnya Mobil dan Motor sama-sama punya merek dan tahun, tetapi Mobil punya jumlah pintu, Motor punya jenis (bebek/sport).

Inheritance memungkinkan Anda menulis bagian yang sama sekali saja di class induk (Kendaraan), lalu class anak (Mobil, Motor) tinggal menambahkan yang khas. Hubungan yang cocok disebut “is-a”: mobil adalah sebuah kendaraan.

Yang tidak cocok: memaksa inheritance hanya karena ingin memakai ulang satu function kecil. Dalam kasus itu, function biasa atau komposisi (object A menyimpan object B) sering lebih sederhana.

## 3.2 super() dan override

Saat class anak punya __init__ sendiri, bagian inisialisasi induk tidak otomatis jalan. Anda memanggil super().__init__(...) agar attribute induk tetap terisi.

Override berarti class anak menulis ulang method yang namanya sama dengan milik induk. Dari luar, pemanggil tetap menulis .info(), tetapi perilaku mengikuti jenis object yang sebenarnya (Mobil atau Motor).

```python
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        return f"{self.merek} ({self.tahun})"

class Mobil(Kendaraan):
    def __init__(self, merek, tahun, pintu):
        super().__init__(merek, tahun)  # isi merek & tahun di induk
        self.pintu = pintu

    def info(self):
        # pakai info induk, lalu tambahkan detail
        return f"{super().info()} — {self.pintu} pintu"

class Motor(Kendaraan):
    def __init__(self, merek, tahun, jenis):
        super().__init__(merek, tahun)
        self.jenis = jenis

m = Mobil("Toyota", 2020, 4)
print(m.info())
print(isinstance(m, Kendaraan))  # True — Mobil adalah Kendaraan
```

**Output:**

```text
Toyota (2020) — 4 pintu
True
```

Contoh lain di dunia akademik: Pegawai punya gaji pokok; Manager menambah tunjangan. Method gaji() di Manager mengoverride versi Pegawai.

```python
class Pegawai:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def gaji(self):
        return self.gaji_pokok

class Manager(Pegawai):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    def gaji(self):
        return self.gaji_pokok + self.tunjangan

p = Pegawai("Siti", 5_000_000)
m = Manager("Rudi", 7_000_000, 2_000_000)
print(p.nama, p.gaji())
print(m.nama, m.gaji())
```

**Output:**

```text
Siti 5000000
Rudi 9000000
```

## 3.3 Latihan Inheritance

1. Implementasikan Pegawai dan Manager seperti di atas; buat satu instance masing-masing dan cetak gajinya.

```text
Pseudocode:
  TULIS class Pegawai dan Manager (lihat pola contoh)
  buat pegawai biasa dan seorang manager
  cetak nama dan hasil gaji() masing-masing
```

2. Class Hewan(nama) dengan method bersuara(); Kucing dan Anjing mengoverride bunyi yang berbeda.

```text
Pseudocode:
  CLASS Hewan: simpan nama; bersuara() kembalikan teks generik
  CLASS Kucing(Hewan): bersuara() → "meong"
  CLASS Anjing(Hewan): bersuara() → "guk"
  uji: buat satu kucing dan satu anjing, panggil bersuara()
```

3. AkunBank → AkunTabungan yang punya suku bunga dan method tambah_bunga().

```text
Pseudocode:
  CLASS AkunBank: saldo, setor, tarik
  CLASS AkunTabungan(AkunBank): simpan suku_bunga
    tambah_bunga(): saldo bertambah sebesar saldo × suku_bunga
```

4. BangunDatar dengan method luas(); Persegi dan PersegiPanjang mengisi rumus masing-masing.

```text
Pseudocode:
  CLASS BangunDatar: luas() kembalikan 0 (placeholder)
  CLASS Persegi: simpan sisi; luas() → sisi × sisi
  CLASS PersegiPanjang: simpan panjang & lebar; luas() → panjang × lebar
```

# 4. Encapsulation & Special Methods

## 4.1 Encapsulation — menjaga data lewat pintu resmi

Encapsulation berarti menyembunyikan detail internal dan hanya membuka cara yang aman untuk mengubah data. Di Python ini lebih ke konvensi daripada kunci ketat.

Attribute yang diawali satu garis bawah (_saldo) dibaca sebagai: “ini internal, jangan diubah sembarangan dari luar.” Yang diawali dua garis bawah memicu name mangling (nama diubah di belakang layar). Untuk level modul ini, cukup pahami _ sebagai sinyal internal.

Praktik yang baik: sediakan method setor, tarik, atau get_saldo. Dengan begitu aturan “saldo tidak boleh negatif” bisa ditegakkan di satu tempat.

```python
class Rekening:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self._saldo = saldo  # internal

    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah

    def get_saldo(self):
        return self._saldo

r = Rekening("Ani", 1000)
r.setor(500)
print(r.get_saldo())  # 1500
```

**Output:**

```text
1500
```

## 4.2 Special methods — __str__, __repr__, __eq__

Method dengan nama berungkung ganda (dunder) dipanggil Python pada situasi tertentu. Tiga yang paling sering Anda butuhkan di awal:

__str__ — dipanggil saat print(object) atau str(object). Isinya teks yang enak dibaca manusia.

__repr__ — representasi untuk debug; idealnya jelas menunjukkan cara membuat object itu.

__eq__ — menentukan kapan dua object dianggap sama dengan operator ==.

```python
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def __str__(self):
        return f"{self.judul} — {self.penulis}"

    def __repr__(self):
        return f"Buku({self.judul!r}, {self.penulis!r})"

    def __eq__(self, other):
        if not isinstance(other, Buku):
            return False
        return self.judul == other.judul and self.penulis == other.penulis

b1 = Buku("Laskar Pelangi", "Andrea Hirata")
b2 = Buku("Laskar Pelangi", "Andrea Hirata")
print(b1)        # memakai __str__
print(b1 == b2)  # True karena __eq__
```

**Output:**

```text
Laskar Pelangi — Andrea Hirata
True
```

## 4.3 Context manager (with) — sekilas

Pernyataan with memastikan resource (misalnya file) ditutup dengan benar. Object yang mendukung with perlu method __enter__ dan __exit__. open() bawaan Python sudah mendukung ini; contoh di bawah hanya untuk memperlihatkan polanya.

```python
class FileCatatan:
    def __init__(self, path, mode="w"):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False  # jangan menelan exception

with FileCatatan("log.txt") as f:
    f.write("Catatan penting\n")
```

**Output:**

```text
(tidak ada output)
```

**Uji pelengkap — membuktikan isi file dan file tertutup**

```python
from pathlib import Path
print(Path("log.txt").read_text(encoding="utf-8"), end="")
print(f.closed)
```

**Output:**

```text
Catatan penting
True
```

## 4.4 Latihan

1. Tambahkan __str__ pada class RekeningBank dari latihan sebelumnya.

```text
Pseudocode:
  DI dalam RekeningBank
    definisikan __str__
    kembalikan teks yang memuat pemilik dan saldo
  uji dengan print(rekening)
```

2. Class Titik(x, y) dengan __str__ berbentuk (x, y) dan method jarak_ke.

```text
Pseudocode:
  CLASS Titik: simpan x, y
  jarak_ke(titik_lain): hitung jarak Euclidean
  __str__: kembalikan "(x, y)"
```

3. Class Fraksi(pembilang, penyebut): tolak penyebut 0; method nilai_nyata(); __str__ sebagai "a/b".

```text
Pseudocode:
  SAAT dibuat: jika penyebut = 0 → beritahu error
  nilai_nyata(): kembalikan pembilang / penyebut
  __str__: "pembilang/penyebut"
```

4. Pastikan dua object Buku dianggap sama dengan == jika judul dan penulis sama.

```text
Pseudocode:
  DEF __eq__(self, other)
    jika other bukan Buku → False
    True hanya jika judul sama dan penulis sama
```

# 5. Mini Project 1 — Manajemen Tugas Kuliah

Anda akan membuat dua class yang bekerja sama. Class Tugas menyimpan data satu tugas. Class ManajerTugas menyimpan daftar tugas dan menyediakan operasi tambah, tampil, tandai selesai, serta filter yang belum selesai.

Pisahkan tanggung jawab itu dengan sengaja: jangan menaruh semua logika di satu class besar. Menu interaktif di bagian bawah hanya memanggil method manajer.

### Fitur wajib

1. Class Tugas: matkul, deskripsi, deadline, status selesai, plus __str__.
2. Class ManajerTugas: tambah, tampilkan, tandai (index), filter belum selesai.
3. Menu teks sederhana di main.

```python
class Tugas:
    def __init__(self, matkul, deskripsi, deadline):
        self.matkul = matkul
        self.deskripsi = deskripsi
        self.deadline = deadline
        self.selesai = False

    def tandai_selesai(self):
        self.selesai = True

    def __str__(self):
        st = "✓" if self.selesai else "○"
        return f"[{st}] {self.matkul}: {self.deskripsi} ({self.deadline})"

class ManajerTugas:
    def __init__(self):
        self.daftar = []

    def tambah(self, tugas):
        self.daftar.append(tugas)

    def tampilkan(self):
        for i, t in enumerate(self.daftar, 1):
            print(f"{i}. {t}")

    def tandai(self, index):
        if 1 <= index <= len(self.daftar):
            self.daftar[index - 1].tandai_selesai()

    def belum_selesai(self):
        return [t for t in self.daftar if not t.selesai]

# while True: menu → panggil method yang sesuai
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok ini hanya mendefinisikan class; menu `while True` dibiarkan sebagai tugas peserta (lihat uji pelengkap)._

**Uji pelengkap — menjalankan ManajerTugas (menu dibiarkan kosong pada modul)**

```python
m = ManajerTugas()
m.tambah(Tugas("Python", "Laporan Modul 3", "2026-10-05"))
m.tambah(Tugas("Basis Data", "ERD", "2026-10-07"))
m.tambah(Tugas("Jaringan", "Subnetting", "2026-10-09"))
m.tampilkan()
m.tandai(2)
m.tandai(9)  # indeks tidak valid diabaikan
print("--- belum selesai ---")
for t in m.belum_selesai():
    print(t)
```

**Output:**

```text
1. [○] Python: Laporan Modul 3 (2026-10-05)
2. [○] Basis Data: ERD (2026-10-07)
3. [○] Jaringan: Subnetting (2026-10-09)
--- belum selesai ---
[○] Python: Laporan Modul 3 (2026-10-05)
[○] Jaringan: Subnetting (2026-10-09)
```

> [!TIP]
> **Urutan mengerjakan Project 1**
>
> 1) Selesaikan class Tugas dan uji dengan print(tugas).
>
> 2) Selesaikan ManajerTugas tanpa menu dulu (panggil method manual).
>
> 3) Baru pasang loop menu.
>
> Ingat: index di menu biasanya mulai 1; index list mulai 0.

# 6. Mini Project 2 — Perpustakaan dengan Inheritance

Class ItemPerpustakaan menjadi induk: semua item punya judul dan status tersedia/dipinjam, plus method pinjam dan kembalikan. Buku dan Jurnal adalah jenis item yang menambahkan detail masing-masing dan menyesuaikan tampilan __str__.

Class Perpustakaan tidak mewarisi Item; ia memiliki koleksi (list) item. Ini contoh komposisi: perpustakaan “mempunyai” banyak item, bukan “adalah” sebuah item.

### Fitur wajib

1. ItemPerpustakaan: judul, status, pinjam, kembalikan.
2. Buku dan Jurnal: attribute tambahan + __str__ jelas.
3. Perpustakaan: tambah, cari, pinjam, kembalikan, tampilkan.

```python
class ItemPerpustakaan:
    def __init__(self, judul):
        self.judul = judul
        self.tersedia = True

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            return True
        return False

    def kembalikan(self):
        self.tersedia = True

class Buku(ItemPerpustakaan):
    def __init__(self, judul, penulis, halaman):
        super().__init__(judul)
        self.penulis = penulis
        self.halaman = halaman

    def __str__(self):
        st = "tersedia" if self.tersedia else "dipinjam"
        return f"Buku: {self.judul} — {self.penulis} [{st}]"

class Jurnal(ItemPerpustakaan):
    def __init__(self, judul, volume, tahun):
        super().__init__(judul)
        self.volume = volume
        self.tahun = tahun

    def __str__(self):
        st = "tersedia" if self.tersedia else "dipinjam"
        return f"Jurnal: {self.judul} Vol.{self.volume} ({self.tahun}) [{st}]"

class Perpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambah(self, item):
        self.koleksi.append(item)

    def cari(self, keyword):
        k = keyword.lower()
        return [i for i in self.koleksi if k in i.judul.lower()]

    def pinjam(self, judul):
        for i in self.koleksi:
            if i.judul.lower() == judul.lower():
                return i.pinjam()
        return False

    def tampilkan(self):
        for i in self.koleksi:
            print(i)
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok ini hanya mendefinisikan class (tanpa pemanggilan); lihat uji pelengkap._

**Uji pelengkap — menjalankan Perpustakaan**

```python
p = Perpustakaan()
p.tambah(Buku("Python Dasar", "Ani", 250))
p.tambah(Buku("Basis Data", "Budi", 300))
p.tambah(Jurnal("Jurnal Informatika", 12, 2025))
p.tampilkan()
print(p.pinjam("python dasar"))
print(p.pinjam("python dasar"))
print(p.pinjam("tidak ada"))
print([str(i) for i in p.cari("data")])
p.tampilkan()
```

**Output:**

```text
Buku: Python Dasar — Ani [tersedia]
Buku: Basis Data — Budi [tersedia]
Jurnal: Jurnal Informatika Vol.12 (2025) [tersedia]
True
False
False
['Buku: Basis Data — Budi [tersedia]']
Buku: Python Dasar — Ani [dipinjam]
Buku: Basis Data — Budi [tersedia]
Jurnal: Jurnal Informatika Vol.12 (2025) [tersedia]
```

# 7. Troubleshooting

TypeError: __init__() missing argument — object dibuat tanpa memberi argumen wajib. Isi semua parameter yang diminta __init__ (kecuali yang berdefault).

AttributeError — nama attribute salah ketik, atau attribute belum di-set di __init__. Cetak object.__dict__ saat debug untuk melihat apa yang tersimpan.

Attribute induk “kosong” di class anak — hampir selalu karena lupa super().__init__(...) di __init__ anak.

print(object) masih jelek — tambahkan __str__ dan pastikan return-nya string, bukan print di dalam __str__.

## Demonstrasi error — output nyata

Bagian Troubleshooting di atas berupa penjelasan teks. Berikut setiap kasusnya dijalankan nyata agar pesan error dan perilakunya terlihat. Alamat memori pada `<... object at 0x...>` berbeda di setiap eksekusi.

### TypeError — argument `__init__` kurang

```python
class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama

m = Mahasiswa("Ani", "2201")
```

**Output:**

```text
  -> TypeError: Mahasiswa.__init__() missing 1 required positional argument: 'prodi'
```

### TypeError — lupa `self` pada method

```python
class Mahasiswa:
    def sapa():
        print("Halo")

Mahasiswa().sapa()
```

**Output:**

```text
  -> TypeError: Mahasiswa.sapa() takes 0 positional arguments but 1 was given
```

### AttributeError — attribute tidak ada

```python
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

m = Mahasiswa("Ani")
print(m.__dict__)
print(m.nim)
```

**Output:**

```text
{'nama': 'Ani'}
  -> AttributeError: 'Mahasiswa' object has no attribute 'nim'
```

### AttributeError — attribute dibuat di method lain yang belum dipanggil

```python
class Keranjang:
    def isi(self):
        self.item = ["buku"]

k = Keranjang()
print(k.__dict__)
print(k.item)
```

**Output:**

```text
{}
  -> AttributeError: 'Keranjang' object has no attribute 'item'
```

### Lupa `super().__init__()` — attribute induk "kosong"

```python
class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class Dosen(Pegawai):
    def __init__(self, nama, gaji, bidang):
        self.bidang = bidang    # super().__init__ tidak dipanggil

d = Dosen("Dr. Sari", 12000000, "ML")
print(d.__dict__)
print(d.nama)
```

**Output:**

```text
{'bidang': 'ML'}
  -> AttributeError: 'Dosen' object has no attribute 'nama'
```

### Perbaikan — panggil `super().__init__()`

```python
class Pegawai:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

class Dosen(Pegawai):
    def __init__(self, nama, gaji, bidang):
        super().__init__(nama, gaji)
        self.bidang = bidang

d = Dosen("Dr. Sari", 12000000, "ML")
print(d.__dict__)
```

**Output:**

```text
{'nama': 'Dr. Sari', 'gaji': 12000000, 'bidang': 'ML'}
```

### `print(object)` jelek — tanpa `__str__`

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul

print(Buku("Python"))
```

**Output:**

```text
<__main__.Buku object at 0x7faae7140550>
```

### `__str__` harus mengembalikan string, bukan mencetak

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul
    def __str__(self):
        print(self.judul)     # salah: mencetak, tidak return

print(Buku("Python"))
```

**Output:**

```text
Python
  -> TypeError: __str__ returned non-string (type NoneType)
```

### `__str__` yang benar

```python
class Buku:
    def __init__(self, judul):
        self.judul = judul
    def __str__(self):
        return f"Buku: {self.judul}"

print(Buku("Python"))
```

**Output:**

```text
Buku: Python
```

### Mutable default argument — semua object berbagi list yang sama

```python
class Kelas:
    def __init__(self, nama, mahasiswa=[]):
        self.nama = nama
        self.mahasiswa = mahasiswa

a, b = Kelas("A"), Kelas("B")
a.mahasiswa.append("Ani")
print(a.mahasiswa, b.mahasiswa, a.mahasiswa is b.mahasiswa)
```

**Output:**

```text
['Ani'] ['Ani'] True
```

### Mutable default — perbaikan dengan `None`

```python
class Kelas:
    def __init__(self, nama, mahasiswa=None):
        self.nama = nama
        self.mahasiswa = mahasiswa if mahasiswa is not None else []

a, b = Kelas("A"), Kelas("B")
a.mahasiswa.append("Ani")
print(a.mahasiswa, b.mahasiswa, a.mahasiswa is b.mahasiswa)
```

**Output:**

```text
['Ani'] [] False
```

### Atribut `__saldo` — name mangling

```python
class Rekening:
    def __init__(self, saldo=0):
        self.__saldo = saldo

r = Rekening(100)
print(vars(r))
print(r._Rekening__saldo)
print(r.__saldo)
```

**Output:**

```text
{'_Rekening__saldo': 100}
100
  -> AttributeError: 'Rekening' object has no attribute '__saldo'
```

# 8. Solusi Latihan (Cuplikan)

```python
class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
        else:
            print("Gagal tarik")

    def __str__(self):
        return f"{self.pemilik}: Rp{self.saldo:,}"

class Pegawai:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    def gaji(self):
        return self.gaji_pokok

class Manager(Pegawai):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan
    def gaji(self):
        return self.gaji_pokok + self.tunjangan

import math
class Titik:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def jarak_ke(self, lain):
        return math.hypot(self.x - lain.x, self.y - lain.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok hanya mendefinisikan class solusi; lihat uji pelengkap._

**Uji pelengkap — memanggil class solusi**

```python
r = RekeningBank("Ani", 1_000_000)
r.setor(250_000)
r.tarik(2_000_000)
r.tarik(300_000)
print(r)
for p in (Pegawai("Rina", 7_000_000), Manager("Budi", 9_000_000, 3_000_000)):
    print(p.nama, p.gaji())
print(Titik(0, 0).jarak_ke(Titik(3, 4)), Titik(1, 2))
```

**Output:**

```text
Gagal tarik
Ani: Rp950,000
Rina 7000000
Budi 12000000
5.0 (1, 2)
```

# 9. Checklist Sebelum Modul 4

- Sudah bisa menjelaskan class vs object dengan kata sendiri
- Inheritance + super() pernah ditulis sendiri, bukan hanya dibaca
- __str__ dipasang setidaknya di satu class buatan sendiri
- Mini Project 1 berjalan; Project 2 diusahakan
- Siap lanjut Modul 4 (NumPy & Pandas)

> **Modul 3 selesai? Lanjut ke Modul 4 — NumPy & Pandas.**
>
> Belajar Pemrograman Python — Modul Belajar Mandiri
