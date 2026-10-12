# Modul 0 — Persiapan Lingkungan

_Python, terminal, virtual environment (venv), pip, dan Jupyter · Estimasi: ± 75 menit · Wajib sebelum Modul 1_

> **Catatan:** perintah pada modul ini berlaku untuk Windows, macOS, dan Linux; perbedaan antarsistem ditandai jelas. Bagian **Contoh output** diambil dari Linux dan nomor versinya dapat berbeda di komputer Anda.

# 1. Apa yang Akan Anda Siapkan

Setelah modul ini selesai, Anda memiliki:

- Python 3.11 atau lebih baru yang terpasang dan dikenali terminal.
- Folder proyek `bootcamp/` dengan virtual environment `.venv`.
- Paket yang dibutuhkan (pandas, numpy, matplotlib, dst.) di dalam venv.
- Jupyter Notebook yang berjalan dari venv tersebut.
- Buku kerja Hari 1 yang bisa dibuka dan dijalankan.

> [!TIP]
> **Aturan emas**
>
> Setiap bagian diakhiri **cek**. Jangan lanjut sebelum cek berhasil — masalah lingkungan yang dibiarkan akan menumpuk dan membuat bagian berikutnya membingungkan.

# 2. Python

## 2.1 Cek: apakah Python sudah ada?

Buka terminal lalu ketik:

```bash
# Windows
py --version
python --version

# macOS / Linux
python3 --version
```

**Contoh output:**

```text
Python 3.11.9
```

Yang dicari adalah **Python 3.11** atau lebih baru (3.12 dan 3.13 juga baik). Jika muncul pesan *not recognized* (Windows) atau *command not found* (macOS/Linux), Python belum terpasang atau belum masuk **PATH**.

## 2.2 Instal Python

| Sistem | Langkah |
|---|---|
| Windows | Unduh installer dari python.org/downloads, jalankan, **centang "Add python.exe to PATH"**, pilih *Install Now*. |
| macOS | Unduh installer dari python.org/downloads, atau gunakan Homebrew: `brew install python`. |
| Linux (Debian/Ubuntu) | `sudo apt install python3 python3-venv python3-pip` |
| Linux (Fedora) | `sudo dnf install python3` |

Setelah instal, **tutup dan buka kembali terminal**, lalu ulangi perintah cek versi.

> [!WARNING]
> **Kotak "Add python.exe to PATH"** pada installer Windows adalah sumber masalah nomor satu. Jika terlewat, jalankan ulang installer, pilih *Modify*, lalu centang opsi PATH.

## 2.3 Jebakan: Python terpasang tapi tidak ketemu

| Gejala | Penyebab | Solusi |
|---|---|---|
| Windows: `python` tidak dikenali | belum centang *Add to PATH* | pakai `py` (Python launcher) atau jalankan ulang installer → *Modify* → centang PATH |
| Windows membuka Microsoft Store | alias bawaan Windows | instal dari python.org; matikan alias di *Manage app execution aliases* |
| macOS/Linux: `python` tidak ada | hanya tersedia `python3` | pakai `python3` (di dalam venv, `python` otomatis ada) |
| Versi lama (mis. 3.8) | beberapa Python terpasang | panggil versi baru secara eksplisit: `python3.11` atau `py -3.11` |

# 3. Terminal Dasar

## 3.1 Perintah yang dipakai

| Tujuan | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Di folder mana saya? | `pwd` atau `cd` | `pwd` |
| Lihat isi folder | `dir` atau `ls` | `ls` |
| Buat folder | `mkdir bootcamp` | `mkdir bootcamp` |
| Masuk folder | `cd bootcamp` | `cd bootcamp` |
| Naik satu level | `cd ..` | `cd ..` |

Terminal Windows yang disarankan: **PowerShell** atau aplikasi **Terminal** (Windows 11). Di VS Code: menu *Terminal → New Terminal*.

## 3.2 Buat folder proyek

```bash
mkdir bootcamp
cd bootcamp
pwd
```

**Contoh output:**

```text
/home/user/bootcamp
```

Semua langkah berikutnya dijalankan **di dalam folder ini**.

# 4. Virtual Environment (venv)

## 4.1 Mengapa perlu venv?

Satu komputer sering dipakai untuk banyak proyek, dan tiap proyek bisa membutuhkan versi paket yang berbeda (misalnya pandas 2.2 untuk proyek lama dan pandas 3.0 untuk proyek baru). Tanpa isolasi, memperbarui satu paket untuk proyek A bisa merusak proyek B.

**Virtual environment** adalah folder berisi salinan Python dan paket khusus untuk satu proyek. Python sistem tidak disentuh; proyek mudah dihapus dan diulang di komputer lain.

## 4.2 Membuat dan mengaktifkan venv

**Langkah 1 — buat (sekali saja per proyek):**

```bash
python -m venv .venv      # macOS/Linux: python3 -m venv .venv
```

**Langkah 2 — aktifkan (setiap membuka terminal baru):**

| Terminal | Perintah |
|---|---|
| Windows PowerShell | `.venv\Scripts\Activate.ps1` |
| Windows CMD | `.venv\Scripts\activate.bat` |
| macOS / Linux | `source .venv/bin/activate` |

Berhasil bila prompt berawalan `(.venv)`, misalnya:

```text
(.venv) PS C:\bootcamp>
(.venv) user@pc:~/bootcamp$
```

## 4.3 Jebakan Windows: skrip dinonaktifkan

Di PowerShell, aktivasi bisa gagal dengan pesan berikut:

```text
Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```

Solusi (pilih salah satu):

```powershell
# A. izinkan skrip lokal untuk akun Anda (cukup sekali)
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# B. atau pakai CMD
.venv\Scripts\activate.bat
```

## 4.4 Cek venv sudah aktif

```bash
python -c "import sys; print(sys.prefix)"
python -m pip --version
deactivate
```

**Contoh output:**

```text
/home/user/bootcamp/.venv
pip 24.0 from /home/user/bootcamp/.venv/lib/python3.11/site-packages/pip (python 3.11)
```

Baris pertama harus menunjuk ke folder `.venv` di dalam `bootcamp`. `deactivate` keluar dari venv; aktifkan lagi sebelum melanjutkan.

# 5. pip dan Paket

## 5.1 Perintah dasar

```bash
python -m pip install --upgrade pip
pip install pandas
pip list
pip freeze > requirements.txt
```

> [!WARNING]
> Pastikan `(.venv)` aktif sebelum `pip install`. Jika `pip` tidak dikenali, gunakan `python -m pip` — perintah ini selalu memakai Python yang sedang aktif.

- `pip list` menampilkan paket di venv ini saja.
- `pip freeze > requirements.txt` menyimpan daftar paket beserta versinya.

## 5.2 Satu perintah untuk semua kebutuhan bootcamp

File `requirements.txt` ada di paket belajar yang Anda terima (folder `Belajar-Pemrograman-Python`) dan berisi:

```text
notebook
numpy
pandas
matplotlib
seaborn
scipy
openpyxl
requests
beautifulsoup4
feedparser
```

Pasang semuanya sekaligus setelah paket diekstrak (lihat bagian 7); perintahnya butuh internet dan beberapa menit:

```bash
pip install -r Belajar-Pemrograman-Python/requirements.txt
```

# 6. Jupyter Notebook

## 6.1 Menjalankan Jupyter

Dengan venv aktif (jika Jupyter belum terpasang: `pip install notebook`):

```bash
jupyter notebook
```

Perintah ini memulai server lokal (`http://localhost:8888`) dan membuka halaman Jupyter di browser. Biarkan terminal tetap terbuka selama bekerja; berhenti dengan `Ctrl+C` di terminal. Jika browser tidak terbuka sendiri, salin alamat `http://localhost:8888/...` lengkap dengan token dari terminal.

## 6.2 Pintasan notebook

| Aksi | Pintasan |
|---|---|
| Jalankan sel dan pindah ke bawah | `Shift + Enter` |
| Mode perintah / mode edit | `Esc` / `Enter` |
| Sisipkan sel di atas / bawah | `A` / `B` (mode perintah) |
| Hapus sel | `D D` |
| Ubah ke Markdown / kode | `M` / `Y` |

Jika kode berperilaku aneh, gunakan menu **Kernel → Restart Kernel and Run All Cells**.

## 6.3 Pastikan kernel memakai venv

Jupyter yang dijalankan dari venv otomatis memakai venv itu. Untuk mendaftarkan venv sebagai kernel yang bisa dipilih:

```bash
pip install ipykernel
python -m ipykernel install --user --name bootcamp --display-name "Python (bootcamp)"
```

Lalu pilih **Kernel → Change kernel → Python (bootcamp)**. Cek di sebuah sel:

```python
import sys
print(sys.executable)
```

Hasilnya harus menunjuk ke folder `.venv`.

# 7. Menyiapkan Buku Kerja

Paket belajar Anda berupa satu berkas ZIP, `Belajar-Pemrograman-Python-Materi-dan-Buku-Kerja.zip`, yang berisi:

```text
Belajar-Pemrograman-Python/
├── MULAI-DI-SINI.txt
├── 1-Buku-Materi.pdf
├── 2-Buku-Kerja/          hari1 … hari6 (.ipynb)
└── requirements.txt
```

**Langkah:**

1. **Ekstrak** ZIP ke dalam folder `bootcamp` yang dibuat pada bagian 3.2, sehingga terbentuk `bootcamp/Belajar-Pemrograman-Python/`. (Windows: klik kanan → *Extract All*; macOS: klik dua kali; Linux: `unzip Belajar-Pemrograman-Python.zip`.)
2. Buka terminal di folder `bootcamp` dan **aktifkan venv** (bagian 4.2) hingga prompt berawalan `(.venv)`.
3. **Pasang paket**, lalu **jalankan Jupyter** pada folder buku kerja:

```bash
pip install -r Belajar-Pemrograman-Python/requirements.txt
jupyter notebook Belajar-Pemrograman-Python/2-Buku-Kerja
```

4. Di Jupyter, buka `hari1-python-fundamentals.ipynb` dan jalankan **sel pertama (setup)** lebih dulu.

> [!TIP]
> **Cara memakai buku kerja**
>
> Tulis jawaban Anda di sel yang ditandai `# TULIS KODE ANDA DI SINI`, lalu jalankan sel **Periksa jawaban** di bawahnya: tanda ✅ berarti benar, ❌ berarti belum tepat. Setelah mencoba sendiri, Anda dapat membandingkan dengan **Buku Solusi** (PDF terpisah).

# 8. Pemecahan Masalah Cepat

| Pesan / gejala | Penyebab | Solusi |
|---|---|---|
| `pip` tidak dikenali | venv belum aktif / PATH | `python -m pip ...` setelah mengaktifkan venv |
| `ModuleNotFoundError: pandas` | paket di venv lain / kernel salah | aktifkan venv, `pip install`, pilih kernel venv |
| `jupyter` tidak dikenali | notebook belum terpasang di venv | `pip install notebook` |
| Port 8888 sibuk | Jupyter lain masih berjalan | `jupyter notebook --port 8889` |
| *running scripts is disabled* | kebijakan PowerShell | lihat bagian 4.3 / pakai CMD |
| Instalasi pip sangat lambat atau gagal | koneksi / proxy | ulangi; cek koneksi; coba jaringan lain |

# 9. Alternatif Jika Instalasi Lokal Bermasalah

| Opsi | Kelebihan | Catatan |
|---|---|---|
| **VS Code** + ekstensi Python & Jupyter | editor, terminal, dan notebook dalam satu jendela | tetap butuh Python dan venv di komputer |
| **Google Colab** | tanpa instal, berjalan di browser | butuh akun Google dan internet; unggah notebook dari folder `2-Buku-Kerja`; berkas hilang saat sesi berakhir |

# 10. Checklist Akhir

- [ ] `python --version` (atau `python3 --version`) menampilkan 3.11 atau lebih baru.
- [ ] Folder `bootcamp/` dan venv `.venv` ada; prompt berawalan `(.venv)` saat aktif.
- [ ] `pip install -r requirements.txt` selesai tanpa error; `pip list` menampilkan pandas.
- [ ] `jupyter notebook` berjalan dari venv; kernel benar.
- [ ] Notebook Hari 1 terbuka dan sel pertamanya berjalan tanpa error.

Selanjutnya: **Modul 1 — Python Fundamentals**.
