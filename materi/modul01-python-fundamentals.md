# Modul 1 — Python Fundamentals

_Versi lengkap — pembahasan dalam + kasus beragam · Estimasi: ± 6 jam  ·  Level: Pemula  ·  Prasyarat: tidak ada_

> **Catatan pengujian:** seluruh blok kode pada modul ini dijalankan (Python 3.11). Bagian **Output** adalah hasil eksekusi nyata. Blok yang memakai `input()` dijalankan dengan input simulasi yang ditulis di samping label output. Blok yang hanya berisi definisi/komentar diberi keterangan, dan "Uji pelengkap" ditambahkan agar function/class pada blok tersebut terbukti berjalan. Kasus error pada bagian Troubleshooting dijalankan nyata di "Demonstrasi error".

# 1. Apa yang Akan Anda Pelajari

- Memakai variabel, tipe data, casting, dan operator dengan tepat — termasuk kasus yang sering salah.
- Membangun logika program dengan if, for, while, break/continue, dan nested loop.
- Memilih dan memanipulasi list, tuple, dict, set — serta list of dict untuk data mahasiswa.
- Menulis kode yang lebih rapi (PEP 8) dan menyelesaikan 2 mini project berbasis menu.

> [!NOTE]
> **Cara memakai modul ini**
>
> Jangan hanya membaca. Ketik ulang contoh, lalu ubah angkanya / konteksnya.
>
> Kerjakan latihan sebelum membuka bagian solusi di akhir.
>
> Setiap topik punya pembahasan + kasus beragam + jebakan — jangan loncat langsung ke project.
>
> Simpan file latihan di portfolio/modul_01/.

# 2. Persiapan Lingkungan

Cek Python terpasang, lalu siapkan editor (VS Code, Cursor, atau Jupyter). Untuk uji cepat, REPL juga cukup.

```text
python --version
# atau: python3 --version

python
>>> print("Halo, Python!")
>>> exit()
```

> [!TIP]
> **Tips**
>
> Google Colab bisa dipakai jika environment lokal bermasalah.
>
> Biasakan satu folder khusus modul ini agar file tidak bercampur.

# 3. Variabel, Tipe Data, Operator & I/O

## 3.1 Variabel — pembahasan

Variabel adalah nama yang merujuk ke nilai di memori. Di Python Anda tidak wajib menulis tipe saat membuat variabel; tipe mengikuti nilainya. Yang penting: nama jelas, dan Anda sadar nilai apa yang sedang dipegang.

Penamaan yang baik mengurangi bug. `n` atau `x` hanya cocok di konteks sangat sempit (misalnya indeks loop). Untuk data akademik, lebih aman memakai `nama`, `nim`, `ipk`, `total_sks`.

### Kasus beragam

```python
# 1) Data diri mahasiswa
nama = "Siti Aminah"
nim = "21012001"
ipk = 3.75
aktif = True
print(nama, nim, ipk, aktif)

# 2) Multiple assignment
matkul, sks, nilai = "Kalkulus", 3, 85
print(matkul, sks, nilai)

# 3) Pertukaran nilai (tanpa variabel bantu eksplisit)
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10

# 4) Konstanta konvensi (huruf besar — kesepakatan, bukan syntax)
MAX_SKS = 24
BIAYA_PER_SKS = 150000

# 5) Menghitung dari variabel lain
sks_diambil = 20
estimasi_biaya = sks_diambil * BIAYA_PER_SKS
print(estimasi_biaya)
```

**Output:**

```text
Siti Aminah 21012001 3.75 True
Kalkulus 3 85
20 10
3000000
```

> [!WARNING]
> **Jebakan umum**
>
> Memakai nama sebelum di-assign → NameError.
>
> Menimpa nama built-in (list, str, input) membuat fungsi asli “hilang” di sesi itu.
>
> Nomor HP / NIM sering lebih aman sebagai string agar nol di depan tidak hilang.

## 3.2 Tipe Data & Casting — pembahasan

Tipe menentukan operasi apa yang masuk akal. Menjumlah dua angka berbeda dengan menggabungkan dua teks. Casting mengubah tipe secara eksplisit; gagal jika isi tidak kompatibel.

```python
print(type(21))
print(type(3.14))
print(type("Python"))
print(type(True))

# Casting yang sering dipakai
print(int("42"))
print(float("3.5"))
print(str(42))
print(int(3.9))      # 3 — truncasi, bukan pembulatan
print(bool(0), bool(1), bool(""), bool("teks"))
# Kasus form: input selalu string
# usia = int(input("Usia: "))  # gagal jika user ketik "dua puluh"

# Kasus nilai desimal dalam string
# int("3.5")  → ValueError; pakai float dulu lalu int jika perlu
print(int(float("3.5")))

# Kasus nomor identitas
nim = "00123"
print(nim, int(nim))  # int menghilangkan leading zero di tampilan numerik
```

**Output:**

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
42
3.5
42
3
False True False True
3
00123 123
```

## 3.3 Operator — pembahasan

Operator aritmatika menghasilkan nilai baru. Operator perbandingan menghasilkan boolean. Operator logika menggabungkan kondisi. Prioritas penting: eksponen lebih dulu, lalu kali/bagi, lalu tambah/kurang; pakai tanda kurung jika ragu.

```python
a, b = 10, 3
print(a + b, a - b, a * b, a / b)   # / selalu float di Python 3
print(a // b, a % b, a ** b)        # 3 1 1000

# Kasus genap/ganjil dan kelipatan
nilai = 85
print(nilai % 2 == 0)
print(nilai % 5 == 0)

# Kasus rata-rata
n1, n2, n3 = 80, 90, 70
print((n1 + n2 + n3) / 3)

# Perbandingan dan logika
ipk = 3.4
sks = 20
print(ipk >= 3.0 and sks >= 18)
print(ipk < 2.0 or sks < 12)
print(not aktif) if False else print("ok")

# Prioritas
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

**Output:**

```text
13 7 30 3.3333333333333335
3 1 1000
False
True
80.0
True
False
ok
14
20
```

## 3.4 String & I/O — pembahasan

`input()` selalu mengembalikan str. Untuk hitung-hitungan, cast dulu. Untuk menampilkan, f-string biasanya paling jelas. String bisa digabung (`+`) atau diulang (`*`), tetapi `+` antara str dan int akan error.

```python
# Kasus sapaan formal
nama = "Rina"
print(f"Halo, {nama}. Selamat belajar.")

# Kasus struk sederhana
item, harga, qty = "Fotokopi", 500, 12
total = harga * qty
print(f"{item}: {qty} x {harga} = {total}")

# Kasus laporan satu baris
mk, huruf = "Basis Data", "A"
print(f"MK {mk} → grade {huruf}")

# Kasus input numerik
# berat = float(input("Berat (kg): "))
# tinggi = float(input("Tinggi (m): "))
# bmi = berat / (tinggi ** 2)

# Concat vs f-string
print("Nilai: " + str(90))
print("Nilai: {}".format(90))
```

**Output:**

```text
Halo, Rina. Selamat belajar.
Fotokopi: 12 x 500 = 6000
MK Basis Data → grade A
Nilai: 90
Nilai: 90
```

## 3.5 Latihan — Variabel & I/O

Kerjakan tanpa melihat solusi di akhir modul. Setiap soal punya konteks berbeda.

1. Form singkat: minta nama dan tiga nilai, cetak rata-rata 2 desimal.
2. Konversi suhu C→F (F = C×9/5+32) dari input user.
3. Hitung estimasi biaya kuliah: input SKS × biaya per SKS (konstanta).
4. Tukar dua nilai variabel tanpa menulis angka literal di baris tukar.
5. Luas & keliling persegi panjang dari input panjang-lebar.
6. Deteksi genap/ganjil dari satu bilangan (pakai %).
7. Hitung BMI dari berat & tinggi; cetak juga kategori kasar (mis. <18.5 underweight).
8. Format struk 2 item berbeda (nama, harga, qty) dan total akhir.
9. Konversi jam ke menit dan detik (input jam desimal atau jam utuh).
10. Input nilai 0–100; cetak True/False apakah masuk rentang valid (tanpa if dulu boleh).

# 4. Control Flow

## 4.1 if / elif / else — pembahasan

Percabangan memilih blok kode berdasarkan kondisi. Urutan `elif` penting: kondisi dicek dari atas; yang pertama True dijalankan, sisanya dilewati. Rentang nilai (grade) harus dipikirkan agar tidak tumpang tindih atau bolong.

```python
# Kasus grade huruf
nilai = 78
if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"
print(grade)

# Kasus kelayakan beasiswa (kondisi majemuk)
ipk, penghasilan = 3.6, 3_000_000
if ipk >= 3.5 and penghasilan < 4_000_000:
    print("Kandidat beasiswa")
else:
    print("Belum memenuhi kriteria")

# Kasus status kehadiran
persen = 78
if persen >= 80:
    print("Boleh ujian")
elif persen >= 70:
    print("Boleh ujian dengan syarat")
else:
    print("Tidak boleh ujian")

# Ternary untuk ekspresi pendek
status = "lulus" if nilai >= 60 else "mengulang"
print(status)
```

**Output:**

```text
B
Kandidat beasiswa
Boleh ujian dengan syarat
lulus
```

> [!WARNING]
> **Miskonsepsi**
>
> Menulis if nilai >= 70 and < 85:  → salah syntax; harus nilai < 85.
>
> Mengandalkan urutan salah: if nilai >= 60 sebelum >= 85 membuat A tidak pernah tercapai jika tidak rapi.
>
> Nested if dalam: berguna, tapi jika terlalu dalam, pertimbangkan merapikan kondisi.

## 4.2 for loop — pembahasan

`for` dipakai saat Anda mengiterasi sesuatu yang diketahui (range, list, string). Akumulator (total, hitung) adalah pola paling sering: mulai dari 0 atau list kosong, lalu update tiap putaran.

```python
# Kasus jumlah 1..n
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(total)

# Kasus rata-rata dari list nilai
nilai_list = [80, 70, 90, 60, 85]
jumlah = 0
for v in nilai_list:
    jumlah += v
print(jumlah / len(nilai_list))

# Kasus hitung yang lulus
lulus = 0
for v in nilai_list:
    if v >= 60:
        lulus += 1
print("Lulus:", lulus)

# Kasus enumerate (nomor urut MK)
mk = ["Kalkulus", "Fisika", "Python"]
for i, nama in enumerate(mk, start=1):
    print(f"{i}. {nama}")

# Kasus iterasi string
for ch in "NIM":
    print(ch)
```

**Output:**

```text
55
77.0
Lulus: 5
1. Kalkulus
2. Fisika
3. Python
N
I
M
```

## 4.3 while loop — pembahasan

`while` cocok saat Anda belum tahu berapa kali mengulang — misalnya menunggu input valid. Bahaya utamanya: kondisi yang tidak pernah False (loop tak hingga). Pastikan ada perubahan variabel di dalam loop.

```python
# Kasus validasi angka 1–100
# while True:
#     x = int(input("Nilai 1-100: "))
#     if 1 <= x <= 100:
#         break
#     print("Di luar rentang.")

# Kasus menu sentinel
# pilihan = ""
# while pilihan != "0":
#     print("1. Lihat  0. Keluar")
#     pilihan = input("Pilih: ")

# Kasus akumulator dengan while
sisa = 5
while sisa > 0:
    print("Sisa kesempatan:", sisa)
    sisa -= 1
```

**Output:**

```text
Sisa kesempatan: 5
Sisa kesempatan: 4
Sisa kesempatan: 3
Sisa kesempatan: 2
Sisa kesempatan: 1
```

## 4.4 break, continue, nested — pembahasan

`break` keluar dari loop terdekat. `continue` lompat ke iterasi berikutnya. Nested loop dipakai untuk pola 2 dimensi (tabel, grid), tetapi kompleksitas naik cepat — jangan memaksa nested jika satu loop + if sudah cukup.

```python
# Kasus cari nilai pertama yang < 60 lalu berhenti
nilai_list = [80, 90, 55, 70]
for v in nilai_list:
    if v < 60:
        print("Ketemu nilai rendah:", v)
        break

# Kasus skip nilai None / kosong (simulasi)
data = [80, None, 70, None, 90]
for v in data:
    if v is None:
        continue
    print(v)

# Kasus tabel perkalian kecil
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()

# Kasus pola bintang
for baris in range(1, 5):
    print("*" * baris)
```

**Output:**

```text
Ketemu nilai rendah: 55
80
70
90
1	2	3	
2	4	6	
3	6	9	
*
**
***
****
```

## 4.5 Latihan — Control Flow

1. Grade huruf dari input nilai (rentang A–E lengkap).
2. Cetak bilangan genap 1…50.
3. Kasir: diskon 10% jika total ≥ 100000; tampilkan bayar.
4. Tebak angka 1–10 dengan while sampai benar.
5. Pola bintang n baris (n dari input).
6. Dari list nilai, hitung berapa yang A (≥85) dan berapa yang tidak lulus (<60).
7. Validasi input IPK 0–4; ulangi sampai valid.
8. Menu 3 opsi (tampilkan teks berbeda) + keluar.
9. Faktorial n dengan loop (bukan rekursi).
10. Cari angka maksimum di list tanpa pakai max().
11. Tabel perkalian 1…5 dalam bentuk baris-kolom.
12. Simulasi: saldo awal, beberapa transaksi (tambah/kurang), tolak jika saldo tidak cukup.

# 5. Data Structures

## 5.1 List — pembahasan

List menyimpan urutan nilai yang bisa berubah (mutable). Indeks mulai dari 0; indeks negatif dari belakang. Slicing menghasilkan list baru. Method seperti `append` mengubah list di tempat. List cocok untuk daftar MK, deret nilai, atau antrian sederhana.

```python
nilai = [80, 90, 75, 88]
print(nilai[0], nilai[-1])
print(nilai[1:3])
print(nilai[::-1])

nilai.append(95)
nilai.insert(1, 70)
nilai.remove(75)
terakhir = nilai.pop()
print(sorted(nilai))
print(sum(nilai), len(nilai), sum(nilai)/len(nilai))

# Kasus daftar MK
mk = ["Kalkulus", "Fisika"]
mk.append("Python")
print("Python" in mk)

# Kasus filter nilai >= 70 (buat list baru)
tinggi = []
for v in nilai:
    if v >= 70:
        tinggi.append(v)
print(tinggi)
```

**Output:**

```text
80 88
[90, 75]
[88, 75, 90, 80]
[70, 80, 88, 90]
328 4 82.0
True
[80, 70, 90, 88]
```

## 5.2 Tuple — pembahasan

Tuple mirip list tetapi tidak bisa diubah setelah dibuat. Cocok untuk data yang seharusnya tetap (pasangan koordinat, rekaman singkat). Unpacking membuat kode lebih jelas.

```python
koordinat = (-6.2, 106.8)
lat, lon = koordinat
print(lat, lon)

# Kasus pasangan NIM-nama
rekaman = ("21012001", "Siti")
nim, nama = rekaman
print(nim, nama)

# Return multi-nilai natural (fungsi dibahas Modul 2)
def min_max(data):
    return min(data), max(data)
print(min_max([3, 1, 4, 2]))
```

**Output:**

```text
-6.2 106.8
21012001 Siti
(1, 4)
```

## 5.3 Dictionary — pembahasan

Dict menyimpan pasangan key → value. Key harus unik dan bertipe immutable (str/int/tuple). Lookup by key biasanya lebih jelas daripada mencari di list of pair. Method `.get` aman saat key bisa absen.

```python
# Kasus profil mahasiswa
mhs = {"nama": "Budi", "nim": "2201", "ipk": 3.6}
print(mhs["nama"])
print(mhs.get("prodi", "belum diisi"))
mhs["prodi"] = "Informatika"
mhs["ipk"] = 3.7
for k, v in mhs.items():
    print(k, "→", v)

# Kasus rekap nilai per MK
nilai_mk = {"Kalkulus": 80, "Python": 90, "Fisika": 70}
print(sum(nilai_mk.values()) / len(nilai_mk))

# Kasus frekuensi huruf grade
grade = ["A", "B", "A", "C", "B", "A"]
freq = {}
for g in grade:
    freq[g] = freq.get(g, 0) + 1
print(freq)

# Nested sederhana
data = {"2201": {"nama": "Ani", "ipk": 3.5}, "2202": {"nama": "Budi", "ipk": 3.1}}
print(data["2201"]["nama"])
```

**Output:**

```text
Budi
belum diisi
nama → Budi
nim → 2201
ipk → 3.7
prodi → Informatika
80.0
{'A': 3, 'B': 2, 'C': 1}
Ani
```

## 5.4 Set — pembahasan

Set menyimpan nilai unik tanpa urutan tetap. Operasi himpunan (irisan, gabungan, selisih) membuatnya cocok untuk anggota kelas, tag, atau deduplikasi.

```python
peserta_a = {"Ani", "Budi", "Cici"}
peserta_b = {"Budi", "Dodi", "Ani"}
print(peserta_a | peserta_b)  # gabungan
print(peserta_a & peserta_b)  # irisan
print(peserta_a - peserta_b)  # hanya di A

# Kasus deduplikasi list
raw = [1, 2, 2, 3, 1, 4]
unik = list(set(raw))
print(unik)
```

**Output:**

```text
{'Cici', 'Ani', 'Dodi', 'Budi'}
{'Budi', 'Ani'}
{'Cici'}
[1, 2, 3, 4]
```

## 5.5 List of dict — pembahasan (penting)

Sebelum database atau Pandas, banyak program menyimpan data tabular sebagai list of dictionary. Satu dict = satu baris entitas (mahasiswa, tugas, buku). Pola ini menjadi dasar Mini Project modul ini.

```python
mahasiswa = [
    {"nama": "Ani", "nim": "2201", "ipk": 3.5, "prodi": "IF"},
    {"nama": "Budi", "nim": "2202", "ipk": 3.1, "prodi": "SI"},
    {"nama": "Cici", "nim": "2203", "ipk": 3.8, "prodi": "IF"},
]

# Tampilkan semua
for m in mahasiswa:
    print(m["nim"], m["nama"], m["ipk"])

# Cari by NIM
cari = "2202"
ketemu = None
for m in mahasiswa:
    if m["nim"] == cari:
        ketemu = m
        break
print(ketemu)

# Filter prodi IF
if_only = [m for m in mahasiswa if m["prodi"] == "IF"]
print(if_only)

# IPK tertinggi
tertinggi = mahasiswa[0]
for m in mahasiswa:
    if m["ipk"] > tertinggi["ipk"]:
        tertinggi = m
print(tertinggi["nama"], tertinggi["ipk"])
```

**Output:**

```text
2201 Ani 3.5
2202 Budi 3.1
2203 Cici 3.8
{'nama': 'Budi', 'nim': '2202', 'ipk': 3.1, 'prodi': 'SI'}
[{'nama': 'Ani', 'nim': '2201', 'ipk': 3.5, 'prodi': 'IF'}, {'nama': 'Cici', 'nim': '2203', 'ipk': 3.8, 'prodi': 'IF'}]
Cici 3.8
```

## 5.6 Kapan memakai struktur yang mana

| Struktur | Pilih jika… | Contoh kasus |
|---|---|---|
| List | Perlu urutan & bisa berubah | Daftar nilai, antrian MK |
| Tuple | Data tetap / pasangan singkat | Koordinat, (nim, nama) |
| Dict | Perlu label / lookup by key | Profil mhs, map MK→nilai |
| Set | Keunikan / operasi himpunan | Peserta unik, irisan kelas |
| List[dict] | Banyak record sejenis | Tabel mahasiswa di memori |

## 5.7 Latihan — Data Structures

1. List MK: tambah, hapus, cetak jumlah.
2. Dict profil diri; cetak semua item.
3. Dari list nilai, hitung jumlah lulus (≥60).
4. Irisan dua set hobi.
5. List of dict mahasiswa: cetak nama dengan IPK tertinggi.
6. Update IPK satu mahasiswa by NIM di list of dict.
7. Filter semua mahasiswa prodi tertentu.
8. Hitung frekuensi angka di list (pakai dict).
9. Gabungkan dua list lalu buang duplikat (set).
10. Tuple (panjang, lebar) → hitung luas (unpacking).
11. Hapus mahasiswa by NIM dari list of dict (buat list baru atau hapus hati-hati).
12. Rata-rata IPK hanya untuk prodi IF dari list of dict.

# 6. Best Practice — PEP 8

PEP 8 adalah panduan gaya resmi Python. Bukan tentang “jalan atau tidak”, tetapi keterbacaan — penting saat kode dibaca orang lain atau Anda sendiri beberapa bulan kemudian.

- Indentasi 4 spasi; jangan campur tab.
- Nama variabel/function: snake_case; class nanti: PascalCase.
- Spasi di sekitar operator: `x = a + b`.
- Baris tidak terlalu panjang; pecah argumen jika perlu.
- Import di bagian atas file.
- Nama bermakna; hindari `a1`, `tmp2` tanpa alasan.

```python
# Kurang baik
def H(x,y):
  return x+y

# Lebih baik
def hitung_jumlah(angka_satu, angka_dua):
    return angka_satu + angka_dua
```

**Output:**

```text
(tidak ada output)
```

# 7. Mini Project 1 — Sistem Data Mahasiswa (Dasar)

### Deskripsi

Program menu untuk mengelola list of dict mahasiswa di memori: tambah, tampil, cari, hapus, IPK tertinggi. Tidak perlu file/database.

### Fitur wajib

1. Tambah mahasiswa (nama, NIM, prodi, IPK).
2. Tampilkan semua.
3. Cari by NIM.
4. Hapus by NIM.
5. Tampilkan IPK tertinggi.
6. Keluar.

### Urutan kerjakan

- Siapkan list kosong `mahasiswa = []`.
- Buat fungsi tampil_menu, tambah, tampilkan, cari, hapus, ipk_tertinggi.
- Hubungkan ke loop `while True` + `input` pilihan.
- Uji setiap fitur manual sebelum lanjut.

### Skeleton

```python
mahasiswa = []

def tampil_menu():
    print("\n1. Tambah  2. Tampilkan  3. Cari")
    print("4. Hapus   5. IPK Tertinggi  6. Keluar")

def tambah():
    nama = input("Nama: ")
    nim = input("NIM: ")
    prodi = input("Prodi: ")
    ipk = float(input("IPK: "))
    mahasiswa.append({"nama": nama, "nim": nim, "prodi": prodi, "ipk": ipk})
    print("Ditambahkan.")

def tampilkan():
    if not mahasiswa:
        print("Data kosong.")
        return
    for m in mahasiswa:
        print(f"{m['nim']} | {m['nama']} | {m['prodi']} | {m['ipk']}")

def cari():
    nim = input("NIM: ")
    for m in mahasiswa:
        if m["nim"] == nim:
            print(m)
            return
    print("Tidak ditemukan.")

def hapus():
    nim = input("NIM: ")
    for i, m in enumerate(mahasiswa):
        if m["nim"] == nim:
            mahasiswa.pop(i)
            print("Dihapus.")
            return
    print("Tidak ditemukan.")

def ipk_tertinggi():
    if not mahasiswa:
        print("Data kosong.")
        return
    terbaik = mahasiswa[0]
    for m in mahasiswa:
        if m["ipk"] > terbaik["ipk"]:
            terbaik = m
    print(terbaik)

while True:
    tampil_menu()
    pilih = input("Pilih: ")
    if pilih == "1": tambah()
    elif pilih == "2": tampilkan()
    elif pilih == "3": cari()
    elif pilih == "4": hapus()
    elif pilih == "5": ipk_tertinggi()
    elif pilih == "6":
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid.")
```

**Output (input simulasi: 1 ⏎ Ani ⏎ 2201 ⏎ IF ⏎ 3.75 ⏎ 1 ⏎ Budi ⏎ 2202 ⏎ SI ⏎ 3.2 ⏎ 2 ⏎ 3 ⏎ 2202 ⏎ 5 ⏎ 4 ⏎ 2201 ⏎ 2 ⏎ 3 ⏎ 9999 ⏎ 7 ⏎ 6):**

```text

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 1
Nama: Ani
NIM: 2201
Prodi: IF
IPK: 3.75
Ditambahkan.

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 1
Nama: Budi
NIM: 2202
Prodi: SI
IPK: 3.2
Ditambahkan.

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 2
2201 | Ani | IF | 3.75
2202 | Budi | SI | 3.2

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 3
NIM: 2202
{'nama': 'Budi', 'nim': '2202', 'prodi': 'SI', 'ipk': 3.2}

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 5
{'nama': 'Ani', 'nim': '2201', 'prodi': 'IF', 'ipk': 3.75}

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 4
NIM: 2201
Dihapus.

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 2
2202 | Budi | SI | 3.2

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 3
NIM: 9999
Tidak ditemukan.

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 7
Pilihan tidak valid.

1. Tambah  2. Tampilkan  3. Cari
4. Hapus   5. IPK Tertinggi  6. Keluar
Pilih: 6
Selesai.
```

_Catatan: program menu penuh dijalankan dengan skenario input di atas: tambah dua mahasiswa, tampilkan, cari, IPK tertinggi, hapus, cari NIM yang tidak ada, pilihan tidak valid, lalu keluar._

> [!TIP]
> **Tantangan opsional Project 1**
>
> Tolak NIM duplikat saat tambah.
>
> Validasi IPK hanya 0–4.
>
> Tambah fitur filter by prodi.

# 8. Mini Project 2 — Sistem Nilai & Statistik

### Deskripsi

Setiap mahasiswa punya banyak nilai MK (dict di dalam dict/list). Hitung rata-rata per orang, statistik global, dan filter yang lulus ambang.

### Fitur wajib

1. Tambah data: nama + nilai per MK.
2. Tampilkan semua + rata-rata tiap mahasiswa.
3. Statistik global (rata-rata kelas, max, min dari rata-rata individu).
4. Filter rata-rata ≥ ambang (mis. 70).
5. Menu interaktif.

### Skeleton inti

```python
data = []  # [{"nama": str, "nilai": {"MK": angka, ...}}, ...]

def rata_rata(nilai_dict):
    if not nilai_dict:
        return 0
    return sum(nilai_dict.values()) / len(nilai_dict)

def tambah_data():
    nama = input("Nama: ")
    nilai = {}
    while True:
        mk = input("Nama MK (kosong=selesai): ").strip()
        if not mk:
            break
        nilai[mk] = float(input(f"Nilai {mk}: "))
    data.append({"nama": nama, "nilai": nilai})

def tampilkan_semua():
    for d in data:
        print(d["nama"], d["nilai"], "rata=", round(rata_rata(d["nilai"]), 2))

def statistik():
    if not data:
        print("Kosong")
        return
    rata_list = [rata_rata(d["nilai"]) for d in data]
    print("Rata kelas:", sum(rata_list)/len(rata_list))
    print("Max:", max(rata_list), "Min:", min(rata_list))

def filter_lulus(ambang=70):
    for d in data:
        r = rata_rata(d["nilai"])
        if r >= ambang:
            print(d["nama"], r)

# while menu: 1 tambah 2 tampil 3 statistik 4 filter 5 keluar
```

**Output:**

```text
(tidak ada output)
```

_Catatan: blok ini hanya mendefinisikan function; menu `while` dibiarkan sebagai tugas peserta (lihat uji pelengkap di bawah)._

**Uji pelengkap — menu yang dibiarkan kosong pada modul**

```python
while True:
    print("\n1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar")
    pilih = input("Pilih: ")
    if pilih == "1": tambah_data()
    elif pilih == "2": tampilkan_semua()
    elif pilih == "3": statistik()
    elif pilih == "4": filter_lulus()
    elif pilih == "5":
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid.")
```

**Output (input simulasi: 1 ⏎ Ani ⏎ Python ⏎ 85 ⏎ Fisika ⏎ 70 ⏎  ⏎ 1 ⏎ Budi ⏎ Python ⏎ 60 ⏎ Fisika ⏎ 55 ⏎  ⏎ 2 ⏎ 3 ⏎ 4 ⏎ 9 ⏎ 5):**

```text

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 1
Nama: Ani
Nama MK (kosong=selesai): Python
Nilai Python: 85
Nama MK (kosong=selesai): Fisika
Nilai Fisika: 70
Nama MK (kosong=selesai): 

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 1
Nama: Budi
Nama MK (kosong=selesai): Python
Nilai Python: 60
Nama MK (kosong=selesai): Fisika
Nilai Fisika: 55
Nama MK (kosong=selesai): 

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 2
Ani {'Python': 85.0, 'Fisika': 70.0} rata= 77.5
Budi {'Python': 60.0, 'Fisika': 55.0} rata= 57.5

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 3
Rata kelas: 67.5
Max: 77.5 Min: 57.5

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 4
Ani 77.5

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 9
Pilihan tidak valid.

1. Tambah  2. Tampil  3. Statistik  4. Filter  5. Keluar
Pilih: 5
Selesai.
```

_Catatan: kode menu di atas ditambahkan hanya untuk menguji function pada blok sebelumnya; skenario: tambah dua mahasiswa (nama MK kosong = selesai), tampilkan, statistik, filter lulus (ambang 70), pilihan tidak valid, keluar._

# 9. Troubleshooting

### NameError

```python
# Kasus 1: belum assign
# print(nama)  → NameError
nama = "Ani"
print(nama)

# Kasus 2: typo
nilai = 80
# print(niali)  → NameError

# Kasus 3: variabel di dalam blok if yang tidak jalan
x = 5
if x > 10:
    pesan = "besar"
# print(pesan)  bisa NameError jika kondisi False
```

**Output:**

```text
Ani
```

### TypeError

```python
# Kasus 1: str + int
# print("Nilai: " + 80)  → TypeError
print("Nilai: " + str(80))
print(f"Nilai: {80}")

# Kasus 2: len pada int
# len(100)  → TypeError

# Kasus 3: argumen fungsi kurang/lebih (Modul 2 lebih detail)
def tambah(a, b):
    return a + b
# tambah(1)  → TypeError
```

**Output:**

```text
Nilai: 80
Nilai: 80
```

### ValueError & ZeroDivisionError

```python
# int("abc")  → ValueError
# float("")    → ValueError
# 10 / 0      → ZeroDivisionError
pembagi = 2
if pembagi != 0:
    print(10 / pembagi)
```

**Output:**

```text
5.0
```

### IndexError & KeyError

```python
data = [10, 20, 30]
# data[5]  → IndexError
if len(data) > 5:
    print(data[5])

mhs = {"nama": "Ani"}
# mhs["nim"]  → KeyError
print(mhs.get("nim", "-"))
if "nim" in mhs:
    print(mhs["nim"])
```

**Output:**

```text
-
```

## Demonstrasi error — output nyata

Bagian ini menjalankan setiap kasus pada tabel di atas secara terpisah, sehingga Anda melihat pesan error yang sebenarnya (pada contoh sebelumnya baris error sengaja dikomentari agar kode dapat dijalankan utuh).

### NameError — tiga kasus

```python
# Kasus 1: belum assign
print(nama)

# Kasus 2: typo
nilai = 80
print(niali)

# Kasus 3: variabel di blok if yang tidak jalan
x = 5
if x > 10:
    pesan = "besar"
print(pesan)
```

**Output:**

```text
# Kasus 1: belum assign
  -> NameError: name 'nama' is not defined
# Kasus 2: typo
  -> NameError: name 'niali' is not defined
# Kasus 3: variabel di blok if yang tidak jalan
  -> NameError: name 'pesan' is not defined
```

### TypeError — tiga kasus

```python
# Kasus 1: str + int
print("Nilai: " + 80)

# Kasus 2: len pada int
len(100)

# Kasus 3: argumen fungsi kurang
def tambah(a, b):
    return a + b
tambah(1)
```

**Output:**

```text
# Kasus 1: str + int
  -> TypeError: can only concatenate str (not "int") to str
# Kasus 2: len pada int
  -> TypeError: object of type 'int' has no len()
# Kasus 3: argumen fungsi kurang
  -> TypeError: tambah() missing 1 required positional argument: 'b'
```

### ValueError & ZeroDivisionError

```python
# int("abc")
int("abc")

# float("")
float("")

# int("3.5") — tidak bisa langsung; solusinya float dulu
print(int(float("3.5")))
int("3.5")

# 10 / 0
10 / 0
```

**Output:**

```text
# int("abc")
  -> ValueError: invalid literal for int() with base 10: 'abc'
# float("")
  -> ValueError: could not convert string to float: ''
# int("3.5") — tidak bisa langsung; solusinya float dulu
3
  -> ValueError: invalid literal for int() with base 10: '3.5'
# 10 / 0
  -> ZeroDivisionError: division by zero
```

### IndexError & KeyError

```python
data = [10, 20, 30]
data[5]

mhs = {"nama": "Ani"}
mhs["nim"]
```

**Output:**

```text
data = [10, 20, 30]
  -> IndexError: list index out of range
mhs = {"nama": "Ani"}
  -> KeyError: 'nim'
```

### IndentationError & SyntaxError

```python
if True:
print("tanpa indentasi")

nilai = 80
if nilai >= 70 and < 85:
    print("B")
```

**Output:**

```text
if True:
  -> IndentationError: expected an indented block after 'if' statement on line 1
nilai = 80
  -> SyntaxError: invalid syntax
```

# 10. Solusi Latihan (Cuplikan Utama)

## 10.1 Variabel & I/O

```python
nama = input("Nama: ")
n1 = float(input("Nilai 1: "))
n2 = float(input("Nilai 2: "))
n3 = float(input("Nilai 3: "))
print(f"{nama}: {(n1+n2+n3)/3:.2f}")

c = float(input("Celsius: "))
print(c * 9/5 + 32)

BIAYA = 150000
sks = int(input("SKS: "))
print(sks * BIAYA)

a = input("a: "); b = input("b: ")
a, b = b, a
print(a, b)
```

**Output (input simulasi: Siti Aminah ⏎ 80 ⏎ 90 ⏎ 85 ⏎ 100 ⏎ 20 ⏎ kiri ⏎ kanan):**

```text
Nama: Siti Aminah
Nilai 1: 80
Nilai 2: 90
Nilai 3: 85
Siti Aminah: 85.00
Celsius: 100
212.0
SKS: 20
3000000
a: kiri
b: kanan
kanan kiri
```

_Catatan: urutan input: nama, tiga nilai, suhu Celsius, SKS, lalu dua string untuk swap._

## 10.2 Control Flow

```python
n = int(input("Nilai: "))
if n >= 85: print("A")
elif n >= 70: print("B")
elif n >= 60: print("C")
elif n >= 50: print("D")
else: print("E")

for i in range(2, 51, 2):
    print(i, end=" ")
print()

total = float(input("Total: "))
bayar = total * 0.9 if total >= 100000 else total
print(bayar)

rahasia = 7
while True:
    if int(input("Tebak: ")) == rahasia:
        print("Benar"); break

nilai_list = [80, 90, 55, 40, 85]
a = sum(1 for v in nilai_list if v >= 85)
g = sum(1 for v in nilai_list if v < 60)
print("A:", a, "tidak lulus:", g)
```

**Output (input simulasi: 78 ⏎ 150000 ⏎ 3 ⏎ 7):**

```text
Nilai: 78
B
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
Total: 150000
135000.0
Tebak: 3
Tebak: 7
Benar
A: 2 tidak lulus: 2
```

_Catatan: urutan input: nilai ujian, total belanja, tebakan (3 salah, 7 benar)._

## 10.3 Data Structures

```python
mk = ["Kalkulus", "Fisika"]; mk.append("Python"); mk.remove("Fisika"); print(len(mk), mk)

mhs = [
    {"nama": "Ani", "nim": "2201", "ipk": 3.5, "prodi": "IF"},
    {"nama": "Budi", "nim": "2202", "ipk": 3.9, "prodi": "SI"},
    {"nama": "Cici", "nim": "2203", "ipk": 3.2, "prodi": "IF"},
]
terbaik = max(mhs, key=lambda x: x["ipk"])
print(terbaik["nama"])
if_only = [m for m in mhs if m["prodi"] == "IF"]
print(sum(m["ipk"] for m in if_only) / len(if_only))
```

**Output:**

```text
2 ['Kalkulus', 'Python']
Budi
3.35
```

# 11. Checklist Sebelum Modul 2

- Contoh variabel, casting, operator, I/O diketik ulang & diubah-ubah
- Latihan control flow dikerjakan sebelum melihat solusi
- List of dict: cari, filter, IPK tertinggi sudah dipraktikkan
- Mini Project 1 berjalan; Project 2 diusahakan
- File tersimpan di portfolio/modul_01/

> **Modul 1 (lengkap) selesai? Lanjut ke Modul 2.**
>
> Python Intensive — Modul Belajar Mandiri
