# Modul 2 — Functions, Modules & File Handling

_Versi lengkap — pembahasan dalam + kasus beragam · Estimasi: ± 6 jam  ·  Prasyarat: Modul 1 selesai_

> **Catatan pengujian:** seluruh blok kode pada modul ini dijalankan (Python 3.11). Bagian **Output** adalah hasil eksekusi nyata. Blok yang memakai `input()` dijalankan dengan input simulasi yang ditulis di samping label output. Blok yang hanya berisi definisi/komentar diberi keterangan, dan "Uji pelengkap" ditambahkan agar function/class pada blok tersebut terbukti berjalan. Kasus error pada bagian Troubleshooting dijalankan nyata di "Demonstrasi error". Blok yang menulis file (`catatan.txt`, `nilai.csv`, `kegiatan.csv`, `buku.csv`, dst.) dijalankan di folder sementara.

# 1. Apa yang Akan Anda Pelajari

- Merancang function: parameter, default, return, *args/**kwargs, docstring, dan scope.
- Memakai lambda, map/filter, dan list comprehension pada kasus yang berbeda.
- Membuat module sendiri dan memahami import.
- Menangani error dengan try/except dan menulis/membaca file teks serta CSV.

> [!NOTE]
> **Sebelum mulai**
>
> Modul 1 (variabel, control flow, list/dict) sebaiknya sudah dipraktikkan.
>
> Ketik contoh, lalu ubah konteksnya — jangan hanya membaca.
>
> Simpan latihan di portfolio/modul_02/.

# 2. Functions — Pembahasan Dalam

## 2.1 Mengapa function?

Function memecah masalah menjadi unit bernama yang bisa dipanggil ulang, diuji terpisah, dan dibaca seperti kosakata domain (“hitung_ipk”, “cek_lulus”). Tanpa function, logika yang sama sering disalin-tempel — sulit dirawat saat aturan berubah.

## 2.2 Dasar, parameter, default, return

Parameter adalah slot input. Default membuat argumen opsional. `return` mengirim hasil ke pemanggil; tanpa return, function mengembalikan `None`. Pisahkan “hitung nilai” dari “cetak nilai” agar function lebih fleksibel.

```python
# Kasus 1: sapaan
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"
print(sapa("Rina"))
print(sapa("Budi", salam="Selamat pagi"))

# Kasus 2: hitung luas — return, jangan hanya print
def luas_persegi(sisi):
    return sisi * sisi
luas = luas_persegi(5)
print("Luas:", luas)

# Kasus 3: grade dari skor
def nilai_huruf(skor):
    if skor >= 85: return "A"
    if skor >= 70: return "B"
    if skor >= 60: return "C"
    if skor >= 50: return "D"
    return "E"
print(nilai_huruf(78))

# Kasus 4: BMI
def hitung_bmi(berat_kg, tinggi_m):
    return berat_kg / (tinggi_m ** 2)
print(round(hitung_bmi(60, 1.65), 2))

# Kasus 5: rata-rata list (kosong = 0)
def rata_rata(angka):
    if not angka:
        return 0
    return sum(angka) / len(angka)
print(rata_rata([80, 90, 70]))
```

**Output:**

```text
Halo, Rina!
Selamat pagi, Budi!
Luas: 25
B
22.04
80.0
```

## 2.3 *args dan **kwargs

`*args` menampung argumen posisional ekstra sebagai tuple. `**kwargs` menampung pasangan nama=nilai sebagai dict. Berguna saat jumlah input tidak tetap, tetapi jangan dipakai jika parameter eksplisit lebih jelas.

```python
# Kasus jumlah tak terbatas
def jumlahkan(*angka):
    total = 0
    for x in angka:
        total += x
    return total
print(jumlahkan(1, 2, 3, 4))

# Kasus max-min
def max_min(*angka):
    return max(angka), min(angka)
print(max_min(3, 1, 4, 2))

# Kasus profil fleksibel
def profil(nama, **info):
    print("Nama:", nama)
    for k, v in info.items():
        print(f"  {k}: {v}")
profil("Ani", prodi="IF", angkatan=2022, ipk=3.5)
```

**Output:**

```text
10
(4, 1)
Nama: Ani
  prodi: IF
  angkatan: 2022
  ipk: 3.5
```

## 2.4 Scope (local vs global)

Nama di dalam function bersifat lokal kecuali Anda memakai `global` (jarang disarankan). Lebih aman: terima input lewat parameter dan kembalikan hasil lewat `return`.

```python
x = 10
def ubah():
    x = 5
    print("dalam:", x)
ubah()
print("luar:", x)  # 10

# Pola yang lebih baik
def tambah_satu(n):
    return n + 1
x = tambah_satu(x)
```

**Output:**

```text
dalam: 5
luar: 10
```

> [!WARNING]
> **Jebakan scope**
>
> UnboundLocalError: Anda assign ke nama yang sama dengan global di dalam function tanpa parameter/return yang jelas.
>
> Mengubah list/dict mutabel lewat side effect bisa mengejutkan — dokumentasikan atau kembalikan objek baru.

## 2.5 Docstring

Docstring menjelaskan kontrak function: apa yang dilakukan, argumen, dan return. Berguna untuk Anda sendiri dan untuk `help()`.

```python
def rata_rata(angka):
    """Menghitung rata-rata iterable numerik.

    Returns 0 jika kosong.
    """
    if not angka:
        return 0
    return sum(angka) / len(angka)
```

**Output:**

```text
(tidak ada output)
```

## 2.6 Latihan Functions

1. hitung_bmi(berat, tinggi) + kategori kasar (under/normal/over).

```text
Pseudocode:
  FUNCTION hitung_bmi(berat, tinggi)
    bmi ← berat / (tinggi × tinggi)
    IF bmi < 18.5 THEN kategori ← "under"
    ELSE IF bmi < 25 THEN kategori ← "normal"
    ELSE kategori ← "over"
    RETURN bmi dan kategori
```

2. nilai_huruf(skor) lengkap A–E.

```text
Pseudocode:
  FUNCTION nilai_huruf(skor)
    IF skor ≥ 85 RETURN "A"
    ELSE IF skor ≥ 70 RETURN "B"
    ELSE IF skor ≥ 60 RETURN "C"
    ELSE IF skor ≥ 50 RETURN "D"
    ELSE RETURN "E"
```

3. max_min(*angka) → tuple.

```text
Pseudocode:
  FUNCTION max_min(*angka)
    RETURN (nilai maksimum, nilai minimum)
```

4. is_palindrome(teks) — abaikan spasi & huruf besar.

```text
Pseudocode:
  FUNCTION is_palindrome(teks)
    s ← teks dalam huruf kecil tanpa spasi
    RETURN (s sama dengan s terbalik)
```

5. hitung_diskon(total, persen=10) — hanya jika total ≥ 100000, else 0 diskon.

```text
Pseudocode:
  FUNCTION hitung_diskon(total, persen default 10)
    IF total ≥ 100000 THEN RETURN total × persen / 100
    ELSE RETURN 0
```

6. rata_rata_ipk(list_of_dict) dari key "ipk".

```text
Pseudocode:
  FUNCTION rata_rata_ipk(list_of_dict)
    IF list kosong RETURN 0
    jumlah ← sum semua elemen["ipk"]
    RETURN jumlah / banyak elemen
```

7. konversi_suhu(nilai, mode="c2f") mendukung c2f dan f2c.

```text
Pseudocode:
  FUNCTION konversi_suhu(nilai, mode="c2f")
    IF mode = "c2f" RETURN nilai×9/5+32
    ELSE IF mode = "f2c" RETURN (nilai-32)×5/9
    ELSE RETURN None / error
```

8. ringkas_nilai(*nilai) → dict berisi rata, maks, min, jumlah.

```text
Pseudocode:
  FUNCTION ringkas_nilai(*nilai)
    RETURN dict {rata, maks, min, jumlah}
```

# 3. Lambda, map, filter, Comprehension

## 3.1 Pembahasan

Lambda adalah function pendek sekali pakai. `map`/`filter` menerapkan function ke iterable. List comprehension sering lebih pythonic untuk transformasi & filter sederhana. Pilih yang paling mudah dibaca di konteks Anda.

```python
angka = [1, 2, 3, 4, 5]
kuadrat = list(map(lambda x: x ** 2, angka))
genap = list(filter(lambda x: x % 2 == 0, angka))
print(kuadrat, genap)

# Comprehension — kasus transformasi nilai
nilai = [55, 80, 90, 40, 70]
lulus = [v for v in nilai if v >= 70]
label = ["L" if v >= 60 else "TL" for v in nilai]
print(lulus, label)

# Kasus list nama → panjang
nama = ["Ani", "Budi", "Citra"]
panjang = [len(n) for n in nama]

# Kasus dict comprehension genap→kuadrat
d = {x: x ** 2 for x in angka if x % 2 == 0}
print(d)

# Kasus sort key
mhs = [{"nama": "Cici", "ipk": 3.2}, {"nama": "Ani", "ipk": 3.8}]
mhs_sorted = sorted(mhs, key=lambda m: m["ipk"], reverse=True)
print(mhs_sorted)
```

**Output:**

```text
[1, 4, 9, 16, 25] [2, 4]
[80, 90, 70] ['TL', 'L', 'L', 'TL', 'L']
{2: 4, 4: 16}
[{'nama': 'Ani', 'ipk': 3.8}, {'nama': 'Cici', 'ipk': 3.2}]
```

## 3.2 Latihan

1. Dari list nilai: list baru yang ≥ 70.

```text
Pseudocode:
  buat list kosong hasil
  FOR tiap v di list nilai:
    IF v ≥ 70 THEN tambahkan v ke hasil
  RETURN hasil
  # alternatif: list comprehension
```

2. List nama → list panjang karakter.

```text
Pseudocode:
  hasil ← []
  FOR tiap nama n:
    tambahkan len(n) ke hasil
  RETURN hasil
```

3. Dict {angka: kuadrat} hanya untuk genap.

```text
Pseudocode:
  hasil ← {}
  FOR x di angka:
    IF x genap THEN hasil[x] ← x²
  RETURN hasil
```

4. Sort list of dict mahasiswa by IPK naik memakai key=lambda.

```text
Pseudocode:
  urutkan list dengan key = field ipk
  urutan naik (ascending)
  # sorted(mhs, key=lambda m: m["ipk"])
```

# 4. Modules & Packages

## 4.1 Pembahasan

Module adalah file `.py` yang bisa di-import. Memecah kode ke module mengurangi file raksasa dan memungkinkan pemakaian ulang (mis. `konversi.py`, `statistik.py`). Nama file module jangan menabrak modul standar (`random.py` berbahaya).

```python
import math
from random import randint, choice
import datetime as dt
print(math.sqrt(16), randint(1, 6), dt.date.today())

# matematika.py (file terpisah)
# def tambah(a, b): return a + b
# PI = 3.14159

# main.py
# import matematika
# from matematika import tambah, PI
# konversi.py — kasus suhu & jarak
def celsius_ke_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_ke_celsius(f):
    return (f - 32) * 5 / 9

def km_ke_mil(km):
    return km * 0.621371
```

**Output:**

```text
4.0 1 2026-10-01
```

## 4.2 Latihan

1. Buat konversi.py (suhu); import dan uji dari file lain.

```text
Pseudocode:
  BUAT file konversi.py berisi function suhu
  DI main: import konversi
  panggil function; cetak hasil uji
```

2. Buat statistik.py berisi rata, maks, min; pakai di main.

```text
Pseudocode:
  BUAT statistik.py: function rata, maks, min
  DI main: import dan uji dengan list contoh
```

# 5. Error Handling

## 5.1 Pembahasan

Error handling memisahkan jalur sukses dari jalur gagal. `try/except` menangkap exception spesifik. `else` jalan jika tidak ada error. `finally` selalu jalan (rapi resource). `raise` memunculkan error sendiri saat kontrak dilanggar.

```python
# Kasus input angka aman
def input_angka(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Masukkan angka valid.")

# Kasus pembagian aman
def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Tidak bisa dibagi nol")
        return None
    except TypeError:
        print("Tipe harus numerik")
        return None

# Kasus raise untuk validasi domain
def set_ipk(ipk):
    if not 0 <= ipk <= 4:
        raise ValueError("IPK harus 0–4")
    return ipk

try:
    set_ipk(4.5)
except ValueError as e:
    print("Gagal:", e)

# Pola lengkap
try:
    x = int("10")
except ValueError:
    print("bukan angka")
else:
    print("ok", x)
finally:
    print("selesai blok")
```

**Output:**

```text
Gagal: IPK harus 0–4
ok 10
selesai blok
```

**Uji pelengkap — memanggil function di atas**

```python
print(input_angka("Angka: "))
print(bagi(10, 4)); print(bagi(10, 0)); print(bagi(10, "a"))
```

**Output (input simulasi: abc ⏎ 3.5):**

```text
Angka: abc
Masukkan angka valid.
Angka: 3.5
3.5
2.5
Tidak bisa dibagi nol
None
Tipe harus numerik
None
```

> [!WARNING]
> **Jebakan**
>
> except: bare — menangkap semua, termasuk KeyboardInterrupt; lebih baik spesifik.
>
> Menelan error tanpa log membuat bug sulit dilacak.
>
> Jangan pakai try/except untuk kontrol alur normal jika if sudah cukup.

## 5.2 Latihan

1. bagi(a,b) aman (ZeroDivision + TypeError).

```text
Pseudocode:
  FUNCTION bagi(a, b)
    TRY: RETURN a / b
    CATCH ZeroDivisionError: pesan; RETURN None
    CATCH TypeError: pesan; RETURN None
```

2. input_angka(prompt) sampai valid.

```text
Pseudocode:
  FUNCTION input_angka(prompt)
    LOOP:
      TRY: RETURN float(input(prompt))
      CATCH ValueError: cetak peringatan
```

3. set_umur(n) raise ValueError jika n < 0 atau n > 120.

```text
Pseudocode:
  FUNCTION set_umur(n)
    IF n < 0 ATAU n > 120 THEN RAISE ValueError
    RETURN n
```

# 6. File Handling

## 6.1 Teks & with

`with open(...)` memastikan file tertutup meski terjadi error. Mode `w` menimpa, `a` menambah, `r` membaca. Selalu pertimbangkan encoding UTF-8 untuk teks Indonesia.

```python
# Tulis catatan
with open("catatan.txt", "w", encoding="utf-8") as f:
    f.write("Baris satu\n")
    f.write("Baris dua\n")

# Baca seluruh
with open("catatan.txt", "r", encoding="utf-8") as f:
    isi = f.read()
print(isi)

# Baca per baris
with open("catatan.txt", "r", encoding="utf-8") as f:
    for baris in f:
        print(baris.strip())

# Kasus: simpan daftar nama
nama_list = ["Ani", "Budi", "Cici"]
with open("nama.txt", "w", encoding="utf-8") as f:
    for n in nama_list:
        f.write(n + "\n")
```

**Output:**

```text
Baris satu
Baris dua

Baris satu
Baris dua
```

## 6.2 pathlib

`pathlib.Path` membuat manipulasi path lebih jelas di Windows/Linux dan mendukung `read_text` / `write_text`.

```python
from pathlib import Path
p = Path("data")
p.mkdir(exist_ok=True)
file = p / "hasil.txt"
file.write_text("Halo\n", encoding="utf-8")
print(file.read_text(encoding="utf-8"))
print(file.exists(), file.suffix)
```

**Output:**

```text
Halo

True .txt
```

## 6.3 CSV

CSV adalah format tabular sederhana. `csv.DictReader`/`DictWriter` cocok untuk list of dict — selaras dengan pola Modul 1. Gunakan `newline=""` saat menulis di Windows.

```python
import csv
from pathlib import Path

# Tulis
with open("nilai.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["nama", "nim", "nilai"])
    w.writeheader()
    w.writerow({"nama": "Ani", "nim": "2201", "nilai": 90})
    w.writerow({"nama": "Budi", "nim": "2202", "nilai": 85})

# Baca
with open("nilai.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["nama"], row["nilai"])

# Kasus: muat ke list of dict
def muat_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))
```

**Output:**

```text
Ani 90
Budi 85
```

## 6.4 Latihan File

1. Tulis 5 nama ke nama.txt; baca dan cetak.

```text
Pseudocode:
  buka nama.txt mode tulis (with)
  FOR 5 nama: tulis baris ke file
  buka mode baca; cetak seluruh isi
```

2. Simpan list of dict mahasiswa ke CSV; baca ulang.

```text
Pseudocode:
  buka CSV tulis + DictWriter + header
  tulis setiap dict sebagai baris
  baca ulang dengan DictReader; tampilkan
```

3. Append baris log ke kegiatan.log setiap kali fungsi dipanggil (mode a).

```text
Pseudocode:
  FUNCTION catat_log(pesan)
    buka kegiatan.log mode append
    tulis pesan (+ opsional waktu)
  panggil beberapa kali untuk menguji
```

# 7. Mini Project 1 — Pencatat Kegiatan Akademik

### Deskripsi

Catat kegiatan (tanggal, jenis, deskripsi, status). Persist ke CSV agar data tidak hilang saat program ditutup.

### Fitur wajib

1. Tambah kegiatan; tampilkan semua; filter jenis/status.
2. Muat CSV di awal; simpan setiap ada perubahan.
3. Menu interaktif; function terpisah per aksi.

```python
import csv
from pathlib import Path

FILE = Path("kegiatan.csv")
kegiatan = []

def muat():
    global kegiatan
    if not FILE.exists():
        return
    with open(FILE, "r", encoding="utf-8") as f:
        kegiatan = list(csv.DictReader(f))

def simpan():
    if not kegiatan:
        return
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=kegiatan[0].keys())
        w.writeheader()
        w.writerows(kegiatan)

def tambah():
    row = {
        "tanggal": input("Tanggal: "),
        "jenis": input("Jenis (tugas/kuliah/ujian): "),
        "deskripsi": input("Deskripsi: "),
        "status": input("Status (belum/selesai): "),
    }
    kegiatan.append(row)
    simpan()

def tampilkan():
    for i, k in enumerate(kegiatan, 1):
        print(i, k)

def filter_kegiatan():
    kunci = input("Filter jenis/status: ")
    for k in kegiatan:
        if kunci in (k["jenis"], k["status"]):
            print(k)

muat()
while True:
    print("\n1.Tambah 2.Tampil 3.Filter 4.Keluar")
    p = input("Pilih: ")
    if p == "1": tambah()
    elif p == "2": tampilkan()
    elif p == "3": filter_kegiatan()
    elif p == "4": break
```

**Output (input simulasi: 1 ⏎ 2026-09-21 ⏎ tugas ⏎ Laporan Python ⏎ belum ⏎ 1 ⏎ 2026-09-22 ⏎ kuliah ⏎ Pemrograman ⏎ selesai ⏎ 2 ⏎ 3 ⏎ tugas ⏎ 4):**

```text

1.Tambah 2.Tampil 3.Filter 4.Keluar
Pilih: 1
Tanggal: 2026-09-21
Jenis (tugas/kuliah/ujian): tugas
Deskripsi: Laporan Python
Status (belum/selesai): belum

1.Tambah 2.Tampil 3.Filter 4.Keluar
Pilih: 1
Tanggal: 2026-09-22
Jenis (tugas/kuliah/ujian): kuliah
Deskripsi: Pemrograman
Status (belum/selesai): selesai

1.Tambah 2.Tampil 3.Filter 4.Keluar
Pilih: 2
1 {'tanggal': '2026-09-21', 'jenis': 'tugas', 'deskripsi': 'Laporan Python', 'status': 'belum'}
2 {'tanggal': '2026-09-22', 'jenis': 'kuliah', 'deskripsi': 'Pemrograman', 'status': 'selesai'}

1.Tambah 2.Tampil 3.Filter 4.Keluar
Pilih: 3
Filter jenis/status: tugas
{'tanggal': '2026-09-21', 'jenis': 'tugas', 'deskripsi': 'Laporan Python', 'status': 'belum'}

1.Tambah 2.Tampil 3.Filter 4.Keluar
Pilih: 4
```

_Catatan: skenario: tambah dua kegiatan (data disimpan ke `kegiatan.csv`), tampilkan, filter `tugas`, keluar._

# 8. Mini Project 2 — Sistem Perpustakaan Mini

### Deskripsi

Kelola buku: tambah, pinjam, kembalikan, cari. Status tersedia/dipinjam. Data di CSV.

### Fitur wajib

1. CRUD status pinjam/kembali; cari keyword judul/penulis.
2. Persistensi CSV; function terpisah; validasi pinjam hanya jika tersedia.

```python
import csv
from pathlib import Path

FILE = Path("buku.csv")
buku = []

def muat():
    global buku
    if FILE.exists():
        with open(FILE, encoding="utf-8") as f:
            buku = list(csv.DictReader(f))

def simpan():
    if not buku: return
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["judul", "penulis", "tahun", "status"])
        w.writeheader(); w.writerows(buku)

def tambah_buku():
    buku.append({
        "judul": input("Judul: "),
        "penulis": input("Penulis: "),
        "tahun": input("Tahun: "),
        "status": "tersedia",
    })
    simpan()

def pinjam(judul):
    for b in buku:
        if b["judul"].lower() == judul.lower() and b["status"] == "tersedia":
            b["status"] = "dipinjam"; simpan(); return True
    return False

def kembalikan(judul):
    for b in buku:
        if b["judul"].lower() == judul.lower():
            b["status"] = "tersedia"; simpan(); return True
    return False

def cari(keyword):
    key = keyword.lower()
    return [b for b in buku if key in b["judul"].lower() or key in b["penulis"].lower()]

muat()
# menu: tambah / pinjam / kembali / cari / tampil / keluar
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok ini hanya mendefinisikan function dan memanggil `muat()`; menu dibiarkan sebagai tugas peserta (lihat uji pelengkap)._

**Uji pelengkap — menu perpustakaan**

```python
while True:
    print("\n1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar")
    p = input("Pilih: ")
    if p == "1": tambah_buku()
    elif p == "2": print("Berhasil" if pinjam(input("Judul: ")) else "Gagal (tidak ada / sedang dipinjam)")
    elif p == "3": print("Berhasil" if kembalikan(input("Judul: ")) else "Judul tidak ditemukan")
    elif p == "4":
        for b in cari(input("Kata kunci: ")):
            print(b)
    elif p == "5":
        for b in buku:
            print(b)
    elif p == "6": break
```

**Output (input simulasi: 1 ⏎ Python Dasar ⏎ Ani ⏎ 2024 ⏎ 1 ⏎ Basis Data ⏎ Budi ⏎ 2023 ⏎ 5 ⏎ 2 ⏎ python dasar ⏎ 2 ⏎ python dasar ⏎ 4 ⏎ budi ⏎ 3 ⏎ Python Dasar ⏎ 5 ⏎ 6):**

```text

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 1
Judul: Python Dasar
Penulis: Ani
Tahun: 2024

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 1
Judul: Basis Data
Penulis: Budi
Tahun: 2023

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 5
{'judul': 'Python Dasar', 'penulis': 'Ani', 'tahun': '2024', 'status': 'tersedia'}
{'judul': 'Basis Data', 'penulis': 'Budi', 'tahun': '2023', 'status': 'tersedia'}

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 2
Judul: python dasar
Berhasil

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 2
Judul: python dasar
Gagal (tidak ada / sedang dipinjam)

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 4
Kata kunci: budi
{'judul': 'Basis Data', 'penulis': 'Budi', 'tahun': '2023', 'status': 'tersedia'}

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 3
Judul: Python Dasar
Berhasil

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 5
{'judul': 'Python Dasar', 'penulis': 'Ani', 'tahun': '2024', 'status': 'tersedia'}
{'judul': 'Basis Data', 'penulis': 'Budi', 'tahun': '2023', 'status': 'tersedia'}

1.Tambah 2.Pinjam 3.Kembali 4.Cari 5.Tampil 6.Keluar
Pilih: 6
```

_Catatan: menu ditambahkan hanya untuk menguji function; data tersimpan di `buku.csv`. Pinjam kedua kali pada judul yang sama gagal karena sudah berstatus dipinjam._

> [!TIP]
> **Tips project**
>
> Selalu simpan() setelah data berubah.
>
> Bandingkan judul dengan .lower() agar tidak gagal karena kapitalisasi.
>
> Project 1 dulu jika CSV masih terasa sulit.

# 9. Troubleshooting

```python
# TypeError: missing argument → cek jumlah argumen saat panggil function
# UnboundLocalError → hindari assign ke nama global di dalam function; pakai return
# Function mengembalikan None → pastikan semua cabang yang perlu nilai punya return
# FileNotFoundError → cek path; Path.exists() sebelum baca
# PermissionError → file sedang dibuka aplikasi lain
# CSV berantakan → newline="" saat write; encoding utf-8
# ModuleNotFoundError → file module di folder yang sama; jangan namai random.py
```

> **Output:** _tidak dijalankan_ — hanya komentar (daftar jebakan); contoh error nyata dijalankan di bagian "Demonstrasi error" di bawah

## Demonstrasi error — output nyata

Setiap kasus pada daftar di atas dijalankan terpisah di folder sementara agar pesan error aslinya terlihat. `PermissionError` tidak ditampilkan karena bergantung pada hak akses sistem file dan tidak dapat direproduksi andal di lingkungan pengujian (berjalan sebagai root).

### TypeError — argument kurang / berlebih

```python
def perkenalan(nama, prodi):
    print(f"Saya {nama} dari {prodi}")

perkenalan("Ani")
```

**Output:**

```text
  -> TypeError: perkenalan() missing 1 required positional argument: 'prodi'
```

### TypeError — argument kurang / berlebih (2)

```python
def perkenalan(nama, prodi):
    print(f"Saya {nama} dari {prodi}")

perkenalan("Ani", "IF", 3)
```

**Output:**

```text
  -> TypeError: perkenalan() takes 2 positional arguments but 3 were given
```

### UnboundLocalError — assign ke nama global di dalam function

```python
counter = 0

def tambah():
    counter += 1
    return counter

tambah()
```

**Output:**

```text
  -> UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

### Solusi UnboundLocalError — pakai return

```python
counter = 0

def tambah(c):
    return c + 1

counter = tambah(counter)
print(counter)
```

**Output:**

```text
1
```

### Function mengembalikan None — tidak ada return pada salah satu cabang

```python
def nilai_huruf(skor):
    if skor >= 70:
        return "Lulus"
    # lupa return untuk cabang lain

hasil = nilai_huruf(50)
print(hasil)
print(hasil.upper())
```

**Output:**

```text
None
  -> AttributeError: 'NoneType' object has no attribute 'upper'
```

### FileNotFoundError — file belum ada

```python
with open("tidak_ada.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

**Output:**

```text
  -> FileNotFoundError: [Errno 2] No such file or directory: 'tidak_ada.txt'
```

### Solusi FileNotFoundError — cek dengan pathlib

```python
from pathlib import Path

p = Path("tidak_ada.txt")
if p.exists():
    print(p.read_text(encoding="utf-8"))
else:
    print("File belum ada, membuat file kosong...")
    p.write_text("", encoding="utf-8")
print(p.exists())
```

**Output:**

```text
File belum ada, membuat file kosong...
True
```

### UnicodeEncodeError — encoding tidak mendukung karakter

```python
with open("uji.txt", "w", encoding="ascii") as f:
    f.write("Café — Ünicode")
```

**Output:**

```text
  -> UnicodeEncodeError: 'ascii' codec can't encode character '\xe9' in position 3: ordinal not in range(128)
```

### UnicodeDecodeError — dibaca dengan encoding berbeda

```python
with open("uji.txt", "w", encoding="utf-8") as f:
    f.write("Café — Ünicode")

with open("uji.txt", "r", encoding="ascii") as f:
    print(f.read())
```

**Output:**

```text
  -> UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
```

### CSV — isi byte file dengan newline=""

```python
import csv

with open("a.csv", "w", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows([["nama", "nilai"], ["Ani", "90"]])

with open("a.csv", "rb") as f:
    print(f.read())
```

**Output:**

```text
b'nama,nilai\r\nAni,90\r\n'
```

### ModuleNotFoundError — module tidak ditemukan

```python
import matematika_utils
```

**Output:**

```text
  -> ModuleNotFoundError: No module named 'matematika_utils'
```

### ModuleNotFoundError teratasi setelah file module ada

```python
import matematika_utils as mu
print(mu.cek_prima(17))
```

**Output:**

```text
True
```

### Menamai file seperti module bawaan — `random.py` menimpa module `random`

```python
import subprocess, sys

# file random.py buatan sendiri berada di folder yang sama dengan main.py
hasil = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
print(hasil.stderr.strip().splitlines()[-1])
```

**Output:**

```text
AttributeError: module 'random' has no attribute 'randint'
```

# 10. Solusi Latihan (Cuplikan)

```text
Pseudocode:
  FUNCTION is_palindrome(teks)
    s ← teks dalam huruf kecil tanpa spasi
    RETURN (s sama dengan s terbalik)
```

```python
def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

def nilai_huruf(skor):
    if skor >= 85: return "A"
    if skor >= 70: return "B"
    if skor >= 60: return "C"
    if skor >= 50: return "D"
    return "E"

def is_palindrome(teks):
    s = "".join(teks.lower().split())
    return s == s[::-1]

def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None

def input_angka(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Angka saja.")
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok hanya mendefinisikan function; uji pelengkap di bawah memanggilnya._

**Uji pelengkap — memanggil function solusi**

```python
print(hitung_bmi(60, 1.7))
print([nilai_huruf(s) for s in (90, 75, 65, 55, 20)])
print(is_palindrome("Kasur ini rusak"), is_palindrome("Python"))
print(bagi(10, 4), bagi(10, 0), bagi(10, "a"))
print(input_angka("Angka: "))
```

**Output (input simulasi: dua ⏎ 2.5):**

```text
20.761245674740486
['A', 'B', 'C', 'D', 'E']
True False
2.5 None None
Angka: dua
Angka saja.
Angka: 2.5
2.5
```

# 11. Checklist Sebelum Modul 3

- Function + docstring + latihan utama selesai
- Comprehension / lambda sudah dicoba di kasus berbeda
- try/except dipakai di input atau file
- CSV: tulis + baca berhasil
- Minimal Project 1 selesai dan datanya persist
- Siap Modul 3 (OOP)

> **Modul 2 (lengkap) selesai? Lanjut ke Modul 3 — OOP.**
>
> Python Intensive — Modul Belajar Mandiri
