# Buku Kerja (Jupyter Notebook)

Satu buku kerja per hari, pendamping Modul 1–6. Setiap notebook berisi ringkasan konsep, contoh yang bisa dijalankan, **latihan dengan pemeriksa otomatis** (✅/❌), mini project, dan rekap.

| Hari | Buku kerja (untuk dikerjakan) | Solusi (sudah dieksekusi) | Latihan |
|---|---|---|---|
| 1 | [hari1-python-fundamentals](hari1-python-fundamentals.ipynb) | [solusi](solusi/hari1-python-fundamentals-solusi.ipynb) | 18 (L1–L16, P1–P2) |
| 2 | [hari2-functions-modules-file-handling](hari2-functions-modules-file-handling.ipynb) | [solusi](solusi/hari2-functions-modules-file-handling-solusi.ipynb) | 22 (L1–L20, P1–P2) |
| 3 | [hari3-oop](hari3-oop.ipynb) | [solusi](solusi/hari3-oop-solusi.ipynb) | 12 (L1–L10, P1–P2) |
| 4 | [hari4-numpy-pandas](hari4-numpy-pandas.ipynb) | [solusi](solusi/hari4-numpy-pandas-solusi.ipynb) | 24 (L1–L19, P1–P5) |
| 5 | [hari5-visualisasi-api-scraping](hari5-visualisasi-api-scraping.ipynb) | [solusi](solusi/hari5-visualisasi-api-scraping-solusi.ipynb) | 17 (L1–L13, P1–P4) |
| 6 | [hari6-capstone-project](hari6-capstone-project.ipynb) | [solusi](solusi/hari6-capstone-project-solusi.ipynb) | 9 (L1–L9) + pemeriksa `cek_deliverable` |

## Versi HTML (hanya-baca)

Salinan HTML semua notebook ada di [html/](html/) — mulai dari [html/index.html](html/index.html). Halaman berdiri sendiri (gambar tertanam, tanpa perlu internet) dan bisa dibuka langsung di browser setelah di-download; buku kerja ditampilkan tanpa output, solusi dengan output hasil eksekusi. Untuk **mengerjakan** latihan dan menjalankan pemeriksa jawaban tetap gunakan file `.ipynb` dengan Jupyter. Dibuat ulang dengan `jupyter nbconvert --to html --template lab <notebook>`.

> GitHub menampilkan file `.html` sebagai teks sumber, bukan halaman. Untuk melihat tampilannya, unduh filenya, atau aktifkan GitHub Pages untuk repo ini.

## Cara memakai

> Belum punya Python/venv/Jupyter? Ikuti slide [Hari 0 — Persiapan Lingkungan](../slides/hari0-setup-lingkungan.html). Semua paket yang dibutuhkan ada di [requirements.txt](../requirements.txt).

1. Pasang kebutuhan dan jalankan Jupyter di komputer Anda:
   ```bash
   pip install notebook numpy pandas matplotlib seaborn scipy openpyxl requests beautifulsoup4 feedparser
   jupyter notebook          # lalu buka folder workbook/ di browser
   ```
2. Buka notebook hari yang dikerjakan. Jalankan sel dari atas ke bawah (`Shift+Enter`). **Sel pertama (setup) wajib dijalankan lebih dulu.**
3. Pada tiap latihan, ganti `# TULIS KODE ANDA DI SINI` dengan jawaban Anda, lalu jalankan sel **Periksa jawaban** di bawahnya:
   - ✅ — jawaban benar;
   - ❌ — belum tepat; pesan menjelaskan apa yang salah. Buka *💡 Petunjuk (pseudocode)* bila buntu.
4. Di akhir notebook, jalankan sel **Rekap hasil latihan** untuk melihat skor (✅ benar · ❌ salah · ⏳ belum dicoba).
5. Bandingkan dengan notebook di `solusi/` **setelah** mencoba sendiri.

## Catatan

- Notebook diuji dengan Python 3.11 (pandas 3.x, numpy 2.x, matplotlib 3.11, seaborn 0.13). Semua latihan bisa dikerjakan **tanpa internet**: data contoh ada di dalam notebook, dan latihan API memakai server lokal. Sel bertanda *(opsional — INTERNET)* memanggil API sungguhan dan otomatis dilewati bila gagal.
- Latihan yang menulis file memakai folder `latihan_hariN/` di samping notebook (dibuat otomatis).
- Notebook solusi telah dieksekusi: seluruh pemeriksa lulus (✅), tanpa error. Notebook latihan diverifikasi tidak ada latihan yang lolos sebelum diisi.
- Materi lengkap tiap hari ada di [materi/](../materi/).
