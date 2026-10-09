# Naskah Video — Hari 0: Persiapan Lingkungan

Deck: [`hari0-setup-lingkungan.html`](../hari0-setup-lingkungan.html) · 28 slide · 94 klik

> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.

**Total perkiraan:** 13 mnt 37 dtk (di luar jeda latihan)

| # | Slide | Klik | Durasi |
|---|---|---|---|
| 1 | Persiapan Lingkungan | 0 | 19 dtk |
| 2 | Agenda | 7 | 33 dtk |
| 3 | Tujuan | 5 | 27 dtk |
| 4 | A. Instal Python | 0 | 9 dtk |
| 5 | Cek versi | 4 | 44 dtk |
| 6 | Instal Python | 4 | 41 dtk |
| 7 | Jebakan PATH | 4 | 47 dtk |
| 8 | B. Terminal Dasar | 0 | 7 dtk |
| 9 | Terminal dasar | 6 | 34 dtk |
| 10 | Folder proyek | 4 | 26 dtk |
| 11 | C. Virtual Environment (venv) | 0 | 7 dtk |
| 12 | Mengapa venv | 5 | 30 dtk |
| 13 | Buat & aktifkan venv | 6 | 55 dtk |
| 14 | PowerShell policy | 2 | 31 dtk |
| 15 | Cek venv | 4 | 32 dtk |
| 16 | D. pip & Paket | 0 | 6 dtk |
| 17 | Pip dasar | 4 | 34 dtk |
| 18 | requirements.txt | 4 | 34 dtk |
| 19 | E. Jupyter Notebook | 0 | 6 dtk |
| 20 | Menjalankan Jupyter | 5 | 38 dtk |
| 21 | Pintasan notebook | 6 | 32 dtk |
| 22 | Kernel venv | 4 | 42 dtk |
| 23 | F. Ambil Materi & Buku Kerja | 0 | 8 dtk |
| 24 | Buka buku kerja | 6 | 44 dtk |
| 25 | Latihan: Python, venv, pip, Jupyter | 0 | 23 dtk |
| 26 | Troubleshooting | 6 | 50 dtk |
| 27 | Alternatif | 2 | 24 dtk |
| 28 | Rekap | 6 | 34 dtk |

---

### Slide 1 — Persiapan Lingkungan

*judul · transisi `zoom` · 0 klik · ⏱ 19 dtk*

**Saat slide muncul**

> Selamat datang di sesi persiapan lingkungan. Sebelum Hari 1, kita pastikan setiap komputer siap: Python terpasang, terminal dipahami, virtual environment dibuat, dan Jupyter Notebook berjalan. Sesi ini sekitar tujuh puluh lima menit, berlaku untuk Windows, macOS, maupun Linux.

---

### Slide 2 — Agenda

*isi · transisi `slide` · 7 klik · ⏱ 33 dtk*

**Saat slide muncul**

> Ini agendanya.

**Klik 1 →** — muncul: `Instal Python`

> Instal Python, lima belas menit.

**Klik 2 →** — muncul: `Terminal`

> Terminal dasar, sepuluh menit.

**Klik 3 →** — muncul: `venv`

> Virtual environment atau venv, lima belas menit.

**Klik 4 →** — muncul: `pip`

> pip untuk memasang paket, sepuluh menit.

**Klik 5 →** — muncul: `Jupyter`

> Jupyter Notebook, lima belas menit.

**Klik 6 →** — muncul: `Buku kerja`

> Dan mengambil buku kerja, sepuluh menit.

**Klik 7 →** — muncul: `Total ±75 menit. Setiap bagian diakhiri cek — jangan lanjut sebelum ce`

> Totalnya sekitar tujuh puluh lima menit. Aturan penting: setiap bagian diakhiri cek, dan jangan lanjut sebelum cek berhasil, karena masalah lingkungan akan menumpuk.

---

### Slide 3 — Tujuan

*isi · transisi `slide` · 5 klik · ⏱ 27 dtk*

**Saat slide muncul**

> Di akhir sesi ini, ada lima hal yang Anda miliki.

**Klik 1 →** — muncul: `Python 3.11 atau lebih baru yang terpasang dan dikenali terminal`

> Python tiga koma sebelas atau lebih baru, terpasang dan dikenali terminal.

**Klik 2 →** — muncul: `folder proyek bootcamp/ dengan virtual environment .venv`

> Folder proyek bootcamp dengan virtual environment bernama titik venv.

**Klik 3 →** — muncul: `paket yang dibutuhkan (pandas, numpy, matplotlib, …) di dalam venv`

> Paket yang dibutuhkan, seperti pandas, numpy, dan matplotlib, terpasang di dalam venv.

**Klik 4 →** — muncul: `Jupyter Notebook yang berjalan dari venv tersebut`

> Jupyter Notebook yang berjalan dari venv tersebut.

**Klik 5 →** — muncul: `buku kerja Hari 1 yang bisa dibuka dan dijalankan`

> Dan buku kerja Hari 1 yang bisa dibuka dan dijalankan.

---

### Slide 4 — A. Instal Python

*bagian · transisi `rise` · 0 klik · ⏱ 9 dtk*

**Saat slide muncul**

> Bagian A: instal Python. Kita cek dulu apakah Python sudah ada, baru memasang bila perlu.

---

### Slide 5 — Cek versi

*isi · transisi `slide` · 4 klik · ⏱ 44 dtk*

**Saat slide muncul**

> Pertama, cek apakah Python sudah terpasang. Buka terminal dan ketik perintah versi.

**Klik 1 →** — muncul: `py --version`

> Di Windows, ketik py spasi minus minus version, atau python spasi minus minus version.

🎬 **Aksi:** Ketik kedua perintah di terminal Windows dan tunjukkan hasilnya.

**Klik 2 →** — muncul: `python3 --version`

> Di macOS dan Linux, perintahnya python3.

**Klik 3 →** — muncul: `Yang dicari: Python 3.11 atau lebih baru (3.12, 3.13 juga baik).`

> Ketik python3 minus minus version. Yang kita cari adalah Python tiga koma sebelas atau lebih baru; tiga koma dua belas dan tiga belas juga baik.

🎬 **Aksi:** Ketik perintahnya di terminal macOS/Linux.

**Klik 4 →** — muncul: `Muncul "not recognized" / "command not found" → Python belum terpasang`

> Kalau muncul pesan not recognized atau command not found, artinya Python belum terpasang, atau belum masuk PATH. Lanjut ke slide berikutnya.

---

### Slide 6 — Instal Python

*isi · transisi `slide` · 4 klik · ⏱ 41 dtk*

**Saat slide muncul**

> Cara memasang Python berbeda untuk tiap sistem operasi.

**Klik 1 →** — muncul: `Windowsunduh installer dari python.org/downloadsjalankan, centang “Add`

> Di Windows, unduh installer dari python titik org slash downloads. Saat menjalankan installer, centang Add python titik exe to PATH, lalu pilih Install Now. Kotak PATH ini penting sekali.

**Klik 2 →** — muncul: `macOSunduh installer dari python.org/downloadsatau Homebrew: brew inst`

> Di macOS, unduh installer dari python titik org, atau pakai Homebrew dengan perintah brew install python.

**Klik 3 →** — muncul: `LinuxDebian/Ubuntu:sudo apt install python3 python3-venv python3-pipFe`

> Di Linux Debian atau Ubuntu, pakai sudo apt install python3 python3-venv python3-pip. Di Fedora, sudo dnf install python3. Paket python3-venv diperlukan agar venv bisa dibuat.

**Klik 4 →** — muncul: `Setelah instal, tutup dan buka lagi terminal, lalu ulangi perintah cek`

> Setelah instal, tutup dan buka lagi terminal, lalu ulangi perintah cek versi.

---

### Slide 7 — Jebakan PATH

*isi · transisi `slide` · 4 klik · ⏱ 47 dtk*

**Saat slide muncul**

> Kadang Python sudah terpasang tapi tidak ketemu. Ini gejala dan solusinya.

**Klik 1 →** — muncul: `Windows: python tidak dikenalibelum centang Add to PATHpakai py (Pytho`

> Di Windows, python tidak dikenali karena belum mencentang Add to PATH. Solusinya pakai py, yaitu Python launcher, atau jalankan ulang installer, pilih Modify, lalu centang PATH.

**Klik 2 →** — muncul: `Windows membuka Microsoft Storealias bawaan Windowsinstal dari python.`

> Windows membuka Microsoft Store: itu alias bawaan Windows. Instal dari python titik org dan matikan alias di Manage app execution aliases.

**Klik 3 →** — muncul: `macOS/Linux: python tidak adahanya tersedia python3pakai python3 (di d`

> Di macOS atau Linux, python tidak ada tapi python3 ada. Itu normal, pakai python3. Di dalam venv, python otomatis tersedia.

**Klik 4 →** — muncul: `versi lama (mis. 3.8)ada beberapa Python terpasangpanggil versi baru s`

> Kalau versi yang muncul lama, misalnya tiga koma delapan, mungkin ada beberapa Python terpasang. Panggil versi baru secara eksplisit, python3.11 atau py minus tiga koma sebelas.

---

### Slide 8 — B. Terminal Dasar

*bagian · transisi `rise` · 0 klik · ⏱ 7 dtk*

**Saat slide muncul**

> Bagian B: terminal dasar. Cukup beberapa perintah untuk berpindah dan membuat folder.

---

### Slide 9 — Terminal dasar

*isi · transisi `slide` · 6 klik · ⏱ 34 dtk*

**Saat slide muncul**

> Ini perintah terminal yang akan kita pakai, di Windows PowerShell dan di macOS atau Linux.

**Klik 1 →** — muncul: `di folder mana saya?pwd / cdpwd`

> Untuk mengetahui kita berada di folder mana: pwd.

**Klik 2 →** — muncul: `lihat isi folderdir / lsls`

> Untuk melihat isi folder: ls, atau dir di Windows.

**Klik 3 →** — muncul: `buat foldermkdir bootcampmkdir bootcamp`

> Membuat folder: mkdir bootcamp, sama di semua sistem.

**Klik 4 →** — muncul: `masuk foldercd bootcampcd bootcamp`

> Masuk ke folder: cd bootcamp.

**Klik 5 →** — muncul: `naik satu levelcd ..cd ..`

> Naik satu level: cd spasi titik titik.

**Klik 6 →** — muncul: `Terminal Windows: PowerShell atau Terminal (Windows 11). Di VS Code: m`

> Terminal Windows yang disarankan adalah PowerShell atau aplikasi Terminal di Windows 11. Di VS Code, lewat menu Terminal, New Terminal.

---

### Slide 10 — Folder proyek

*isi · transisi `slide` · 4 klik · ⏱ 26 dtk*

**Saat slide muncul**

> Sekarang kita buat folder proyek.

**Klik 1 →** — muncul: `mkdir bootcamp`

> Ketik mkdir bootcamp. Folder baru bernama bootcamp muncul di direktori home.

🎬 **Aksi:** Ketik perintah dan tunjukkan folder baru muncul.

**Klik 2 →** — muncul: `cd bootcamp`

> Lalu cd bootcamp untuk masuk ke dalamnya.

**Klik 3 →** — muncul: `pwd # Windows: cd`

> Dan pwd, atau cd saja di Windows, untuk memastikan kita berada di folder bootcamp.

**Klik 4 →** — muncul: `Semua langkah berikutnya dijalankan di dalam folder ini.`

> Semua langkah berikutnya dijalankan di dalam folder ini.

---

### Slide 11 — C. Virtual Environment (venv)

*bagian · transisi `rise` · 0 klik · ⏱ 7 dtk*

**Saat slide muncul**

> Bagian C: virtual environment, atau venv. Lingkungan terisolasi untuk tiap proyek.

---

### Slide 12 — Mengapa venv

*isi · transisi `slide` · 5 klik · ⏱ 30 dtk*

**Saat slide muncul**

> Mengapa perlu venv? Bayangkan satu komputer dengan banyak proyek.

**Klik 1 →**

> Di atas ada Python sistem, yang sebaiknya tidak diotak-atik.

**Klik 2 →**

> Proyek A punya venv sendiri dengan pandas versi dua koma dua.

**Klik 3 →**

> Proyek bootcamp kita punya venv sendiri, dengan pandas versi tiga koma nol.

**Klik 4 →**

> Dan proyek C boleh memakai versi lain lagi.

**Klik 5 →** — muncul: `Tiap proyek punya paket sendiri → tidak bentrok, mudah dihapus, mudah `

> Intinya, tiap proyek punya paket sendiri sehingga tidak bentrok, mudah dihapus, dan mudah diulang di komputer lain.

---

### Slide 13 — Buat & aktifkan venv

*isi · transisi `slide` · 6 klik · ⏱ 55 dtk*

**Saat slide muncul**

> Sekarang kita buat dan aktifkan venv di folder bootcamp.

**Klik 1 →** — muncul: `1 · Buat (sekali saja)`

> Langkah satu, membuat venv, hanya sekali: python spasi minus m spasi venv spasi titik venv. Di macOS dan Linux, pakai python3.

🎬 **Aksi:** Ketik perintah dan tunggu hingga folder .venv muncul.

**Klik 2 →** — muncul: `2 · Aktifkan (setiap membuka terminal baru)`

> Langkah dua, aktivasi, diulang setiap membuka terminal baru. Perintahnya berbeda untuk tiap terminal.

**Klik 3 →** — muncul: `Windows PowerShell.venv\Scripts\Activate.ps1`

> Di Windows PowerShell: titik venv backslash Scripts backslash Activate titik ps1.

🎬 **Aksi:** Jalankan perintah aktivasi sesuai terminal Anda.

**Klik 4 →** — muncul: `Windows CMD.venv\Scripts\activate.bat`

> Di Windows CMD: titik venv backslash Scripts backslash activate titik bat.

**Klik 5 →** — muncul: `macOS / Linuxsource .venv/bin/activate`

> Di macOS dan Linux: source titik venv slash bin slash activate.

**Klik 6 →** — muncul: `Berhasil bila prompt berawalan (.venv), misalnya (.venv) PS C:\bootcam`

> Berhasil bila prompt berawalan kurung titik venv. Misalnya di Windows muncul kurung venv, PS, C titik dua bootcamp, dan di Linux kurung venv, user at pc.

---

### Slide 14 — PowerShell policy

*isi · transisi `slide` · 2 klik · ⏱ 31 dtk*

**Saat slide muncul**

> Ada satu jebakan khusus di Windows PowerShell.

**Klik 1 →** — muncul: `Gejala di PowerShell`

> Gejalanya: pesan Activate titik ps1 cannot be loaded because running scripts is disabled on this system. Artinya PowerShell memblokir skrip.

**Klik 2 →** — muncul: `Solusi (pilih satu)`

> Ada dua solusi. A: izinkan skrip lokal untuk akun Anda dengan Set-ExecutionPolicy minus Scope CurrentUser RemoteSigned. Cukup sekali, dan jawab Y kalau diminta konfirmasi. B: pakai CMD dengan activate titik bat.

🎬 **Aksi:** Jalankan Set-ExecutionPolicy di PowerShell, lalu aktifkan venv lagi.

---

### Slide 15 — Cek venv

*isi · transisi `slide` · 4 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Sekarang kita cek apakah venv benar-benar aktif.

**Klik 1 →** — muncul: `python -c "import sys; print(sys.prefix)"`

> Ketik python minus c, import sys, print sys titik prefix.

🎬 **Aksi:** Ketik perintah ini di terminal dengan venv aktif.

**Klik 2 →** — muncul: `python -m pip --version`

> Baris pertama harus menunjuk ke folder titik venv di dalam bootcamp. Berikutnya python minus m pip minus minus version.

**Klik 3 →** — muncul: `deactivate`

> Baris kedua menampilkan lokasi pip, yang harus berada di dalam venv. Terakhir, deactivate.

**Klik 4 →** — muncul: `deactivate keluar dari venv; prompt kembali normal.`

> Deactivate keluar dari venv dan prompt kembali normal. Aktifkan lagi sebelum lanjut.

---

### Slide 16 — D. pip & Paket

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian D: pip dan paket. Memasang library yang dibutuhkan.

---

### Slide 17 — Pip dasar

*isi · transisi `slide` · 4 klik · ⏱ 34 dtk*

**Saat slide muncul**

> pip adalah alat untuk memasang paket Python.

**Klik 1 →** — muncul: `python -m pip install --upgrade pip`

> Pertama, perbarui pip dengan python minus m pip install minus minus upgrade pip. Pastikan kurung venv aktif sebelum pip install apa pun.

🎬 **Aksi:** Pastikan prompt berawalan (.venv), lalu jalankan perintah.

**Klik 2 →** — muncul: `pip install pandas`

> pip install pandas memasang satu paket, misalnya pandas.

**Klik 3 →** — muncul: `pip list`

> pip list menampilkan paket yang terpasang di venv ini saja.

**Klik 4 →** — muncul: `pip freeze > requirements.txt`

> Dan pip freeze lalu tanda lebih besar requirements titik txt menyimpan daftar paket beserta versinya ke sebuah file.

---

### Slide 18 — requirements.txt

*isi · transisi `slide` · 4 klik · ⏱ 34 dtk*

**Saat slide muncul**

> Daripada memasang satu per satu, kita pakai file requirements.

**Klik 1 →**

> File requirements titik txt ada di akar repositori.

**Klik 2 →** — muncul: `pip install -r requirements.txtterminal`

> Isinya daftar paket: notebook, numpy, pandas, matplotlib, seaborn, scipy, openpyxl, requests, beautifulsoup4, dan feedparser. Pasang semuanya dengan satu perintah: pip install minus r requirements titik txt.

🎬 **Aksi:** Jalankan perintah di folder repositori dengan venv aktif; tunggu beberapa menit.

**Klik 3 →** — muncul: `Memasang semua paket sekaligus. Butuh internet dan beberapa menit.`

> Perintah ini memasang semua paket sekaligus. Butuh internet dan beberapa menit; selama menunggu, jelaskan fungsi tiap paket.

**Klik 4 →** — muncul: `Pasang ulang di komputer lain = perintah yang sama.`

> Dan di komputer lain, perintahnya sama persis.

---

### Slide 19 — E. Jupyter Notebook

*bagian · transisi `rise` · 0 klik · ⏱ 6 dtk*

**Saat slide muncul**

> Bagian E: Jupyter Notebook. Menulis dan menjalankan kode per sel.

---

### Slide 20 — Menjalankan Jupyter

*isi · transisi `slide` · 5 klik · ⏱ 38 dtk*

**Saat slide muncul**

> Menjalankan Jupyter itu mudah.

**Klik 1 →** — muncul: `jupyter notebookterminal`

> Di terminal dengan venv aktif, ketik jupyter notebook. Perintah ini memulai server lokal.

🎬 **Aksi:** Jalankan jupyter notebook dan tunggu browser terbuka.

**Klik 2 →**

> Server berjalan di komputer Anda sendiri, di alamat localhost port delapan ribu delapan ratus delapan puluh delapan.

**Klik 3 →**

> Lalu halaman Jupyter terbuka di browser. Browser hanyalah antarmukanya.

**Klik 4 →** — muncul: `Biarkan terminal tetap terbuka selama bekerja. Berhenti dengan Ctrl+C `

> Biarkan terminal tetap terbuka selama bekerja. Berhenti dengan Ctrl dan C di terminal.

**Klik 5 →** — muncul: `Browser tidak terbuka sendiri? Salin alamat http://localhost:8888/… (l`

> Kalau browser tidak terbuka sendiri, salin alamat localhost lengkap dengan token dari terminal.

---

### Slide 21 — Pintasan notebook

*isi · transisi `slide` · 6 klik · ⏱ 32 dtk*

**Saat slide muncul**

> Beberapa pintasan notebook yang berguna.

**Klik 1 →** — muncul: `jalankan sel & pindah ke bawahShift + Enter`

> Shift dan Enter: menjalankan sel dan pindah ke bawah. Ini yang paling sering dipakai.

**Klik 2 →** — muncul: `mode perintah / mode editEsc / Enter`

> Escape untuk mode perintah, Enter untuk mode edit.

**Klik 3 →** — muncul: `sisipkan sel di atas / bawahA / B (mode perintah)`

> Di mode perintah, A menyisipkan sel di atas dan B di bawah.

**Klik 4 →** — muncul: `hapus selD D`

> Menghapus sel: tekan D dua kali.

**Klik 5 →** — muncul: `ubah ke Markdown / kodeM / Y`

> M mengubah sel menjadi Markdown, dan Y menjadi kode.

**Klik 6 →** — muncul: `Jika kode aneh/error tak masuk akal: menu Kernel → Restart Kernel and `

> Kalau kode berperilaku aneh, pakai menu Kernel, lalu Restart Kernel and Run All Cells.

---

### Slide 22 — Kernel venv

*isi · transisi `slide` · 4 klik · ⏱ 42 dtk*

**Saat slide muncul**

> Satu hal penting: pastikan kernel notebook memakai venv kita.

**Klik 1 →** — muncul: `pip install ipykernel`

> Jupyter yang dijalankan dari venv otomatis memakai venv itu.

**Klik 2 →** — muncul: `python -m ipykernel install --user --name bootcamp --display-name "Pyt`

> Untuk berjaga-jaga, pasang ipykernel dengan pip install ipykernel.

🎬 **Aksi:** Jalankan perintahnya di terminal venv.

**Klik 3 →** — muncul: `Perintah kedua mendaftarkan venv sebagai kernel yang bisa dipilih: Ker`

> Lalu daftarkan venv sebagai kernel: python minus m ipykernel install minus minus user, dengan nama bootcamp dan display name Python kurung bootcamp. Setelah itu muncul di menu Kernel, Change kernel.

🎬 **Aksi:** Jalankan perintah, lalu buka menu Kernel → Change kernel.

**Klik 4 →** — muncul: `Cek di sel: import sys; sys.executable → harus menunjuk ke folder .ven`

> Untuk mengecek, di sel notebook ketik import sys, sys titik executable. Hasilnya harus menunjuk ke folder titik venv.

---

### Slide 23 — F. Ambil Materi & Buku Kerja

*bagian · transisi `rise` · 0 klik · ⏱ 8 dtk*

**Saat slide muncul**

> Bagian F: mengambil materi dan buku kerja, dari repositori ke notebook Hari 1.

---

### Slide 24 — Buka buku kerja

*isi · transisi `slide` · 6 klik · ⏱ 44 dtk*

**Saat slide muncul**

> Sekarang kita ambil buku kerjanya.

**Klik 1 →** — muncul: `git clone https://github.com/standungan/python-intensive-bootcamp`

> Pertama, git clone alamat repositori python-intensive-bootcamp.

🎬 **Aksi:** Jalankan git clone di folder yang Anda inginkan.

**Klik 2 →** — muncul: `cd python-intensive-bootcamp`

> Lalu cd python-intensive-bootcamp untuk masuk ke folder hasil clone.

**Klik 3 →** — muncul: `pip install -r requirements.txt`

> Pasang kebutuhan dengan pip install minus r requirements titik txt, pastikan venv aktif.

**Klik 4 →** — muncul: `jupyter notebook workbook/`

> Dan jalankan jupyter notebook workbook slash. Browser terbuka menampilkan folder workbook.

**Klik 5 →** — muncul: `Tanpa Git: tombol hijau Code → Download ZIP di GitHub, ekstrak, lalu b`

> Kalau tidak memakai Git: di GitHub klik tombol hijau Code, lalu Download ZIP, ekstrak, dan buka terminal di folder hasil ekstrak.

**Klik 6 →** — muncul: `Di Jupyter buka hari1-python-fundamentals.ipynb; jalankan sel pertama `

> Di Jupyter, buka hari1 minus python minus fundamentals titik ipynb, dan jalankan sel pertama, yaitu setup, lebih dulu.

---

### Slide 25 — Latihan: Python, venv, pip, Jupyter

*latihan · transisi `zoom` · 0 klik · ⏱ 23 dtk*

**Saat slide muncul**

> Sekarang cek akhir, sepuluh menit. Pastikan empat hal: python minus minus version berhasil, prompt berawalan kurung titik venv, pip list menampilkan pandas, dan sel pertama notebook Hari 1 berjalan tanpa error. Jeda video ini dan lanjutkan setelah selesai.

🎬 **Aksi:** Jeda video; jalankan timer 10 menit (tekan Mulai).

---

### Slide 26 — Troubleshooting

*isi · transisi `slide` · 6 klik · ⏱ 50 dtk*

**Saat slide muncul**

> Slide rujukan pemecahan masalah. Tinggalkan di layar saat peserta mengerjakan cek akhir.

**Klik 1 →** — muncul: `pip tidak dikenalivenv belum aktif / PATHpython -m pip … setelah menga`

> pip tidak dikenali: venv belum aktif atau masalah PATH. Aktifkan venv, lalu pakai python minus m pip.

**Klik 2 →** — muncul: `ModuleNotFoundError: pandaspaket di venv lain / kernel salahaktifkan v`

> ModuleNotFoundError pandas: paket terpasang di venv lain atau kernel salah. Aktifkan venv, pip install, dan pilih kernel venv.

**Klik 3 →** — muncul: `jupyter tidak dikenalinotebook belum terpasang di venvpip install note`

> jupyter tidak dikenali: notebook belum terpasang di venv. Jalankan pip install notebook.

**Klik 4 →** — muncul: `Port 8888 sibukJupyter lain masih berjalanjupyter notebook --port 8889`

> Port delapan ribu delapan ratus delapan puluh delapan sibuk: Jupyter lain masih berjalan. Pakai jupyter notebook minus minus port delapan ribu delapan ratus delapan puluh sembilan.

**Klik 5 →** — muncul: `running scripts is disabledkebijakan PowerShelllihat slide PowerShell `

> Running scripts is disabled: kebijakan PowerShell. Lihat slide PowerShell, atau pakai CMD.

**Klik 6 →** — muncul: `instalasi pip sangat lambat/gagalkoneksi / proxyulangi; cek koneksi; m`

> Instalasi pip sangat lambat atau gagal: biasanya koneksi atau proxy. Ulangi, cek koneksi, atau pakai jaringan lain.

---

### Slide 27 — Alternatif

*isi · transisi `slide` · 2 klik · ⏱ 24 dtk*

**Saat slide muncul**

> Kalau instalasi lokal bermasalah, ada alternatif.

**Klik 1 →** — muncul: `VS Code + ekstensi Python & Jupytereditor + terminal + notebook dalam `

> VS Code dengan ekstensi Python dan Jupyter: editor, terminal, dan notebook dalam satu jendela. Tetap butuh Python dan venv di komputer.

**Klik 2 →** — muncul: `Google Colabtanpa instal, jalan di browserbutuh akun Google & internet`

> Google Colab: tanpa instal, berjalan di browser. Butuh akun Google dan internet; unggah notebook dari folder workbook. Berkas akan hilang saat sesi berakhir.

---

### Slide 28 — Rekap

*isi · transisi `slide` · 6 klik · ⏱ 34 dtk*

**Saat slide muncul**

> Rekap persiapan.

**Klik 1 →** — muncul: `Python 3.11+ terpasang; python --version / python3 --version berhasil`

> Python tiga koma sebelas atau lebih baru terpasang dan perintah cek versi berhasil.

**Klik 2 →** — muncul: `folder bootcamp/ dan venv .venv (aktif: prompt (.venv))`

> Folder bootcamp dan venv titik venv, aktif dengan prompt kurung venv.

**Klik 3 →** — muncul: `paket terpasang dengan pip install -r requirements.txt`

> Paket terpasang dengan pip install minus r requirements titik txt.

**Klik 4 →** — muncul: `Jupyter berjalan dari venv; kernel benar`

> Jupyter berjalan dari venv dan kernel benar.

**Klik 5 →** — muncul: `buku kerja Hari 1 terbuka dan sel pertama berjalan`

> Buku kerja Hari 1 terbuka dan sel pertamanya berjalan.

**Klik 6 →** — muncul: `Selanjutnya (Hari 1): Python Fundamentals`

> Selanjutnya, Hari 1: Python Fundamentals. Sampai jumpa!

🎬 **Aksi:** Pastikan semua peserta lolos sebelum Hari 1.

---
