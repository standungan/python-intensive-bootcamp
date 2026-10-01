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

**Output**:

```text
Halo, selamat belajar Python!
Halo, selamat belajar Python!
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

**Output**:

```text
Halo, Rina!
Halo, Budi!
Saya Ani, prodi Informatika, semester 3.
Saya Citra, prodi SI, semester 5.
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

**Output**:

```text
Halo, Rina!
Selamat pagi, Rina!
16
8
6
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

**Output**:

```text
25
59
Luas: 25, Keliling: 20
Lulus
Tidak Lulus
Nilai tidak valid
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

**Output**:

```text
6
100
nama: Ani
prodi: IF
ipk: 3.8
Wajib: utama
Args: (1, 2, 3)
Kwargs: {'nama': 'Budi', 'umur': 20}
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

**Output**:

```text
Dalam fungsi: 20
Luar fungsi: 10
1
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

**Output**:

```text
Help on function hitung_ipk in module __main__:

hitung_ipk(nilai1, nilai2, nilai3)
    Menghitung rata-rata dari tiga nilai.
    
    Parameters:
        nilai1 (float): Nilai pertama
        nilai2 (float): Nilai kedua
        nilai3 (float): Nilai ketiga
    
    Returns:
        float: Rata-rata ketiga nilai
```

_Catatan: `help()` menampilkan docstring lewat pager; di sini output apa adanya saat tidak interaktif._

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

**Output**:

```text
25
10
20
[{'nama': 'Budi', 'ipk': 3.9}, {'nama': 'Ani', 'ipk': 3.5}, {'nama': 'Citra', 'ipk': 3.2}]
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

**Output**:

```text
[2, 4, 6, 8, 10]
[2, 4, 6, 8, 10]
[11, 22, 33]
[10, 20, 30]
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

**Output**:

```text
[2, 4, 6, 8, 10]
[6, 7, 8, 9, 10]
['Ani', 'Eka']
[{'nama': 'Ani', 'ipk': 3.5}, {'nama': 'Citra', 'ipk': 3.9}]
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

**Output**:

```text
[1, 4, 9, 16, 25]
[2, 4]
['ganjil', 'genap', 'ganjil', 'genap', 'ganjil']
[1, 2, 3, 4, 5, 6]
['P', 'Y', 'T', 'H', 'N']
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{0, 1, 2}
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

**Output**:

```text
4.0
3.141592653589793
4
3
5.0
3.141592653589793
6.0
7
B
[30, 48, 35, 4, 49, 16]
2026-10-01 08:05
2026-10-02
```

_Catatan: random.randint/choice/sample dan datetime.now() berubah di setiap eksekusi; nilai di atas hanya contoh satu kali jalan._

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

> **Output:** _tidak dijalankan/tanpa output_ — definisi module `matematika_utils.py` saja (dipakai oleh blok berikutnya)

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

**Output**:

```text
153.93791
True
3.14159
78.53975
```

_Catatan: dijalankan dengan file `matematika_utils.py` dari blok sebelumnya di folder yang sama._

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

**Output**:

```text
import berhasil
```

_Catatan: materi tidak mendefinisikan `slugify`; untuk pengujian dibuat `mypackage/` dengan `matematika.py` dan `string_utils.py` (berisi `slugify`). Baris `print("import berhasil")` ditambahkan hanya untuk bukti import sukses._

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

**Output**:

```text
# skenario 1 — input: 7, 0
Masukkan angka: 7
Hasil: 14
Pembagi: 0
Tidak bisa dibagi nol!

# skenario 2 — input: abc, 5
Masukkan angka: abc
Input harus berupa angka!
Pembagi: 5
2.0
```

_Catatan: dua skenario dijalankan terpisah; di skenario 2 input `abc` memicu ValueError pada `int()` pertama sehingga blok `try` kedua tetap menerima `5`._

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

**Output**:

```text
# skenario 1 — input: 4
Angka: 4
Hasil: 25.0
Proses selesai.

# skenario 2 — input: 0
Angka: 0
Jangan masukkan 0!
Proses selesai.

# skenario 3 — input: abc
Angka: abc
Bukan angka!
Proses selesai.
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

**Output**:

```text
Error: Umur tidak masuk akal
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

**Output**:

```text
Halo, ini baris pertama.
Ini baris kedua.

Halo, ini baris pertama.
Ini baris kedua.
```

_Catatan: dijalankan di folder sementara; `catatan.txt` dibuat otomatis. Baris kosong ekstra setelah "baris kedua" berasal dari `print(isi)` (isi berakhir `\n`)._

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

**Output**:

```text
False
False
False
Ani,2201,3.75
Budi,2202,3.50

main.py
_run.py
```

_Catatan: di folder sementara hanya ada `main.py` dan `_run.py` (skrip penguji), jadi hanya itu yang terdaftar oleh `glob("*.py")`. Pada percobaan pertama `exists()` bernilai False karena folder `data` belum dibuat._

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

**Output**:

```text
['Ani', '2201', '3.75']
['Budi', '2202', '3.50']
['Citra', '2203', '3.90']
Ani - IPK: 3.75
Budi - IPK: 3.50
Citra - IPK: 3.90
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

> **Output:** _tidak dijalankan/tanpa output_ — hanya definisi struktur data, tidak mencetak apa pun

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

> **Output:** _tidak dijalankan/tanpa output_ — skeleton; `while True:` hanya berisi komentar sehingga belum valid dijalankan (IndentationError) — peserta wajib mengisinya

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

> **Output:** _tidak dijalankan/tanpa output_ — hanya komentar (contoh format CSV)

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

> **Output:** _tidak dijalankan/tanpa output_ — skeleton (function berisi `...`, tanpa logika menu)

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

> **Output:** _tidak dijalankan/tanpa output_ — hanya komentar; contoh kasus nyata ada di bagian 10b

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

> **Output:** _tidak dijalankan/tanpa output_ — hanya komentar; contoh kasus nyata ada di bagian 10b

## 10.3 Module

```python
# ModuleNotFoundError
# → File module tidak berada di folder yang sama / sys.path tidak mengandung folder tersebut.
# → Atau virtual environment belum diaktifkan.
```

> **Output:** _tidak dijalankan/tanpa output_ — hanya komentar; contoh kasus nyata ada di bagian 10b

# 10b. Troubleshooting Lengkap (Contoh Kasus)

Berikut contoh kasus nyata untuk error yang sering muncul di Hari 2. Setiap kasus dijalankan terpisah di folder sementara agar semua error terlihat.

## TypeError — argument kurang / berlebih

```python
def perkenalan(nama, prodi):
    print(f"Saya {nama} dari {prodi}")

# Kasus 1: argument wajib tidak diberikan
perkenalan("Ani")

# Kasus 2: argument berlebih
perkenalan("Ani", "IF", 3)

# Solusi: sesuaikan jumlah argument, atau beri default → def perkenalan(nama, prodi="-")
```

**Output:**

```text
# Kasus 1: argument wajib tidak diberikan
  -> TypeError: perkenalan() missing 1 required positional argument: 'prodi'
# Kasus 2: argument berlebih
  -> TypeError: perkenalan() takes 2 positional arguments but 3 were given
```

## UnboundLocalError — mengubah variabel global tanpa `global`

```python
counter = 0

def tambah():
    counter += 1      # UnboundLocalError
    return counter

tambah()

# Solusi 1: return nilai baru → counter = tambah(counter)
# Solusi 2: gunakan `global counter` (hindari jika memungkinkan)
```

**Output:**

```text
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

## FileNotFoundError — file belum ada

```python
# Kasus 1: baca file yang belum dibuat
with open("tidak_ada.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Solusi: cek dulu dengan pathlib atau tangani dengan try-except
```

**Output:**

```text
FileNotFoundError: [Errno 2] No such file or directory: 'tidak_ada.txt'
```

## Menangani FileNotFoundError dengan try-except / pathlib

```python
from pathlib import Path

try:
    with open("tidak_ada.txt", "r", encoding="utf-8") as f:
        isi = f.read()
except FileNotFoundError:
    print("File belum ada, membuat file kosong...")
    Path("tidak_ada.txt").write_text("", encoding="utf-8")

print(Path("tidak_ada.txt").exists())
```

**Output:**

```text
File belum ada, membuat file kosong...
True
```

## UnicodeEncodeError — lupa/salah `encoding`

```python
# Menulis karakter non-ASCII dengan encoding ascii
with open("uji.txt", "w", encoding="ascii") as f:
    f.write("Café — Ünicode")

# Solusi: selalu pakai encoding="utf-8"
```

**Output:**

```text
UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 3: ordinal not in range(128)
```

## UnicodeDecodeError — membaca dengan encoding yang berbeda

```python
with open("uji.txt", "w", encoding="utf-8") as f:
    f.write("Café — Ünicode")

# File ditulis UTF-8 tetapi dibaca sebagai ascii
with open("uji.txt", "r", encoding="ascii") as f:
    print(f.read())

# Solusi: baca dengan encoding yang sama dengan saat menulis → encoding="utf-8"
```

**Output:**

```text
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
```

## CSV — efek `newline=""`

```python
import csv

with open("a.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["nama", "ipk"], ["Ani", "3.75"]])

with open("a.csv", "rb") as f:
    print(f.read())

# Dengan newline="" Python tidak menambah konversi baris sendiri.
# Tanpa newline="" di Windows, \r\n bisa berubah menjadi \r\r\n sehingga muncul baris kosong ekstra.
```

**Output:**

```text
b'nama,ipk\r\nAni,3.75\r\n'
```

_Catatan: Efek baris kosong ganda hanya muncul di Windows; di Linux (lingkungan pengujian) kedua cara menghasilkan byte yang sama, jadi yang ditampilkan adalah isi byte file dengan `newline=""`._

## ModuleNotFoundError — module tidak ditemukan

```python
# Kasus 1: nama module salah / belum ada
import matematika_utils

# Solusi: pastikan file matematika_utils.py ada di folder yang sama,
# atau aktifkan virtual environment bila itu library pihak ketiga (pip install ...).
```

**Output:**

```text
ModuleNotFoundError: No module named 'matematika_utils'
```

## ModuleNotFoundError teratasi setelah file module ada

```python
import sys
print("matematika_utils" in sys.modules)

import matematika_utils as mu
print(mu.cek_prima(17))
```

**Output:**

```text
False
True
```

_Catatan: Folder pengujian berisi `matematika_utils.py` dari bagian 5.3._

## PermissionError — tidak punya izin menulis

```python
from pathlib import Path

try:
    Path("/folder/terlindungi/data.txt").write_text("x", encoding="utf-8")
except PermissionError:
    print("Tidak punya izin menulis di folder tersebut.")
except FileNotFoundError:
    print("Folder tujuan tidak ada.")
```

**Output:**

```text
Folder tujuan tidak ada.
```

_Catatan: `PermissionError` bergantung pada hak akses sistem file sehingga tidak dapat direproduksi andal di lingkungan pengujian ini (berjalan sebagai root). Kode di atas menunjukkan cara menanganinya; solusinya: tulis ke folder yang boleh ditulis (mis. folder project) atau ubah izin folder._

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

> **Output:** _tidak dijalankan/tanpa output_ — hanya definisi function; uji cepat ada di bawah

**Uji cepat** (kode tambahan untuk memverifikasi function di atas):

```python
from math import isclose
print(hitung_luas_segitiga(10, 4))
print(cek_genap(8), cek_genap(7))
print(rata_rata(80, 90, 70), rata_rata())
info_mahasiswa(nama="Ani", prodi="IF", ipk=3.8)
print([konversi_nilai(n) for n in (95, 75, 60, 45, 10)])
```

**Output:**

```text
20.0
True False
80.0 0
nama: Ani
prodi: IF
ipk: 3.8
['A', 'B', 'C', 'D', 'E']
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

> **Output:** _tidak dijalankan/tanpa output_ — hanya ekspresi tanpa print; uji cepat ada di bawah

**Uji cepat** (kode tambahan untuk memverifikasi function di atas):

```python
print(kuadrat)
print(bonus)
print(panjang)
print(paritas)
```

**Output:**

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
[82.5, 99.00000000000001, 88.0]
['Citra', 'Fajar']
{1: 'ganjil', 2: 'genap', 3: 'ganjil', 4: 'genap', 5: 'ganjil', 6: 'genap', 7: 'ganjil', 8: 'genap', 9: 'ganjil', 10: 'genap'}
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

**Output**:

```text
Kalkulus
Fisika
Pemrograman
Basis Data
AI
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

**Output**:

```text
7
30
3.14159
```

_Catatan: dijalankan sebagai dua file (`matematika.py` dan `main.py`) di folder yang sama._

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

**Output**:

```text
Operasi selesai
5.0
Error: tidak bisa dibagi nol
Operasi selesai
None
Error: input harus angka
Operasi selesai
None
```

_Catatan: urutan: "Operasi selesai" tercetak lebih dulu karena `finally` berjalan sebelum hasil `print()` luar._

Tips Mini Project Hari 2

• Pecah logika menjadi function kecil (satu function = satu tugas).

• Gunakan try-except saat membaca/menulis file.

• Simpan data ke CSV agar mudah dibaca ulang.

• Uji setiap menu satu per satu sebelum menggabungkan.
