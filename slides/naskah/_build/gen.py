"""Menggabungkan struktur slide (struktur/*.json, hasil extract.js) dengan narasi (nN.py)
menjadi naskah Markdown per hari. Gagal bila jumlah narasi != jumlah langkah slide."""
import json, os, sys, re, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
OUT = os.path.join(HERE, '..')
DECKS = [(1, 'hari1-python-fundamentals', 'Python Fundamentals'), (2, 'hari2-functions-modules-file-handling', 'Functions, Modules & File Handling'),
         (3, 'hari3-oop', 'Object-Oriented Programming'), (4, 'hari4-numpy-pandas', 'NumPy & Pandas'),
         (5, 'hari5-visualisasi-api-scraping', 'Visualisasi, API & Scraping'), (6, 'hari6-capstone-project', 'Capstone Project')]
WPS = 2.3  # kata per detik (±140 kata/menit, tempo tutorial)

def dur(text, aksi_s=0):
    return max(3, round(len(re.findall(r'\S+', text)) / WPS)) + aksi_s

def fmt(sec):
    m, s = divmod(int(sec), 60)
    return f'{m} mnt {s:02d} dtk' if m else f'{s} dtk'

def entry(e):
    return (e, '') if isinstance(e, str) else (e[0], e[1])

only = {int(a) for a in sys.argv[1:]} or None
summary = []
for day, fn, title in DECKS:
    if only and day not in only: continue
    try: N = importlib.import_module(f'n{day}').N
    except ModuleNotFoundError: continue
    S = json.load(open(os.path.join(HERE, 'struktur', fn + '.json')))
    errs = []
    for s in S:
        got = len(N.get(s['n'], []))
        if got != s['max'] + 1: errs.append(f"slide {s['n']} ({s['title']}): butuh {s['max']+1} narasi, ada {got}")
    extra = set(N) - {s['n'] for s in S}
    if extra: errs.append(f'nomor slide tak dikenal: {sorted(extra)}')
    if errs:
        print(f'Hari {day}: GAGAL'); [print('  ', e) for e in errs]; sys.exit(1)
    lines = [f'# Naskah Video — Hari {day}: {title}', '',
             f'Deck: [`{fn}.html`](../{fn}.html) · {len(S)} slide · {sum(s["max"] for s in S)} klik', '',
             '> **Cara pakai:** buka deck, tekan `F` (layar penuh). Baca narasi per blok, tekan `→` saat tertulis **Klik**. Tanda ⏱ adalah perkiraan durasi baca (±140 kata/menit). Baris **🎬 Aksi** adalah hal yang dilakukan di layar selain menekan `→`.', '']
    total = 0; toc = []
    body = []
    for s in S:
        entries = [entry(e) for e in N[s['n']]]
        sdur = sum(dur(t, 4 if a else 0) for t, a in entries) + 2
        total += sdur
        kind = 'bagian' if 'section' in s['cls'] else 'latihan' if ' work' in s['cls'] and s['max'] == 0 and 'Latihan' in s['title'] else 'judul' if 'title' in s['cls'].split() else 'isi'
        trans = (re.search(r't-(\w+)', s['cls']) or [None, 'slide'])[1]
        toc.append(f"| {s['n']} | {s['title']} | {s['max']} | {fmt(sdur)} |")
        body += [f"### Slide {s['n']} — {s['title']}", '', f"*{kind} · transisi `{trans}` · {s['max']} klik · ⏱ {fmt(sdur)}*", '']
        for i, (t, a) in enumerate(entries):
            if i == 0:
                body += ['**Saat slide muncul**']
            else:
                ap = [x for x in s['steps'][i-1]['appear'] if x]
                tag = f" — muncul: `{ap[0][:70]}`" if ap else ''
                body += [f'**Klik {i} →**{tag}']
            body += ['', '> ' + t.replace('\n', '\n> '), '']
            if a: body += [f'🎬 **Aksi:** {a}', '']
        body += ['---', '']
    lines += [f'**Total perkiraan:** {fmt(total)} (di luar jeda latihan)', '', '| # | Slide | Klik | Durasi |', '|---|---|---|---|'] + toc + ['', '---', ''] + body
    open(os.path.join(OUT, f'hari{day}-naskah.md'), 'w', encoding='utf-8').write('\n'.join(lines))
    summary.append((day, title, len(S), sum(s['max'] for s in S), total))
    print(f'Hari {day}: {len(S)} slide, {sum(s["max"] for s in S)} klik, {fmt(total)}')
