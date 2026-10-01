# Hari 5 — Visualisasi Data, API & Web Scraping

Python Intensive Bootcamp  •  Durasi 6 Jam  •  Level Menengah

> **Catatan pengujian:** kode diuji dengan Python 3.11, matplotlib 3.11.2, seaborn 0.13.2, pandas 3.0.6, requests, beautifulsoup4 4.15, feedparser 6.0.14. Grafik hasil eksekusi disimpan sebagai gambar di `materi/images/hari5/` dan ditampilkan di bawah tiap blok kode. Peringatan `MatplotlibDeprecationWarning: vert ...` pada boxplot/violinplot muncul dari kombinasi seaborn 0.13.2 dengan matplotlib 3.11 dan tidak memengaruhi hasil. Host API selain `api.github.com` diblokir di lingkungan pengujian; bagian yang memakai API/scraping/arXiv dijalankan dengan respons tiruan dan diberi catatan.

# 1. Tujuan Pembelajaran

Setelah menyelesaikan Hari 5, peserta diharapkan mampu:

- Membuat berbagai jenis visualisasi data menggunakan Matplotlib (line, bar, scatter, histogram, pie, dan subplot).
- Membuat visualisasi statistik yang informatif dengan Seaborn.
- Mengambil data dari API publik menggunakan requests dan mengolah JSON menjadi DataFrame.
- Melakukan web scraping sederhana secara etis dan menggunakan arXiv API.
- Menyelesaikan soal latihan di setiap bagian serta minimal tiga Mini Project.

# 2. Agenda dan Alokasi Waktu

| Waktu | Sesi | Durasi | Fokus |
|---|---|---|---|
| 00:00 – 00:10 | Setup library | 10 menit | Persiapan |
| 00:10 – 01:40 | Matplotlib & Seaborn + Latihan | 90 menit | Visualisasi |
| 01:40 – 02:25 | API dengan requests + Latihan | 45 menit | API |
| 02:25 – 02:45 | Istirahat | 20 menit | — |
| 02:45 – 03:45 | Web Scraping & arXiv + Latihan | 60 menit | Scraping |
| 03:45 – 05:30 | Pengerjaan Mini Project | 105 menit | Praktik |
| 05:30 – 06:00 | Review dan Showcase | 30 menit | Refleksi |

# 3. Visualisasi Data dengan Matplotlib

## 3.1 Pengenalan

Matplotlib adalah library visualisasi paling fundamental di Python. Kita menggunakan interface pyplot.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use("seaborn-v0_8-whitegrid")
```

**Output:**

```text
(tidak ada output)
```

## 3.2 Line Plot

```python
x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 5))
plt.plot(x, np.sin(x), label="sin(x)", color="blue", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", color="red", linestyle="--")
plt.title("Fungsi Trigonometri"); plt.xlabel("x"); plt.ylabel("f(x)")
plt.legend(); plt.grid(True, alpha=0.3); plt.tight_layout(); plt.show()

bulan = ["Jan","Feb","Mar","Apr","Mei","Jun"]
ani = [75,78,80,82,85,88]; budi = [70,72,75,74,78,80]
plt.figure(figsize=(9, 5))
plt.plot(bulan, ani, marker="o", label="Ani")
plt.plot(bulan, budi, marker="s", label="Budi")
plt.title("Perkembangan Nilai"); plt.legend(); plt.ylim(60,100)
plt.tight_layout(); plt.show()
```

**Output:**

![Grafik hasil blok kode — 1_0.png](images/hari5/1_0.png)

![Grafik hasil blok kode — 1_1.png](images/hari5/1_1.png)

## 3.3 Bar Chart

```python
prodi = ["IF","SI","TI","Manajemen","Akuntansi"]
jumlah = [120,95,80,150,110]
plt.figure(figsize=(9, 5))
bars = plt.bar(prodi, jumlah, color="steelblue", edgecolor="black")
for bar, val in zip(bars, jumlah):
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2, str(val), ha="center")
plt.title("Jumlah Mahasiswa per Prodi"); plt.tight_layout(); plt.show()

labels=["IF","SI","TI"]; uts=[78,72,80]; uas=[85,79,88]
x=np.arange(len(labels)); width=0.35
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x-width/2, uts, width, label="UTS")
ax.bar(x+width/2, uas, width, label="UAS")
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.set_title("UTS vs UAS"); ax.legend(); plt.tight_layout(); plt.show()
```

**Output:**

![Grafik hasil blok kode — 2_0.png](images/hari5/2_0.png)

![Grafik hasil blok kode — 2_1.png](images/hari5/2_1.png)

## 3.4 Scatter, Histogram, Pie

```python
np.random.seed(42)
x=np.random.rand(60)*100; y=0.6*x+np.random.randn(60)*12
plt.figure(figsize=(8,5))
sc=plt.scatter(x,y,c=y,cmap="viridis",alpha=0.8,edgecolors="k")
plt.colorbar(sc,label="Nilai"); plt.title("Scatter Plot"); plt.tight_layout(); plt.show()

nilai=np.random.normal(75,10,250)
plt.figure(figsize=(8,5))
plt.hist(nilai,bins=20,color="steelblue",edgecolor="black",alpha=0.75)
plt.axvline(nilai.mean(),color="red",linestyle="--",label=f"Mean={nilai.mean():.1f}")
plt.axvline(np.median(nilai),color="orange",linestyle=":",label=f"Median={np.median(nilai):.1f}")
plt.legend(); plt.title("Histogram Nilai"); plt.tight_layout(); plt.show()

sizes=[35,25,20,12,8]; labels=["IF","SI","TI","Manajemen","Lainnya"]
plt.figure(figsize=(7,7))
plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90,explode=(0.05,0,0,0,0))
plt.title("Proporsi Mahasiswa"); plt.tight_layout(); plt.show()
```

**Output:**

![Grafik hasil blok kode — 3_0.png](images/hari5/3_0.png)

![Grafik hasil blok kode — 3_1.png](images/hari5/3_1.png)

![Grafik hasil blok kode — 3_2.png](images/hari5/3_2.png)

## 3.5 Subplot dan Menyimpan Gambar

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes[0,0].plot([1,2,3,4],[1,4,9,16],"b-o"); axes[0,0].set_title("Line")
axes[0,1].bar(["A","B","C"],[10,20,15],color="orange"); axes[0,1].set_title("Bar")
axes[1,0].hist(np.random.randn(200),bins=20,color="green",alpha=0.7); axes[1,0].set_title("Hist")
axes[1,1].scatter(np.random.rand(40),np.random.rand(40),c="red",alpha=0.6); axes[1,1].set_title("Scatter")
plt.suptitle("Dashboard 2x2"); plt.tight_layout(); plt.show()

plt.figure(figsize=(8,5)); plt.plot([1,2,3],[10,25,15],marker="o")
plt.savefig("grafik.png",dpi=150,bbox_inches="tight")
plt.savefig("grafik.pdf",bbox_inches="tight"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 4_0.png](images/hari5/4_0.png)

![Grafik hasil blok kode — 4_1.png](images/hari5/4_1.png)

## 3.6 Latihan Matplotlib

1. Buat line plot penjualan produk A dan B selama 6 bulan (marker, legend, judul, grid).
2. Buat bar chart jumlah mahasiswa per angkatan (minimal 5), tampilkan nilai di atas bar.
3. Buat histogram 300 bilangan normal (mean=70, std=8), tampilkan garis mean dan median.
4. Buat subplot 1x3 histogram nilai tiga kelas (sharey=True).
5. Buat pie chart lima kategori pengeluaran, simpan sebagai PNG.

# 4. Visualisasi Statistik dengan Seaborn

## 4.1 Pengenalan

```python
import seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
print(tips.head())
```

**Output:**

```text
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

_Catatan: `load_dataset` mengunduh dataset dari repositori seaborn-data di GitHub (memerlukan internet)._

## 4.2 Distribusi

```python
plt.figure(figsize=(8,5))
sns.histplot(data=tips, x="total_bill", kde=True, bins=20)
plt.title("Distribusi Total Bill"); plt.show()

plt.figure(figsize=(8,5))
sns.histplot(data=tips, x="total_bill", hue="time", kde=True)
plt.title("Total Bill: Lunch vs Dinner"); plt.show()

plt.figure(figsize=(9,5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("Box Plot Total Bill"); plt.show()

plt.figure(figsize=(9,5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 6_0.png](images/hari5/6_0.png)

![Grafik hasil blok kode — 6_1.png](images/hari5/6_1.png)

![Grafik hasil blok kode — 6_2.png](images/hari5/6_2.png)

![Grafik hasil blok kode — 6_3.png](images/hari5/6_3.png)

## 4.3 Relasi

```python
plt.figure(figsize=(8,5))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex")
plt.title("Tip vs Total Bill"); plt.show()

plt.figure(figsize=(8,5))
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Regresi Tip vs Total Bill"); plt.show()

sns.pairplot(tips, hue="sex", corner=True); plt.show()

corr = tips.corr(numeric_only=True)
plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Heatmap Korelasi"); plt.tight_layout(); plt.show()
```

**Output:**

![Grafik hasil blok kode — 7_0.png](images/hari5/7_0.png)

![Grafik hasil blok kode — 7_1.png](images/hari5/7_1.png)

![Grafik hasil blok kode — 7_2.png](images/hari5/7_2.png)

![Grafik hasil blok kode — 7_3.png](images/hari5/7_3.png)

## 4.4 Categorical Plot

```python
plt.figure(figsize=(8,5))
sns.countplot(data=tips, x="day", hue="sex", order=["Thur","Fri","Sat","Sun"])
plt.title("Jumlah Transaksi per Hari"); plt.show()

plt.figure(figsize=(8,5))
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", errorbar="sd",
            order=["Thur","Fri","Sat","Sun"])
plt.title("Rata-rata Total Bill"); plt.show()

plt.figure(figsize=(9,5))
sns.boxplot(data=tips, x="day", y="tip", color="lightblue", showfliers=False,
            order=["Thur","Fri","Sat","Sun"])
sns.stripplot(data=tips, x="day", y="tip", color="darkblue", alpha=0.4, size=3,
              order=["Thur","Fri","Sat","Sun"])
plt.title("Box + Strip: Tip per Hari"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 8_0.png](images/hari5/8_0.png)

![Grafik hasil blok kode — 8_1.png](images/hari5/8_1.png)

![Grafik hasil blok kode — 8_2.png](images/hari5/8_2.png)

## 4.5 Latihan Seaborn

1. Histogram total_bill dataset tips dengan hue="smoker".
2. Box plot tip berdasarkan day + strip plot di atasnya.
3. Heatmap korelasi dataset iris (kolom numerik).
4. Pairplot dataset iris dengan hue="species".
5. Countplot class pada dataset titanic, hue="sex".

# 5. Bekerja dengan API (requests)

## 5.1 Dasar requests

```python
import requests, json
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.headers.get("Content-Type"))
data = response.json(); print(list(data.keys())[:5])

params = {"q": "python", "sort": "stars"}
r = requests.get("https://api.github.com/search/repositories", params=params)
print(r.url, r.status_code)
```

**Output:**

```text
200
application/json; charset=utf-8
[]
https://api.github.com/search/repositories?q=python&sort=stars 403
```

_Catatan: dijalankan langsung ke `api.github.com` dari lingkungan pengujian. Respons permintaan kedua (`/search/repositories`) adalah 403 karena pembatasan akses/rate limit tanpa token; di komputer peserta biasanya 200. Isi `list(data.keys())` kosong pada respons yang diterima di lingkungan ini._

## 5.2 API Publik

```python
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()
for u in users[:3]:
    print(u["name"], "-", u["email"], "-", u["address"]["city"])

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": -6.2088, "longitude": 106.8456,
          "current_weather": True, "timezone": "Asia/Jakarta"}
r = requests.get(url, params=params)
cw = r.json()["current_weather"]
print(f"Suhu Jakarta: {cw['temperature']}°C, Angin: {cw['windspeed']} km/h")

params = {"latitude": -6.2088, "longitude": 106.8456,
          "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
          "timezone": "Asia/Jakarta", "forecast_days": 5}
r = requests.get(url, params=params)
daily = r.json()["daily"]
for i, t in enumerate(daily["time"]):
    print(f"{t}: max {daily['temperature_2m_max'][i]}°C / min {daily['temperature_2m_min'][i]}°C")
```

**Output:**

```text
Leanne Graham - Sincere@april.biz - Gwenborough
Ervin Howell - Shanna@melissa.tv - Wisokyburgh
Clementine Bauch - Nathan@yesenia.net - McKenziehaven
Suhu Jakarta: 31.2°C, Angin: 9.4 km/h
2026-10-01: max 32.1°C / min 24.5°C
2026-10-02: max 31.8°C / min 24.8°C
2026-10-03: max 33.0°C / min 25.0°C
2026-10-04: max 32.5°C / min 24.7°C
2026-10-05: max 31.2°C / min 24.1°C
```

_Catatan: host jsonplaceholder.typicode.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

_Catatan: host api.open-meteo.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

## 5.3 Error Handling dan DataFrame

```python
def ambil_json(url, params=None, timeout=10):
    try:
        resp = requests.get(url, params=params, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Gagal: {e}")
        return None

data = ambil_json("https://jsonplaceholder.typicode.com/users")
if data: print(f"Berhasil: {len(data)} user")

import pandas as pd
df = pd.json_normalize(data)
print(df[["id","name","address.city","company.name"]].head())
df.to_csv("users_api.csv", index=False)
```

**Output:**

```text
Berhasil: 10 user
   id              name   address.city        company.name
0   1     Leanne Graham    Gwenborough     Romaguera-Crona
1   2      Ervin Howell    Wisokyburgh        Deckow-Crist
2   3  Clementine Bauch  McKenziehaven  Romaguera-Jacobson
3   4  Patricia Lebsack    South Elvis       Robel-Corkery
4   5  Chelsey Dietrich     Roscoeview         Keebler LLC
```

_Catatan: host jsonplaceholder.typicode.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

## 5.4 Latihan API

1. Ambil posts dari JSONPlaceholder, tampilkan 5 judul pertama, hitung jumlah post per userId.
2. Ambil cuaca terkini Bandung (koordinat -6.9175, 107.6191).
3. Buat fungsi ambil_json yang aman, uji dengan URL benar dan salah.
4. Ambil users → DataFrame (json_normalize) → bar chart jumlah user per kota.

# 6. Web Scraping dan arXiv API

## 6.1 Etika

> **Etika Scraping**
>
> Periksa robots.txt. Hormati rate limit. Utamakan API resmi (seperti arXiv).
>
> Jangan membebani server — gunakan time.sleep.

## 6.2 BeautifulSoup

```python
from bs4 import BeautifulSoup
r = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(r.text, "html.parser")
for q in soup.find_all("div", class_="quote")[:3]:
    teks = q.find("span", class_="text").get_text()
    penulis = q.find("small", class_="author").get_text()
    print(f"{penulis}: {teks[:55]}...")
```

**Output:**

```text
Albert Einstein: “The world as we have created it is a process of our th...
J.K. Rowling: “It is our choices, Harry, that show what we truly are....
Albert Einstein: “There are only two ways to live your life.”...
```

_Catatan: host quotes.toscrape.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

## 6.3 arXiv API

```python
import feedparser
from urllib.parse import urlencode

def cari_arxiv(keyword, max_results=5):
    base = "http://export.arxiv.org/api/query?"
    params = {"search_query": f"all:{keyword}", "start": 0,
              "max_results": max_results, "sortBy": "submittedDate",
              "sortOrder": "descending"}
    r = requests.get(base + urlencode(params))
    feed = feedparser.parse(r.text)
    records = []
    for e in feed.entries:
        records.append({"judul": e.title.replace("\n"," "),
                        "penulis": ", ".join(a.name for a in e.authors),
                        "published": e.published[:10],
                        "link": e.link})
    return pd.DataFrame(records)

df = cari_arxiv("deep learning education", max_results=5)
print(df[["judul","penulis","published"]])
df.to_csv("arxiv_hasil.csv", index=False)
```

**Output:**

```text
                              judul                 penulis   published
0  Contoh Paper 1  on Deep Learning  Penulis 1A, Penulis 1B  2025-12-15
1  Contoh Paper 2  on Deep Learning  Penulis 2A, Penulis 2B  2025-10-15
2  Contoh Paper 3  on Deep Learning  Penulis 3A, Penulis 3B  2025-08-15
3  Contoh Paper 4  on Deep Learning  Penulis 4A, Penulis 4B  2025-06-15
4  Contoh Paper 5  on Deep Learning  Penulis 5A, Penulis 5B  2024-12-15
```

_Catatan: host export.arxiv.org tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

> **Rate Limit arXiv**
>
> Maksimal 1 request per 3 detik. Dokumentasi: https://info.arxiv.org/help/api/user-manual.html

## 6.4 Latihan Scraping & arXiv

1. Scrape quotes.toscrape.com, tampilkan 5 quote + penulis.
2. Cari 8 paper arXiv kata kunci "python programming education", simpan CSV.
3. Dari hasil arXiv, buat bar chart jumlah paper per tahun.

# 7. Empat Mini Project

## Mini Project 1 — Dashboard Visualisasi Nilai Mahasiswa (Level Dasar)

### Deskripsi

Gunakan data nilai mahasiswa (bisa data dari Hari 4 atau buat data baru). Buat beberapa visualisasi untuk memahami distribusi dan perbandingan nilai.

### Fitur Wajib

1. Histogram distribusi nilai akhir.
2. Bar chart rata-rata nilai per program studi.
3. Pie chart proporsi grade (A/B/C/D/E).
4. Box plot perbandingan nilai antar prodi.
5. Simpan semua grafik sebagai file PNG.

### Skeleton Code

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 1. Siapkan data
df = pd.DataFrame({
    "nama": [...],
    "prodi": [...],
    "nilai_akhir": [...],
    "grade": [...]
})

# 2. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="nilai_akhir", kde=True)
plt.title("Distribusi Nilai Akhir")
plt.savefig("hist_nilai.png", dpi=150, bbox_inches="tight")
plt.show()

# 3. Bar chart rata-rata per prodi
# ...

# 4. Pie chart grade
# ...

# 5. Box plot
# ...
```

> **Output:** _tidak dijalankan_ — skeleton; berisi placeholder `[...]` dan `# ...` yang harus diisi peserta

> **Tips Project 1**
>
> Gunakan subplot 2x2 agar semua grafik berada dalam satu figure.
>
> Pastikan setiap grafik memiliki judul dan label yang jelas.

## Mini Project 2 — Ambil Data API dan Visualisasikan (Level Menengah)

### Deskripsi

Ambil data dari API publik (JSONPlaceholder, Open-Meteo, atau API lain yang tidak memerlukan key), ubah menjadi DataFrame, lalu buat minimal dua visualisasi yang bermakna.

### Fitur Wajib

1. Ambil data dari minimal satu API publik menggunakan requests.
2. Ubah hasil JSON menjadi DataFrame.
3. Lakukan inspeksi data sederhana.
4. Buat minimal 2 visualisasi yang bermakna.
5. Simpan DataFrame ke CSV dan grafik ke PNG.

### Skeleton Code

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ambil data dari API
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# 2. Ke DataFrame
df = pd.json_normalize(data)
print(df.head())
print(df.columns.tolist())

# 3. Inspeksi
# print(df.describe())

# 4. Visualisasi 1 (contoh: jumlah user per kota)
# ...

# 5. Visualisasi 2
# ...

# 6. Simpan
df.to_csv("hasil_api.csv", index=False)
```

**Output:**

```text
   id              name   username                      email phone address.street   address.city  \
0   1     Leanne Graham       Bret          Sincere@april.biz     -              -    Gwenborough   
1   2      Ervin Howell  Antonette          Shanna@melissa.tv     -              -    Wisokyburgh   
2   3  Clementine Bauch   Samantha         Nathan@yesenia.net     -              -  McKenziehaven   
3   4  Patricia Lebsack   Karianne  Julianne.OConner@kory.org     -              -    South Elvis   
4   5  Chelsey Dietrich     Kamren   Lucio_Hettinger@annie.ca     -              -     Roscoeview   

  address.zipcode        company.name  
0               -     Romaguera-Crona  
1               -        Deckow-Crist  
2               -  Romaguera-Jacobson  
3               -       Robel-Corkery  
4               -         Keebler LLC  
['id', 'name', 'username', 'email', 'phone', 'address.street', 'address.city', 'address.zipcode', 'company.name']
```

_Catatan: host jsonplaceholder.typicode.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

> **Tips Project 2**
>
> Gunakan pd.json_normalize() untuk data JSON yang nested.
>
> Pilih kolom yang relevan sebelum membuat visualisasi.

## Mini Project 3 — Pencarian Paper dengan arXiv API (Level Menengah-Tinggi)

### Deskripsi

Buat program yang menerima kata kunci pencarian, mengambil data paper dari arXiv API, menampilkan ringkasan, menyimpan ke CSV, dan memvisualisasikan jumlah paper per tahun.

### Fitur Wajib

1. Fungsi pencarian paper berdasarkan kata kunci menggunakan arXiv API.
2. Tampilkan judul, penulis, tanggal, dan ringkasan singkat.
3. Simpan hasil pencarian ke file CSV.
4. Buat visualisasi jumlah paper berdasarkan tahun publikasi.
5. Hormati rate limit arXiv (maksimal 1 request per 3 detik).

### Skeleton Code

```python
import requests
import feedparser
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlencode

def cari_arxiv(keyword, max_results=15):
    base_url = "http://export.arxiv.org/api/query?"
    params = {
        "search_query": f"all:{keyword}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending"
    }
    url = base_url + urlencode(params)
    response = requests.get(url)
    feed = feedparser.parse(response.text)
    records = []
    for entry in feed.entries:
        records.append({
            "judul": entry.title.replace("\n", " "),
            "penulis": ", ".join(a.name for a in entry.authors),
            "published": entry.published[:10],
            "summary": entry.summary.replace("\n", " ")[:300],
            "link": entry.link
        })
    return pd.DataFrame(records)

# Main
keyword = input("Masukkan kata kunci: ")
df = cari_arxiv(keyword, max_results=15)
print(df[["judul", "penulis", "published"]])
df.to_csv(f"arxiv_{keyword.replace(' ', '_')}.csv", index=False)

# Visualisasi per tahun
df["tahun"] = pd.to_datetime(df["published"]).dt.year
df["tahun"].value_counts().sort_index().plot(kind="bar", color="steelblue")
plt.title(f"Jumlah Paper per Tahun — {keyword}")
plt.xlabel("Tahun"); plt.ylabel("Jumlah")
plt.tight_layout()
plt.savefig("arxiv_per_tahun.png", dpi=150)
plt.show()
```

**Output:**

```text
Masukkan kata kunci: deep learning
                                judul                   penulis   published
0    Contoh Paper 1  on Deep Learning    Penulis 1A, Penulis 1B  2025-12-15
1    Contoh Paper 2  on Deep Learning    Penulis 2A, Penulis 2B  2025-10-15
2    Contoh Paper 3  on Deep Learning    Penulis 3A, Penulis 3B  2025-08-15
3    Contoh Paper 4  on Deep Learning    Penulis 4A, Penulis 4B  2025-06-15
4    Contoh Paper 5  on Deep Learning    Penulis 5A, Penulis 5B  2024-12-15
5    Contoh Paper 6  on Deep Learning    Penulis 6A, Penulis 6B  2024-10-15
6    Contoh Paper 7  on Deep Learning    Penulis 7A, Penulis 7B  2024-08-15
7    Contoh Paper 8  on Deep Learning    Penulis 8A, Penulis 8B  2024-06-15
8    Contoh Paper 9  on Deep Learning    Penulis 9A, Penulis 9B  2023-12-15
9   Contoh Paper 10  on Deep Learning  Penulis 10A, Penulis 10B  2023-10-15
10  Contoh Paper 11  on Deep Learning  Penulis 11A, Penulis 11B  2023-08-15
11  Contoh Paper 12  on Deep Learning  Penulis 12A, Penulis 12B  2023-06-15
12  Contoh Paper 13  on Deep Learning  Penulis 13A, Penulis 13B  2022-12-15
13  Contoh Paper 14  on Deep Learning  Penulis 14A, Penulis 14B  2022-10-15
14  Contoh Paper 15  on Deep Learning  Penulis 15A, Penulis 15B  2022-08-15
```

![Grafik hasil blok kode — 16_0.png](images/hari5/16_0.png)

_Catatan: input simulasi: `deep learning`._

_Catatan: host export.arxiv.org tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

> **Tips Project 3**
>
> Sangat cocok untuk mahasiswa S2/S3 yang membutuhkan literatur.
>
> Jangan lupa time.sleep(3) jika melakukan banyak request.

## Mini Project 4 — Mini EDA + Visualisasi Lengkap (Level Tinggi)

### Deskripsi

Pilih sebuah dataset (hasil API, arXiv, atau dataset publik). Lakukan EDA singkat dan buat minimal empat visualisasi berbeda dalam satu figure (subplot). Tuliskan insight yang diperoleh.

### Fitur Wajib

1. Load dan inspeksi data.
2. Minimal 4 jenis visualisasi berbeda (histogram, bar, scatter, heatmap, box, dll).
3. Gunakan kombinasi Matplotlib dan Seaborn.
4. Tambahkan judul, label, dan legenda yang jelas pada setiap grafik.
5. Simpan figure ke file PNG berkualitas tinggi (dpi >= 150).
6. Tuliskan minimal 3 insight dari visualisasi.

### Skeleton Code

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("data_anda.csv")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Grafik 1
sns.histplot(data=df, x="kolom1", kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Distribusi ...")

# Grafik 2
sns.barplot(data=df, x="kategori", y="nilai", ax=axes[0, 1])
axes[0, 1].set_title("Rata-rata ...")

# Grafik 3
sns.scatterplot(data=df, x="kolom_x", y="kolom_y", hue="kategori", ax=axes[1, 0])
axes[1, 0].set_title("Hubungan ...")

# Grafik 4
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, ax=axes[1, 1], cmap="coolwarm")
axes[1, 1].set_title("Korelasi")

plt.suptitle("EDA Visualisasi — Judul Dataset", fontsize=16)
plt.tight_layout()
plt.savefig("eda_visualisasi.png", dpi=150, bbox_inches="tight")
plt.show()

# Insight:
# 1. ...
# 2. ...
# 3. ...
```

**Output:**

![Grafik hasil blok kode — 17_0.png](images/hari5/17_0.png)

_Catatan: dijalankan dengan `data_anda.csv` contoh (40 baris, kolom `kolom1`, `kategori`, `nilai`, `kolom_x`, `kolom_y`) karena file aslinya milik peserta._

> **Tips Project 4**
>
> Pilih visualisasi yang benar-benar menceritakan sesuatu dari data.
>
> Insight harus didukung oleh apa yang terlihat di grafik.

> **Panduan Pengerjaan Mini Project**
>
> Project 1 dan 2 bersifat wajib.
>
> Project 3 (arXiv) sangat direkomendasikan bagi mahasiswa S2/S3.
>
> Project 4 adalah challenge integrasi skill visualisasi.
>
> Gunakan Jupyter Notebook agar grafik langsung terlihat.

# 8. Solusi Latihan

## 8.1 Solusi Matplotlib

### Soal 1

```python
bulan=["Jan","Feb","Mar","Apr","Mei","Jun"]
a=[120,135,150,140,160,175]; b=[90,100,110,105,125,140]
plt.figure(figsize=(9,5))
plt.plot(bulan,a,marker="o",label="Produk A"); plt.plot(bulan,b,marker="s",label="Produk B")
plt.title("Penjualan A vs B"); plt.legend(); plt.grid(True,alpha=0.3); plt.show()
```

**Output:**

![Grafik hasil blok kode — 18_0.png](images/hari5/18_0.png)

### Soal 2

```python
angkatan=["2019","2020","2021","2022","2023"]; jumlah=[180,210,195,230,250]
plt.figure(figsize=(8,5))
bars=plt.bar(angkatan,jumlah,color="steelblue",edgecolor="black")
for bar,val in zip(bars,jumlah):
    plt.text(bar.get_x()+bar.get_width()/2, bar.get_height()+3, str(val), ha="center")
plt.title("Mahasiswa per Angkatan"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 19_0.png](images/hari5/19_0.png)

### Soal 3

```python
np.random.seed(42); data=np.random.normal(70,8,300)
plt.figure(figsize=(8,5))
plt.hist(data,bins=20,color="steelblue",edgecolor="black",alpha=0.75)
plt.axvline(data.mean(),color="red",linestyle="--",label=f"Mean={data.mean():.1f}")
plt.axvline(np.median(data),color="orange",linestyle=":",label=f"Median={np.median(data):.1f}")
plt.legend(); plt.title("Distribusi Nilai"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 20_0.png](images/hari5/20_0.png)

### Soal 4

```python
fig,axes=plt.subplots(1,3,figsize=(14,4),sharey=True)
for ax,d,n in zip(axes,[np.random.normal(78,7,100),np.random.normal(72,9,100),np.random.normal(80,6,100)],["A","B","C"]):
    ax.hist(d,bins=12,color="steelblue",edgecolor="black",alpha=0.8); ax.set_title(f"Kelas {n}")
plt.suptitle("Distribusi Nilai per Kelas"); plt.tight_layout(); plt.show()
```

**Output:**

![Grafik hasil blok kode — 21_0.png](images/hari5/21_0.png)

### Soal 5

```python
plt.figure(figsize=(7,7))
plt.pie([40,25,15,10,10],labels=["Sewa","Makan","Transport","Hiburan","Lainnya"],
        autopct="%1.1f%%",startangle=90,explode=(0.05,0,0,0,0))
plt.title("Pengeluaran Bulanan"); plt.savefig("pengeluaran.png",dpi=150,bbox_inches="tight"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 22_0.png](images/hari5/22_0.png)

## 8.2 Solusi Seaborn

```python
# Soal 1
sns.histplot(data=tips, x="total_bill", hue="smoker", kde=True, bins=15); plt.show()

# Soal 2
sns.boxplot(data=tips, x="day", y="tip", color="lightblue", showfliers=False, order=["Thur","Fri","Sat","Sun"])
sns.stripplot(data=tips, x="day", y="tip", color="darkblue", alpha=0.4, size=3, order=["Thur","Fri","Sat","Sun"]); plt.show()

# Soal 3
sns.heatmap(iris.corr(numeric_only=True), annot=True, cmap="coolwarm", center=0, fmt=".2f"); plt.show()

# Soal 4
sns.pairplot(iris, hue="species", corner=True); plt.show()

# Soal 5
sns.countplot(data=titanic, x="class", hue="sex"); plt.show()
```

**Output:**

![Grafik hasil blok kode — 23_0.png](images/hari5/23_0.png)

![Grafik hasil blok kode — 23_1.png](images/hari5/23_1.png)

![Grafik hasil blok kode — 23_2.png](images/hari5/23_2.png)

![Grafik hasil blok kode — 23_3.png](images/hari5/23_3.png)

![Grafik hasil blok kode — 23_4.png](images/hari5/23_4.png)

## 8.3 Solusi API

```python
# Soal 1
posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
for p in posts[:5]: print(p["title"])
print(pd.DataFrame(posts).groupby("userId").size())

# Soal 2
params={"latitude":-6.9175,"longitude":107.6191,"current_weather":True,"timezone":"Asia/Jakarta"}
cw=requests.get("https://api.open-meteo.com/v1/forecast",params=params).json()["current_weather"]
print(f"Suhu Bandung: {cw['temperature']}°C, Angin: {cw['windspeed']} km/h")

# Soal 3 & 4 — gunakan fungsi ambil_json + json_normalize + value_counts().plot(kind="bar")
```

**Output:**

```text
judul post contoh 1
judul post contoh 2
judul post contoh 3
judul post contoh 4
judul post contoh 5
userId
1     10
2     10
3     10
4     10
5     10
6     10
7     10
8     10
9     10
10    10
dtype: int64
Suhu Bandung: 31.2°C, Angin: 9.4 km/h
```

_Catatan: host jsonplaceholder.typicode.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

_Catatan: host api.open-meteo.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

## 8.4 Solusi Scraping & arXiv

```python
# Soal 1
soup = BeautifulSoup(requests.get("https://quotes.toscrape.com/").text, "html.parser")
for q in soup.find_all("div", class_="quote")[:5]:
    print(q.find("small", class_="author").get_text(), ":", q.find("span", class_="text").get_text())

# Soal 2 & 3
df = cari_arxiv("python programming education", max_results=8)
df.to_csv("arxiv_python_edu.csv", index=False)
df["tahun"] = pd.to_datetime(df["published"]).dt.year
df["tahun"].value_counts().sort_index().plot(kind="bar")
plt.title("Paper per Tahun"); plt.tight_layout(); plt.savefig("arxiv_tahun.png", dpi=150); plt.show()
```

**Output:**

```text
Albert Einstein : “The world as we have created it is a process of our thinking.”
J.K. Rowling : “It is our choices, Harry, that show what we truly are.”
Albert Einstein : “There are only two ways to live your life.”
Jane Austen : “The person, be it gentleman or lady, who has not pleasure in a good novel.”
Marilyn Monroe : “Imperfection is beauty, madness is genius.”
```

![Grafik hasil blok kode — 25_0.png](images/hari5/25_0.png)

_Catatan: host export.arxiv.org tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

_Catatan: host quotes.toscrape.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

# 9. Troubleshooting

Masalah yang sering muncul saat visualisasi, API, dan scraping:

## Visualisasi (Matplotlib / Seaborn)

```python
%matplotlib inline   # jika grafik tidak muncul di Jupyter
plt.tight_layout()
plt.savefig("gambar.png", dpi=150, bbox_inches="tight")
sns.set_theme(style="whitegrid")  # panggil SEBELUM plot
```

> **Output:** _tidak dijalankan_ — perintah magic Jupyter (`%matplotlib inline`) yang tidak valid di skrip Python biasa; berisi tips, bukan kode untuk dijalankan

## API (requests)

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
print(response.status_code)
print(response.text[:200])
import time; time.sleep(3)  # rate limit arXiv
```

**Output:**

```text
200
```

_Catatan: baris `url = ...` ditambahkan agar snippet dapat dijalankan; `time.sleep(3)` dipersingkat saat pengujian._

_Catatan: host jsonplaceholder.typicode.com tidak dapat diakses dari lingkungan pengujian (kebijakan jaringan), sehingga kode dijalankan dengan respons tiruan yang bentuknya sama dengan API asli. **Nilai/teks pada output ini contoh, bukan data nyata.**_

## Scraping & arXiv

```python
el = soup.find("span", class_="text")
if el:
    print(el.get_text())
# arXiv kosong → cek format query: all:keyword atau ti:keyword
# pip install feedparser
```

**Output:**

```text
“The world as we have created it is a process of our thinking.”
```

_Catatan: memakai variabel `soup` dari blok scraping sebelumnya._

## Tips Debugging

```python
print(response.status_code)
print(response.text[:300])
# Gunakan try-except + data cadangan jika API gagal
```

**Output:**

```text
200
```

_Catatan: memakai variabel `response` dari blok sebelumnya._

# 9b. Troubleshooting Lengkap (Contoh Kasus)

Berikut contoh kasus nyata untuk error dan jebakan yang sering muncul di Hari 5. Setiap kasus dijalankan terpisah. Kasus `requests` dijalankan terhadap server HTTP lokal sederhana (di bawah) agar error yang muncul asli dan dapat diulang tanpa internet.

## Persiapan — server uji lokal

```python
import threading, time, json
from http.server import BaseHTTPRequestHandler, HTTPServer

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_GET(self):
        if self.path == "/ok":
            body, ctype, code = json.dumps({"nama": "Ani"}), "application/json", 200
        elif self.path == "/html":
            body, ctype, code = "<html><body>Halaman, bukan JSON</body></html>", "text/html", 200
        elif self.path == "/cuaca-error":
            body, ctype, code = json.dumps({"error": True, "reason": "Parameter salah"}), "application/json", 200
        elif self.path == "/lambat":
            time.sleep(2); body, ctype, code = "{}", "application/json", 200
        else:
            body, ctype, code = "tidak ada", "text/plain", 404
        self.send_response(code); self.send_header("Content-Type", ctype); self.end_headers()
        self.wfile.write(body.encode())

server = HTTPServer(("127.0.0.1", 8765), H)
threading.Thread(target=server.serve_forever, daemon=True).start()
BASE = "http://127.0.0.1:8765"

import requests
```

_Catatan: server ini hanya untuk latihan troubleshooting; semua kasus `requests` di bawah memakai `BASE` yang sama (`http://127.0.0.1:8765`)._

## Matplotlib — ukuran x dan y tidak sama

```python
# Kasus 1: panjang x dan y berbeda
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [10, 20])

# Kasus 2: solusi — samakan panjang
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [10, 20, 30])
print("OK:", len(plt.gca().lines), "garis")
```

**Output:**

```text
# Kasus 1: panjang x dan y berbeda
  -> ValueError: x and y must have same first dimension, but have shapes (3,) and (2,)
# Kasus 2: solusi — samakan panjang
OK: 1 garis
```

## Seaborn — nama kolom salah

```python
# Kasus 1: kolom "total" tidak ada (seharusnya "total_bill")
import seaborn as sns
tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total")

# Kasus 2: periksa nama kolom lebih dulu
import seaborn as sns
tips = sns.load_dataset("tips")
print(tips.columns.tolist())
sns.histplot(data=tips, x="total_bill")
print("OK")
```

**Output:**

```text
# Kasus 1: kolom "total" tidak ada (seharusnya "total_bill")
  -> ValueError: Could not interpret value `total` for `x`. An entry with this name does not appear in `data`.
# Kasus 2: periksa nama kolom lebih dulu
['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
OK
```

## requests — HTTPError (404) dan `raise_for_status()`

```python
# Kasus 1: tanpa raise_for_status, 404 lolos diam-diam
r = requests.get(BASE + "/tidak-ada")
print(r.status_code, r.text)

# Kasus 2: raise_for_status() melempar HTTPError
r = requests.get(BASE + "/tidak-ada")
r.raise_for_status()
```

**Output:**

```text
# Kasus 1: tanpa raise_for_status, 404 lolos diam-diam
404 tidak ada
# Kasus 2: raise_for_status() melempar HTTPError
  -> requests.exceptions.HTTPError: 404 Client Error: Not Found for url: http://127.0.0.1:8765/tidak-ada
```

## requests — JSONDecodeError saat respons bukan JSON

```python
# Kasus 1: .json() pada halaman HTML
r = requests.get(BASE + "/html")
print(r.status_code, r.headers["Content-Type"])
r.json()

# Kasus 2: cek Content-Type / gunakan try-except
r = requests.get(BASE + "/html")
try:
    data = r.json()
except requests.exceptions.JSONDecodeError:
    data = None
    print("Respons bukan JSON:", r.text[:30])
```

**Output:**

```text
# Kasus 1: .json() pada halaman HTML
200 text/html
  -> requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
# Kasus 2: cek Content-Type / gunakan try-except
Respons bukan JSON: <html><body>Halaman, bukan JSO
```

## requests — Timeout dan ConnectionError

```python
# Kasus 1: server lambat, timeout 0.5 detik
requests.get(BASE + "/lambat", timeout=0.5)

# Kasus 2: server tidak ada (port tertutup)
requests.get("http://127.0.0.1:9/", timeout=2)

# Kasus 3: solusi — tangkap RequestException
try:
    requests.get(BASE + "/lambat", timeout=0.5)
except requests.exceptions.RequestException as e:
    print("Gagal:", type(e).__name__)
```

**Output:**

```text
# Kasus 1: server lambat, timeout 0.5 detik
  -> requests.exceptions.ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=0.5)
# Kasus 2: server tidak ada (port tertutup)
  -> requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=9): Max retries exceeded with url: / (Caused by NewConnectionError("HTTPConnection(host='127.0.0.1', port=9): Failed to establish a new connection: [Errno 111] Connection refused"))
# Kasus 3: solusi — tangkap RequestException
Gagal: ReadTimeout
```

## KeyError — respons API berisi error, bukan data

```python
# Kasus 1: langsung mengakses key tanpa memeriksa
data = requests.get(BASE + "/cuaca-error").json()
print(data["current_weather"])

# Kasus 2: solusi — gunakan .get() / cek key error
data = requests.get(BASE + "/cuaca-error").json()
if data.get("error"):
    print("API error:", data["reason"])
else:
    print(data["current_weather"])
```

**Output:**

```text
# Kasus 1: langsung mengakses key tanpa memeriksa
  -> KeyError: 'current_weather'
# Kasus 2: solusi — gunakan .get() / cek key error
API error: Parameter salah
```

## BeautifulSoup — AttributeError karena elemen tidak ditemukan

```python
# Kasus 1: find() mengembalikan None
from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><span class='judul'>Halo</span></div>", "html.parser")
print(soup.find("span", class_="text").get_text())

# Kasus 2: solusi — periksa None dulu
from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><span class='judul'>Halo</span></div>", "html.parser")
el = soup.find("span", class_="text")
print(el.get_text() if el else "Elemen tidak ditemukan")
```

**Output:**

```text
# Kasus 1: find() mengembalikan None
  -> AttributeError: 'NoneType' object has no attribute 'get_text'
# Kasus 2: solusi — periksa None dulu
Elemen tidak ditemukan
```

## feedparser/arXiv — hasil kosong menyebabkan KeyError

```python
# Kasus 1: tidak ada entry (mis. format query salah)
import feedparser, pandas as pd
feed = feedparser.parse('<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"></feed>')
df = pd.DataFrame([{"judul": e.title} for e in feed.entries])
print(df.shape)
print(df["judul"])

# Kasus 2: solusi — cek df.empty sebelum diproses
import feedparser, pandas as pd
feed = feedparser.parse('<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"></feed>')
df = pd.DataFrame([{"judul": e.title} for e in feed.entries])
if df.empty:
    print("Tidak ada hasil — cek query: all:keyword atau ti:keyword")
```

**Output:**

```text
# Kasus 1: tidak ada entry (mis. format query salah)
(0, 0)
  -> KeyError: 'judul'
# Kasus 2: solusi — cek df.empty sebelum diproses
Tidak ada hasil — cek query: all:keyword atau ti:keyword
```

> **Materi Hari 5 Selesai**
>
> Format Mini Project sudah konsisten  •  Latihan + Solusi lengkap  •  Siap ke Hari 6
