"""Membangun dua produk PDF:  python3 build.py [materi|solusi]   (default: keduanya)
Kebutuhan: mistune, pygments, pypdf (nomor halaman daftar isi), Node + Playwright + Chromium."""
import os, re, subprocess, sys, json, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C

ROOT = os.path.abspath(os.path.join(C.HERE, '..', '..'))
OUT = os.path.join(ROOT, 'produk')
YEAR = '2026'
OWNER = 'Python Intensive Bootcamp'   # ubah sesuai nama penerbit/penulis
COLORS = ['#f59e0b', '#0ea5e9', '#10b981', '#8b5cf6', '#f97316', '#ec4899', '#14b8a6']

def render(html_path, pdf_path):
    subprocess.run(['node', os.path.join(C.HERE, 'render.js'), html_path, pdf_path], check=True,
                   env={**os.environ, 'NODE_PATH': os.environ.get('NODE_PATH', '/opt/node22/lib/node_modules:/opt/node-tools/node_modules')})

def page_map(pdf_path, toc):
    """Cocokkan entri daftar isi dengan outline PDF (berurutan) -> {id: nomor halaman}."""
    from pypdf import PdfReader
    rd = PdfReader(pdf_path); flat = []
    def walk(o):
        for it in o:
            if isinstance(it, list): walk(it)
            else: flat.append((it.title.strip(), rd.get_destination_page_number(it) + 1))
    walk(rd.outline)
    res, ptr = {}, 0
    for lv, text, hid in toc:
        for j in range(ptr, len(flat)):
            if re.sub(r'\s+', '', flat[j][0]) == re.sub(r'\s+', '', text):
                res[hid] = f'{flat[j][1]}'; ptr = j + 1; break
    return res, len(rd.pages)

def build_book(name, make_html, toc, out_pdf):
    """make_html(pages) -> html; dua lintasan agar daftar isi memuat nomor halaman."""
    tmp = tempfile.mkdtemp(prefix='produk_')
    h = os.path.join(tmp, name + '.html'); p1 = os.path.join(tmp, name + '-1.pdf')
    open(h, 'w', encoding='utf-8').write(make_html({}))
    render(h, p1)
    pages, n1 = page_map(p1, toc)
    missing = [t for _, t, i in toc if i not in pages]
    if missing: print('PERINGATAN: entri daftar isi tanpa halaman:', missing[:5])
    open(h, 'w', encoding='utf-8').write(make_html(pages))
    render(h, out_pdf)
    from pypdf import PdfReader
    n = len(PdfReader(out_pdf).pages)
    print(f'{os.path.basename(out_pdf)}: {n} halaman, {os.path.getsize(out_pdf)/1e6:.1f} MB (lintasan 1: {n1} hlm)')
    return n

if __name__ == '__main__':
    which = sys.argv[1:] or ['materi', 'solusi']
    if 'materi' in which:
        import build_materi; build_materi.run()
    if 'solusi' in which:
        import build_solusi; build_solusi.run()
