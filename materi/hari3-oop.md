# Hari 3 — Object-Oriented Programming (OOP)

_Python Intensive Bootcamp • 6 Jam_

Python Intensive Bootcamp  •  6 Jam  •  Level Menengah

# 1. Tujuan Pembelajaran

- Memahami paradigma OOP dan membuat class serta object di Python.
- Menguasai inheritance, encapsulation, dan special methods.
- Menggunakan context manager (with) dan pengenalan unit testing.
- Menyelesaikan 2 Mini Project berbasis OOP dengan format lengkap.

# 2. Agenda

| Waktu | Sesi | Durasi | Fokus |
|---|---|---|---|
| 00:00–00:10 | Review singkat + setup | 10 mnt | Persiapan |
| 00:10–01:20 | Class, Object, Attribute, Method | 70 mnt | OOP Dasar |
| 01:20–02:10 | Inheritance + Encapsulation | 50 mnt | Pewarisan |
| 02:10–02:30 | Istirahat | 20 mnt | — |
| 02:30–03:20 | Special Methods + Context Manager | 50 mnt | Lanjutan |
| 03:20–05:20 | Mini Project | 120 mnt | Praktik |
| 05:20–06:00 | Review + Sharing | 40 mnt | Refleksi |

# 3. Class, Object, Attribute & Method

## 3.1 Paradigma OOP

OOP mengorganisasi kode dalam bentuk object yang menggabungkan data (attribute) dan perilaku (method). Empat pilar utama: Encapsulation, Abstraction, Inheritance, Polymorphism.

## 3.2 Membuat Class dan Object

```python
class Mahasiswa:
    """Merepresentasikan data seorang mahasiswa."""

    def __init__(self, nama, nim, prodi, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.ipk = ipk

    def info(self):
        return f"{self.nama} ({self.nim}) — {self.prodi}, IPK {self.ipk}"

    def update_ipk(self, ipk_baru):
        if 0 <= ipk_baru <= 4:
            self.ipk = ipk_baru
        else:
            print("IPK tidak valid")

m1 = Mahasiswa("Ani", "2201", "Informatika", 3.75)
m2 = Mahasiswa("Budi", "2202", "Sistem Informasi")
print(m1.info())
m2.update_ipk(3.40)
print(m2.info())
```

## 3.3 Class Attribute vs Instance Attribute

```python
class Mahasiswa:
    jumlah = 0   # class attribute (milik class)

    def __init__(self, nama, nim):
        self.nama = nama   # instance attribute
        self.nim = nim
        Mahasiswa.jumlah += 1

a = Mahasiswa("Ani", "2201")
b = Mahasiswa("Budi", "2202")
print(Mahasiswa.jumlah)  # 2
```

## 3.4 Latihan Class Dasar

1. Buat class RekeningBank dengan attribute: nama, no_rek, saldo. Method: setor, tarik, info.
2. Tambahkan validasi: saldo tidak boleh negatif saat tarik.
3. Buat 2 object rekening dan lakukan beberapa transaksi, lalu tampilkan info.

# 4. Inheritance (Pewarisan)

## 4.1 Konsep dan super()

```python
class Pegawai:
    def __init__(self, nama, id_pegawai, gaji):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.gaji = gaji

    def info(self):
        return f"{self.nama} ({self.id_pegawai}) — Gaji: {self.gaji}"

class Dosen(Pegawai):
    def __init__(self, nama, id_pegawai, gaji, bidang):
        super().__init__(nama, id_pegawai, gaji)
        self.bidang = bidang

    def info(self):
        return super().info() + f" | Bidang: {self.bidang}"

class Staff(Pegawai):
    def __init__(self, nama, id_pegawai, gaji, divisi):
        super().__init__(nama, id_pegawai, gaji)
        self.divisi = divisi

d = Dosen("Dr. Sari", "D001", 12000000, "Machine Learning")
s = Staff("Rina", "S010", 7000000, "Keuangan")
print(d.info())
print(s.info())
print(isinstance(d, Pegawai))   # True
print(issubclass(Dosen, Pegawai))  # True
```

## 4.2 Latihan Inheritance

4. Buat class Kendaraan (merek, tahun). Turunkan class Mobil dan Motor.
5. Override method info() di masing-masing subclass. Buat 1 object dari tiap class.

# 5. Encapsulation & Special Methods

## 5.1 Encapsulation

```python
class Rekening:
    def __init__(self, nama, saldo=0):
        self.nama = nama
        self.__saldo = saldo   # private-by-convention

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Transaksi gagal")
```

## 5.2 Special Methods

```python
class Buku:
    def __init__(self, judul, penulis, halaman):
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman

    def __str__(self):
        return f"'{self.judul}' oleh {self.penulis}"

    def __repr__(self):
        return f"Buku('{self.judul}', '{self.penulis}', {self.halaman})"

    def __len__(self):
        return self.halaman

    def __eq__(self, other):
        return self.judul == other.judul and self.penulis == other.penulis

b1 = Buku("Python Dasar", "Ani", 250)
b2 = Buku("Python Dasar", "Ani", 250)
print(b1)          # __str__
print(len(b1))     # 250
print(b1 == b2)    # True
```

## 5.3 Context Manager

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager("catatan.txt", "w") as f:
    f.write("Belajar OOP di Hari 3\n")
```

# 6. Mini Project

## Mini Project 1 — Sistem Manajemen Tugas Kuliah (Level Dasar)

### Deskripsi

Buat sistem sederhana untuk mengelola daftar tugas kuliah menggunakan class. Pengguna dapat menambah tugas, menampilkan semua tugas, menandai selesai, dan melihat tugas yang belum selesai.

### Fitur Wajib

1. Class Tugas dengan attribute: nama, mata_kuliah, deadline, selesai (bool).
2. Class ManajerTugas untuk menampung list tugas.
3. Method: tambah_tugas, tampilkan_semua, tandai_selesai, filter_belum_selesai.
4. Method info() atau __str__ pada class Tugas.
5. Program interaktif berbasis menu (loop).

### Skeleton Code

```python
class Tugas:
    def __init__(self, nama, mata_kuliah, deadline):
        self.nama = nama
        self.mata_kuliah = mata_kuliah
        self.deadline = deadline
        self.selesai = False

    def __str__(self):
        status = "Selesai" if self.selesai else "Belum"
        return f"[{status}] {self.nama} — {self.mata_kuliah} (deadline: {self.deadline})"

class ManajerTugas:
    def __init__(self):
        self.daftar = []

    def tambah_tugas(self, tugas):
        # ...
        pass

    def tampilkan_semua(self):
        # ...
        pass

    def tandai_selesai(self, index):
        # ...
        pass

    def filter_belum_selesai(self):
        # return list tugas yang belum selesai
        pass

# Main menu interaktif
manajer = ManajerTugas()
while True:
    print("\n1. Tambah  2. Tampilkan  3. Tandai Selesai  4. Belum Selesai  5. Keluar")
    pilih = input("Pilih: ")
    # implementasi menu ...
```

> Tips Project 1 Gunakan enumerate() saat menampilkan daftar agar user bisa memilih index. Validasi index saat menandai selesai agar tidak IndexError.

## Mini Project 2 — Sistem Perpustakaan dengan Inheritance (Level Lebih Tinggi)

### Deskripsi

Buat sistem perpustakaan mini yang mengelola berbagai jenis item (Buku, Jurnal, DVD) menggunakan inheritance. Semua item diturunkan dari class ItemPerpustakaan.

### Fitur Wajib

1. Class induk ItemPerpustakaan (judul, tahun, tersedia).
2. Subclass: Buku (penulis, halaman), Jurnal (volume, penerbit), DVD (durasi, genre).
3. Class Perpustakaan untuk menampung koleksi, method: tambah, pinjam, kembalikan, cari, tampilkan.
4. Override __str__ di setiap subclass.
5. Menu interaktif untuk operasi perpustakaan.

### Skeleton Code

```python
class ItemPerpustakaan:
    def __init__(self, judul, tahun):
        self.judul = judul
        self.tahun = tahun
        self.tersedia = True

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} ({self.tahun}) — {status}"

class Buku(ItemPerpustakaan):
    def __init__(self, judul, tahun, penulis, halaman):
        super().__init__(judul, tahun)
        self.penulis = penulis
        self.halaman = halaman

    def __str__(self):
        return f"[Buku] {super().__str__()} | Penulis: {self.penulis}"

class Jurnal(ItemPerpustakaan):
    def __init__(self, judul, tahun, volume, penerbit):
        super().__init__(judul, tahun)
        self.volume = volume
        self.penerbit = penerbit

    def __str__(self):
        return f"[Jurnal] {super().__str__()} | Vol.{self.volume}"

class DVD(ItemPerpustakaan):
    def __init__(self, judul, tahun, durasi, genre):
        super().__init__(judul, tahun)
        self.durasi = durasi
        self.genre = genre

    def __str__(self):
        return f"[DVD] {super().__str__()} | {self.genre}, {self.durasi} mnt"

class Perpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambah(self, item):
        self.koleksi.append(item)

    def pinjam(self, judul):
        # cari item, set tersedia=False jika ada dan tersedia
        pass

    def kembalikan(self, judul):
        pass

    def cari(self, keyword):
        # return list item yang judulnya mengandung keyword
        pass

    def tampilkan(self):
        for item in self.koleksi:
            print(item)

# Main menu
perpustakaan = Perpustakaan()

# tambah beberapa item sample, lalu loop menu
```

> Tips Project 2 Manfaatkan polymorphism: tampilkan() cukup memanggil print(item) karena tiap subclass punya __str__ sendiri. Method pinjam/kembalikan bisa memakai loop + break saat item ditemukan.

# 7. Troubleshooting

```python

# TypeError: __init__() missing arguments

# → Pastikan saat membuat object, semua parameter wajib diisi

# AttributeError: 'X' object has no attribute 'y'

# → Cek apakah attribute di-set di __init__ atau method lain sudah dipanggil

# super() tidak bekerja seperti yang diharapkan

# → Pastikan class child memanggil super().__init__(...) dengan argumen yang benar

# Semua object berbagi list yang sama

# → Jangan pakai mutable default (list/dict) sebagai default argument

#   Salah: def __init__(self, items=[]):

#   Benar: def __init__(self, items=None):

#            self.items = items if items is not None else []
```

# 8. Solusi Latihan

## 8.1 Solusi Class Dasar — RekeningBank

```python
class RekeningBank:
    def __init__(self, nama, no_rek, saldo=0):
        self.nama = nama
        self.no_rek = no_rek
        self.saldo = saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Setor {jumlah}. Saldo: {self.saldo}")
        else:
            print("Jumlah tidak valid")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Tarik {jumlah}. Saldo: {self.saldo}")
        else:
            print("Saldo tidak cukup atau jumlah tidak valid")

    def info(self):
        return f"{self.nama} ({self.no_rek}) — Saldo: Rp{self.saldo:,}"

r1 = RekeningBank("Ani", "001", 500000)
r2 = RekeningBank("Budi", "002", 1000000)
r1.setor(200000)
r1.tarik(100000)
r2.tarik(2000000)  # gagal
print(r1.info())
print(r2.info())
```

## 8.2 Solusi Inheritance — Kendaraan

```python
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        return f"{self.merek} ({self.tahun})"

class Mobil(Kendaraan):
    def __init__(self, merek, tahun, jumlah_pintu):
        super().__init__(merek, tahun)
        self.jumlah_pintu = jumlah_pintu

    def info(self):
        return f"[Mobil] {super().info()} — {self.jumlah_pintu} pintu"

class Motor(Kendaraan):
    def __init__(self, merek, tahun, jenis):
        super().__init__(merek, tahun)
        self.jenis = jenis

    def info(self):
        return f"[Motor] {super().info()} — {self.jenis}"

m = Mobil("Toyota", 2022, 4)
n = Motor("Honda", 2023, "Matic")
print(m.info())
print(n.info())
```

> Hari 3 Selesai Kerjakan Mini Project 1 (wajib) dan Project 2 (challenge). Pastikan menggunakan class, inheritance, dan __str__ dengan benar. Lanjut ke Hari 4: NumPy & Pandas.

