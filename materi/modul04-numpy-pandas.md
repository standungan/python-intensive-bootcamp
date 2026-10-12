# Modul 4 — NumPy & Pandas

_Pembahasan jelas  ·  Banyak kasus  ·  Pseudocode latihan  ·  5 Mini Project · Estimasi: ± 6–8 jam  ·  Prasyarat: Modul 1–3  ·  pip install numpy pandas_

> **Catatan pengujian:** seluruh blok kode pada modul ini dijalankan (Python 3.11, numpy 2.4.6, pandas 3.0.6, openpyxl 3.1.5). Bagian **Output** adalah hasil eksekusi nyata. Blok yang memakai `input()` dijalankan dengan input simulasi yang ditulis di samping label output. Blok yang hanya berisi definisi/komentar diberi keterangan, dan "Uji pelengkap" ditambahkan agar function/class pada blok tersebut terbukti berjalan. Kasus error pada bagian Troubleshooting dijalankan nyata di "Demonstrasi error". Pada pandas 3.x kolom teks bertipe `str` (di pandas 2.x tampil sebagai `object`).

# 1. Apa yang Akan Anda Pelajari

- Memakai NumPy untuk array, indexing, masking, broadcasting, dan agregasi.
- Membangun workflow Pandas: inspeksi, filter, cleaning, groupby, merge, pivot.
- Menyelesaikan minimal 2–3 dari 5 mini project berjenjang.

> [!NOTE]
> **Persiapan**
>
> pip install numpy pandas
>
> Jupyter Notebook sangat membantu karena output tabel langsung terlihat.
>
> Simpan kerja di portfolio/modul_04/.

# 2. NumPy — Array Numerik

## 2.1 Mengapa bukan list saja?

List Python fleksibel: bisa campur tipe, mudah diubah ukurannya. Namun untuk ribuan atau jutaan angka, operasi dengan loop Python terasa lambat. NumPy menyediakan array bertipe seragam dan operasi vektorisasi — satu perintah diterapkan ke seluruh elemen tanpa Anda menulis for secara eksplisit.

Anda tidak harus membuang list. Pakai NumPy saat data utamanya numerik dan Anda butuh hitung cepat, slicing multidimensi, atau fondasi untuk Pandas/visualisasi.

## 2.2 Membuat array

Array bisa dibuat dari list, atau dengan helper seperti zeros, ones, arange, linspace, dan generator acak. Perhatikan shape (bentuk) dan dtype (tipe elemen) — dua atribut yang paling sering dicek saat debug.

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4], [5, 6]])
print(a.ndim, a.shape, a.dtype)
print(b.ndim, b.shape)

print(np.zeros((2, 3)))
print(np.ones((2, 2)))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5))

rng = np.random.default_rng(42)  # seed agar hasil bisa diulang
print(rng.integers(1, 10, size=5))
```

**Output:**

```text
1 (4,) int64
2 (3, 2)
[[0. 0. 0.]
 [0. 0. 0.]]
[[1. 1.]
 [1. 1.]]
[0 2 4 6 8]
[0.   0.25 0.5  0.75 1.  ]
[1 7 6 4 4]
```

## 2.3 Indexing, slicing, boolean masking

Indexing 2D memakai [baris, kolom]. Slicing menyerupai list, tetapi hasilnya sering berupa view: mengubah slice bisa mengubah array asli. Boolean masking memilih elemen yang memenuhi kondisi — sangat berguna untuk filter nilai ujian, outlier, atau data di luar rentang.

```python
m = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(m[0, 1])     # 20
print(m[:, 1])     # kolom tengah
print(m[1:, :2])   # submatriks

nilai = np.array([55, 80, 90, 40, 70, 95])
print(nilai[nilai >= 70])
print(nilai[(nilai >= 60) & (nilai < 90)])

label = np.where(nilai >= 70, "lulus", "mengulang")
print(label)
adjusted = np.where(nilai < 60, 60, nilai)  # floor 60
print(adjusted)
```

**Output:**

```text
20
[20 50 80]
[[40 50]
 [70 80]]
[80 90 70 95]
[80 70]
['mengulang' 'lulus' 'lulus' 'mengulang' 'lulus' 'lulus']
[60 80 90 60 70 95]
```

> [!WARNING]
> **Perhatian slicing**
>
> b = a[1:3] sering berbagi memori dengan a. Jika perlu salinan independen: b = a[1:3].copy()
>
> Operator and/or Python biasa tidak dipakai antar array; pakai & | dengan tanda kurung.

## 2.4 Operasi, agregasi, broadcasting

Operasi + * ** pada array diterapkan per elemen. Agregasi (sum, mean, std) bisa global atau per sumbu: axis=0 biasanya “turun per kolom”, axis=1 “menyamping per baris” (untuk array 2D).

Broadcasting memungkinkan operasi antara array berbeda ukuran jika bentuknya kompatibel. Contoh penting: menormalisasi setiap kolom data dengan (data - mean) / std tanpa menulis loop.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b, a * 2)

m = np.array([[1, 2, 3], [4, 5, 6]])
print(m.sum(axis=0))  # per kolom
print(m.sum(axis=1))  # per baris
print(m.mean(), m.std())

data = np.array([[10., 200.], [20., 300.], [30., 400.]])
mean = data.mean(axis=0)
std = data.std(axis=0)
print((data - mean) / std)
```

**Output:**

```text
[11 22 33] [2 4 6]
[5 7 9]
[ 6 15]
3.5 1.707825127659933
[[-1.22474487 -1.22474487]
 [ 0.          0.        ]
 [ 1.22474487  1.22474487]]
```

## 2.5 Reshape

```python
a = np.arange(12)
print(a.reshape(3, 4))
print(a.reshape(2, -1))  # -1 = otomatis
print(np.eye(3))
print(np.diag(np.eye(3)))
```

**Output:**

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[1. 1. 1.]
```

## 2.6 Latihan NumPy

1. Buat array 6×6 berisi 1…36; ambil blok tengah 2×2; hitung mean, min, max blok itu.

```text
Pseudocode:
  a ← arange 1..36, reshape 6×6
  blok ← a[baris tengah, kolom tengah]  # mis. [2:4, 2:4]
  cetak mean, min, max dari blok
```

2. Normalisasi min-max sebuah array 1D ke rentang 0…1.

```text
Pseudocode:
  norm ← (x - min(x)) / (max(x) - min(x))
  hati-hati jika max = min (pembagi nol)
```

3. Ganti semua nilai < 60 menjadi 60 dengan np.where.

```text
Pseudocode:
  hasil ← where(nilai < 60, 60, nilai)
```

4. Matriks identitas 5×5; ambil diagonal utamanya.

```text
Pseudocode:
  I ← eye(5)
  cetak diag(I)
```

# 3. Pandas — Series & DataFrame

## 3.1 Ide dasar

Jika NumPy andal untuk angka murni, Pandas andal untuk tabel berlabel: baris dan kolom punya nama. Series mirip satu kolom; DataFrame mirip spreadsheet atau tabel database di memori.

Alur kerja tipikal: muat data → inspeksi (head, info, describe) → bersihkan → filter/groupby → simpan hasil. Modul ini membangun fondasi itu langkah demi langkah.

## 3.2 Series dan DataFrame

```python
import pandas as pd
import numpy as np

s = pd.Series([80, 90, 75], index=["Ani", "Budi", "Cici"])
print(s["Ani"], s.mean())

df = pd.DataFrame({
    "nama": ["Ani", "Budi", "Cici", "Dodi", "Eka"],
    "nim": ["2201", "2202", "2203", "2204", "2205"],
    "prodi": ["IF", "SI", "IF", "SI", "IF"],
    "ipk": [3.50, 3.20, 3.80, 2.90, 3.60],
})
print(df.head())
print(df.info())
print(df.describe())
print(df["prodi"].value_counts())
```

**Output:**

```text
80 81.66666666666667
   nama   nim prodi  ipk
0   Ani  2201    IF  3.5
1  Budi  2202    SI  3.2
2  Cici  2203    IF  3.8
3  Dodi  2204    SI  2.9
4   Eka  2205    IF  3.6
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   nama    5 non-null      str    
 1   nim     5 non-null      str    
 2   prodi   5 non-null      str    
 3   ipk     5 non-null      float64
dtypes: float64(1), str(3)
memory usage: 292.0 bytes
None
            ipk
count  5.000000
mean   3.400000
std    0.353553
min    2.900000
25%    3.200000
50%    3.500000
75%    3.600000
max    3.800000
prodi
IF    3
SI    2
Name: count, dtype: int64
```

## 3.3 Selection: [], loc, iloc

Ambil kolom dengan df["nama"] atau df[["nama", "ipk"]]. loc memakai label (termasuk filter boolean). iloc memakai posisi angka seperti indeks list. Membiasakan ketiganya mencegah kebingungan saat index tidak berurutan 0,1,2,...

```python
print(df["nama"])
print(df.loc[0, "ipk"])
print(df.loc[df["ipk"] >= 3.5, ["nama", "ipk"]])
print(df.iloc[0:3, 0:2])
print(df.query("ipk >= 3.5 and prodi == 'IF'"))
```

**Output:**

```text
0     Ani
1    Budi
2    Cici
3    Dodi
4     Eka
Name: nama, dtype: str
3.5
   nama  ipk
0   Ani  3.5
2  Cici  3.8
4   Eka  3.6
   nama   nim
0   Ani  2201
1  Budi  2202
2  Cici  2203
   nama   nim prodi  ipk
0   Ani  2201    IF  3.5
2  Cici  2203    IF  3.8
4   Eka  2205    IF  3.6
```

## 3.4 Menambah kolom, filter, sort

```python
df = df.copy()
df["status"] = df["ipk"].apply(lambda x: "unggul" if x >= 3.5 else "baik")
df["skor"] = df["ipk"] * 25
print(df[df["ipk"] >= 3.5].sort_values("ipk", ascending=False))
```

**Output:**

```text
   nama   nim prodi  ipk  status  skor
2  Cici  2203    IF  3.8  unggul  95.0
4   Eka  2205    IF  3.6  unggul  90.0
0   Ani  2201    IF  3.5  unggul  87.5
```

# 4. Cleaning & Operasi Lanjutan

## 4.1 Missing values dan duplikat

Data nyata sering berlubang atau berulang. isna() memetakan lubang; dropna menghapus; fillna mengisi (mean, median, atau nilai tetap). Pilihan strategi bergantung pada konteks: menghapus baris mahasiswa karena satu nilai kosong bisa membuang informasi penting.

```python
df = pd.DataFrame({
    "nama": ["Ani", "Budi", None, "Ani"],
    "nilai": [80, np.nan, 70, 80],
})
print(df.isna().sum())
df["nilai"] = df["nilai"].fillna(df["nilai"].median())
df = df.dropna(subset=["nama"])
df = df.drop_duplicates()
print(df)
```

**Output:**

```text
nama     1
nilai    1
dtype: int64
   nama  nilai
0   Ani   80.0
1  Budi   80.0
```

## 4.2 GroupBy

groupby memecah tabel menurut kunci (misalnya prodi), lalu menerapkan agregasi (mean, count, sum) pada tiap kelompok. Ini padanan “pivot sederhana” di spreadsheet.

```python
df = pd.DataFrame({
    "prodi": ["IF", "IF", "SI", "SI", "IF"],
    "nilai": [80, 90, 70, 85, 75],
})
print(df.groupby("prodi")["nilai"].mean())
print(df.groupby("prodi").agg(rata=("nilai", "mean"), n=("nilai", "count")))
```

**Output:**

```text
prodi
IF    81.666667
SI    77.500000
Name: nilai, dtype: float64
            rata  n
prodi              
IF     81.666667  3
SI     77.500000  2
```

## 4.3 Merge dan concat

Merge menggabungkan tabel berdasarkan kolom kunci (mirip JOIN SQL). how="left" mempertahankan semua baris kiri; inner hanya yang cocok di kedua sisi. Concat menumpuk tabel secara vertikal atau horizontal.

```python
mhs = pd.DataFrame({"nim": ["2201", "2202"], "nama": ["Ani", "Budi"]})
nilai = pd.DataFrame({"nim": ["2201", "2202"], "ipk": [3.5, 3.1]})
print(mhs.merge(nilai, on="nim", how="left"))
```

**Output:**

```text
    nim  nama  ipk
0  2201   Ani  3.5
1  2202  Budi  3.1
```

## 4.4 Pivot table

```python
df = pd.DataFrame({
    "prodi": ["IF", "IF", "SI", "SI"],
    "semester": [1, 2, 1, 2],
    "nilai": [80, 85, 70, 90],
})
print(df.pivot_table(values="nilai", index="prodi", columns="semester", aggfunc="mean"))
```

**Output:**

```text
semester     1     2
prodi               
IF        80.0  85.0
SI        70.0  90.0
```

## 4.5 Baca dan simpan file

```python
df = pd.read_csv("data.csv")
df.to_csv("hasil.csv", index=False)
# pd.read_excel / df.to_excel memerlukan openpyxl
```

**Output:**

```text
(tidak ada output)
```

_Catatan: dijalankan dengan file contoh `data.csv` (3 baris) yang dibuat untuk pengujian; blok ini sengaja tidak mencetak apa pun — hasil baca/tulis dapat dilihat pada file `hasil.csv`._

**Uji pelengkap — memeriksa hasil baca/tulis CSV**

```python
from pathlib import Path
print(df)
print(Path("hasil.csv").read_text())
```

**Output:**

```text
    nama  ipk
0    Ani  3.7
1   Budi  3.2
2  Citra  3.9
nama,ipk
Ani,3.7
Budi,3.2
Citra,3.9
```

## 4.6 Latihan Pandas

1. DataFrame 8 mahasiswa (nama, prodi, ipk, sks). Filter IPK ≥ 3.5; sort IPK menurun.

```text
Pseudocode:
  buat DataFrame
  subset ← baris dengan ipk ≥ 3.5
  urutkan subset by ipk descending
  cetak hasil
```

2. Groupby prodi: rata-rata IPK, total SKS, jumlah mahasiswa.

```text
Pseudocode:
  groupby prodi
  agg: mean(ipk), sum(sks), count(nama)
```

3. Sengaja buat missing & duplikat; bersihkan; bandingkan shape sebelum/sesudah.

```text
Pseudocode:
  catat shape dan jumlah na awal
  fillna / dropna / drop_duplicates sesuai kebutuhan
  catat shape akhir
```

4. Merge mahasiswa + nilai (how="left"); hitung berapa yang tidak punya nilai.

```text
Pseudocode:
  gabung ← merge left on nim
  jumlah_na ← gabung["ipk"].isna().sum()
```

# 5. Mini Project (5 Berjenjang)

Minimal selesaikan 2–3 project. Kerjakan berurutan jika memungkinkan.

## Project 1 — Kalkulator Nilai Akhir (Dasar)

Dari komponen tugas, UTS, UAS, hitung nilai akhir berbobot dan huruf mutu; tampilkan ringkasan kelas.

```python
import pandas as pd
df = pd.DataFrame({
    "nama": ["Ani", "Budi", "Cici", "Dodi"],
    "tugas": [80, 70, 90, 60],
    "uts": [85, 75, 88, 65],
    "uas": [90, 80, 85, 70],
})
df["nilai_akhir"] = 0.3*df["tugas"] + 0.3*df["uts"] + 0.4*df["uas"]

def ke_huruf(n):
    if n >= 85: return "A"
    if n >= 70: return "B"
    if n >= 60: return "C"
    if n >= 50: return "D"
    return "E"

df["huruf"] = df["nilai_akhir"].apply(ke_huruf)
print(df)
print("Rata kelas:", df["nilai_akhir"].mean())
print(df["huruf"].value_counts())
```

**Output:**

```text
   nama  tugas  uts  uas  nilai_akhir huruf
0   Ani     80   85   90         85.5     A
1  Budi     70   75   80         75.5     B
2  Cici     90   88   85         87.4     A
3  Dodi     60   65   70         65.5     C
Rata kelas: 78.475
huruf
A    2
B    1
C    1
Name: count, dtype: int64
```

## Project 2 — Cleaning Dataset Kotor

Rapikan missing, duplikat, dan tipe data; simpan CSV bersih; bandingkan shape.

```python
df = pd.DataFrame({
    "nama": ["Ani", "Budi", None, "Ani", "Cici"],
    "nilai": ["80", "90", None, "80", "70"],
    "prodi": ["IF", "SI", "IF", "IF", None],
})
print("Sebelum:", df.shape)
df["nilai"] = pd.to_numeric(df["nilai"], errors="coerce")
df["nilai"] = df["nilai"].fillna(df["nilai"].median())
df["prodi"] = df["prodi"].fillna("unknown")
df = df.dropna(subset=["nama"]).drop_duplicates()
print("Sesudah:", df.shape)
df.to_csv("data_bersih.csv", index=False)
```

**Output:**

```text
Sebelum: (5, 3)
Sesudah: (3, 3)
```

## Project 3 — Merge Multi-Tabel

```python
mhs = pd.DataFrame({"nim": ["2201", "2202", "2203"], "nama": ["Ani", "Budi", "Cici"], "kode_prodi": ["IF", "SI", "IF"]})
nilai = pd.DataFrame({"nim": ["2201", "2202"], "ipk": [3.5, 3.1]})
prodi = pd.DataFrame({"kode_prodi": ["IF", "SI"], "nama_prodi": ["Informatika", "Sistem Informasi"]})
df = mhs.merge(nilai, on="nim", how="left").merge(prodi, on="kode_prodi", how="left")
print(df)
print(df.groupby("nama_prodi")["ipk"].mean())
print("Tanpa nilai:", df["ipk"].isna().sum())
```

**Output:**

```text
    nim  nama kode_prodi  ipk        nama_prodi
0  2201   Ani         IF  3.5       Informatika
1  2202  Budi         SI  3.1  Sistem Informasi
2  2203  Cici         IF  NaN       Informatika
nama_prodi
Informatika         3.5
Sistem Informasi    3.1
Name: ipk, dtype: float64
Tanpa nilai: 1
```

## Project 4 — Pivot & Reporting

```python
df = pd.DataFrame({
    "prodi": ["IF", "IF", "SI", "SI", "IF", "SI"],
    "semester": [1, 1, 1, 1, 2, 2],
    "nilai": [80, 85, 70, 75, 90, 88],
})
print(df.pivot_table(values="nilai", index="prodi", columns="semester", aggfunc="mean"))
print(df.groupby("prodi")["nilai"].agg(["mean", "count", "std"]))
```

**Output:**

```text
semester     1     2
prodi               
IF        82.5  90.0
SI        72.5  88.0
            mean  count       std
prodi                            
IF     85.000000      3  5.000000
SI     77.666667      3  9.291573
```

## Project 5 — EDA Dataset Publik

Ambil dataset dari seaborn (penguins, tips, titanic) atau CSV publik. Inspeksi, cleaning ringan, minimal 2 groupby bermakna, tulis 3–5 insight, simpan ringkasan CSV.

```python
import seaborn as sns
df = sns.load_dataset("penguins")
print(df.head()); print(df.info()); print(df.isna().sum())
print(df.groupby("species")["body_mass_g"].mean())
# tulis insight; simpan tabel ringkas
```

**Output:**

```text
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
<class 'pandas.DataFrame'>
RangeIndex: 344 entries, 0 to 343
Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   species            344 non-null    str    
 1   island             344 non-null    str    
 2   bill_length_mm     342 non-null    float64
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    str    
dtypes: float64(4), str(3)
memory usage: 18.9 KB
None
species               0
island                0
bill_length_mm        2
bill_depth_mm         2
flipper_length_mm     2
body_mass_g           2
sex                  11
dtype: int64
species
Adelie       3700.662252
Chinstrap    3733.088235
Gentoo       5076.016260
Name: body_mass_g, dtype: float64
```

> [!TIP]
> **Sumber cepat**
>
> sns.load_dataset("tips"), "penguins", "titanic"
>
> Fokus ke pertanyaan analisis, bukan hanya memanggil fungsi.

# 6. Troubleshooting

```python
# KeyError kolom → cek df.columns; perhatikan huruf besar/kecil
# SettingWithCopyWarning → pakai .copy() setelah filter, atau .loc[]
# Merge menghasilkan NaN → normal pada how="left" jika kunci tidak cocok
# dtype object padahal angka → pd.to_numeric(..., errors="coerce")
# Broadcasting error NumPy → cek shape; reshape bila perlu
```

> **Output:** _tidak dijalankan_ — hanya komentar (daftar jebakan); contoh error nyata dijalankan di bagian "Demonstrasi error" di bawah

## Demonstrasi error — output nyata

Daftar jebakan di atas hanya berupa komentar. Berikut setiap kasusnya dijalankan nyata (pandas 3.x / numpy 2.x). Pada pandas 3.x chained assignment tidak mengubah `df` dan memunculkan peringatan `ChainedAssignmentError`; pada pandas 2.x hasilnya bisa tidak konsisten.

### KeyError — nama kolom salah / ada spasi tersembunyi

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"nama ": ["Ani"], "ipk": [3.7]})
print(df.columns.tolist())
print(df["nama"])
```

**Output:**

```text
['nama ', 'ipk']
  -> KeyError: 'nama'
```

### Solusi KeyError — bersihkan nama kolom

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"nama ": ["Ani"], "ipk": [3.7]})
df.columns = df.columns.str.strip()
print(df["nama"])
```

**Output:**

```text
0    Ani
Name: nama, dtype: str
```

### Chained assignment — nilai tidak berubah

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
df[df["a"] > 1]["b"] = 0
print(df)
```

**Output:**

```text
   a   b
0  1  10
1  2  20
2  3  30
[WARNING] ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment.
```

### Perbaikan — pakai `.loc`

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})
df.loc[df["a"] > 1, "b"] = 0
print(df)
```

**Output:**

```text
   a   b
0  1  10
1  2   0
2  3   0
```

### SettingWithCopy — gunakan `.copy()` pada subset yang diubah

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"IPK": [3.2, 3.8, 3.6]})
subset = df[df["IPK"] > 3.5].copy()
subset["flag"] = 1
print(subset)
print(df.columns.tolist())
```

**Output:**

```text
   IPK  flag
1  3.8     1
2  3.6     1
['IPK']
```

### Merge menghasilkan NaN — normal pada `how="left"`

```python
import pandas as pd
import numpy as np
a = pd.DataFrame({"nim": ["2201", "2202", "2203"], "nama": ["Ani", "Budi", "Citra"]})
b = pd.DataFrame({"nim": ["2201", "2202"], "skor": [85, 90]})
print(a.merge(b, on="nim", how="left"))
print(a.merge(b, on="nim", how="inner"))
```

**Output:**

```text
    nim   nama  skor
0  2201    Ani  85.0
1  2202   Budi  90.0
2  2203  Citra   NaN
    nim  nama  skor
0  2201   Ani    85
1  2202  Budi    90
```

### ValueError — merge pada kolom dengan tipe berbeda

```python
import pandas as pd
import numpy as np
a = pd.DataFrame({"nim": [2201, 2202], "nama": ["Ani", "Budi"]})
b = pd.DataFrame({"nim": ["2201", "2202"], "skor": [85, 90]})
print(a.merge(b, on="nim"))
```

**Output:**

```text
  -> ValueError: You are trying to merge on int64 and str columns for key 'nim'. If you wish to proceed you should use pd.concat
```

### Solusi — samakan tipe kunci merge

```python
import pandas as pd
import numpy as np
a = pd.DataFrame({"nim": [2201, 2202], "nama": ["Ani", "Budi"]})
b = pd.DataFrame({"nim": ["2201", "2202"], "skor": [85, 90]})
a["nim"] = a["nim"].astype(str)
print(a.merge(b, on="nim"))
```

**Output:**

```text
    nim  nama  skor
0  2201   Ani    85
1  2202  Budi    90
```

### dtype object padahal angka — `to_numeric`

```python
import pandas as pd
import numpy as np
s = pd.Series(["80", "90", "n/a"])
print(s.dtype)
print(pd.to_numeric(s, errors="coerce").tolist())
print(s.astype(int))
```

**Output:**

```text
str
[80.0, 90.0, nan]
  -> ValueError: invalid literal for int() with base 10: 'n/a'
```

### Broadcasting error NumPy — cek shape

```python
import pandas as pd
import numpy as np
a = np.ones((3, 4))
b = np.array([1, 2, 3])
print(a.shape, b.shape)
print(a + b)
```

**Output:**

```text
(3, 4) (3,)
  -> ValueError: operands could not be broadcast together with shapes (3,4) (3,)
```

### Solusi — reshape agar broadcasting berhasil

```python
import pandas as pd
import numpy as np
a = np.ones((3, 4))
b = np.array([1, 2, 3]).reshape(3, 1)
print(a + b)
```

**Output:**

```text
[[2. 2. 2. 2.]
 [3. 3. 3. 3.]
 [4. 4. 4. 4.]]
```

### ValueError — `and` / `or` pada filter DataFrame

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"ipk": [3.7, 2.8], "prodi": ["IF", "SI"]})
print(df[(df["ipk"] > 3) and (df["prodi"] == "IF")])
```

**Output:**

```text
  -> ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

### Perbaikan — `&` dengan kurung

```python
import pandas as pd
import numpy as np
df = pd.DataFrame({"ipk": [3.7, 2.8], "prodi": ["IF", "SI"]})
print(df[(df["ipk"] > 3) & (df["prodi"] == "IF")])
```

**Output:**

```text
   ipk prodi
0  3.7    IF
```

# 7. Solusi Latihan (Cuplikan)

```python
import numpy as np
a = np.arange(1, 37).reshape(6, 6)
blok = a[2:4, 2:4]
print(blok.mean(), blok.min(), blok.max())

x = np.array([2., 4., 6., 8.])
print((x - x.min()) / (x.max() - x.min()))

import pandas as pd
df = pd.DataFrame({
    "nama": list("ABCDEFGH"),
    "prodi": ["IF", "SI"] * 4,
    "ipk": [3.6, 3.1, 3.9, 2.8, 3.4, 3.7, 3.0, 3.5],
    "sks": [20, 18, 21, 19, 20, 22, 18, 19],
})
print(df[df["ipk"] >= 3.5].sort_values("ipk", ascending=False))
print(df.groupby("prodi").agg(rata=("ipk", "mean"), total_sks=("sks", "sum"), n=("nama", "count")))
```

**Output:**

```text
18.5 15 22
[0.         0.33333333 0.66666667 1.        ]
  nama prodi  ipk  sks
2    C    IF  3.9   21
5    F    SI  3.7   22
0    A    IF  3.6   20
7    H    SI  3.5   19
        rata  total_sks  n
prodi                     
IF     3.475         79  4
SI     3.275         78  4
```

# 8. Checklist Sebelum Modul 5

- Array NumPy: indexing, mask, agregasi sudah dicoba sendiri
- Pandas: loc/filter/groupby/merge pernah dijalankan
- Minimal 2–3 mini project selesai
- Siap Modul 5 — Visualisasi, API & Scraping

> **Modul 4 selesai? Lanjut ke Modul 5.**
>
> Belajar Pemrograman Python — Modul Belajar Mandiri
