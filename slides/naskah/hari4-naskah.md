# Naskah Video — Hari 4: NumPy & Pandas

Deck: [`hari4-numpy-pandas.html`](../hari4-numpy-pandas.html) · 26 slide · 104 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 12 mnt 47 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | NumPy & Pandas | 0 | 15 dtk |
| 2 | Agenda | 8 | 30 dtk |
| 3 | Tujuan | 6 | 29 dtk |
| 4 | A. NumPy | 0 | 5 dtk |
| 5 | List vs array | 5 | 33 dtk |
| 6 | Slicing | 5 | 49 dtk |
| 7 | Masking | 5 | 39 dtk |
| 8 | Axis & broadcasting | 4 | 43 dtk |
| 9 | Latihan: L1, L2, L3, L4, L5, L6, L7, L8, L9 | 0 | 22 dtk |
| 10 | Rehat | 0 | 11 dtk |
| 11 | B. Pandas — Series & DataFrame | 0 | 6 dtk |
| 12 | DataFrame | 11 | 52 dtk |
| 13 | Seleksi | 9 | 54 dtk |
| 14 | Kolom baru | 5 | 33 dtk |
| 15 | Latihan: L10, L11, L12, L13, L14 | 0 | 22 dtk |
| 16 | C. Cleaning & Operasi Lanjutan | 0 | 8 dtk |
| 17 | Missing & duplikat | 7 | 46 dtk |
| 18 | groupby | 5 | 33 dtk |
| 19 | merge | 7 | 50 dtk |
| 20 | pivot_table | 5 | 29 dtk |
| 21 | Latihan: L15, L16, L17, L18, L19 | 0 | 22 dtk |
| 22 | D. Mini Project | 0 | 6 dtk |
| 23 | Pipeline | 9 | 36 dtk |
| 24 | Latihan: P1, P3, P4 | 0 | 23 dtk |
| 25 | Jebakan umum | 7 | 38 dtk |
| 26 | Rekap | 6 | 33 dtk |

---

### Slide 1 — NumPy & Pandas

*judul · transisi `zoom` · 0 klik · ⏱ 15 dtk*

**Saat slide muncul**

> Selamat datang di hari keempat: NumPy dan Pandas. Mulai hari ini kita beralih dari menulis program ke mengolah data: array untuk komputasi cepat, dan DataFrame untuk data berbentuk tabel.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 8 klik · ⏱ 30 dtk*

**Saat slide muncul**

> Agenda hari keempat, sekitar enam jam.

**Klik 1 →** — muncul: `Opening`

> Pembukaan dua puluh menit.

**Klik 2 →** — muncul: `NumPy`

> NumPy, sembilan puluh menit.

**Klik 3 →** — muncul: `Rehat`

> Istirahat dua puluh menit.

**Klik 4 →** — muncul: `Pandas dasar`

> Pandas dasar, tujuh puluh menit.

**Klik 5 →** — muncul: `Cleaning & operasi`

> Cleaning dan operasi lanjutan, tujuh puluh menit.

**Klik 6 →** — muncul: `Mini project`

> Mini project, tujuh puluh menit.

**Klik 7 →** — muncul: `Rekap`

> Dan rekap dua puluh menit.

**Klik 8 →** — muncul: `Total ±6 jam. Demo singkat → peserta coba di buku kerja.`

> Seperti biasa, demo singkat lalu latihan di buku kerja.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 6 klik · ⏱ 29 dtk*

**Saat slide muncul**

> Setelah hari ini, Anda akan bisa melakukan enam hal.

**Klik 1 →** — muncul: `membuat & mengiris array NumPy, boolean masking, broadcasting`

> Membuat dan mengiris array NumPy, memakai boolean masking, dan broadcasting.

**Klik 2 →** — muncul: `menghitung statistik (mean, std, korelasi) dengan axis`

> Menghitung statistik seperti mean, standar deviasi, dan korelasi dengan axis.

**Klik 3 →** — muncul: `membuat Series & DataFrame; seleksi dengan [], loc, iloc`

> Membuat Series dan DataFrame, dan memilih data dengan kurung siku, loc, dan iloc.

**Klik 4 →** — muncul: `membersihkan data: missing values, duplikat, tipe data`

> Membersihkan data: nilai kosong, duplikat, dan tipe data.

**Klik 5 →** — muncul: `meringkas data: groupby, merge, pivot_table`

> Meringkas data dengan groupby, merge, dan pivot table.

**Klik 6 →** — muncul: `membuat laporan akhir dari dataset kotor`

> Dan membuat laporan akhir dari dataset yang kotor.

---

### Slide 4 — A. NumPy

*bagian · transisi `rise` · 0 klik · ⏱ 5 dtk*

**Saat slide muncul**

> Bagian A: NumPy. Array, indexing, masking, dan broadcasting.

---

### Slide 5 — List vs array

*isi · transisi `slide` · 5 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Kenapa memakai array, bukan list biasa? Mari bandingkan.

**Klik 1 →** — muncul: `list_a = [1, 2, 3]`

> Kita punya list berisi satu, dua, tiga, dan array NumPy dengan isi yang sama.

**Klik 2 →** — muncul: `print(list_a * 2)`

> List dikali dua menggandakan list menjadi enam elemen.

**Klik 3 →** — muncul: `print(arr * 2)`

> Array dikali dua mengalikan setiap elemennya: dua, empat, enam. Inilah operasi vectorized.

**Klik 4 →** — muncul: `print(arr.dtype, arr.shape)`

> Array punya tipe dan bentuk: int64 dan bentuk tiga koma kosong, artinya satu dimensi dengan tiga elemen.

**Klik 5 →** — muncul: `Operasi array berlaku untuk seluruh elemen sekaligus (vectorized) — le`

> Intinya, operasi array berlaku untuk seluruh elemen sekaligus: lebih ringkas, dan jauh lebih cepat untuk data besar.

---

### Slide 6 — Slicing

*isi · transisi `slide` · 5 klik · ⏱ 49 dtk*

**Saat slide muncul**

> Indexing dan slicing array dua dimensi. Di sini ada array tiga baris empat kolom berisi angka nol sampai sebelas.

**Klik 1 →**

> Formatnya array kurung siku baris koma kolom. Indeks dimulai dari nol, baik baris maupun kolom.

**Klik 2 →** — muncul: `print(arr[1, 2])`

> arr satu koma dua mengambil baris satu, kolom dua, yaitu angka enam. Kotak oranye pada tabel.

**Klik 3 →** — muncul: `print(arr[:, 1])`

> Titik dua berarti semua. arr titik dua koma satu mengambil semua baris pada kolom satu: satu, lima, sembilan. Kolom biru pada tabel.

**Klik 4 →** — muncul: `[[1 2]`

> Dan irisan nol titik dua dua koma satu titik dua tiga mengambil baris nol dan satu, kolom satu dan dua. Empat sel hijau pada tabel.

**Klik 5 →** — muncul: `[5 6]]`

> Hasilnya matriks dua kali dua: satu, dua, lima, enam.

---

### Slide 7 — Masking

*isi · transisi `slide` · 5 klik · ⏱ 39 dtk*

**Saat slide muncul**

> Boolean masking memilih data berdasarkan kondisi. Kita punya lima nilai.

**Klik 1 →** — muncul: `lulus = nilai >= 60`

> Pertama, kita buat mask: nilai lebih dari atau sama dengan enam puluh. Di kanan, setiap elemen dicek oleh syarat itu.

**Klik 2 →** — muncul: `print(lulus)`

> Mask berisi True atau False untuk setiap elemen. Lima puluh lima dan empat puluh lima ditolak, ditandai coret.

**Klik 3 →** — muncul: `print(nilai[lulus])`

> Dengan nilai kurung siku mask, kita ambil elemen yang True saja: delapan puluh, sembilan puluh, tujuh puluh.

**Klik 4 →** — muncul: `['remedi' 'lulus' 'remedi' 'lulus' 'lulus']`

> np.where adalah if else untuk seluruh array: lolos diberi lulus, sisanya remedi.

**Klik 5 →** — muncul: `70`

> Hasil akhirnya satu array label: remedi, lulus, remedi, lulus, lulus.

---

### Slide 8 — Axis & broadcasting

*isi · transisi `slide` · 4 klik · ⏱ 43 dtk*

**Saat slide muncul**

> Agregasi dengan axis dan broadcasting. Kita punya matriks dua baris tiga kolom.

**Klik 1 →** — muncul: `print(m.sum(axis=0))`

> Axis sama dengan nol menjumlah turun per kolom: lima, tujuh, sembilan. Semua kolom menyala biru.

**Klik 2 →** — muncul: `print(m.mean(axis=1))`

> Axis sama dengan satu menghitung menyamping per baris. Mean baris pertama dua, baris kedua lima.

**Klik 3 →** — muncul: `[[11 22 33]`

> Broadcasting: kita tambahkan vektor sepuluh, dua puluh, tiga puluh ke matriks. NumPy menariknya ke kedua baris.

**Klik 4 →** — muncul: `[14 25 36]]`

> Hasilnya sebelas, dua puluh dua, tiga puluh tiga di baris pertama, dan empat belas, dua puluh lima, tiga puluh enam di baris kedua. Ingat: axis nol turun per kolom, axis satu menyamping per baris.

---

### Slide 9 — Latihan: L1, L2, L3, L4, L5, L6, L7, L8, L9

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 4, bagian A, dan kerjakan latihan L1 sampai L9. Waktunya 35 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari4-numpy-pandas.ipynb dan jalankan timer 35 menit (tekan Mulai).

---

### Slide 10 — Rehat

*isi · transisi `slide` · 0 klik · ⏱ 11 dtk*

**Saat slide muncul**

> Waktunya istirahat sekitar 20 menit. Setelah ini kita lanjut ke Pandas.

🎬 **Aksi:** Jeda video; tampilkan timer istirahat.

---

### Slide 11 — B. Pandas — Series & DataFrame

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian B: Pandas, Series dan DataFrame. Tabel data dengan label.

---

### Slide 12 — DataFrame

*isi · transisi `slide` · 11 klik · ⏱ 52 dtk*

**Saat slide muncul**

> DataFrame adalah tabel di Python: setiap kolom adalah Series, dan setiap baris punya indeks.

**Klik 1 →** — muncul: `df = pd.DataFrame({`

> Kita buat DataFrame dari dictionary berisi nama, prodi, dan ipk untuk empat mahasiswa.

**Klik 2 →** — muncul: `print(df.shape)`

> Lalu kita print DataFrame-nya. Header tabel muncul lebih dulu: nama, prodi, ipk.

**Klik 3 →** — muncul: `print(df.dtypes)`

> Baris nol: Ani, IF, tiga koma lima.

**Klik 4 →** — muncul: `1 Budi SI 3.9`

> Baris satu: Budi, SI, tiga koma sembilan.

**Klik 5 →** — muncul: `2 Cici IF 3.2`

> Baris dua: Cici, IF, tiga koma dua.

**Klik 6 →** — muncul: `3 Dedi SI 3.6`

> Baris tiga: Dedi, SI, tiga koma enam.

**Klik 7 →** — muncul: `(4, 3)`

> Atribut shape memberi ukuran tabel: empat baris dan tiga kolom.

**Klik 8 →** — muncul: `nama str`

> Atribut dtypes menampilkan tipe tiap kolom. Kolom nama bertipe str.

**Klik 9 →** — muncul: `prodi str`

> Kolom prodi juga str.

**Klik 10 →** — muncul: `ipk float64`

> Dan kolom ipk bertipe float enam puluh empat.

**Klik 11 →** — muncul: `dtype: object`

> Catatan: pada pandas versi tiga, kolom teks bertipe str, bukan object seperti di versi lama.

---

### Slide 13 — Seleksi

*isi · transisi `slide` · 9 klik · ⏱ 54 dtk*

**Saat slide muncul**

> Memilih data dari DataFrame. Ada empat cara yang perlu dikuasai.

**Klik 1 →** — muncul: `df["ipk"].mean()`

> Pertama, memilih satu kolom dan menghitung statistiknya: rata-rata ipk adalah tiga koma lima lima.

**Klik 2 →** — muncul: `df.loc[1, "nama"]`

> Kedua, loc memilih berdasarkan label: baris satu, kolom nama, hasilnya Budi.

**Klik 3 →** — muncul: `prodi ipk`

> Ketiga, iloc memilih berdasarkan posisi. iloc nol titik dua dua koma satu titik dua tiga mengambil dua baris pertama dan kolom prodi serta ipk.

**Klik 4 →** — muncul: `df[df["ipk"] >= 3.5]`

> Header hasil iloc muncul: prodi dan ipk.

**Klik 5 →** — muncul: `1 SI 3.9`

> Baris nol: IF dan tiga koma lima.

**Klik 6 →** — muncul: `nama prodi ipk`

> Baris satu: SI dan tiga koma sembilan. Itulah hasil iloc.

**Klik 7 →** — muncul: `0 Ani IF 3.5`

> Keempat, filter dengan kondisi: df kurung siku ipk lebih dari atau sama dengan tiga koma lima. Hasilnya tiga baris.

**Klik 8 →** — muncul: `1 Budi SI 3.9`

> Ani dengan IF dan tiga koma lima, lolos.

**Klik 9 →** — muncul: `3 Dedi SI 3.6`

> Dan Budi serta Dedi juga lolos. Cici tidak, karena ipk-nya tiga koma dua.

---

### Slide 14 — Kolom baru

*isi · transisi `slide` · 5 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Sekarang kita tambah kolom baru, lalu mengurutkan.

**Klik 1 →**

> Kolom status dibuat dengan apply dan lambda: cumlaude bila ipk tiga koma lima atau lebih, selain itu reguler.

**Klik 2 →** — muncul: `nama ipk status`

> Lalu sort values dengan ascending False mengurutkan dari ipk terbesar, dan head tiga mengambil tiga teratas.

**Klik 3 →** — muncul: `1 Budi 3.9 cumlaude`

> Hasilnya tiga baris dengan kolom nama, ipk, dan status. Pertama Budi, tiga koma sembilan, cumlaude.

**Klik 4 →** — muncul: `3 Dedi 3.6 cumlaude`

> Kedua Dedi, tiga koma enam, cumlaude.

**Klik 5 →** — muncul: `0 Ani 3.5 cumlaude`

> Dan ketiga Ani, tiga koma lima, cumlaude.

---

### Slide 15 — Latihan: L10, L11, L12, L13, L14

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 4, bagian B, dan kerjakan latihan L10 sampai L14. Waktunya 30 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari4-numpy-pandas.ipynb dan jalankan timer 30 menit (tekan Mulai).

---

### Slide 16 — C. Cleaning & Operasi Lanjutan

*bagian · transisi `rise` · 0 klik · ⏱ 8 dtk*

**Saat slide muncul**

> Bagian C: cleaning dan operasi lanjutan. Menangani missing values, groupby, merge, dan pivot.

---

### Slide 17 — Missing & duplikat

*isi · transisi `slide` · 7 klik · ⏱ 46 dtk*

**Saat slide muncul**

> Data nyata hampir selalu kotor. Contoh ini punya nilai kosong dan baris duplikat.

**Klik 1 →** — muncul: `nama 0`

> Tabel menunjukkan empat baris: Budi muncul dua kali, dan nilainya kosong atau NaN.

**Klik 2 →** — muncul: `print(df.isna().sum())`

> Kita hitung nilai kosong per kolom dengan isna dan sum. Kolom nama nol kosong.

**Klik 3 →** — muncul: `df = df.drop_duplicates()`

> Kolom nilai punya dua yang kosong.

**Klik 4 →** — muncul: `print(df)`

> Lalu drop duplicates menghapus baris duplikat, dan fillna mengisi yang kosong dengan rata-rata, yaitu tujuh puluh lima. Pada tabel, sel Budi berubah menjadi tujuh puluh lima.

**Klik 5 →** — muncul: `0 Ani 80.0`

> Kita print hasil akhirnya. Header tabel: nama dan nilai.

**Klik 6 →** — muncul: `1 Budi 75.0`

> Ani delapan puluh. Budi tujuh puluh lima, hasil pengisian.

**Klik 7 →** — muncul: `3 Cici 70.0`

> Dan Cici tujuh puluh. Dua baris duplikat sudah menjadi satu.

---

### Slide 18 — groupby

*isi · transisi `slide` · 5 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Groupby menjawab pertanyaan seperti: berapa rata-rata ipk per prodi. Polanya split, apply, combine.

**Klik 1 →** — muncul: `df.groupby("prodi")["ipk"] .agg(["mean", "count"])`

> Kode: groupby prodi, ambil kolom ipk, hitung mean dan count.

**Klik 2 →** — muncul: `mean count`

> Grafik di kanan memvisualisasikan hasilnya: IF dan SI sebagai dua batang, dan angka rata-rata di atasnya.

**Klik 3 →** — muncul: `prodi`

> Prosesnya tiga tahap: pisahkan data per prodi, hitung di tiap kelompok, lalu gabungkan hasilnya.

**Klik 4 →** — muncul: `IF 3.35 2`

> IF rata-ratanya tiga koma tiga lima dari dua mahasiswa.

**Klik 5 →** — muncul: `SI 3.75 2`

> SI rata-ratanya tiga koma tujuh lima dari dua mahasiswa.

---

### Slide 19 — merge

*isi · transisi `slide` · 7 klik · ⏱ 50 dtk*

**Saat slide muncul**

> Merge menggabungkan dua tabel lewat kolom kunci, seperti join di database.

**Klik 1 →** — muncul: `nim`

> Kita punya tabel mhs dan tabel nilai. Kolom kuncinya nim, ditandai.

**Klik 2 →** — muncul: `1Ani`

> Nim satu dan dua ada di kedua tabel, ditandai hijau. Nim tiga hanya ada di mhs, dan nim empat hanya ada di nilai, jadi redup.

**Klik 3 →** — muncul: `⋈`

> Hasil gabungan dengan how sama dengan left: semua baris mhs dipertahankan, Cici tidak punya pasangan, sehingga skornya NaN.

**Klik 4 →** — muncul: `nim nama skor`

> Ingat: how left mempertahankan semua baris kiri. Dan tipe kolom kunci harus sama di kedua tabel.

**Klik 5 →** — muncul: `0 1 Ani 90.0`

> Kode hasilnya menampilkan header nim, nama, skor.

**Klik 6 →** — muncul: `1 2 Budi 80.0`

> Baris pertama: Ani dengan skor sembilan puluh. Baris kedua: Budi dengan delapan puluh.

**Klik 7 →** — muncul: `2 3 Cici NaN`

> Baris ketiga: Cici dengan NaN.

---

### Slide 20 — pivot_table

*isi · transisi `slide` · 5 klik · ⏱ 29 dtk*

**Saat slide muncul**

> Pivot table meringkas data dua dimensi.

**Klik 1 →** — muncul: `df.pivot_table(index="prodi", columns="angkatan", values="ipk", aggfun`

> Baris adalah prodi, kolom adalah angkatan, dan isinya rata-rata ipk.

**Klik 2 →** — muncul: `angkatan 2023 2024`

> Hasilnya tabel dengan kolom angkatan dua ribu dua puluh tiga dan dua ribu dua puluh empat.

**Klik 3 →** — muncul: `prodi`

> Indeks barisnya prodi.

**Klik 4 →** — muncul: `IF 3.5 3.2`

> IF: tiga koma lima untuk angkatan dua puluh tiga, tiga koma dua untuk angkatan dua puluh empat.

**Klik 5 →** — muncul: `SI 3.9 3.6`

> SI: tiga koma sembilan dan tiga koma enam.

---

### Slide 21 — Latihan: L15, L16, L17, L18, L19

*latihan · transisi `zoom` · 0 klik · ⏱ 22 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 4, bagian C, dan kerjakan latihan L15 sampai L19. Waktunya 30 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari4-numpy-pandas.ipynb dan jalankan timer 30 menit (tekan Mulai).

---

### Slide 22 — D. Mini Project

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian D: mini project. Dari data kotor ke laporan.

---

### Slide 23 — Pipeline

*isi · transisi `slide` · 9 klik · ⏱ 36 dtk*

**Saat slide muncul**

> Semua proyek hari ini mengikuti satu pipeline analisis data.

**Klik 1 →**

> Pertama, load: baca data dengan read csv.

**Klik 2 →**

> Kedua, cleaning: tangani NaN dan ubah tipe data.

**Klik 3 →**

> Ketiga, merge: gabungkan tabel yang berbeda.

**Klik 4 →**

> Keempat, analisis: groupby dan pivot.

**Klik 5 →**

> Kelima, laporan: simpan hasilnya dengan to csv.

**Klik 6 →** — muncul: `P1 Kalkulator nilai akhir (dasar)`

> Kita punya tiga proyek. P1, kalkulator nilai akhir, tingkat dasar.

**Klik 7 →** — muncul: `P3 Merge multi-tabel`

> P3, merge multi-tabel.

**Klik 8 →** — muncul: `P4 Pivot & reporting`

> Dan P4, pivot dan reporting.

**Klik 9 →** — muncul: `Pola yang sama dipakai lagi di Capstone (Hari 6).`

> Pola pipeline ini akan dipakai lagi di Capstone pada Hari 6.

---

### Slide 24 — Latihan: P1, P3, P4

*latihan · transisi `zoom` · 0 klik · ⏱ 23 dtk*

**Saat slide muncul**

> Sekarang giliran Anda. Buka buku kerja Hari 4, bagian D, dan kerjakan project P1, P3, dan P4. Waktunya 50 menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video. Tampilkan notebook workbook/hari4-numpy-pandas.ipynb dan jalankan timer 50 menit (tekan Mulai).

---

### Slide 25 — Jebakan umum

*isi · transisi `slide` · 7 klik · ⏱ 38 dtk*

**Saat slide muncul**

> Tiga jebakan yang paling sering di NumPy dan Pandas.

**Klik 1 →** — muncul: `df["Nama"]`

> Pertama, nama kolom salah ketik, misalnya Nama huruf besar padahal kolomnya nama huruf kecil.

**Klik 2 →** — muncul: `KeyError: 'Nama'`

> Hasilnya KeyError. Cek nama kolom dan spasi tersembunyi.

**Klik 3 →** — muncul: `df[a > 1 and a < 9]`

> Kedua, memakai and pada filter DataFrame.

**Klik 4 →** — muncul: `ValueError: The truth value of a Series is ambiguous. Use a.empty, a.b`

> Hasilnya ValueError: nilai kebenaran sebuah Series ambigu. Gunakan tanda dan komersial dengan kurung.

**Klik 5 →** — muncul: `shape (2,3) + (2,)`

> Ketiga, menjumlahkan array dengan bentuk yang tidak cocok.

**Klik 6 →** — muncul: `ValueError: operands could not be broadcast together with shapes (2,3)`

> Hasilnya ValueError: operand tidak bisa di-broadcast bersama.

**Klik 7 →** — muncul: `Perbaikan: df["x"].str.strip() untuk nama kolom · (a > 1) & (a < 9) · `

> Perbaikannya: bersihkan nama kolom dengan str strip, pakai tanda dan komersial dengan kurung, dan samakan bentuk dengan reshape.

---

### Slide 26 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Rekap Hari 4.

**Klik 1 →** — muncul: `NumPy: array, slicing, masking, np.where, axis, broadcasting`

> NumPy: array, slicing, masking, np.where, axis, dan broadcasting.

**Klik 2 →** — muncul: `Pandas: Series/DataFrame, loc/iloc, filter, kolom baru, sort`

> Pandas: Series dan DataFrame, loc dan iloc, filter, kolom baru, dan sort.

**Klik 3 →** — muncul: `Cleaning: missing values, duplikat, to_numeric`

> Cleaning: missing values, duplikat, dan konversi tipe dengan to numeric.

**Klik 4 →** — muncul: `Ringkasan: groupby, merge, pivot_table`

> Ringkasan data: groupby, merge, dan pivot table.

**Klik 5 →** — muncul: `Mini project pipeline data end-to-end`

> Mini project pipeline data dari awal sampai akhir.

**Klik 6 →** — muncul: `Besok (Hari 5): Visualisasi, API & Scraping`

> Jalankan sel Rekap hasil latihan. Besok, Hari 5: Visualisasi, API, dan Scraping. Sampai jumpa!

🎬 **Aksi:** Tampilkan sel rekap di notebook.

---
