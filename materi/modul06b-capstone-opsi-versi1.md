# Modul 6b — Capstone Project (Versi 1: Opsi A/B/C)

Python Intensive Bootcamp  •  Durasi 6 Jam  •  Level Menengah hingga Lanjut

> **Catatan pengujian:** kode diuji dengan Python 3.11, pandas 3.0.6, matplotlib 3.11.2, seaborn 0.13.2. Kerangka (skeleton) Opsi A/B/C sengaja belum lengkap; yang dapat dijalankan diuji dengan data contoh/sintetis dan diberi catatan di bawah outputnya. Grafik hasil eksekusi disimpan di `materi/images/modul06b/`.

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Hari 6, peserta diharapkan mampu:

- Mengintegrasikan skill Python dari Modul 1–5 ke dalam satu project analisis data yang utuh.
- Merancang alur kerja: pengambilan data → cleaning → analisis → visualisasi → insight.
- Menulis kode yang terstruktur, modular, dan mengikuti kaidah PEP 8.
- Menyajikan hasil analisis melalui visualisasi dan dokumentasi yang jelas.
- Menyusun dokumentasi Capstone Project yang rapi dan mudah dipahami.

# 2. Agenda dan Time Management

| Waktu | Sesi | Durasi | Fokus |
|---|---|---|---|
| 00:00–00:20 | Briefing + Pemilihan Topik | 20 mnt | Orientasi |
| 00:20–01:00 | Perencanaan (outline + struktur) | 40 mnt | Design |
| 01:00–04:00 | Pengerjaan Capstone | 180 mnt | Implementasi |
| 04:00–04:20 | Istirahat | 20 mnt | — |
| 04:20–05:20 | Finalisasi + Dokumentasi | 60 mnt | Polish |
| 05:20–06:00 | Showcase / Review | 40 mnt | Presentasi |

## 2.1 Saran Alokasi Waktu saat Coding (180 menit)

| Tahap | Waktu | Aktivitas |
|---|---|---|
| Load + Inspeksi | 20 mnt | Baca data, cek shape/dtypes/missing/duplikat |
| Cleaning | 25 mnt | Tangani missing, duplikat, tipe data |
| Analisis | 40 mnt | Groupby, pivot, korelasi, filter, ranking |
| Visualisasi | 45 mnt | Minimal 4–5 grafik, judul & label jelas |
| Insight + Export | 25 mnt | Tulis insight, simpan CSV/Excel |
| Buffer / Perbaikan | 25 mnt | Cadangan jika ada error |

> **Tips Time Management**
>
> Jangan terlalu lama di tahap cleaning. Cleaning yang cukup baik lebih baik daripada sempurna tapi kehabisan waktu.
>
> Kerjakan visualisasi paling penting dulu.
>
> Simpan file sesering mungkin.

# 3. Overview Capstone Project

Capstone adalah puncak bootcamp. Anda membangun project analisis data utuh dengan memanfaatkan skill dari Modul 1 sampai Modul 5. Project bersifat individual. Pilih salah satu dari tiga opsi di bawah, atau ajukan ide sendiri (dengan persetujuan instruktur).

## 3.1 Skill yang Harus Terintegrasi

| Modul | Skill yang Digunakan |
|---|---|
| Modul 1–2 | Variabel, control flow, function, error handling, file I/O |
| Modul 3 | Class / OOP (opsional tapi dianjurkan) |
| Modul 4 | NumPy & Pandas (wajib: cleaning, filtering, groupby, merge/pivot) |
| Modul 5 | Matplotlib/Seaborn + API atau Scraping (wajib ada visualisasi) |

## 3.2 Ekspektasi Kualitas Kode

> **Standar Kode yang Diharapkan**
>
> Nama variabel dan fungsi bermakna.
>
> Minimal ada beberapa function (atau class) — jangan semua kode di top-level.
>
> Ada docstring singkat pada function/class utama.
>
> Mengikuti PEP 8 secara wajar.
>
> Ada error handling pada bagian yang berisiko (baca file, panggil API).
>
> Kode dapat dijalankan dari atas ke bawah tanpa error.

# 4. Rekomendasi Dataset & Sumber Data

| Dataset / Sumber | Cocok untuk | Keterangan |
|---|---|---|
| Student Performance | Opsi A | Kaggle / UCI — nilai, gender, pendidikan ortu |
| Titanic | Opsi A | Kaggle — klasik untuk EDA |
| Iris / Penguins | Opsi A | Seaborn bawaan — kecil dan bersih |
| Gapminder | Opsi A | Data pembangunan dunia |
| JSONPlaceholder | Opsi B | API palsu — users, posts |
| Open-Meteo | Opsi B | API cuaca gratis tanpa key |
| arXiv API | Opsi B | Metadata paper ilmiah — cocok S2/S3 |
| Data nilai buatan sendiri | Opsi C | Buat CSV sendiri atau generate |

# 5. Pilihan Capstone Project

## Opsi A — Analisis Dataset Publik (Level Menengah)

### Deskripsi

Pilih satu dataset publik. Lakukan EDA lengkap, cleaning, analisis, dan visualisasi, lalu tuliskan insight yang bermakna.

### Fitur Wajib

1. Load dataset dan inspeksi awal (shape, dtypes, missing, duplikat).
2. Data cleaning yang diperlukan.
3. Minimal 5 visualisasi berbeda yang informatif.
4. Gunakan groupby / pivot_table / korelasi.
5. Minimal 5 insight yang didukung data.
6. Simpan hasil (CSV ringkasan + figure PNG/PDF).

### Stretch Goals (Bonus)

1. Tambahkan analisis statistik sederhana.
2. Buat dashboard 1 halaman (subplot 2x3 atau 3x2).
3. Export laporan multi-sheet ke Excel.

### Skeleton Code

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset.csv")
print(df.shape); print(df.dtypes); print(df.isna().sum())

# Cleaning
# df = df.drop_duplicates() / fillna / astype ...

# Analisis + Visualisasi (minimal 5 grafik)
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
# isi setiap axes ...
plt.tight_layout()
plt.savefig("capstone_visualisasi.png", dpi=150, bbox_inches="tight")
plt.show()

# Insight
# 1. ...  2. ...  3. ...  4. ...  5. ...
```

**Output:**

```text
(30, 2)
nilai       float64
kategori        str
dtype: object
nilai       0
kategori    0
dtype: int64
```

![Grafik hasil blok kode — 0_0.png](images/modul06b/0_0.png)

_Catatan: dijalankan dengan `dataset.csv` contoh (30 baris: `nilai`, `kategori`). Karena bagian "isi setiap axes" masih kosong, gambar berisi 6 panel kosong — itu memang kerangka yang harus diisi peserta._

## Opsi B — Pipeline Data dari API / arXiv (Level Menengah-Tinggi)

### Deskripsi

Ambil data secara live dari API publik atau arXiv, lakukan cleaning, analisis, visualisasi, lalu simpan hasilnya.

### Fitur Wajib

1. Ambil data dari API (requests) atau arXiv API.
2. Ubah ke DataFrame + cleaning.
3. Minimal 4 visualisasi relevan.
4. Simpan data mentah dan data bersih ke CSV.
5. Minimal 4 insight.
6. Error handling yang baik.

### Stretch Goals (Bonus)

1. Buat fungsi generik berparameter.
2. Gabungkan data dari dua sumber.
3. Caching sederhana hasil API ke file.

### Skeleton Code

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def ambil_data(...):
    try:
        # requests / arXiv call
        pass
    except Exception as e:
        print(f"Error: {e}")
        return None

data = ambil_data(...)
df = pd.DataFrame(data)  # atau pd.json_normalize
# Cleaning → Analisis → Visualisasi → Simpan → Insight
```

> **Output:** _tidak dijalankan_ — skeleton; `def ambil_data(...)` memakai `...` di daftar parameter sehingga belum valid (SyntaxError) — peserta wajib mengisi function dan memanggil API/arXiv

## Opsi C — Mini Aplikasi Analisis Nilai / Akademik (Level Tinggi)

### Deskripsi

Bangun mini sistem analisis data akademik yang memanfaatkan class/OOP, Pandas, dan visualisasi.

### Fitur Wajib

1. Minimal satu class untuk mengelola data.
2. Fitur: tambah data, statistik, filter, ranking.
3. Minimal 4 visualisasi.
4. Export laporan ke CSV/Excel.
5. Kode modular dan mudah dibaca.

### Stretch Goals (Bonus)

1. Method perbandingan dua prodi/kelas.
2. Mode interaktif sederhana (input terminal).
3. Simpan dan load state aplikasi.

### Skeleton Code

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class AnalisisNilai:
    def __init__(self, data_path=None):
        self.df = pd.read_csv(data_path) if data_path else pd.DataFrame()

    def tambah_mahasiswa(self, nama, prodi, nilai):
        pass

    def statistik(self):
        pass

    def ranking(self, n=10):
        pass

    def visualisasi(self):
        pass

    def export(self, path):
        self.df.to_csv(path, index=False)

app = AnalisisNilai("nilai.csv")
print(app.statistik())
app.visualisasi()
app.export("laporan_akhir.csv")
```

**Output:**

```text
None
```

_Catatan: dijalankan dengan `nilai.csv` contoh (20 baris). Semua method masih `pass`, sehingga `statistik()` mengembalikan `None`, `visualisasi()` belum menggambar apa pun, dan `export()` menulis ulang CSV masukan._

# 6. Ketentuan Umum dan Deliverables

## 6.1 Struktur Folder yang Direkomendasikan

```text
capstone_nama_anda/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/            # jika pakai Jupyter
├── src/                  # kode .py
├── output/
│   ├── figures/
│   └── reports/
├── requirements.txt
└── README.md
```

## 6.2 Deliverables (Yang Harus Dikumpulkan)

1. Kode sumber (.py atau .ipynb) yang dapat dijalankan.
2. File data atau instruksi cara mendapatkannya.
3. Minimal 4–5 visualisasi (PNG/PDF).
4. Dokumentasi Capstone (mengikuti template di Bagian 7).
5. README.md
6. requirements.txt berisi library yang dipakai.

## 6.3 Template README.md

````markdown
# Capstone Project: [Judul Project]

## Nama
[Nama Lengkap]

## Opsi Project
Opsi A / B / C

## Deskripsi Singkat
1–3 kalimat menjelaskan apa yang dikerjakan dan mengapa menarik.

## Sumber Data
- Nama dataset / API
- Link (jika ada)

## Cara Menjalankan
```bash
pip install -r requirements.txt
python src/main.py
# atau buka notebooks/analisis.ipynb
```

## Hasil Utama / Insight
1. Insight pertama
2. Insight kedua
3. Insight ketiga

## Struktur Folder
(jelaskan singkat)

## Pengembangan Selanjutnya (opsional)
- ...
````

# 7. Template Dokumentasi Capstone Project

Setiap peserta wajib menyusun dokumentasi Capstone dengan struktur di bawah ini. Dokumentasi dapat ditulis di dalam file Markdown (DOCUMENTATION.md), di cell Markdown pada Jupyter Notebook, atau dalam bentuk laporan singkat (PDF/DOCX).

## 7.1 Struktur Dokumentasi

1. Judul Project dan Identitas — Nama, opsi project (A/B/C), tanggal.
2. Latar Belakang / Masalah — Apa yang ingin dijawab atau dianalisis? Mengapa penting?
3. Sumber Data — Dataset/API yang digunakan, link, jumlah baris/kolom, deskripsi singkat variabel penting.
4. Metodologi / Alur Kerja — Langkah-langkah yang dilakukan (load → cleaning → analisis → visualisasi).
5. Hasil dan Visualisasi — Tampilkan grafik utama + penjelasan singkat setiap grafik.
6. Insight dan Temuan — Minimal sesuai ketentuan opsi (4–5 insight), didukung data.
7. Kesimpulan — Ringkasan temuan utama dalam 3–5 kalimat.
8. Pengembangan Selanjutnya (opsional) — Apa yang bisa ditambahkan jika ada waktu lebih.

## 7.2 Contoh Kerangka Dokumentasi

```markdown
# Dokumentasi Capstone Project

## 1. Judul dan Identitas
- Judul: Analisis Performa Akademik Mahasiswa
- Nama: [Nama Anda]
- Opsi: A (Dataset Publik)
- Tanggal: ...

## 2. Latar Belakang / Masalah
Project ini bertujuan untuk memahami faktor-faktor yang
berhubungan dengan performa akademik mahasiswa berdasarkan
dataset Student Performance. Pertanyaan utama:
- Apakah ada perbedaan nilai berdasarkan gender?
- Bagaimana pengaruh tingkat pendidikan orang tua?

## 3. Sumber Data
- Dataset: Student Performance (Kaggle/UCI)
- Jumlah baris: ... | Jumlah kolom: ...
- Variabel penting: math_score, reading_score, writing_score,
  gender, parental_level_of_education, ...

## 4. Metodologi / Alur Kerja
1. Load data dan inspeksi awal
2. Cleaning (duplikat, missing values, tipe data)
3. Feature engineering (rata-rata nilai, status lulus)
4. Analisis deskriptif dan groupby
5. Visualisasi (histogram, boxplot, bar, heatmap)
6. Penarikan insight

## 5. Hasil dan Visualisasi
(Sisipkan gambar grafik + 1–2 kalimat penjelasan per grafik)

## 6. Insight dan Temuan
1. ...
2. ...
3. ...
4. ...
5. ...

## 7. Kesimpulan
(3–5 kalimat ringkasan temuan utama)

## 8. Pengembangan Selanjutnya
- Menambahkan model prediksi sederhana
- Membandingkan dengan dataset tahun lain
```

> **Tips Menulis Dokumentasi**
>
> Tulis seolah-olah dibaca oleh orang yang belum melihat kode Anda.
>
> Insight harus menjawab pertanyaan di bagian Latar Belakang.
>
> Setiap grafik yang ditampilkan wajib dijelaskan secara singkat.
>
> Usahakan dokumentasi tidak lebih dari 2–3 halaman agar tetap fokus.

# 8. Common Pitfalls & Troubleshooting

> **Kesalahan yang Sering Terjadi**
>
> Terlalu lama membersihkan data sampai tidak sempat visualisasi dan insight.
>
> Grafik tanpa judul, tanpa label sumbu, atau warna yang sulit dibedakan.
>
> Insight hanya mengulang angka di grafik tanpa makna lebih dalam.
>
> Kode hanya berjalan di mesin sendiri karena path file hard-coded.
>
> API/arXiv gagal diakses dan tidak ada data cadangan (fallback).

```python
# Fallback jika API gagal
data = ambil_data(...)
if data is None:
    print("API gagal. Memuat data cadangan...")
    df = pd.read_csv("data/raw/backup.csv")
else:
    df = pd.DataFrame(data)

# Path relatif (agar portable)
df = pd.read_csv("data/raw/dataset.csv")

# Cek sebelum plot
print(df.columns.tolist())
print(df.head())
```

> **Output:** _tidak dijalankan_ — potongan kode ilustrasi; `ambil_data(...)` adalah placeholder. Versi yang dapat dijalankan ada di bagian 8b

# 8b. Troubleshooting Lengkap (Contoh Kasus)

Berikut contoh kasus nyata yang paling sering menghambat pengerjaan Capstone. Setiap kasus dijalankan terpisah.

## FileNotFoundError — path relatif bergantung pada folder tempat program dijalankan

Struktur folder (mengikuti bagian 6.1):

```text
proj/
├── data/raw/dataset.csv
└── src/
    ├── salah.py     # memakai path relatif "data/raw/dataset.csv"
    └── main.py      # memakai Path(__file__) sebagai acuan
```

`src/salah.py`:

```python
import pandas as pd

df = pd.read_csv("data/raw/dataset.csv")   # relatif terhadap folder tempat perintah dijalankan
print(df.shape)
```

`src/main.py`:

```python
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent   # folder proj/
df = pd.read_csv(BASE_DIR / "data" / "raw" / "dataset.csv")
print(df.shape)
```

**Output:**

```text
$ cd proj/src && python salah.py
FileNotFoundError: [Errno 2] No such file or directory: 'data/raw/dataset.csv'

$ cd proj && python src/salah.py
(2, 2)

$ cd proj/src && python main.py
(2, 2)

$ python proj/src/main.py        # dari folder lain
(2, 2)
```

## Fallback saat API gagal (data cadangan)

```python
import pandas as pd

# Kasus 1: API tidak dapat dijangkau → pakai data cadangan
import requests

def ambil_data(url):
    try:
        r = requests.get(url, timeout=2)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {type(e).__name__}")
        return None

data = ambil_data("http://127.0.0.1:9/users")
if data is None:
    print("API gagal. Memuat data cadangan...")
    df = pd.read_csv("data/raw/backup.csv")
else:
    df = pd.DataFrame(data)
print(df)
```

**Output:**

```text
# Kasus 1: API tidak dapat dijangkau → pakai data cadangan
Error: ConnectionError
API gagal. Memuat data cadangan...
   nilai kategori
0     80        A
1     70        B
```

_Catatan: `data/raw/backup.csv` pada pengujian berisi dua baris contoh (`nilai`, `kategori`); alamat `127.0.0.1:9` dipakai karena pasti menolak koneksi, sehingga jalur fallback selalu terpicu._

## KeyError — nama kolom dataset berbeda dari yang diasumsikan kode

```python
import pandas as pd

# Kasus 1: file Kaggle memakai spasi pada nama kolom
df = pd.DataFrame({"math score": [80, 90], "reading score": [70, 85]})
print(df[["math_score", "reading_score"]])

# Kasus 2: solusi — normalisasi nama kolom di awal
df = pd.DataFrame({"Math Score": [80, 90], "race/ethnicity": ["A", "B"]})
df.columns = (df.columns.str.strip().str.lower()
              .str.replace("/", "_").str.replace(" ", "_"))
print(df.columns.tolist())
```

**Output:**

```text
# Kasus 1: file Kaggle memakai spasi pada nama kolom
  -> KeyError: "None of [Index(['math_score', 'reading_score'], dtype='str')] are in the [columns]"
# Kasus 2: solusi — normalisasi nama kolom di awal
['math_score', 'race_ethnicity']
```

## FileNotFoundError — folder `output/figures` belum dibuat saat `savefig`

```python
# Kasus 1: folder tujuan belum ada
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.savefig("output/figures/grafik.png")

# Kasus 2: solusi — buat folder dulu dengan pathlib
import matplotlib.pyplot as plt
from pathlib import Path
Path("output/figures").mkdir(parents=True, exist_ok=True)
plt.plot([1, 2, 3])
plt.savefig("output/figures/grafik.png")
print(Path("output/figures/grafik.png").exists())
```

**Output:**

```text
# Kasus 1: folder tujuan belum ada
  -> FileNotFoundError: [Errno 2] No such file or directory: 'output/figures/grafik.png'
# Kasus 2: solusi — buat folder dulu dengan pathlib
True
```

## ValueError — `corr()` / heatmap pada kolom non-angka

```python
import pandas as pd

# Kasus 1: DataFrame berisi kolom teks
df = pd.DataFrame({"gender": ["f", "m", "f"], "math": [80, 70, 90], "reading": [75, 72, 88]})
print(df.corr())

# Kasus 2: solusi — hanya kolom numerik
df = pd.DataFrame({"gender": ["f", "m", "f"], "math": [80, 70, 90], "reading": [75, 72, 88]})
print(df.corr(numeric_only=True).round(2))
```

**Output:**

```text
# Kasus 1: DataFrame berisi kolom teks
  -> ValueError: could not convert string to float: 'f'
# Kasus 2: solusi — hanya kolom numerik
         math  reading
math     1.00     0.94
reading  0.94     1.00
```

# 9. Contoh Outline Kode (Student Performance)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

# 1. Load & Inspeksi
df = pd.read_csv("data/raw/student_performance.csv")
print(df.shape, df.isna().sum(), sep="\n")

# 2. Cleaning
df = df.drop_duplicates()

# 3. Feature engineering
df["rata_rata"] = df[["math_score","reading_score","writing_score"]].mean(axis=1)
df["lulus"] = df["rata_rata"] >= 60

# 4. Analisis
print(df.groupby("gender")["rata_rata"].mean())
print(df.groupby("parental_level_of_education")["rata_rata"].mean())

# 5. Visualisasi
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.histplot(data=df, x="rata_rata", kde=True, ax=axes[0,0])
axes[0,0].set_title("Distribusi Rata-rata Nilai")
sns.boxplot(data=df, x="gender", y="rata_rata", ax=axes[0,1])
axes[0,1].set_title("Nilai by Gender")
sns.barplot(data=df, x="parental_level_of_education", y="rata_rata", ax=axes[1,0])
axes[1,0].tick_params(axis="x", rotation=45)
sns.heatmap(df[["math_score","reading_score","writing_score"]].corr(),
            annot=True, ax=axes[1,1], cmap="coolwarm")
plt.tight_layout()
plt.savefig("output/figures/capstone_student.png", dpi=150, bbox_inches="tight")
plt.show()
```

**Output:**

```text
(301, 8)
gender                         0
race_ethnicity                 0
parental_level_of_education    0
lunch                          0
test_preparation_course        0
math_score                     0
reading_score                  0
writing_score                  0
dtype: int64
gender
female    67.083857
male      66.756501
Name: rata_rata, dtype: float64
parental_level_of_education
associate's degree    67.380117
bachelor's degree     71.782946
high school           63.570370
master's degree       69.768116
some college          66.212121
some high school      63.703704
Name: rata_rata, dtype: float64
```

![Grafik hasil blok kode — 4_0.png](images/modul06b/4_0.png)

_Catatan: dijalankan dengan dataset sintetis berstruktur seperti Student Performance (300 baris + 1 duplikat sengaja) di `data/raw/student_performance.csv`, bukan data asli Kaggle/UCI, sehingga angka pada output hanya contoh. Folder `output/figures/` harus sudah ada (lihat kasus `FileNotFoundError` di bagian 8b). Jika memakai file Kaggle asli, nama kolomnya memuat spasi (mis. `math score`) sehingga harus dinormalisasi dulu — lihat bagian 8b._

# 10. Checklist Sebelum Submit

> **Pastikan Semua Poin Ini Sudah Dipenuhi**
>
> - [ ] Kode dapat dijalankan dari atas ke bawah tanpa error.
> - [ ] Semua fitur wajib dari opsi yang dipilih sudah ada.
> - [ ] Minimal 4–5 visualisasi dengan judul dan label jelas.
> - [ ] Insight tertulis sesuai ketentuan opsi.
> - [ ] Dokumentasi Capstone sudah ditulis (mengikuti template Bagian 7).
> - [ ] README.md sudah diisi.
> - [ ] requirements.txt berisi library yang dipakai.
> - [ ] File output (CSV/PNG) tersimpan rapi.
> - [ ] (Bonus) Stretch goals dikerjakan jika masih ada waktu.

> **Selamat Mengerjakan Capstone Project!**
>
> Fokus pada insight dan dokumentasi yang jelas  •  Selamat berjuang!
