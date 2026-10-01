# Hari 4 — Data Analysis dengan NumPy & Pandas

Python Intensive Bootcamp  •  Durasi 6 Jam  •  Level Menengah  •  5 Mini Project

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Hari 4, peserta diharapkan mampu:

- Menguasai pembuatan array NumPy, indexing, slicing, boolean masking, broadcasting, dan operasi statistik dasar hingga menengah.
- Menguasai Pandas Series dan DataFrame, termasuk inspeksi data, selection, filtering, dan transformasi kolom.
- Melakukan data cleaning secara sistematis (menangani missing values, data duplikat, dan konversi tipe data).
- Melakukan grouping, aggregation, merging, joining, serta membuat pivot table.
- Membaca data dari file CSV dan Excel, serta menyimpan hasil analisis kembali ke file.
- Menyelesaikan minimal tiga dari lima Mini Project yang disediakan pada materi ini.
# 2. Agenda dan Alokasi Waktu

| Waktu | Sesi | Durasi | Fokus |
|---|---|---|---|
| 00:00 – 00:10 | Setup library (numpy, pandas, openpyxl) | 10 menit | Persiapan |
| 00:10 – 01:30 | NumPy Deep Dive | 80 menit | Array dan Statistik |
| 01:30 – 02:25 | Pandas Dasar hingga Menengah | 55 menit | DataFrame |
| 02:25 – 02:45 | Istirahat | 20 menit | — |
| 02:45 – 04:00 | Data Cleaning, GroupBy, Merge, Pivot | 75 menit | Pandas Lanjutan |
| 04:00 – 05:40 | Pengerjaan Mini Project | 100 menit | Praktik |
| 05:40 – 06:00 | Review dan Sharing Insight | 20 menit | Refleksi |

# 3. NumPy Deep Dive

## 3.1 Mengapa NumPy Penting?

NumPy (Numerical Python) merupakan fondasi dari hampir seluruh ekosistem data science di Python. Library populer seperti Pandas, Matplotlib, Scikit-learn, TensorFlow, dan PyTorch semuanya dibangun di atas NumPy. Array NumPy disimpan secara kontigu di memori dan sebagian besar operasinya dijalankan dalam bahasa C, sehingga jauh lebih cepat dan hemat memori dibandingkan list biasa di Python ketika kita bekerja dengan data numerik dalam jumlah besar.

## 3.2 Membuat Array

Berikut adalah berbagai cara yang paling sering digunakan untuk membuat array NumPy:

```python
import numpy as np

# Membuat array dari list atau tuple
a = np.array([1, 2, 3, 4, 5])
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

print(a.shape)      # (5,)
print(b.shape)      # (2, 3)
print(a.ndim)       # 1 (dimensi)
print(b.ndim)       # 2
print(a.dtype)      # int64 atau int32 (tergantung sistem)
print(b.dtype)      # float64

# Membuat array khusus
np.zeros(5)                     # array 1 dimensi berisi nol
np.zeros((3, 4))                # matriks 3 baris x 4 kolom berisi nol
np.ones((2, 3))                 # matriks 2x3 berisi satu
np.full((2, 2), 7)              # matriks 2x2 yang seluruhnya berisi angka 7
np.eye(4)                       # matriks identitas berukuran 4x4
np.arange(0, 12, 2)             # [0 2 4 6 8 10]  (mirip range di Python)
np.linspace(0, 1, 6)            # 6 angka dari 0 sampai 1 yang jaraknya merata

# Membuat array berisi bilangan acak
np.random.seed(42)              # agar hasil random bisa direproduksi
np.random.rand(3, 3)            # distribusi uniform antara 0 dan 1
np.random.randn(3, 3)           # distribusi normal standar (mean=0, std=1)
np.random.randint(1, 100, size=(2, 5))  # bilangan bulat acak
```

## 3.3 Indexing, Slicing, dan Boolean Masking

Kemampuan untuk memilih dan memfilter elemen array merupakan salah satu kekuatan utama NumPy. Perhatikan contoh-contoh berikut:

```python
arr = np.array([[10, 20, 30, 40],
                [50, 60, 70, 80],
                [90, 100, 110, 120]])

# Indexing dasar
print(arr[0, 2])                # 30  (baris ke-0, kolom ke-2)
print(arr[-1, -1])              # 120 (baris terakhir, kolom terakhir)
print(arr[1])                   # [50 60 70 80]  seluruh baris ke-1

# Slicing
print(arr[0:2, 1:3])            # [[20 30] [60 70]]
print(arr[:, 2])                # [30 70 110]  seluruh baris pada kolom ke-2
print(arr[::2, ::2])            # mengambil dengan loncatan 2

# Boolean masking (sangat sering digunakan dalam analisis data)
print(arr[arr > 60])            # semua elemen yang lebih besar dari 60
print(arr[arr % 20 == 0])       # elemen yang merupakan kelipatan 20

# Menggabungkan beberapa kondisi
mask = (arr > 40) & (arr < 100)
print(arr[mask])

# np.where : mengganti nilai berdasarkan kondisi
print(np.where(arr > 70, arr, -1))   # yang <= 70 diganti menjadi -1
```

## 3.4 Operasi Aritmatika, Aggregasi, dan Broadcasting

Broadcasting memungkinkan kita melakukan operasi antara array yang memiliki shape berbeda tanpa harus menyalin data secara manual. Fitur ini sangat powerful dan sering digunakan.

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)
print(a * 3)
print(a ** 2)
print(np.sqrt(a))
print(np.exp(a))

# Operasi agregasi
print(a.sum(), a.mean(), a.std())
print(a.min(), a.max())
print(a.argmin(), a.argmax())     # index dari nilai minimum/maksimum
print(np.median(a))
print(np.percentile(a, 75))

# Aggregasi dengan parameter axis
m = np.arange(12).reshape(3, 4)
print(m.sum(axis=0))              # jumlah ke bawah (per kolom)
print(m.sum(axis=1))              # jumlah ke samping (per baris)

# Contoh praktis broadcasting: menghitung nilai akhir berbobot
nilai = np.array([[80, 90, 70],
                  [60, 75, 85],
                  [90, 95, 88]])
bobot = np.array([0.3, 0.4, 0.3])  # bobot UTS, UAS, Tugas
nilai_akhir = (nilai * bobot).sum(axis=1)
print(nilai_akhir)
```

## 3.5 Manipulasi Shape

```python
a = np.arange(12)
print(a.reshape(3, 4))
print(a.reshape(2, -1))           # -1 artinya ukuran dihitung otomatis
print(a.ravel())                  # mengubah menjadi 1 dimensi (view)
print(np.vstack([a, a]))          # menumpuk secara vertikal
print(np.hstack([a, a]))          # menumpuk secara horizontal
```

## 3.6 Latihan NumPy

1. Buat array berukuran 6x6 yang berisi angka 1 sampai 36. Ambil bagian tengahnya (sub-array 4x4), kemudian hitung nilai mean dan standar deviasinya.
2. Buat dua buah array random yang masing-masing berisi 100 elemen. Hitung korelasi Pearson antara kedua array tersebut.
3. Lakukan normalisasi min-max terhadap sebuah array random sehingga seluruh nilainya berada pada rentang 0 sampai 1.
4. Buat matriks identitas berukuran 5x5, kemudian ganti seluruh elemen pada diagonal utamanya menjadi [10, 20, 30, 40, 50].
# 4. Pandas — Series dan DataFrame

## 4.1 Series

Series adalah struktur data satu dimensi yang memiliki label (disebut index). Series mirip dengan array NumPy, namun dilengkapi dengan index yang dapat berupa label non-numerik.

```python
import pandas as pd
import numpy as np

s = pd.Series([85, 90, 78, 92], index=["Ani", "Budi", "Citra", "Dedi"])
print(s)
print(s["Budi"])
print(s[s >= 90])
print(s.mean())
print(s.std())
print(s.describe())
```

## 4.2 DataFrame

DataFrame adalah struktur data dua dimensi yang mirip dengan tabel pada Microsoft Excel atau tabel pada database. DataFrame dapat dipandang sebagai kumpulan Series yang berbagi index yang sama.

```python
data = {
    "nama": ["Ani", "Budi", "Citra", "Dedi", "Eka", "Fajar"],
    "nim": ["2201", "2202", "2203", "2204", "2205", "2206"],
    "prodi": ["IF", "SI", "IF", "SI", "IF", "SI"],
    "ipk": [3.75, 3.20, 3.90, 2.85, 3.55, 3.10],
    "semester": [3, 5, 3, 7, 5, 3],
    "kota": ["Jakarta", "Bandung", "Jakarta", "Surabaya", "Bandung", "Jakarta"]
}
df = pd.DataFrame(data)

# Berbagai cara untuk menginspeksi data
print(df.head())                  # 5 baris pertama
print(df.tail(3))                 # 3 baris terakhir
print(df.sample(3))               # 3 baris acak
print(df.shape)                   # (jumlah baris, jumlah kolom)
print(df.columns.tolist())
print(df.dtypes)
print(df.info())
print(df.describe())              # statistik deskriptif kolom numerik
print(df.describe(include="all"))
print(df["prodi"].value_counts())
print(df["prodi"].unique())
print(df.nunique())
```

## 4.3 Selection dengan loc dan iloc

Gunakan loc apabila Anda memilih data berdasarkan label (nama index atau nama kolom). Gunakan iloc apabila Anda memilih data berdasarkan posisi integer.

```python
# Mengambil kolom
print(df["nama"])
print(df[["nama", "ipk"]])

# loc — berbasis label
print(df.loc[0])
print(df.loc[0, "nama"])
print(df.loc[0:3, ["nama", "ipk"]])
print(df.loc[df["ipk"] > 3.5, ["nama", "ipk"]])

# iloc — berbasis posisi integer
print(df.iloc[0])
print(df.iloc[0:3, 0:2])
print(df.iloc[[0, 2, 4], [0, 3]])
```

## 4.4 Filtering Data

```python
print(df[df["ipk"] >= 3.5])
print(df[(df["ipk"] >= 3.5) & (df["prodi"] == "IF")])
print(df[(df["ipk"] < 3.0) | (df["semester"] >= 7)])
print(df[df["prodi"].isin(["IF", "SI"])])
print(df[df["nama"].str.contains("a", case=False)])
print(df[df["kota"].str.startswith("J")])

# Metode query — lebih mudah dibaca untuk kondisi yang kompleks
print(df.query("ipk >= 3.5 and prodi == 'IF'"))
print(df.query("kota in ['Jakarta', 'Bandung']"))
```

## 4.5 Menambah, Mengubah, dan Menghapus Kolom atau Baris

```python
# Menambah kolom baru
df["status"] = np.where(df["ipk"] >= 3.5, "Cumlaude", "Reguler")
df["sks"] = [20, 18, 21, 16, 19, 20]

# Menggunakan apply untuk menerapkan fungsi ke setiap elemen
def tentukan_grade(ipk):
    if ipk >= 3.5:
        return "A"
    elif ipk >= 3.0:
        return "B"
    elif ipk >= 2.5:
        return "C"
    else:
        return "D"

df["grade"] = df["ipk"].apply(tentukan_grade)

# Mapping nilai kategori
df["prodi_lengkap"] = df["prodi"].map({
    "IF": "Informatika",
    "SI": "Sistem Informasi"
})

# Mengubah nilai pada baris tertentu
df.loc[df["nama"] == "Budi", "ipk"] = 3.35

# Menghapus kolom atau baris
df.drop(columns=["sks"], inplace=True)
df.drop(index=[5], inplace=True)

# Mengganti nama kolom
df.rename(columns={"ipk": "IPK", "nim": "NIM"}, inplace=True)
```

## 4.6 Sorting

```python
print(df.sort_values("IPK", ascending=False))
print(df.sort_values(["prodi", "IPK"], ascending=[True, False]))
print(df.nlargest(3, "IPK"))          # 3 baris dengan IPK tertinggi
print(df.nsmallest(3, "IPK"))         # 3 baris dengan IPK terendah
```

# 5. Data Cleaning dan Operasi Lanjutan

## 5.1 Menangani Missing Values

Missing values (nilai yang hilang) adalah masalah yang sangat umum dijumpai pada data nyata. Pandas menyediakan berbagai cara untuk mendeteksi dan menanganinya.

```python
df_kotor = pd.DataFrame({
    "nama": ["Ani", "Budi", np.nan, "Dedi", "Eka", "Budi"],
    "ipk": [3.7, np.nan, 3.9, 2.8, np.nan, 3.2],
    "prodi": ["IF", "SI", "IF", np.nan, "IF", "SI"],
    "umur": [20, 21, 20, 22, 19, 21]
})

# Mendeteksi missing values
print(df_kotor.isna().sum())              # jumlah per kolom
print(df_kotor.isna().mean() * 100)       # dalam bentuk persentase

# Menghapus baris atau kolom yang mengandung missing values
print(df_kotor.dropna())                  # hapus baris yang punya NaN
print(df_kotor.dropna(subset=["nama"]))   # hapus hanya jika kolom nama NaN

# Mengisi missing values
print(df_kotor["ipk"].fillna(df_kotor["ipk"].mean()))
print(df_kotor["ipk"].fillna(df_kotor["ipk"].median()))
print(df_kotor["prodi"].fillna("Unknown"))
print(df_kotor.fillna(method="ffill"))    # forward fill
print(df_kotor.fillna(method="bfill"))    # backward fill
```

## 5.2 Menangani Data Duplikat dan Konversi Tipe Data

```python
print(df_kotor.duplicated())
print(df_kotor.drop_duplicates())
print(df_kotor.drop_duplicates(subset=["nama"], keep="first"))

# Konversi tipe data
df["semester"] = df["semester"].astype("int32")
df["IPK"] = pd.to_numeric(df["IPK"], errors="coerce")
df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
```

## 5.3 GroupBy dan Aggregation

GroupBy memungkinkan kita membagi data ke dalam kelompok berdasarkan nilai kolom tertentu, kemudian menerapkan fungsi agregasi pada masing-masing kelompok.

```python
print(df.groupby("prodi")["IPK"].mean())
print(df.groupby("prodi")["IPK"].agg(["mean", "median", "std", "count", "min", "max"]))

print(df.groupby(["prodi", "status"]).size())
print(df.groupby(["prodi", "status"])["IPK"].mean())

# transform menghasilkan output yang panjangnya sama dengan data asli
df["ipk_mean_prodi"] = df.groupby("prodi")["IPK"].transform("mean")
df["ipk_rank"] = df.groupby("prodi")["IPK"].rank(ascending=False)

# filter: menyaring kelompok berdasarkan kondisi
print(df.groupby("prodi").filter(lambda x: x["IPK"].mean() > 3.3))
```

## 5.4 Merge, Join, dan Concat

Sering kali data yang kita butuhkan tersebar di beberapa tabel. Pandas menyediakan fungsi merge dan concat untuk menggabungkan data.

```python
mahasiswa = pd.DataFrame({
    "nim": ["2201", "2202", "2203"],
    "nama": ["Ani", "Budi", "Citra"]
})
nilai = pd.DataFrame({
    "nim": ["2201", "2202", "2204"],
    "matkul": ["Python", "BD", "Python"],
    "skor": [85, 90, 78]
})
absensi = pd.DataFrame({
    "nim": ["2201", "2202", "2203"],
    "hadir": [90, 75, 95]
})

print(pd.merge(mahasiswa, nilai, on="nim", how="inner"))
print(pd.merge(mahasiswa, nilai, on="nim", how="left"))
print(pd.merge(mahasiswa, nilai, on="nim", how="outer"))
print(pd.merge(mahasiswa, absensi, on="nim"))

print(pd.concat([mahasiswa, mahasiswa], ignore_index=True))
```

## 5.5 Pivot Table

```python
data = pd.DataFrame({
    "nama": ["Ani", "Ani", "Budi", "Budi", "Citra", "Citra"],
    "semester": [1, 2, 1, 2, 1, 2],
    "matkul": ["Python", "BD", "Python", "BD", "Python", "BD"],
    "nilai": [85, 90, 78, 88, 92, 85]
})

print(data.pivot_table(values="nilai", index="nama", columns="matkul", aggfunc="mean"))
print(data.pivot_table(values="nilai", index="nama", columns="semester", aggfunc="mean", margins=True))
print(pd.crosstab(data["nama"], data["matkul"]))
```

## 5.6 Membaca dan Menyimpan File

```python
# Membaca file CSV
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", sep=";", encoding="utf-8", na_values=["-", "NA"])
df = pd.read_csv("data.csv", usecols=["nama", "ipk"], nrows=1000)

# Membaca file Excel
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

# Menyimpan ke file
df.to_csv("hasil.csv", index=False)
df.to_excel("hasil.xlsx", index=False, sheet_name="Analisis")
```

# 6. Lima Mini Project

## Mini Project 1 — Kalkulator Nilai Akhir Mahasiswa (Level Dasar)

### Deskripsi

Buat sebuah DataFrame yang berisi data nilai mahasiswa (minimal 12 baris) dengan kolom: nama, nim, prodi, nilai_uts, nilai_uas, dan nilai_tugas. Hitung nilai akhir berdasarkan bobot tertentu, tentukan grade, dan lakukan beberapa ringkasan statistik.

### Fitur Wajib

1. Hitung nilai akhir dengan bobot UTS 30%, UAS 40%, dan Tugas 30%.
2. Tambahkan kolom grade (A jika nilai >= 85, B jika >= 70, C jika >= 55, D jika >= 40, E jika < 40).
3. Tampilkan 5 mahasiswa dengan nilai akhir tertinggi.
4. Hitung rata-rata nilai akhir untuk setiap program studi.
5. Hitung jumlah mahasiswa pada setiap grade.
### Skeleton Code

```python
import pandas as pd
import numpy as np

# 1. Buat DataFrame (minimal 12 baris data)
data = {
    "nama": [...],
    "nim": [...],
    "prodi": [...],
    "nilai_uts": [...],
    "nilai_uas": [...],
    "nilai_tugas": [...]
}
df = pd.DataFrame(data)

# 2. Hitung nilai akhir
df["nilai_akhir"] = ...

# 3. Buat fungsi untuk menentukan grade, lalu terapkan dengan apply
def tentukan_grade(nilai):
    # tuliskan logika if-elif-else di sini
    pass

df["grade"] = df["nilai_akhir"].apply(tentukan_grade)

# 4. Tampilkan 5 mahasiswa dengan nilai tertinggi
top5 = df.nlargest(5, "nilai_akhir")
print(top5[["nama", "nilai_akhir", "grade"]])

# 5. Rata-rata nilai akhir per prodi
print(df.groupby("prodi")["nilai_akhir"].mean())

# 6. Jumlah mahasiswa per grade
print(df["grade"].value_counts())
```

> Tips Pengerjaan Project 1 Gunakan metode nlargest() untuk mengambil baris dengan nilai tertinggi agar kode lebih ringkas. Fungsi penentuan grade dapat juga dibuat dengan np.where yang bersarang, namun if-elif biasanya lebih mudah dibaca.

## Mini Project 2 — Cleaning Dataset Kotor (Level Menengah)

### Deskripsi

Buat sebuah dataset yang sengaja dibuat kotor (mengandung missing values, data duplikat, tipe data yang tidak sesuai, dan spasi berlebih pada teks). Lakukan proses cleaning secara menyeluruh, kemudian simpan hasilnya ke file CSV.

### Fitur Wajib

1. Deteksi missing values (tampilkan jumlah dan persentasenya untuk setiap kolom).
2. Tangani missing values dengan strategi yang tepat (menghapus atau mengisi nilai).
3. Hapus data yang duplikat.
4. Perbaiki tipe data dan bersihkan spasi yang tidak perlu pada kolom teks.
5. Simpan hasil cleaning ke dalam file CSV baru.
### Skeleton Code

```python
import pandas as pd
import numpy as np

# 1. Buat dataset yang kotor
df = pd.DataFrame({
    "nama": ["Ani", "Budi", np.nan, "Dedi", "Eka", "Budi", " Ani "],
    "ipk": [3.7, np.nan, 3.9, 2.8, np.nan, 3.2, 3.7],
    "prodi": ["IF", "SI", "IF", None, "IF", "SI", "IF"],
    "umur": ["20", "21", "20", "22", "19", "21", "20"]
})

print("Shape sebelum cleaning:", df.shape)
print(df.isna().sum())
print(df.isna().mean() * 100)

# 2. Tangani missing values
df["nama"] = df["nama"].fillna("Unknown")
df["ipk"] = df["ipk"].fillna(df["ipk"].median())
df["prodi"] = df["prodi"].fillna("Unknown")

# 3. Hapus data duplikat
df = df.drop_duplicates()

# 4. Bersihkan spasi dan perbaiki tipe data
df["nama"] = df["nama"].str.strip()
df["umur"] = pd.to_numeric(df["umur"], errors="coerce")

print("Shape setelah cleaning:", df.shape)
print(df)

# 5. Simpan hasil cleaning
df.to_csv("data_bersih.csv", index=False)
print("File berhasil disimpan.")
```

## Mini Project 3 — Analisis Multi-Tabel dengan Merge (Level Menengah)

### Deskripsi

Buat tiga buah DataFrame terpisah yang merepresentasikan data mahasiswa, data nilai, dan data kehadiran. Gabungkan ketiga data tersebut, kemudian lakukan analisis terhadap hubungan antar variabel.

### Fitur Wajib

1. Merge ketiga sumber data menjadi satu DataFrame yang utuh.
2. Buat ranking mahasiswa berdasarkan nilai akhir.
3. Analisis hubungan antara tingkat kehadiran dan nilai (menggunakan korelasi atau groupby).
4. Filter kasus yang menarik, misalnya mahasiswa dengan kehadiran rendah namun nilai tinggi.
5. Buat ringkasan statistik per program studi menggunakan groupby dan agg.
### Skeleton Code

```python
import pandas as pd

# 1. Buat tiga DataFrame
mahasiswa = pd.DataFrame({
    "nim": ["2201", "2202", "2203", "2204", "2205"],
    "nama": ["Ani", "Budi", "Citra", "Dedi", "Eka"],
    "prodi": ["IF", "SI", "IF", "SI", "IF"]
})

nilai = pd.DataFrame({
    "nim": ["2201", "2202", "2203", "2204", "2205"],
    "nilai_akhir": [85, 78, 92, 70, 88]
})

kehadiran = pd.DataFrame({
    "nim": ["2201", "2202", "2203", "2204", "2205"],
    "persen_hadir": [95, 70, 90, 60, 85]
})

# 2. Merge ketiga DataFrame
df = mahasiswa.merge(nilai, on="nim").merge(kehadiran, on="nim")
print(df)

# 3. Buat ranking berdasarkan nilai akhir
df["rank"] = df["nilai_akhir"].rank(ascending=False).astype(int)
print(df.sort_values("rank"))

# 4. Hitung korelasi antara kehadiran dan nilai
print(df[["persen_hadir", "nilai_akhir"]].corr())

# 5. Filter kasus menarik
print(df[(df["persen_hadir"] < 75) & (df["nilai_akhir"] >= 80)])

# 6. Ringkasan statistik per prodi
print(df.groupby("prodi").agg({
    "nilai_akhir": ["mean", "min", "max"],
    "persen_hadir": "mean"
}))
```

## Mini Project 4 — Pivot Table dan Reporting (Level Menengah-Tinggi)

### Deskripsi

Gunakan data nilai yang mencakup beberapa mata kuliah. Buat laporan dalam bentuk pivot table, hitung ringkasan yang relevan, dan export hasilnya ke file Excel.

### Fitur Wajib

1. Buat pivot table yang menampilkan nilai per mahasiswa per mata kuliah.
2. Hitung rata-rata nilai untuk setiap mata kuliah dan setiap program studi.
3. Tambahkan kolom rata-rata keseluruhan dan status kelulusan pada pivot table.
4. Export hasil analisis ke file Excel.
5. Tuliskan minimal tiga insight yang diperoleh dari hasil analisis.
### Skeleton Code

```python
import pandas as pd

# 1. Siapkan data multi-matakuliah
data = pd.DataFrame({
    "nama": ["Ani", "Ani", "Ani", "Budi", "Budi", "Budi", "Citra", "Citra", "Citra"],
    "prodi": ["IF", "IF", "IF", "SI", "SI", "SI", "IF", "IF", "IF"],
    "matkul": ["Python", "BD", "Jaringan"] * 3,
    "nilai": [85, 90, 78, 70, 88, 75, 92, 85, 80]
})

# 2. Buat pivot table
pivot = data.pivot_table(
    values="nilai",
    index="nama",
    columns="matkul",
    aggfunc="mean"
)
print(pivot)

# 3. Rata-rata per mata kuliah dan per prodi
print(data.groupby("matkul")["nilai"].mean())
print(data.groupby("prodi")["nilai"].mean())

# 4. Tambahkan kolom rata-rata dan status kelulusan
pivot["rata_rata"] = pivot.mean(axis=1)
pivot["status"] = pivot["rata_rata"].apply(
    lambda x: "Lulus" if x >= 75 else "Tidak Lulus"
)
print(pivot)

# 5. Export ke file Excel
pivot.to_excel("laporan_nilai.xlsx")
print("Laporan berhasil disimpan.")

# 6. Tuliskan insight yang diperoleh
# Insight 1: ...
# Insight 2: ...
# Insight 3: ...
```

## Mini Project 5 — Exploratory Data Analysis pada Dataset Publik (Level Tinggi)

### Deskripsi

Pilih salah satu dataset publik yang tersedia (contoh: Student Performance, Titanic, Iris, atau dataset lain yang relevan dengan bidang Anda). Lakukan proses Exploratory Data Analysis secara lengkap dan tuliskan temuan-temuan penting yang didukung oleh data.

### Fitur Wajib

1. Lakukan inspeksi awal terhadap data: shape, dtypes, describe, missing values, dan jumlah duplikat.
2. Lakukan data cleaning yang diperlukan.
3. Lakukan analisis univariat (distribusi variabel numerik dan frekuensi variabel kategorikal).
4. Lakukan analisis bivariat (menggunakan groupby, pivot table, atau korelasi).
5. Tuliskan minimal empat insight atau temuan menarik yang didukung oleh data.
6. Simpan tabel ringkasan penting ke dalam file CSV atau Excel.
### Skeleton Code

```python
import pandas as pd
import numpy as np

# 1. Load dataset (ganti dengan path atau URL dataset yang Anda pilih)
df = pd.read_csv("nama_dataset.csv")

# 2. Inspeksi awal
print("Shape:", df.shape)
print(df.dtypes)
print(df.describe())
print(df.describe(include="object"))
print("Missing values:")
print(df.isna().sum())
print("Jumlah duplikat:", df.duplicated().sum())
print(df.head())

# 3. Data cleaning
# df = df.dropna(subset=[...])
# df["kolom"] = df["kolom"].fillna(...)
# df = df.drop_duplicates()

# 4. Analisis univariat
# print(df["kolom_numerik"].describe())
# print(df["kolom_kategori"].value_counts())

# 5. Analisis bivariat
# print(df.groupby("kategori")["numerik"].mean())
# print(df.pivot_table(...))
# print(df[["kolom1", "kolom2"]].corr())

# 6. Tuliskan insight (bagian ini wajib diisi)
# Insight 1: ...
# Insight 2: ...
# Insight 3: ...
# Insight 4: ...

# 7. Simpan ringkasan penting
# ringkasan = df.groupby(...).agg(...)
# ringkasan.to_csv("ringkasan_eda.csv")
```

> Panduan Pengerjaan Mini Project Mini Project 1 dan Mini Project 2 bersifat wajib untuk dikerjakan oleh seluruh peserta. Mini Project 3, 4, dan 5 bersifat challenge. Kerjakan sesuai dengan sisa waktu dan kemampuan masing-masing. Sangat disarankan menggunakan Jupyter Notebook agar seluruh proses analisis terdokumentasi dengan rapi. Dataset publik yang direkomendasikan antara lain: Student Performance (UCI atau Kaggle), Titanic, Iris, dan Gapminder.

# 7. Troubleshooting dan Best Practice

```python
# SettingWithCopyWarning
# Solusi: tambahkan .copy() ketika membuat subset yang akan dimodifikasi
subset = df[df["IPK"] > 3.5].copy()
subset["flag"] = 1

# KeyError saat mencoba mengakses kolom
# Periksa nama kolom dengan perintah: df.columns.tolist()
# Perhatikan kemungkinan adanya spasi tersembunyi pada nama kolom

# Hindari chained assignment
# Jangan menulis: df[df["a"] > 1]["b"] = 0
# Tuliskan dengan: df.loc[df["a"] > 1, "b"] = 0

# Ketika bekerja dengan dataset berukuran besar
pd.read_csv("data_besar.csv", usecols=["kolom1", "kolom2"])
df["kategori"] = df["kategori"].astype("category")
```

> Best Practice dalam Menggunakan Pandas Gunakan .loc dan .iloc secara eksplisit agar kode lebih jelas dan terhindar dari ambiguitas. Setelah melakukan operasi penting, selalu periksa hasilnya dengan .head() atau .shape. Apabila terdapat rangkaian langkah cleaning yang berulang, bungkus langkah-langkah tersebut ke dalam sebuah function agar mudah digunakan kembali.

> Materi Hari 4 Selesai Kerjakan Mini Project 1 dan 2 (wajib)   •   Challenge Project 3 sampai 5   •   Lanjut ke Hari 5

8. Solusi Latihan NumPy

Berikut solusi untuk latihan pada bagian 3.6 Latihan NumPy.

Soal 1 — Array 6x6 dan statistik bagian tengah

```python
import numpy as np
arr = np.arange(1, 37).reshape(6, 6)
tengah = arr[1:5, 1:5]
print(tengah)
print("Mean:", tengah.mean())
print("Std:", tengah.std())
```

Soal 2 — Korelasi Pearson

```python
np.random.seed(42)
a = np.random.randn(100)
b = np.random.randn(100)
print("Korelasi:", np.corrcoef(a, b)[0, 1])
```

Soal 3 — Normalisasi min-max

```python
np.random.seed(42)
x = np.random.rand(20) * 100
x_norm = (x - x.min()) / (x.max() - x.min())
print(x_norm)
```

Soal 4 — Diagonal matriks identitas

```python
m = np.eye(5)
np.fill_diagonal(m, [10, 20, 30, 40, 50])
print(m)
```

Untuk latihan Pandas, praktikkan ulang contoh groupby, merge, dan pivot_table. Gunakan dataset Mini Project sebagai latihan tambahan.

Tips Umum Mini Project Hari 4

• Project 1 & 2 wajib; Project 3–5 challenge sesuai kemampuan.

• Selalu cek df.head(), df.info(), df.isna().sum() sebelum analisis.

• Gunakan .copy() saat membuat subset yang akan dimodifikasi.

• Simpan hasil akhir ke CSV/Excel agar mudah dilaporkan.

• Beri judul dan label yang jelas pada setiap ringkasan/groupby.

