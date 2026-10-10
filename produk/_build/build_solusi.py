import glob, json, os, re, html
import common as C
from build import ROOT, OUT, YEAR, OWNER, COLORS, build_book

DAYS = [
 (1, 'hari1-python-fundamentals-solusi.ipynb', 'Python Fundamentals', 'Variabel, control flow, struktur data, mini project menu mahasiswa'),
 (2, 'hari2-functions-modules-file-handling-solusi.ipynb', 'Functions, Modules & File Handling', 'Function, lambda, module, error handling, file dan CSV'),
 (3, 'hari3-oop-solusi.ipynb', 'Object-Oriented Programming', 'Class, inheritance, encapsulation, special methods'),
 (4, 'hari4-numpy-pandas-solusi.ipynb', 'NumPy & Pandas', 'Array, DataFrame, cleaning, groupby, merge, pivot'),
 (5, 'hari5-visualisasi-api-scraping-solusi.ipynb', 'Visualisasi, API & Scraping', 'Matplotlib, Seaborn, API/JSON, scraping, arXiv'),
 (6, 'hari6-capstone-project-solusi.ipynb', 'Capstone Project', 'Perencanaan, pipeline, README, dan pemeriksaan deliverable'),
]
ANSI = re.compile(r'\x1b\[[0-9;]*m')
JALUR = [
 ('A', 'jalur_a_eda_titanic', 'EDA Dataset Publik (Titanic)', ['src/main.py'], 'figures'),
 ('B', 'jalur_b_api_pypi_npm', 'API PyPI & npm → Analisis → Visualisasi', ['src/main.py'], 'figures'),
 ('C', 'jalur_c_arxiv', 'Pipeline Paper arXiv', ['src/main.py'], 'figures'),
 ('D', 'jalur_d_analisis_nilai_oop', 'Aplikasi Analisis Nilai Berbasis OOP', ['src/analisis_nilai.py', 'src/main.py', 'src/generate_data.py', 'tests/test_analisis_nilai.py'], 'output/figures'),
]

def src_of(c): return ''.join(c['source'])

def outputs_html(outs):
    text, imgs = [], []
    for o in outs:
        t = o.get('output_type')
        if t == 'stream': text.append(ANSI.sub('', ''.join(o['text'])))
        elif t in ('execute_result', 'display_data'):
            d = o.get('data', {})
            if 'image/png' in d: imgs.append('<img src="data:image/png;base64,' + ''.join(d['image/png']).strip() + '">')
            elif 'text/plain' in d: text.append(ANSI.sub('', ''.join(d['text/plain'])))
    return text, imgs

def split_details(md):
    m = re.search(r'<details>\s*<summary>.*?</summary>(.*?)</details>', md, re.S)
    if not m: return md, ''
    return (md[:m.start()] + md[m.end():]).strip(), m.group(1).strip()

def exercise_html(md_cell, ans, chk, base, n):
    stmt_md, hint_md = split_details(src_of(md_cell))
    title_m = re.match(r'#+\s*(.+)\n', stmt_md); title = title_m.group(1).strip() if title_m else f'Latihan {n}'
    stmt_md = stmt_md[title_m.end():] if title_m else stmt_md
    hid = f'ex{n}'
    h = [f'<div class="ex"><h3 id="{hid}">{html.escape(title)}</h3>']
    h.append('<div class="stmt">' + C.md_to_html(stmt_md, base, shift=3) + '</div>')
    if hint_md:
        hh = re.sub(r'^```\w*\n|\n```\s*$', '', hint_md.strip()) if hint_md.strip().startswith('```') else hint_md
        h.append('<div class="label hint">Pendekatan (pseudocode)</div><pre class="pseudo"><code>' + C.esc(hh.strip()) + '</code></pre>')
    code = src_of(ans).rstrip()
    cls = 'code long' if code.count('\n') > 40 else 'code'
    h.append('<div class="label sol">Solusi</div><pre class="%s"><code>%s</code></pre>' % (cls, C.hl(code, 'python')))
    text, imgs = outputs_html(ans.get('outputs', []))
    if text or imgs:
        h.append('<div class="label out">Output</div>')
        if text: h.append('<pre class="out"><code>' + C.esc(''.join(text).rstrip()) + '</code></pre>')
        h.extend(imgs)
    ctext, _ = outputs_html(chk.get('outputs', [])) if chk else ([], [])
    if ctext:
        h.append('<div class="label chk">Hasil pemeriksa</div><pre class="chk"><code>' + C.esc(''.join(ctext).strip()) + '</code></pre>')
    h.append('</div>')
    return ''.join(h), hid, title

def day_html(day, fn, short, tagline, toc):
    nb = json.load(open(os.path.join(ROOT, 'workbook', 'solusi', fn), encoding='utf-8'))
    cells = nb['cells']; base = os.path.join(ROOT, 'workbook')
    oid = f'day{day}'; toc.append((1, f'Hari {day} — {short}', oid))
    body, i, count = [], 0, 0
    while i < len(cells):
        c = cells[i]; tags = c['metadata'].get('tags', [])
        if c['cell_type'] == 'markdown' and 'latihan' in tags:
            ans = chk = None; j = i + 1
            while j < len(cells) and 'latihan' not in cells[j]['metadata'].get('tags', []):
                t = cells[j]['metadata'].get('tags', [])
                if 'jawaban' in t and ans is None: ans = cells[j]
                if 'periksa' in t and chk is None: chk = cells[j]
                j += 1
            if ans is not None:
                count += 1
                eh, hid, title = exercise_html(c, ans, chk, base, f'{day}-{count}')
                toc.append((3, title, hid)); body.append(eh)
            i = j; continue
        if c['cell_type'] == 'markdown':
            s = src_of(c); m = re.match(r'##\s+([A-F]\.\s[^\n]+)\n+(.*)', s, re.S)
            if m and 'Rekap' in m.group(1): m = None
            if m:
                first = m.group(2).strip().split('\n\n')[0]
                hid = f'sec{day}-{len(body)}'
                toc.append((2, m.group(1).strip(), hid))
                body.append(f'<h2 id="{hid}">{C.esc(m.group(1).strip())}</h2>' + (f'<div class="sec-note">' + C.md_to_html(first, base, shift=0) + '</div>' if first and not first.startswith(('#', '|', '-', '1.', '```')) else ''))
        i += 1
    items = [t for lv, t, h in toc if lv == 2 and h.startswith(f'sec{day}-')]
    return C.opener(str(day), f'Hari {day} — {short}', tagline, COLORS[day], oid, items) + '<section class="chapter">' + ''.join(body) + '</section>', count

def appendix(toc):
    parts = ['']; oid = 'lampiran'
    toc.append((1, 'Lampiran — Contoh Capstone Lengkap', oid))
    parts[0] = C.opener('★', 'Lampiran — Contoh Capstone Lengkap', 'Solusi utuh untuk Modul 6: empat jalur capstone beserta dokumentasi, grafik hasil, dan kode sumbernya.', '#14b8a6', oid, [f'Jalur {k} — {t}' for k, _, t, _, _ in JALUR])
    for k, folder, title, srcs, figdir in JALUR:
        base = os.path.join(ROOT, 'contoh-capstone', folder)
        hid = f'jalur{k}'; toc.append((2, f'Jalur {k} — {title}', hid))
        readme = open(os.path.join(base, 'README.md'), encoding='utf-8').read()
        readme = re.sub(r'^\s*# .+\n', '', readme, count=1)
        readme = re.sub(r'\n## 11\. Bahan belajar.*', '\n', readme, flags=re.S)
        parts.append(f'<section class="chapter"><h2 id="{hid}" style="break-before:page">Jalur {k} — {C.esc(title)}</h2>' + C.md_to_html(readme, base, shift=2, id_prefix=f'j{k}-') )
        figs = sorted(glob.glob(os.path.join(base, figdir, '*.png')))
        if figs:
            parts.append('<h3>Grafik hasil</h3><div class="gallery">' + ''.join(f'<img src="{C.data_uri(f)}" alt="{os.path.basename(f)}">' for f in figs) + '</div>')
        parts.append('<h3>Kode sumber</h3>')
        for s in srcs:
            code = open(os.path.join(base, s), encoding='utf-8').read()
            parts.append(f'<div class="src-title">{folder}/{s}</div><pre class="code src long"><code>{C.hl(code, "python")}</code></pre>')
        parts.append('</section>')
    return ''.join(parts)

HOWTO = """
<section class="legal">
<h2>Tentang buku ini</h2>
<p><b>Python Intensive Bootcamp — Buku Solusi</b> memuat solusi lengkap untuk <b>%(n)d latihan dan mini project</b> pada buku kerja Hari 1–6, ditambah contoh capstone utuh sebagai lampiran. Setiap solusi dijalankan sungguhan: output dan hasil pemeriksa adalah hasil eksekusi nyata.</p>
<h3>Cara membaca setiap latihan</h3>
<ul>
<li><b>Soal</b> — instruksi latihan persis seperti di buku kerja.</li>
<li><b>Pendekatan (pseudocode)</b> — kerangka berpikir sebelum menulis kode (kotak kuning).</li>
<li><b>Solusi</b> — kode jawaban (kotak gelap).</li>
<li><b>Output</b> — hasil menjalankan solusi (kotak hijau; grafik ditampilkan bila ada).</li>
<li><b>Hasil pemeriksa</b> — keluaran sel pemeriksa jawaban otomatis pada buku kerja (kotak ungu).</li>
</ul>
<h3>Saran belajar</h3>
<ul>
<li><b>Coba dulu sendiri.</b> Kerjakan latihan di buku kerja; buka buku ini hanya setelah mencoba, atau untuk membandingkan.</li>
<li>Solusi di sini adalah <b>salah satu</b> cara yang benar. Jika jawaban Anda lolos pemeriksa, itu juga benar.</li>
<li>Buka petunjuk pseudocode lebih dulu bila buntu, baru lihat kode.</li>
<li>Bagian <b>Lampiran</b> memuat contoh capstone lengkap (kode, grafik, dokumentasi) untuk dibaca, dijalankan, dan dimodifikasi.</li>
</ul>
<h3>Isi per hari</h3>
<table><tr><th>Hari</th><th>Topik</th><th>Latihan</th></tr>%(rows)s</table>
<p style="margin-top:14pt;color:#64748b;font-size:8.5pt">© %(y)s %(o)s. Seluruh hak dilindungi. Dilarang memperbanyak atau mendistribusikan ulang tanpa izin tertulis.</p>
</section>
"""

def run():
    toc, chapters, rows, total = [], [], [], 0
    for day, fn, short, tag in DAYS:
        h, n = day_html(day, fn, short, tag, toc)
        chapters.append(h); total += n; rows.append(f'<tr><td>{day}</td><td>{C.esc(short)}</td><td>{n}</td></tr>')
    chapters.append(appendix(toc))
    howto = HOWTO % {'n': total, 'rows': ''.join(rows), 'y': YEAR, 'o': OWNER}
    def make(pages):
        cov = C.cover('Python Intensive Bootcamp', 'Buku Solusi<br>Semua Latihan, Lengkap', f'Solusi bertahap untuk {total} latihan dan mini project, lengkap dengan output, hasil pemeriksa, dan contoh capstone utuh.',
                      f'{total} solusi · Edisi 1', 'def solusi(soal):<br>&nbsp;&nbsp;&nbsp;&nbsp;return jawaban', f'{OWNER} · {YEAR}')
        return C.page('Python Intensive Bootcamp — Buku Solusi', cov + howto + C.toc_html(toc, pages) + ''.join(chapters))
    build_book('solusi', make, toc, os.path.join(OUT, 'Python-Intensive-Bootcamp-Buku-Solusi.pdf'))
