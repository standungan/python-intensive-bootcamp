import os, re
import common as C
from build import ROOT, OUT, YEAR, OWNER, COLORS, build_book

MODS = [
 ('modul00-persiapan-lingkungan.md', 'Persiapan Lingkungan'),
 ('modul01-python-fundamentals.md', 'Python Fundamentals'),
 ('modul02-functions-modules-file-handling.md', 'Functions, Modules & File Handling'),
 ('modul03-oop.md', 'Object-Oriented Programming'),
 ('modul04-numpy-pandas.md', 'NumPy & Pandas'),
 ('modul05-visualisasi-api-scraping.md', 'Visualisasi, API & Scraping'),
 ('modul06-capstone-project.md', 'Capstone Project'),
]

def load(md):
    t = open(os.path.join(ROOT, 'materi', md), encoding='utf-8').read()
    m = re.match(r'\s*# (.+)\n+(?:_(.+?)_\n)?', t)
    body = t[m.end():] if m else t
    return (m.group(1) if m else md), (m.group(2) or '' if m else ''), body

HOWTO = f"""
<section class="legal">
<h2>Tentang buku ini</h2>
<p><b>Belajar Pemrograman Python — Buku Materi</b> adalah materi lengkap pemrograman Python dari dasar hingga analisis data, visualisasi, dan capstone project (disusun untuk bootcamp enam hari), ditambah bab persiapan lingkungan. Setiap pembahasan disertai kasus beragam, kode yang <b>sudah dijalankan</b>, dan <b>contoh output</b> asli sehingga Anda dapat membandingkan hasil di komputer sendiri.</p>
<h3>Isi buku</h3>
<ul>
<li><b>Modul 0</b> — Persiapan lingkungan: Python, terminal, venv, pip, Jupyter.</li>
<li><b>Modul 1–2</b> — Dasar Python, function, module, error handling, file.</li>
<li><b>Modul 3</b> — Object-Oriented Programming.</li>
<li><b>Modul 4–5</b> — NumPy, Pandas, visualisasi, API, dan scraping.</li>
<li><b>Modul 6</b> — Capstone: empat jalur proyek analisis data.</li>
</ul>
<h3>Cara memakai</h3>
<ul>
<li><b>Ketik ulang</b> contoh kode, lalu ubah angka atau konteksnya — jangan hanya membaca.</li>
<li>Bandingkan hasil Anda dengan blok <b>Output</b> (berlatar hijau). Blok <b>Pseudocode</b> (kuning) adalah kerangka berpikir sebelum menulis kode.</li>
<li>Kerjakan latihan di akhir tiap bab sebelum melihat <b>Buku Solusi</b> (produk pendamping).</li>
<li>Bagian <b>Troubleshooting</b> memuat kasus error nyata beserta perbaikannya.</li>
</ul>
<h3>Lingkungan pengujian</h3>
<p>Seluruh kode dijalankan dengan Python 3.11 (pandas 3.0.6, numpy 2.4.6, matplotlib 3.11.2, seaborn 0.13.2). Blok yang memakai <code>input()</code> dijalankan dengan input simulasi; blok yang memanggil API yang tidak dapat diakses saat pengujian memakai respons tiruan dan diberi catatan.</p>
<h3>Produk pendamping</h3>
<ul>
<li><b>Buku Solusi</b> — solusi lengkap setiap latihan dan mini project.</li>
<li><b>Buku kerja Jupyter</b> dengan pemeriksa jawaban otomatis, dan <b>slide</b> untuk pengajar (tersedia di repositori).</li>
</ul>
<p style="margin-top:14pt;color:#64748b;font-size:8.5pt">© {YEAR} {OWNER}. Seluruh hak dilindungi. Dilarang memperbanyak atau mendistribusikan ulang tanpa izin tertulis.</p>
</section>
"""

def run():
    toc, parts = [], []
    # lintasan pertama mengumpulkan heading; id harus stabil -> konversi sekali
    for i, (md, short) in enumerate(MODS):
        title, sub, body = load(md)
        coll = []
        html_body = C.md_to_html(body, os.path.join(ROOT, 'materi'), shift=1, id_prefix=f'm{i}-', collect=coll)
        oid = f'part{i}'
        toc.append((1, f'Modul {i} — {short}', oid))
        h2s = [(lv, t, h) for lv, t, h in coll if lv == 2]
        toc += [(2, t, h) for lv, t, h in h2s]
        tag = sub if sub else ''
        op = C.opener(str(i), f'Modul {i} — {short}', tag, COLORS[i], oid, [t for _, t, _ in h2s][:16])
        parts.append(op + f'<section class="chapter">{html_body}</section>')
    def make(pages):
        cov = C.cover('Buku Materi', 'Belajar<br>Pemrograman Python', C.SUBTITLE,
                      'Edisi 1 · Python 3.11', 'x = 42<br>if x &gt; 0:<br>&nbsp;&nbsp;&nbsp;&nbsp;print("halo")', f'{OWNER} · {YEAR}')
        return C.page('Belajar Pemrograman Python — Buku Materi', cov + HOWTO + C.toc_html(toc, pages) + ''.join(parts), footer='Belajar Pemrograman Python · Buku Materi')
    os.makedirs(OUT, exist_ok=True)
    build_book('materi', make, toc, os.path.join(OUT, 'Belajar-Pemrograman-Python-Buku-Materi.pdf'))
