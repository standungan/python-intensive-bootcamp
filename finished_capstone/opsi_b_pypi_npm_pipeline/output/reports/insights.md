# Insight — Pipeline PyPI & npm

1. **Django punya rilis stabil terbanyak (377), tetapi fastapi paling aktif per tahun** (40.2 rilis/tahun) sedangkan seaborn paling jarang (2.0/tahun). Jumlah total dipengaruhi umur paket, sehingga rilis per tahun lebih adil untuk membandingkan.

2. **Jarak antar rilis sangat bervariasi.** Median tercepat: Django (0.1 hari), terlama: seaborn (93.2 hari). Untuk Django, 52% interval antar rilis kurang dari 1 hari karena beberapa cabang dukungan dirilis bersamaan (rilis keamanan), sehingga mediannya mendekati nol. Pandas memiliki 114 rilis stabil dengan median 35.5 hari.

3. **Perbandingan ekosistem:** median rilis per paket per tahun di PyPI = 6.1 vs npm = 11.7; median jarak antar rilis PyPI = 18.4 hari vs npm = 5.8 hari (sampel hanya 10 paket PyPI dan 5 paket npm, jadi bukan generalisasi ekosistem).

4. **Tahun 2014 adalah tahun dengan rilis stabil terbanyak** (203 rilis dari seluruh paket yang dipantau; express sendiri menyumbang 100); pada tahun penuh terakhir (2025) total rilis = 172.

5. **Proporsi pre-release berbeda jauh:** PyPI 9.0% vs npm 76.3% dari seluruh versi terdaftar. Angka npm didominasi react: 95% versinya pre-release (2819 versi, 70% di antaranya build canary/experimental/nightly/dev).

6. **Paket dengan rilis terakhir paling lama:** seaborn (979 hari sebelum tanggal pengambilan data), sedangkan paling baru: fastapi (0 hari).

7. **Ukuran distribusi NumPy** (median per rilis) berubah dari 126.60 MB (2015) menjadi 901.74 MB (2026); median jumlah file per rilis naik dari 13 menjadi 72 (makin banyak wheel per platform/versi Python).
