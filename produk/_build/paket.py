"""Merakit paket ZIP untuk pembeli: dua PDF + buku kerja (versi latihan, tanpa solusi) + panduan awal.
    python3 paket.py        # -> produk/paket/Belajar-Pemrograman-Python.zip
PDF dibangun lebih dulu dengan:  python3 build.py"""
import glob, os, zipfile
from build import ROOT, OUT, YEAR, OWNER

ROOT_NAME = 'Belajar-Pemrograman-Python'
PDFS = [('Belajar-Pemrograman-Python-Buku-Materi.pdf', '1-Buku-Materi.pdf'),
        ('Belajar-Pemrograman-Python-Buku-Solusi.pdf', '2-Buku-Solusi.pdf')]

START = f"""BELAJAR PEMROGRAMAN PYTHON
Materi dasar, Data Analisis, Visualisasi data, dan Capstone Project
=====================================================================

ISI PAKET
  1-Buku-Materi.pdf      Materi lengkap Modul 0-6 dengan contoh output asli
  2-Buku-Solusi.pdf      Solusi 102 latihan dan mini project + contoh capstone utuh
  3-Buku-Kerja/          Buku kerja Jupyter (hari1 ... hari6) dengan pemeriksa jawaban otomatis
  requirements.txt       Daftar paket Python yang dibutuhkan

URUTAN BELAJAR
  1. Baca bab/modul di Buku Materi (mulai dari Modul 0: Persiapan Lingkungan).
  2. Ketik ulang contoh kodenya dan bandingkan dengan blok Output.
  3. Kerjakan latihan hari yang sama di Buku Kerja (3-Buku-Kerja/).
     Jalankan sel "Periksa jawaban": tanda centang berarti benar.
  4. Setelah mencoba sendiri, bandingkan dengan Buku Solusi.
  5. Hari 6: kerjakan capstone Anda sendiri; contoh lengkapnya ada di lampiran Buku Solusi.

PERSIAPAN CEPAT (rincian lengkap ada di Buku Materi, Modul 0)
  Butuh: Python 3.11 atau lebih baru dan koneksi internet untuk instalasi paket.

  Windows (PowerShell):
    cd Belajar-Pemrograman-Python
    python -m venv .venv
    .venv\\Scripts\\Activate.ps1
    pip install -r requirements.txt
    jupyter notebook 3-Buku-Kerja

  macOS / Linux:
    cd Belajar-Pemrograman-Python
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    jupyter notebook 3-Buku-Kerja

  Tanpa instalasi: unggah notebook ke Google Colab (colab.research.google.com).
  Catatan: latihan yang menulis file membuat folder latihan_hariN di samping notebook.

CATATAN
  - Buku Kerja berisi soal dan tempat jawaban kosong; solusinya ada di Buku Solusi.
  - Seluruh kode diuji dengan Python 3.11 (pandas 3.0, numpy 2.4, matplotlib 3.11, seaborn 0.13).
  - Bagian latihan yang memakai internet bersifat opsional dan dilewati otomatis bila gagal.

(c) {YEAR} {OWNER}. Seluruh hak dilindungi. Dilarang memperbanyak atau
mendistribusikan ulang tanpa izin tertulis.
"""

def run():
    dist = os.path.join(OUT, 'paket'); os.makedirs(dist, exist_ok=True)
    zp = os.path.join(dist, ROOT_NAME + '.zip')
    items = [(os.path.join(OUT, src), f'{ROOT_NAME}/{dst}') for src, dst in PDFS]
    for f in sorted(glob.glob(os.path.join(ROOT, 'workbook', 'hari*.ipynb'))):
        items.append((f, f'{ROOT_NAME}/3-Buku-Kerja/{os.path.basename(f)}'))
    items.append((os.path.join(ROOT, 'requirements.txt'), f'{ROOT_NAME}/requirements.txt'))
    for src, _ in items:
        if not os.path.exists(src): raise SystemExit(f'berkas tidak ditemukan: {src} (jalankan build.py lebih dulu)')
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr(zipfile.ZipInfo(f'{ROOT_NAME}/MULAI-DI-SINI.txt', (2026, 1, 1, 0, 0, 0)), START.replace('\n', '\r\n'), zipfile.ZIP_DEFLATED)
        for src, arc in items:
            zi = zipfile.ZipInfo(arc, (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, open(src, 'rb').read())
    print(f'{os.path.relpath(zp, ROOT)}: {len(items)+1} berkas, {os.path.getsize(zp)/1e6:.1f} MB')
    return zp

if __name__ == '__main__':
    run()
