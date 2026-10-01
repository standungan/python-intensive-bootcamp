# Hari 2 — Functions, Modules & File Handling

_Python Intensive Bootcamp • 6 Jam_

Python Intensive Bootcamp  •  6 Jam  •  Level Pemula → Menengah

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Hari 2, peserta mampu:

- Membuat function yang baik (parameter, default argument, return, *args, **kwargs, docstring).
- Menggunakan lambda, map, filter, dan list comprehension untuk transformasi data yang ringkas.
- Membuat dan menggunakan module serta memahami struktur package sederhana.
- Menangani error dengan try-except-else-finally secara tepat.
- Membaca dan menulis file teks serta CSV menggunakan pathlib dan modul csv.
- Menyelesaikan 2 Mini Project yang mengintegrasikan function, module, dan file handling.

# 2. Agenda & Alokasi Waktu

| Waktu | Sesi | Durasi | Jenis |
|---|---|---|---|
| 00:00–00:15 | Review Hari 1 + Opening | 15 menit | Review |
| 00:15–01:30 | Modul 1: Functions (dasar → menengah) | 75 menit | Teori + Latihan |
| 01:30–02:15 | Modul 2: Lambda, map, filter, List Comp | 45 menit | Teori + Latihan |
| 02:15–02:40 | Istirahat | 25 menit | — |
| 02:40–03:25 | Modul 3: Modules & Packages | 45 menit | Teori + Praktik |
| 03:25–04:10 | Modul 4: Error Handling | 45 menit | Teori + Latihan |
| 04:10–05:00 | Modul 5: File Handling + pathlib | 50 menit | Teori + Praktik |
| 05:00–05:50 | Mini Project 1 + Mini Project 2 | 50 menit | Project |
| 05:50–06:00 | Review + Q&A | 10 menit | Review |

# 3. Modul 1 — Functions

## 3.1 Mengapa Function Penting?

Function memungkinkan kita mengorganisir kode menjadi blok-blok yang reusable, mudah diuji, dan mudah dipahami. Prinsip utamanya: Don’t Repeat Yourself (DRY).

## 3.2 Membuat Function Dasar

```python
def sapa():
    """Menampilkan salam sederhana."""
    print("Halo, selamat belajar Python!")

sapa()          # memanggil function
sapa()          # bisa dipanggil berkali-kali
```

## 3.3 Parameter dan Argument

```python

# Parameter tunggal
def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Rina")
sapa_nama("Budi")

# Multiple parameter
def perkenalan(nama, prodi, semester):
    print(f"Saya {nama}, prodi {prodi}, semester {semester}.")

perkenalan("Ani", "Informatika", 3)

# Keyword argument (urutan bebas)
perkenalan(semester=5, nama="Citra", prodi="SI")
```

## 3.4 Default Argument

```python
def sapa(nama, salam="Halo"):
    print(f"{salam}, {nama}!")

sapa("Rina")                  # Halo, Rina!
sapa("Rina", "Selamat pagi")  # Selamat pagi, Rina!

# Default argument harus di sebelah kanan
def hitung(a, b=10, c=5):
    return a + b + c

print(hitung(1))              # 16
print(hitung(1, 2))           # 8
print(hitung(1, 2, 3))        # 6
```

## 3.5 Return Value

```python
def luas_persegi(sisi):
    return sisi * sisi

hasil = luas_persegi(5)
print(hasil)                  # 25
print(luas_persegi(7) + 10)   # 59

# Multiple return
def hitung_luas_keliling(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    return luas, keliling

l, k = hitung_luas_keliling(5)
print(f"Luas: {l}, Keliling: {k}")

# Early return
def cek_lulus(nilai):
    if nilai < 0 or nilai > 100:
        return "Nilai tidak valid"
    if nilai >= 75:
        return "Lulus"
    return "Tidak Lulus"

print(cek_lulus(80))
print(cek_lulus(60))
print(cek_lulus(105))
```

## 3.6 *args dan **kwargs

```python

# *args → menerima banyak positional argument sebagai tuple
def jumlahkan(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(jumlahkan(1, 2, 3))           # 6
print(jumlahkan(10, 20, 30, 40))    # 100

# **kwargs → menerima banyak keyword argument sebagai dictionary
def tampilkan_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

tampilkan_info(nama="Ani", prodi="IF", ipk=3.8)

# Kombinasi
def fungsi_lengkap(wajib, *args, **kwargs):
    print("Wajib:", wajib)
    print("Args:", args)
    print("Kwargs:", kwargs)

fungsi_lengkap("utama", 1, 2, 3, nama="Budi", umur=20)
```

## 3.7 Scope (Local vs Global)

```python
x = 10                    # global

def ubah():
    x = 20                # local (tidak mengubah global)
    print("Dalam fungsi:", x)

ubah()
print("Luar fungsi:", x)  # tetap 10

# Mengubah variabel global (hindari jika memungkinkan)
counter = 0
def tambah_counter():
    global counter
    counter += 1

tambah_counter()
print(counter)            # 1
```

> Best Practice Scope Hindari penggunaan 'global' sebisa mungkin. Lebih baik menggunakan return value. Function yang baik bersifat pure: menerima input → memproses → mengembalikan output, tanpa side effect tersembunyi.

## 3.8 Docstring

```python
def hitung_ipk(nilai1, nilai2, nilai3):
    """
    Menghitung rata-rata dari tiga nilai.

    Parameters:
        nilai1 (float): Nilai pertama
        nilai2 (float): Nilai kedua
        nilai3 (float): Nilai ketiga

    Returns:
        float: Rata-rata ketiga nilai
    """
    return (nilai1 + nilai2 + nilai3) / 3

help(hitung_ipk)          # menampilkan docstring
```

## 3.9 Latihan Modul 1 — Functions

1. Buat function hitung_luas_segitiga(alas, tinggi) yang mengembalikan luas.
2. Buat function cek_genap(angka) yang return True jika genap, False jika ganjil.
3. Buat function rata_rata(*angka) menggunakan *args yang menghitung rata-rata banyak angka.
4. Buat function info_mahasiswa(**data) yang menampilkan semua data mahasiswa dari kwargs.
5. Buat function konversi_nilai(angka) yang mengubah nilai 0-100 menjadi grade A/B/C/D/E.

# 4. Modul 2 — Lambda, map, filter & List Comprehension

## 4.1 Lambda Function

Lambda adalah function anonim (tanpa nama) yang biasanya digunakan untuk operasi sederhana dalam satu baris.

```python

# Function biasa
def kuadrat(x):
    return x ** 2

# Lambda equivalent
kuadrat = lambda x: x ** 2
print(kuadrat(5))               # 25

# Lambda dengan multiple argument
tambah = lambda a, b: a + b
print(tambah(3, 7))             # 10

# Lambda langsung dipanggil
print((lambda x: x * 2)(10))    # 20

# Penggunaan umum: sorting
mahasiswa = [
    {"nama": "Ani", "ipk": 3.5},
    {"nama": "Budi", "ipk": 3.9},
    {"nama": "Citra", "ipk": 3.2}
]
urut = sorted(mahasiswa, key=lambda m: m["ipk"], reverse=True)
print(urut)
```

## 4.2 map()

map() menerapkan function ke setiap elemen iterable dan mengembalikan iterator.

```python
angka = [1, 2, 3, 4, 5]

# Dengan function biasa
def kali_dua(x):
    return x * 2
hasil = list(map(kali_dua, angka))
print(hasil)                    # [2, 4, 6, 8, 10]

# Dengan lambda
hasil = list(map(lambda x: x * 2, angka))
print(hasil)

# map dengan multiple iterable
a = [1, 2, 3]
b = [10, 20, 30]
jumlah = list(map(lambda x, y: x + y, a, b))
print(jumlah)                   # [11, 22, 33]

# Konversi tipe
teks_angka = ["10", "20", "30"]
angka_int = list(map(int, teks_angka))
print(angka_int)
```

## 4.3 filter()

filter() menyaring elemen iterable berdasarkan kondisi (function yang return True/False).

```python
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ambil yang genap
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)                    # [2, 4, 6, 8, 10]

# Ambil yang > 5
besar = list(filter(lambda x: x > 5, angka))
print(besar)                    # [6, 7, 8, 9, 10]

# Filter string
nama = ["Ani", "Budi", "Citra", "Dedi", "Eka"]
nama_a = list(filter(lambda n: n.startswith("A") or n.startswith("E"), nama))
print(nama_a)                   # ['Ani', 'Eka']

# Filter dictionary
mhs = [
    {"nama": "Ani", "ipk": 3.5},
    {"nama": "Budi", "ipk": 2.8},
    {"nama": "Citra", "ipk": 3.9}
]
lulus = list(filter(lambda m: m["ipk"] >= 3.0, mhs))
print(lulus)
```

## 4.4 List Comprehension

Cara paling Pythonic untuk membuat list baru dari iterable yang sudah ada. Lebih readable daripada map/filter di banyak kasus.

```python
angka = [1, 2, 3, 4, 5]

# Dasar
kuadrat = [x ** 2 for x in angka]
print(kuadrat)                  # [1, 4, 9, 16, 25]

# Dengan kondisi (filter)
genap = [x for x in angka if x % 2 == 0]
print(genap)                    # [2, 4]

# Dengan if-else
label = ["genap" if x % 2 == 0 else "ganjil" for x in angka]
print(label)

# Nested
matriks = [[1, 2], [3, 4], [5, 6]]
datar = [num for baris in matriks for num in baris]
print(datar)                    # [1, 2, 3, 4, 5, 6]

# Dari string
huruf = [c.upper() for c in "python" if c not in "aeiou"]
print(huruf)                    # ['P', 'Y', 'T', 'H', 'N']

# Dictionary comprehension
kuadrat_dict = {x: x**2 for x in range(1, 6)}
print(kuadrat_dict)             # {1:1, 2:4, 3:9, 4:16, 5:25}

# Set comprehension
unik = {x % 3 for x in range(10)}
print(unik)                     # {0, 1, 2}
```

> Kapan pakai apa? List comprehension → pilihan utama untuk membuat list baru (paling readable). map/filter → berguna jika sudah punya function yang siap pakai. Lambda → cocok untuk operasi sangat sederhana, terutama sebagai key di sorted().

## 4.5 Latihan Modul 2

6. Dengan list comprehension: buat list kuadrat dari 1 sampai 20.
7. Dari list nilai = [60, 75, 40, 90, 55, 80], ambil hanya yang lulus (≥75) lalu kalikan 1.1 (bonus).
8. Gunakan filter + lambda untuk mengambil nama yang panjangnya > 4 dari list nama.
9. Buat dictionary comprehension: {angka: "genap"/"ganjil"} untuk angka 1–10.

# 5. Modul 3 — Modules & Packages

## 5.1 Apa itu Module?

Module adalah file Python (.py) yang berisi function, class, atau variabel yang bisa digunakan kembali di file lain. Package adalah kumpulan module dalam satu folder.

## 5.2 Import Module Built-in

```python
import math
print(math.sqrt(16))            # 4.0
print(math.pi)                  # 3.14159...
print(math.ceil(3.2))           # 4
print(math.floor(3.8))          # 3

from math import sqrt, pi
print(sqrt(25))                 # 5.0
print(pi)

from math import sqrt as akar
print(akar(36))                 # 6.0

import random
print(random.randint(1, 10))
print(random.choice(["A", "B", "C"]))
print(random.sample(range(1, 50), 6))   # 6 angka unik

from datetime import datetime, timedelta
sekarang = datetime.now()
print(sekarang.strftime("%Y-%m-%d %H:%M"))
besok = sekarang + timedelta(days=1)
print(besok.date())
```

## 5.3 Membuat Module Sendiri

Buat file matematika_utils.py:

```python

# File: matematika_utils.py
"""Kumpulan function matematika sederhana."""

PI = 3.14159

def luas_lingkaran(r):
    return PI * r ** 2

def keliling_lingkaran(r):
    return 2 * PI * r

def luas_persegi(sisi):
    return sisi * sisi

def cek_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

Lalu di file utama (main.py):

```python
import matematika_utils as mu

print(mu.luas_lingkaran(7))
print(mu.cek_prima(17))         # True
print(mu.PI)

# Atau
from matematika_utils import luas_lingkaran, cek_prima
print(luas_lingkaran(5))
```

## 5.4 Struktur Package Sederhana

```python

# Struktur folder:

# mypackage/

# ├── __init__.py          (boleh kosong)

# ├── matematika.py

# └── string_utils.py

# Cara import:
from mypackage import matematika
from mypackage.string_utils import slugify
```

## 5.5 Latihan Modul 3

10. Buat module konversi.py berisi function: celsius_ke_fahrenheit, fahrenheit_ke_celsius, meter_ke_km.
11. Buat module string_utils.py berisi: hitung_vokal, balik_string, apakah_palindrome.

# 6. Modul 4 — Error Handling (try-except)

## 6.1 Mengapa Perlu Error Handling?

Program yang baik tidak boleh langsung crash ketika terjadi kesalahan input atau kondisi tak terduga. try-except memungkinkan kita menangani error secara elegan.

## 6.2 Dasar try-except

```python
try:
    angka = int(input("Masukkan angka: "))
    print(f"Hasil: {angka * 2}")
except ValueError:
    print("Input harus berupa angka!")

# Multiple except
try:
    hasil = 10 / int(input("Pembagi: "))
    print(hasil)
except ValueError:
    print("Harus angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")

# Menangkap semua error (hati-hati, kurang spesifik)
try:
    # kode berisiko
    pass
except Exception as e:
    print(f"Terjadi error: {e}")
```

## 6.3 else dan finally

```python
try:
    angka = int(input("Angka: "))
    hasil = 100 / angka
except ValueError:
    print("Bukan angka!")
except ZeroDivisionError:
    print("Jangan masukkan 0!")
else:
    # Dijalankan jika TIDAK ada error
    print(f"Hasil: {hasil}")
finally:
    # SELALU dijalankan (ada error maupun tidak)
    print("Proses selesai.")
```

## 6.4 raise — Memunculkan Error Sendiri

```python
def set_umur(umur):
    if not isinstance(umur, int):
        raise TypeError("Umur harus integer")
    if umur < 0 or umur > 150:
        raise ValueError("Umur tidak masuk akal")
    print(f"Umur diset: {umur}")

try:
    set_umur(-5)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
```

## 6.5 Latihan Modul 4

12. Buat program pembagian yang menangani ValueError dan ZeroDivisionError dengan baik.
13. Buat function ambil_nilai_dict(data, key) yang mengembalikan value atau pesan error jika key tidak ada (jangan sampai KeyError).

# 7. Modul 5 — File Handling

## 7.1 Membaca & Menulis File Teks

```python

# Menulis file (mode 'w' = write, menimpa; 'a' = append)
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Halo, ini baris pertama.\n")
    f.write("Ini baris kedua.\n")

# Membaca seluruh isi
with open("catatan.txt", "r", encoding="utf-8") as f:
    isi = f.read()
    print(isi)

# Membaca per baris
with open("catatan.txt", "r", encoding="utf-8") as f:
    for baris in f:
        print(baris.strip())

# Membaca semua baris ke list
with open("catatan.txt", "r", encoding="utf-8") as f:
    baris_list = f.readlines()
```

> Penting: with statement Selalu gunakan 'with open(...) as f' agar file otomatis ditutup, bahkan jika terjadi error. Ini adalah praktik terbaik (context manager).

## 7.2 pathlib — Cara Modern Mengelola Path

```python
from pathlib import Path

# Membuat path
folder = Path("data")
file_path = folder / "mahasiswa.txt"   # operator / sangat nyaman

# Cek keberadaan
print(file_path.exists())
print(file_path.is_file())
print(folder.is_dir())

# Membuat folder
folder.mkdir(exist_ok=True)

# Menulis dengan pathlib
file_path.write_text("Ani,2201,3.75\nBudi,2202,3.50\n", encoding="utf-8")

# Membaca
isi = file_path.read_text(encoding="utf-8")
print(isi)

# List semua file di folder
for f in Path(".").glob("*.py"):
    print(f.name)
```

## 7.3 Membaca & Menulis CSV

```python
import csv
from pathlib import Path

# Menulis CSV
data = [
    ["nama", "nim", "ipk"],
    ["Ani", "2201", "3.75"],
    ["Budi", "2202", "3.50"],
    ["Citra", "2203", "3.90"]
]

with open("mahasiswa.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Membaca CSV
with open("mahasiswa.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)            # skip header
    for row in reader:
        print(row)

# Membaca sebagai Dictionary (lebih nyaman)
with open("mahasiswa.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['nama']} - IPK: {row['ipk']}")

# Menulis dengan DictWriter
data_dict = [
    {"nama": "Dewi", "nim": "2204", "ipk": "3.60"},
    {"nama": "Eka", "nim": "2205", "ipk": "3.80"}
]
with open("mahasiswa2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nama", "nim", "ipk"])
    writer.writeheader()
    writer.writerows(data_dict)
```

## 7.4 Latihan Modul 5

14. Tulis daftar 5 mata kuliah ke file mk.txt (satu per baris), lalu baca dan tampilkan.
15. Buat file CSV nilai.csv berisi header + 3 data mahasiswa, lalu baca dengan DictReader.
16. Gunakan pathlib untuk mengecek apakah file tertentu ada, jika ada baca isinya.

# 8. Mini Project 1 — Pencatat Kegiatan Akademik (Level Dasar)

## 8.1 Deskripsi

Buat program untuk mencatat kegiatan akademik harian mahasiswa (kuliah, mengerjakan tugas, riset, organisasi, dll.). Data disimpan ke file CSV agar tidak hilang saat program ditutup.

## 8.2 Fitur Wajib

1. Tambah kegiatan baru (tanggal, jenis kegiatan, deskripsi, durasi menit)
2. Tampilkan semua kegiatan yang sudah dicatat
3. Tampilkan total durasi kegiatan hari ini / semua
4. Simpan data ke file CSV secara otomatis
5. Muat data dari CSV saat program dimulai
6. Keluar

## 8.3 Struktur Data yang Disarankan

```python

# List of Dictionary
kegiatan = [
    {
        "tanggal": "2026-09-21",
        "jenis": "Kuliah",
        "deskripsi": "Pemrograman Python",
        "durasi": 120
    },
    # ...
]
```

## 8.4 Ketentuan Teknis

- Gunakan function untuk setiap fitur
- Gunakan modul csv + pathlib
- File CSV disimpan otomatis setiap ada perubahan data
- Saat program dimulai, muat data dari CSV jika file sudah ada
- Validasi input sederhana (durasi harus angka positif)
- Ikuti PEP 8

## 8.5 Petunjuk Implementasi (Skeleton)

```python
from pathlib import Path
import csv
from datetime import date

FILE_CSV = Path("kegiatan.csv")

def muat_data():
    # jika file ada, baca dengan DictReader, return list of dict
    # jika tidak ada, return list kosong
    pass

def simpan_data(data):
    # tulis data ke CSV dengan DictWriter
    pass

def tambah_kegiatan(data):
    # minta input, validasi, append, lalu simpan_data()
    pass

def tampilkan_kegiatan(data):
    pass

def total_durasi(data):
    # hitung jumlah durasi
    pass

# Program utama
data = muat_data()
while True:
    # menu + if-elif
```

> Tips Mini Project 1 Kerjakan dulu fitur muat_data dan simpan_data — ini fondasinya. Gunakan date.today().isoformat() untuk tanggal otomatis jika ingin. Uji dengan menambah data, tutup program, buka lagi — data harus tetap ada.

# 9. Mini Project 2 — Sistem Perpustakaan Mini (Level Lebih Tinggi)

## 9.1 Deskripsi

Buat sistem sederhana untuk mengelola koleksi buku dan peminjaman. Data buku dan peminjaman disimpan di dua file CSV terpisah. Memanfaatkan function, module, error handling, dan file handling.

## 9.2 Fitur Wajib

1. Tambah buku baru (judul, penulis, tahun, stok)
2. Tampilkan daftar semua buku + stok tersedia
3. Pinjam buku (kurangi stok, catat peminjaman)
4. Kembalikan buku (tambah stok, update status peminjaman)
5. Tampilkan riwayat peminjaman aktif
6. Data tersimpan di buku.csv dan peminjaman.csv

## 9.3 Struktur Data yang Disarankan

```python

# buku.csv

# id,judul,penulis,tahun,stok

# peminjaman.csv

# id,id_buku,nama_peminjam,tanggal_pinjam,status

# status: "aktif" atau "selesai"
```

## 9.4 Ketentuan Teknis

- Pisahkan logic ke beberapa function (atau bahkan module terpisah jika memungkinkan)
- Gunakan try-except saat membaca/menulis file dan konversi angka
- Validasi: stok tidak boleh negatif, tidak bisa pinjam jika stok = 0
- ID buku dan ID peminjaman di-generate otomatis (misalnya max id + 1)
- Ikuti PEP 8

## 9.5 Petunjuk Implementasi (Skeleton)

```python
from pathlib import Path
import csv
from datetime import date

def muat_buku(): ...
def simpan_buku(data): ...
def muat_peminjaman(): ...
def simpan_peminjaman(data): ...

def tambah_buku(buku): ...
def tampilkan_buku(buku): ...
def pinjam_buku(buku, peminjaman): ...
def kembalikan_buku(buku, peminjaman): ...
def tampilkan_peminjaman_aktif(peminjaman, buku): ...

# Program utama dengan menu
```

> Tips Mini Project 2 Mulai dari CRUD buku dulu sampai lancar. Baru kerjakan fitur pinjam dan kembalikan. Gunakan ID unik agar relasi antara buku dan peminjaman mudah. Banyak gunakan function agar kode tidak berantakan.

# 10. Troubleshooting Hari 2

## 10.1 Function terkait

```python

# TypeError: function missing required argument

# → Anda memanggil function tanpa memberi argument yang wajib

# UnboundLocalError

# → Anda mengubah variabel yang sama dengan nama global di dalam function

#   tanpa menulis 'global'. Solusi: gunakan return, hindari global.
```

## 10.2 File Handling

```python

# FileNotFoundError

# → File yang ingin dibaca belum ada. Cek path atau buat file dulu.

# PermissionError

# → Tidak punya izin menulis di folder tersebut.

# csv.Error atau data berantakan

# → Selalu gunakan newline="" saat open untuk menulis CSV di Windows.

# UnicodeEncodeError / DecodeError

# → Selalu tentukan encoding="utf-8".
```

## 10.3 Module

```python

# ModuleNotFoundError

# → File module tidak berada di folder yang sama / sys.path tidak mengandung folder tersebut.

# → Atau virtual environment belum diaktifkan.
```

# 11. Solusi Latihan Hari 2

## 11.1 Solusi Modul Functions

```python
def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def cek_genap(angka):
    return angka % 2 == 0

def rata_rata(*angka):
    if not angka:
        return 0
    return sum(angka) / len(angka)

def info_mahasiswa(**data):
    for k, v in data.items():
        print(f"{k}: {v}")

def konversi_nilai(angka):
    if angka >= 85: return "A"
    elif angka >= 70: return "B"
    elif angka >= 55: return "C"
    elif angka >= 40: return "D"
    else: return "E"
```

## 11.2 Solusi Lambda / List Comp

```python
kuadrat = [x**2 for x in range(1, 21)]

nilai = [60, 75, 40, 90, 55, 80]
bonus = [n * 1.1 for n in nilai if n >= 75]

nama = ["Ani", "Budi", "Citra", "Eko", "Fajar"]
panjang = list(filter(lambda n: len(n) > 4, nama))

paritas = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
```

## 11.3 Solusi File Handling (contoh)

```python
from pathlib import Path

# Tulis mata kuliah
mk = ["Kalkulus", "Fisika", "Pemrograman", "Basis Data", "AI"]
Path("mk.txt").write_text("\n".join(mk), encoding="utf-8")

# Baca lagi
print(Path("mk.txt").read_text(encoding="utf-8"))
```

> ✓ Materi Hari 2 Selesai Kerjakan kedua Mini Project  •  Siapkan diri untuk Hari 3 (OOP)

11.4 Solusi Modul 3 — Modules & Packages

```python

# File: matematika.py
def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b

PI = 3.14159

# File: main.py
import matematika
from matematika import kali, PI

print(matematika.tambah(3, 4))  # 7
print(kali(5, 6))              # 30
print(PI)
```

11.5 Solusi Modul 4 — Error Handling

```python

# Soal: fungsi bagi yang aman
def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: tidak bisa dibagi nol")
        return None
    except TypeError:
        print("Error: input harus angka")
        return None
    else:
        return hasil
    finally:
        print("Operasi selesai")

print(bagi(10, 2))   # 5.0
print(bagi(10, 0))   # Error + None
print(bagi(10, "a")) # Error + None

# Validasi input angka dari user
def input_angka(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid!")
```

Tips Mini Project Hari 2

• Pecah logika menjadi function kecil (satu function = satu tugas).

• Gunakan try-except saat membaca/menulis file.

• Simpan data ke CSV agar mudah dibaca ulang.

• Uji setiap menu satu per satu sebelum menggabungkan.

