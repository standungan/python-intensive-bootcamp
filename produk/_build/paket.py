"""Merakit paket ZIP untuk pembeli: Buku Materi (PDF) + buku kerja (versi latihan, tanpa solusi) + panduan awal.
Buku Solusi (PDF) dijual terpisah dan TIDAK ada di paket ini.
    python3 paket.py        # -> produk/paket/Belajar-Pemrograman-Python-Materi-dan-Buku-Kerja.zip
PDF dibangun lebih dulu dengan:  python3 build.py"""
import glob, os, zipfile
from build import ROOT, OUT, YEAR, OWNER

ROOT_NAME = 'Belajar-Pemrograman-Python'
PDFS = [('Belajar-Pemrograman-Python-Buku-Materi.pdf', '1-Buku-Materi.pdf')]
ZIP_NAME = 'Belajar-Pemrograman-Python-Materi-dan-Buku-Kerja.zip'

START = f"""BELAJAR PEMROGRAMAN PYTHON
Materi dasar, Data Analisis, Visualisasi data, dan Capstone Project
=====================================================================

ISI PAKET
  1-Buku-Materi.pdf      Materi lengkap Modul 0-6 dengan contoh output asli
  2-Buku-Kerja/          Buku kerja Jupyter (hari1 ... hari6) dengan pemeriksa jawaban otomatis
  requirements.txt       Daftar paket Python yang dibutuhkan

URUTAN BELAJAR
  1. Baca bab/modul di Buku Materi (mulai dari Modul 0: Persiapan Lingkungan).
  2. Ketik ulang contoh kodenya dan bandingkan dengan blok Output.
  3. Kerjakan latihan hari yang sama di Buku Kerja (2-Buku-Kerja/).
     Jalankan sel "Periksa jawaban": tanda centang berarti benar.
  4. Hari 6: kerjakan capstone Anda sendiri dengan mengikuti Modul 6.

PERSIAPAN CEPAT (rincian lengkap ada di Buku Materi, Modul 0)
  Butuh: Python 3.11 atau lebih baru dan koneksi internet untuk instalasi paket.
  Buat folder "bootcamp", ekstrak ZIP ini ke dalamnya, lalu buka terminal di folder "bootcamp".

  Windows (PowerShell):
    python -m venv .venv
    .venv\\Scripts\\Activate.ps1
    pip install -r Belajar-Pemrograman-Python/requirements.txt
    jupyter notebook Belajar-Pemrograman-Python/2-Buku-Kerja

  macOS / Linux:
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r Belajar-Pemrograman-Python/requirements.txt
    jupyter notebook Belajar-Pemrograman-Python/2-Buku-Kerja

  Tanpa instalasi: unggah notebook ke Google Colab (colab.research.google.com).
  Catatan: latihan yang menulis file membuat folder latihan_hariN di samping notebook.

CATATAN
  - Buku Kerja berisi soal dan tempat jawaban kosong. Solusi lengkap tersedia di Buku Solusi (PDF terpisah, tidak termasuk paket ini).
  - Seluruh kode diuji dengan Python 3.11 (pandas 3.0, numpy 2.4, matplotlib 3.11, seaborn 0.13).
  - Bagian latihan yang memakai internet bersifat opsional dan dilewati otomatis bila gagal.

(c) {YEAR} {OWNER}. Seluruh hak dilindungi. Dilarang memperbanyak atau
mendistribusikan ulang tanpa izin tertulis.
"""

def run():
    dist = os.path.join(OUT, 'paket'); os.makedirs(dist, exist_ok=True)
    zp = os.path.join(dist, ZIP_NAME)
    items = [(os.path.join(OUT, src), f'{ROOT_NAME}/{dst}') for src, dst in PDFS]
    for f in sorted(glob.glob(os.path.join(ROOT, 'workbook', 'hari*.ipynb'))):
        items.append((f, f'{ROOT_NAME}/2-Buku-Kerja/{os.path.basename(f)}'))
    items.append((os.path.join(ROOT, 'requirements.txt'), f'{ROOT_NAME}/requirements.txt'))
    for src, _ in items:
        if not os.path.exists(src): raise SystemExit(f'berkas tidak ditemukan: {src} (jalankan build.py lebih dulu)')
    with zipfile.ZipFile(zp, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr(zipfile.ZipInfo(f'{ROOT_NAME}/MULAI-DI-SINI.txt', (2026, 1, 1, 0, 0, 0)), START.replace('\n', '\r\n'), zipfile.ZIP_DEFLATED)
        for src, arc in items:
            zi = zipfile.ZipInfo(arc, (2026, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            data = open(src, 'rb').read()
            if src.endswith('.ipynb'):   # paket tidak memuat notebook solusi -> rujukan diarahkan ke Buku Solusi
                data = data.replace('ada di notebook `solusi/`'.encode(), 'ada di Buku Solusi (PDF terpisah)'.encode())
            z.writestr(zi, data)
    print(f'{os.path.relpath(zp, ROOT)}: {len(items)+1} berkas, {os.path.getsize(zp)/1e6:.1f} MB')
    return zp

if __name__ == '__main__':
    run()
