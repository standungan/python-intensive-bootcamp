# Hari 1 — Python Fundamentals & Environment Setup

_Python Intensive Bootcamp • 6 Jam_

Python Intensive Bootcamp  •  6 Jam  •  Level Pemula → Menengah Awal

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Hari 1, peserta mampu:

- Menyiapkan environment Python profesional (Python, venv, VS Code/Cursor, Jupyter).
- Menguasai variabel, tipe data, operator, dan input/output dengan f-string.
- Menguasai control flow: if-elif-else, for, while, break, continue, dan nested loop.
- Menggunakan List, Tuple, Dictionary, dan Set beserta operasi pentingnya.
- Menulis kode sesuai PEP 8 secara konsisten.
- Menyelesaikan 2 Mini Project dengan level berbeda.

# 2. Agenda & Alokasi Waktu

| Waktu | Sesi | Durasi | Jenis |
|---|---|---|---|
| 00:00–00:40 | Opening + Environment Setup | 40 menit | Praktik |
| 00:40–01:25 | Modul 2: Variabel, Tipe Data, Operator, I/O | 45 menit | Teori + Banyak Contoh |
| 01:25–02:25 | Modul 3: Control Flow | 60 menit | Teori + Latihan |
| 02:25–02:50 | Istirahat | 25 menit | — |
| 02:50–04:15 | Modul 4: Data Structures | 85 menit | Teori + Latihan Intensif |
| 04:15–05:30 | Mini Project 1 + Mini Project 2 | 75 menit | Project + Mentoring |
| 05:30–06:00 | Review + PEP 8 + Q&A | 30 menit | Review |

# 3. Modul 1 — Environment Setup (Ringkas)

Pastikan setup berikut sudah selesai:

- Python terinstall (python --version berhasil)
- Virtual environment (.venv) dibuat dan diaktifkan
- VS Code / Cursor + ekstensi Python & Jupyter
- Interpreter mengarah ke .venv

# 4. Modul 2 — Variabel, Tipe Data, Operator & I/O

## 4.1 Variabel — Banyak Contoh

```python
nama = "Rina Kartika"
nim = "2201010234"
semester = 3
ipk = 3.67
aktif = True

x, y, z = 10, 20, 30
a = b = c = 0
p, q = 5, 9
p, q = q, p                    # swap

print(type(nama))              # <class 'str'>
data = 100
data = "seratus"               # tipe bisa berubah
```

## 4.2 Tipe Data & Casting — Banyak Contoh

```python
print(int("42") + 8)            # 50
print(float("3.14") * 2)        # 6.28
print(str(100) + " poin")       # 100 poin
print(int(3.99))                # 3
print(round(3.99))              # 4
print(bool(0), bool(1))         # False True
print(bool(""), bool("Python")) # False True

prodi = "Teknik Informatika"
print(prodi.upper())
print(prodi[0:6])               # Teknik
print("Info" in prodi)          # True
```

## 4.3 Operator — Banyak Contoh

```python
print(17 // 5)                  # 3
print(17 % 5)                   # 2
print(2 ** 8)                   # 256
total = 10
total += 5                      # 15
total *= 2                      # 30

nilai = 80
print(60 <= nilai <= 90)        # True (chained)
ipk, sks = 3.6, 20
print(ipk >= 3.5 and sks >= 18) # True
```

## 4.4 Input & Output — Banyak Contoh

```python
nama = "Siti"
nilai = 88.5
print(f"Mahasiswa {nama} mendapat nilai {nilai}")
print(f"Nilai: {nilai:.1f}")

nama = input("Nama: ").strip()
umur_str = input("Umur: ")
if umur_str.isdigit():
    print(f"Halo {nama}, umur {int(umur_str)}")
else:
    print("Umur harus angka!")
```

## 4.5 Latihan Modul 2

1. Buat variabel nama, NIM, semester, IPK, status aktif. Tampilkan dengan f-string rapi.
2. Minta dua angka, tampilkan hasil +, -, *, /, //, %.
3. Konversi suhu Celsius → Fahrenheit (F = C × 9/5 + 32).
4. Hitung luas & keliling lingkaran dari jari-jari user (π = 3.14159).

# 5. Modul 3 — Control Flow

## 5.1 if-elif-else — Banyak Contoh

```python
nilai = int(input("Nilai: "))
if nilai >= 85: grade = "A"
elif nilai >= 70: grade = "B"
elif nilai >= 55: grade = "C"
elif nilai >= 40: grade = "D"
else: grade = "E"
print(f"Grade: {grade}")

username = input("Username: ")
password = input("Password: ")
if username == "admin" and password == "python123":
    print("Login berhasil!")
else:
    print("Gagal login.")

ipk = float(input("IPK: "))
sks = int(input("SKS: "))
if ipk >= 3.5:
    if sks >= 20:
        print("Berhak magang.")
    else:
        print("SKS kurang.")
else:
    print("IPK belum cukup.")
```

## 5.2 for Loop — Banyak Contoh

```python
for i in range(5): print(i)             # 0-4
for i in range(2, 11, 2): print(i)      # 2 4 6 8 10

warna = ["merah", "hijau", "biru"]
for idx, w in enumerate(warna, 1):
    print(f"{idx}. {w}")

nilai_list = [65, 80, 55, 90, 70]
for n in nilai_list:
    if n >= 70: print(n)

total = sum(nilai_list)
print(f"Rata-rata: {total / len(nilai_list):.2f}")
```

## 5.3 while Loop — Banyak Contoh

```python
n = 5
while n > 0:
    print(n)
    n -= 1

while True:
    angka = input("Angka positif: ")
    if angka.isdigit() and int(angka) > 0:
        print(f"Valid: {angka}")
        break
    print("Coba lagi.")

rahasia = 7
while True:
    tebak = int(input("Tebak 1-10: "))
    if tebak < rahasia: print("Terlalu kecil")
    elif tebak > rahasia: print("Terlalu besar")
    else:
        print("Benar!")
        break
```

## 5.4 break, continue & Nested Loop

```python
for i in range(1, 11):
    if i == 6: break
    print(i, end=" ")              # 1-5
print()

for i in range(1, 11):
    if i % 2 == 0: continue
    print(i, end=" ")              # ganjil
print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

## 5.5 Latihan Modul 3

5. Program penentu genap/ganjil.
6. Tampilkan bilangan genap 1–50.
7. Kasir: total ≥100.000 dapat diskon 10%.
8. Game tebak angka dengan petunjuk.
9. Cetak pola segitiga bintang (nested for).

# 6. Modul 4 — Data Structures

## 6.1 List — Banyak Contoh

```python
mk = ["Kalkulus", "Fisika", "Pemrograman"]
nilai = [78, 85, 90, 70, 88]
print(mk[0], mk[-1], mk[1:3])
mk.append("AI")
mk.insert(1, "Statistika")
mk.remove("Fisika")
print(len(mk), min(nilai), max(nilai), sum(nilai))
nilai.sort(reverse=True)
lulus = [n for n in nilai if n >= 75]
print(lulus)
```

## 6.2 Tuple — Banyak Contoh

```python
titik = (3, 5)
x, y = titik
data = ("Ani", "210123", 3.8)
nama, nim, ipk = data
satu = (42,)                      # single-element tuple
```

## 6.3 Dictionary — Banyak Contoh

```python
mhs = {"nama": "Dewi", "nim": "2201", "ipk": 3.72, "mk": ["AI", "BD"]}
print(mhs.get("alamat", "Belum diisi"))
mhs["semester"] = 4
mhs["mk"].append("Jaringan")

daftar = [
    {"nama": "Ani", "ipk": 3.5},
    {"nama": "Budi", "ipk": 3.8},
    {"nama": "Citra", "ipk": 3.2}
]
terbaik = max(daftar, key=lambda x: x["ipk"])
print(terbaik["nama"])
```

## 6.4 Set — Banyak Contoh

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)                      # union
print(a & b)                      # intersection
print(a - b)                      # difference
unik = list(set([1, 2, 2, 3, 3]))  # hapus duplikat
```

## 6.5 Latihan Modul 4

10. List 5 mata kuliah: tampilkan, tambah 1, hapus pertama.
11. Dictionary data diri (nama, nim, prodi, hobi list). Tampilkan key-value.
12. nilai = [75,80,90,65,88,70,95] → hitung yang lulus (≥75).
13. Dua set hobi: tampilkan intersection & union.
14. List of dict 3 mahasiswa → tampilkan IPK tertinggi.

# 7. Best Practice — PEP 8 (Pembahasan Lengkap)

PEP 8 (Python Enhancement Proposal 8) adalah style guide resmi untuk penulisan kode Python. Tujuan utamanya adalah membuat kode mudah dibaca, konsisten, dan profesional. Kode yang rapi akan sangat membantu saat Anda bekerja dalam tim, mengerjakan skripsi/tesis, atau membuka kembali kode lama.

## 7.1 Mengapa PEP 8 Penting?

- Kode lebih mudah dibaca oleh orang lain (dan diri sendiri di masa depan)
- Mengurangi bug yang disebabkan oleh ketidakjelasan struktur
- Standar industri — hampir semua perusahaan dan open source project mengikuti PEP 8
- Membiasakan diri menulis kode profesional sejak awal

## 7.2 Aturan Indentasi & Layout

1. Gunakan 4 spasi untuk setiap level indentasi. Jangan menggunakan Tab.
2. Usahakan setiap baris tidak lebih dari 79 karakter.
3. Pisahkan function dan class tingkat atas dengan 2 baris kosong.
4. Pisahkan method di dalam class dengan 1 baris kosong.

## 7.3 Aturan Penamaan (Naming Convention)

| Jenis | Konvensi | Contoh |
|---|---|---|
| Variabel & Function | snake_case | hitung_rata_rata, total_nilai |
| Class | PascalCase | DataMahasiswa, SistemNilai |
| Konstanta | UPPER_CASE | MAX_SKS = 24, PI = 3.14159 |
| Private (konvensi) | _single_leading_underscore | _cache, _internal_data |

## 7.4 Spasi & Operator

```python

# ❌ Buruk
x=1+2
daftar=[1,2,3]
def fungsi(a,b=10):

# ✅ Baik
x = 1 + 2
daftar = [1, 2, 3]
def fungsi(a, b=10):
```

## 7.5 Import

```python

# ❌ Buruk — import di tengah file / wildcard
from math import *

# ✅ Baik — import di bagian paling atas, spesifik
import math
from math import sqrt, pi
```

## 7.6 Contoh Perbandingan Lengkap

```python

# ========== VERSI BURUK ==========
def HitungIPK(n1,n2,n3):
  hasil=(n1+n2+n3)/3
  return hasil
x=HitungIPK(3.5,3.8,3.2)
print("IPK:"+str(x))

# ========== VERSI BAIK (PEP 8) ==========
def hitung_ipk(nilai1, nilai2, nilai3):
    """Menghitung rata-rata dari tiga nilai IPK."""
    hasil = (nilai1 + nilai2 + nilai3) / 3
    return hasil

ipk = hitung_ipk(3.5, 3.8, 3.2)
print(f"IPK: {ipk:.2f}")
```

## 7.7 Tips Menerapkan PEP 8

- Aktifkan formatter otomatis di VS Code/Cursor (misalnya Black atau autopep8)
- Gunakan ekstensi Pylint atau Flake8 untuk memeriksa pelanggaran PEP 8
- Biasakan menulis kode rapi sejak latihan kecil — jangan menunggu project besar
- Baca ulang kode sendiri sebelum dianggap selesai
> Alat Bantu PEP 8 Black (formatter otomatis yang sangat populer) autopep8, yapf Pylint / Flake8 / Ruff (linter) Di VS Code: aktifkan 'Format On Save'

# 8. Mini Project 1 — Sistem Data Mahasiswa Sederhana (Level Dasar)

## 8.1 Deskripsi

Buat program konsol interaktif berbasis menu untuk mengelola data mahasiswa. Data disimpan dalam List of Dictionary di memori (belum perlu file). Program terus berjalan sampai user memilih keluar.

## 8.2 Fitur Wajib

1. Tambah data mahasiswa (Nama, NIM, Prodi, IPK)
2. Tampilkan semua data mahasiswa secara rapi
3. Cari mahasiswa berdasarkan NIM
4. Hapus mahasiswa berdasarkan NIM
5. Tampilkan mahasiswa dengan IPK tertinggi
6. Keluar dari program

## 8.3 Struktur Data yang Disarankan

```python
data_mahasiswa = [
    {
        "nama": "Ani Wijaya",
        "nim": "2201010234",
        "prodi": "Informatika",
        "ipk": 3.75
    },
    # ... data berikutnya
]
```

## 8.4 Ketentuan Teknis

- Gunakan List of Dictionary sebagai struktur data utama
- Gunakan while True untuk menu utama
- Gunakan if-elif-else untuk cabang menu
- Validasi sederhana: IPK harus antara 0.0 – 4.0
- Berikan pesan yang jelas kepada user setiap aksi
- Kode harus rapi dan mengikuti PEP 8
- Pisahkan setiap fitur ke dalam function tersendiri

## 8.5 Contoh Tampilan Menu

```python
========================================
   SISTEM DATA MAHASISWA SEDERHANA
========================================
1. Tambah Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Cari Mahasiswa (berdasarkan NIM)
4. Hapus Mahasiswa
5. Mahasiswa dengan IPK Tertinggi
6. Keluar
----------------------------------------
Pilih menu (1-6):
```

## 8.6 Petunjuk Implementasi (Skeleton)

```python
def tampilkan_menu():
    # tampilkan pilihan 1-6
    pass

def tambah_mahasiswa(data):
    # minta input nama, nim, prodi, ipk
    # validasi IPK 0-4
    # append dictionary baru ke data
    pass

def tampilkan_semua(data):
    # jika data kosong, tampilkan pesan
    # jika ada, loop dan tampilkan rapi
    pass

def cari_mahasiswa(data):
    # minta NIM, cari di data, tampilkan hasil
    pass

def hapus_mahasiswa(data):
    # minta NIM, hapus jika ditemukan
    pass

def ipk_tertinggi(data):
    # gunakan max() + key=lambda
    pass

# Program utama
data_mahasiswa = []
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-6): ").strip()
    # if-elif-else untuk memanggil function yang sesuai
```

> Tips Pengerjaan Mini Project 1 Kerjakan satu function pada satu waktu. Uji dulu sebelum lanjut. Untuk IPK tertinggi: max(data, key=lambda m: m['ipk']) Gunakan .strip() pada setiap input agar spasi berlebih tidak mengganggu. Tambahkan pesan konfirmasi setelah berhasil menambah/menghapus data.

## 8.7 Tantangan Tambahan (Opsional)

- Fitur edit data mahasiswa berdasarkan NIM
- Validasi agar NIM tidak boleh duplikat
- Hitung rata-rata IPK seluruh mahasiswa
- Filter mahasiswa berdasarkan Program Studi

# 9. Mini Project 2 — Sistem Nilai & Statistik Mahasiswa (Level Lebih Tinggi)

## 9.1 Deskripsi

Project ini sedikit lebih menantang. Selain mengelola data mahasiswa, Anda harus mengelola nilai per mata kuliah, menghitung statistik, dan menampilkan peringkat.

## 9.2 Fitur Wajib

1. Tambah mahasiswa (nama, NIM) — NIM tidak boleh duplikat
2. Tambah nilai mata kuliah untuk mahasiswa tertentu (satu mahasiswa bisa punya banyak nilai)
3. Tampilkan semua mahasiswa beserta daftar nilai dan rata-rata masing-masing
4. Hitung & tampilkan rata-rata kelas (semua mahasiswa)
5. Tampilkan peringkat mahasiswa berdasarkan rata-rata nilai (dari tertinggi)
6. Keluar

## 9.3 Struktur Data yang Disarankan

```python
data = [
    {
        "nama": "Ani",
        "nim": "2201",
        "nilai": [80, 90, 85]      # list nilai, bisa bertambah
    },
    {
        "nama": "Budi",
        "nim": "2202",
        "nilai": [70, 75]
    }
]
```

## 9.4 Ketentuan Teknis

- Gunakan function untuk setiap fitur utama
- Validasi: nilai harus 0–100; NIM tidak boleh duplikat
- Jika mahasiswa belum punya nilai, tampilkan pesan yang sesuai
- Urutkan peringkat dari rata-rata tertinggi ke terendah
- Kode harus rapi dan sesuai PEP 8

## 9.5 Petunjuk Implementasi (Skeleton)

```python
def tambah_mahasiswa(data):
    # minta nama & NIM, cek duplikat NIM
    # append dict baru dengan nilai=[]
    pass

def tambah_nilai(data):
    # minta NIM, cari mahasiswa
    # minta nilai, validasi 0-100, append ke list nilai
    pass

def tampilkan_semua(data):
    # loop mahasiswa, hitung rata-rata jika ada nilai
    pass

def rata_rata_kelas(data):
    # kumpulkan semua nilai, hitung rata-rata total
    pass

def peringkat(data):
    # buat list (rata_rata, nama), sorted descending
    pass

# Program utama dengan while True + menu
```

> Tips Pengerjaan Mini Project 2 Mulai dari fitur tambah mahasiswa dulu, pastikan berjalan. Baru lanjut ke tambah nilai. Untuk peringkat: buat list sementara berisi tuple/list [rata_rata, nama], lalu sorted(reverse=True). Gunakan print() untuk debugging di setiap tahap.

# 10. Troubleshooting Singkat

Error yang sering muncul dan solusinya:

- IndentationError → Gunakan 4 spasi konsisten, jangan campur Tab.
- ValueError saat int() → Validasi input dengan .isdigit() atau try-except.
- KeyError → Gunakan .get() atau cek ‘in’ sebelum mengakses key.
- IndexError → Cek len() sebelum mengakses index.
- Infinite Loop → Pastikan ada update variabel atau break yang bisa dicapai.

# 11. Solusi Lengkap Latihan

## 11.1 Solusi Modul 2

### Soal 1

```python
nama = "Rina Kartika"
nim = "2201010234"
semester = 3
ipk = 3.67
aktif = True
print(f"Nama: {nama} | NIM: {nim} | Semester: {semester} | IPK: {ipk} | {'Aktif' if aktif else 'Tidak'}")
```

### Soal 2

```python
a = float(input("Angka 1: "))
b = float(input("Angka 2: "))
print(f"+ : {a+b} | - : {a-b} | * : {a*b} | / : {a/b} | // : {a//b} | % : {a%b}")
```

### Soal 3

```python
c = float(input("Celsius: "))
print(f"{c}°C = {c * 9/5 + 32}°F")
```

### Soal 4

```python
PI = 3.14159
r = float(input("Jari-jari: "))
print(f"Luas: {PI * r**2:.2f} | Keliling: {2 * PI * r:.2f}")
```

## 11.2 Solusi Modul 3

### Genap/Ganjil

```python
n = int(input("Angka: "))
print("Genap" if n % 2 == 0 else "Ganjil")
```

### Genap 1-50

```python
print(*range(2, 51, 2))
```

### Kasir Diskon

```python
total = float(input("Total: "))
bayar = total * 0.9 if total >= 100000 else total
print(f"Bayar: Rp {bayar:,.0f}")
```

### Tebak Angka

```python
rahasia = 7
while True:
    t = int(input("Tebak: "))
    if t < rahasia: print("Kecil")
    elif t > rahasia: print("Besar")
    else: print("Benar!"); break
```

### Pola Bintang

```python
for i in range(1, 6):
    print("* " * i)
```

## 11.3 Solusi Modul 4

### List MK

```python
mk = ["Kalkulus", "Fisika", "Pemrograman", "Basis Data", "Jaringan"]
print(mk)
mk.append("AI")
del mk[0]
print(mk)
```

### Dictionary Data Diri

```python
diri = {"nama": "Rina", "nim": "2201", "prodi": "IF", "hobi": ["baca", "musik"]}
for k, v in diri.items(): print(f"{k}: {v}")
```

### Hitung Lulus

```python
nilai = [75, 80, 90, 65, 88, 70, 95]
print(len([n for n in nilai if n >= 75]))
```

### Set Hobi

```python
a = {"baca", "musik", "olahraga"}
b = {"musik", "gaming", "olahraga"}
print("Irisan:", a & b)
print("Gabungan:", a | b)
```

### IPK Tertinggi

```python
mhs = [{"nama": "Ani", "ipk": 3.5}, {"nama": "Budi", "ipk": 3.85}, {"nama": "Citra", "ipk": 3.2}]
terbaik = max(mhs, key=lambda m: m["ipk"])
print(terbaik["nama"], terbaik["ipk"])
```

> ✓ Materi Hari 1 (Revisi Final) Selesai Kedua Mini Project sekarang memiliki format penyajian yang konsisten • PEP 8 sudah diperluas

10b. Troubleshooting Lengkap (Contoh Kasus)

Berikut contoh kasus nyata untuk error yang sering muncul di Hari 1:

NameError

```python

# Kasus 1: variabel belum didefinisikan
print(nama)          # NameError: name 'nama' is not defined

# Solusi: definisikan dulu → nama = "Ani"

# Kasus 2: salah ketik nama variabel
nilai = 80
print(niali)         # NameError

# Solusi: periksa ejaan → print(nilai)

# Kasus 3: memakai variabel di luar scope
def hitung():
    x = 10
print(x)             # NameError

# Solusi: return x, atau jadikan parameter/global (hindari global)
```

TypeError

```python

# Kasus 1: operasi antar tipe tidak kompatibel
print("Nilai: " + 80)     # TypeError

# Solusi: print("Nilai: " + str(80))  atau  print(f"Nilai: {80}")

# Kasus 2: memanggil non-callable
x = 10
x()                      # TypeError: 'int' object is not callable

# Kasus 3: salah jumlah argumen
def tambah(a, b):
    return a + b
tambah(1)                # TypeError: missing 1 required argument
```

IndexError & KeyError

```python

# IndexError
data = [10, 20, 30]
print(data[5])           # IndexError: list index out of range

# Solusi: cek len(data) atau gunakan try-except

# KeyError
mhs = {"nama": "Ani", "nim": "2201"}
print(mhs["prodi"])      # KeyError: 'prodi'

# Solusi: mhs.get("prodi", "-")  atau  if "prodi" in mhs
```

ValueError & ZeroDivisionError

```python

# ValueError
int("abc")               # ValueError: invalid literal

# Solusi: validasi input sebelum konversi

# ZeroDivisionError
print(10 / 0)            # ZeroDivisionError

# Solusi: cek pembagi != 0 sebelum membagi
```

