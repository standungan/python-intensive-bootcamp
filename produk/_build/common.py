"""Pembangun HTML cetak untuk produk PDF (buku materi dan buku solusi)."""
import base64, html, mimetypes, re, os
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name, TextLexer
from pygments.formatters import HtmlFormatter

HERE = os.path.dirname(os.path.abspath(__file__))
FMT = HtmlFormatter(nowrap=True, classprefix='k-')
TITLE = 'Python Intensive Bootcamp'

def esc(s): return html.escape(str(s), quote=False)
def slug(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')[:60]

def data_uri(path):
    mt = mimetypes.guess_type(path)[0] or 'image/png'
    return f'data:{mt};base64,' + base64.b64encode(open(path, 'rb').read()).decode()

def hl(code, lang):
    try: lex = get_lexer_by_name(lang) if lang else TextLexer()
    except Exception: lex = TextLexer()
    return highlight(code.rstrip('\n'), lex, FMT)

class R(mistune.HTMLRenderer):
    """Renderer: heading bergeser, id unik, alert GitHub, blok output, gambar tertanam."""
    def __init__(self, base_dir, shift=1, id_prefix='', collect=None):
        super().__init__(escape=False)
        self.base, self.shift, self.pre, self.collect = base_dir, shift, id_prefix, collect
        self.last_label = ''; self.n = 0

    def heading(self, text, level, **attrs):
        lv = min(6, level + self.shift); self.n += 1
        hid = f'{self.pre}h{self.n}'
        if self.collect is not None: self.collect.append((lv, html.unescape(re.sub(r'<[^>]+>', '', text)), hid))
        return f'<h{lv} id="{hid}">{text}</h{lv}>\n'

    def paragraph(self, text):
        plain = re.sub(r'<[^>]+>', '', text).strip()
        self.last_label = plain.lower() if re.match(r'^(contoh )?output', plain, re.I) else ''
        cls = ' class="outlabel"' if self.last_label else ''
        return f'<p{cls}>{text}</p>\n'

    def block_code(self, code, info=None):
        lang = (info or '').split()[0] if info else ''
        if self.last_label:
            self.last_label = ''
            return f'<pre class="out"><code>{esc(code.rstrip())}</code></pre>\n'
        if lang in ('text', 'txt', '') and code.lstrip().lower().startswith(('pseudocode', 'pseudo-code')):
            return f'<pre class="pseudo"><code>{esc(code.rstrip())}</code></pre>\n'
        if lang in ('text', 'txt', 'markdown', 'md', ''):
            return f'<pre class="plain"><code>{esc(code.rstrip())}</code></pre>\n'
        lang = {'powershell': 'powershell', 'bash': 'bash', 'py': 'python'}.get(lang, lang)
        return f'<pre class="code lang-{lang}"><code>{hl(code, lang)}</code></pre>\n'

    def image(self, text, url, title=None):
        path = url if os.path.isabs(url) else os.path.normpath(os.path.join(self.base, url))
        src = data_uri(path) if os.path.exists(path) else url
        return f'<img src="{src}" alt="{esc(text)}">'

    def block_quote(self, text):
        m = re.match(r'\s*<p>\[!(NOTE|TIP|WARNING|IMPORTANT|CAUTION)\]\s*(?:<br\s*/?>)?\s*', text)
        if m:
            kind = m.group(1); body = text[m.end():]
            body = '<p>' + body if not body.startswith('<p') else body
            label = {'NOTE': 'Catatan', 'TIP': 'Tips', 'WARNING': 'Perhatian', 'IMPORTANT': 'Penting', 'CAUTION': 'Hati-hati'}[kind]
            return f'<div class="callout {kind.lower()}"><div class="ct">{label}</div>{body}</div>\n'
        return f'<blockquote>{text}</blockquote>\n'

def md_to_html(text, base_dir, shift=1, id_prefix='', collect=None):
    md = mistune.create_markdown(renderer=R(base_dir, shift, id_prefix, collect), plugins=['table', 'task_lists', 'strikethrough'])
    return md(text)

CSS = r'''
@page { size: A4; margin: 22mm 18mm 22mm 18mm;
  @bottom-left { content: "%(title)s"; font: 8pt "Liberation Sans", sans-serif; color: #64748b; }
  @bottom-right { content: counter(page); font: 8pt "Liberation Sans", sans-serif; color: #64748b; } }
@page cover { margin: 0; @bottom-left { content: none } @bottom-right { content: none } }
@page opener { @bottom-left { content: none } @bottom-right { content: none } }
:root { --ink:#0f172a; --mut:#475569; --line:#cbd5e1; --acc:#1d4ed8; --bg2:#f1f5f9; }
* { box-sizing: border-box; }
html { font: 10pt/1.55 "Liberation Sans", "DejaVu Sans", sans-serif; color: var(--ink); }
body { margin: 0; }
h1,h2,h3,h4,h5 { font-family: "Liberation Sans", sans-serif; line-height: 1.25; color: #0b1b3f; break-after: avoid; }
h2 { font-size: 17pt; margin: 22pt 0 8pt; padding-bottom: 4pt; border-bottom: 2px solid var(--acc); }
h3 { font-size: 13pt; margin: 16pt 0 6pt; color: var(--acc); }
h4 { font-size: 11pt; margin: 12pt 0 4pt; }
h5 { font-size: 10pt; margin: 10pt 0 3pt; }
p { margin: 0 0 7pt; orphans: 3; widows: 3; }
ul,ol { margin: 0 0 8pt; padding-left: 18pt; } li { margin: 2pt 0; }
li input[type=checkbox] { margin-right: 5pt; }
a { color: var(--acc); text-decoration: none; }
code { font: 8.6pt "DejaVu Sans Mono", monospace; background: var(--bg2); padding: 0.5pt 3pt; border-radius: 3pt; word-break: break-word; }
pre { margin: 6pt 0 8pt; padding: 7pt 9pt; border-radius: 5pt; font: 8pt/1.45 "DejaVu Sans Mono", monospace; white-space: pre-wrap; word-break: break-word; overflow-wrap: anywhere; }
pre code { font: inherit; background: none; padding: 0; word-break: inherit; }
pre.code { background: #0f172a; color: #e2e8f0; border: 1px solid #1e293b; break-inside: avoid; }
pre.code.long { break-inside: auto; }
pre.out { background: #ecfdf5; color: #064e3b; border-left: 3pt solid #10b981; break-inside: avoid; }
pre.plain { background: var(--bg2); color: #1e293b; border: 1px solid var(--line); break-inside: avoid; }
pre.pseudo { background: #fffbeb; color: #78350f; border-left: 3pt solid #f59e0b; break-inside: avoid; }
pre.err { background: #fef2f2; color: #7f1d1d; border-left: 3pt solid #ef4444; }
p.outlabel { font: bold 7.5pt "Liberation Sans"; letter-spacing: .08em; text-transform: uppercase; color: #047857; margin: 6pt 0 -3pt; break-after: avoid; }
.k-k,.k-kn,.k-kp,.k-kr,.k-kt,.k-ow { color: #f472b6; } .k-kc { color: #fb923c; }
.k-s,.k-s1,.k-s2,.k-sa,.k-sb,.k-sc,.k-sd,.k-se,.k-sh,.k-si,.k-sr,.k-ss,.k-sx { color: #86efac; }
.k-c,.k-c1,.k-cm,.k-cs,.k-cp,.k-ch { color: #94a3b8; font-style: italic; }
.k-m,.k-mi,.k-mf,.k-mh,.k-mo,.k-il { color: #fdba74; }
.k-nf,.k-fm { color: #7dd3fc; } .k-nc,.k-nn { color: #a5b4fc; } .k-nb,.k-bp { color: #7dd3fc; } .k-nd { color: #fbbf24; }
.k-o { color: #f472b6; } .k-err { color: #fecaca; }
table { border-collapse: collapse; width: 100%%; margin: 6pt 0 10pt; font-size: 9pt; break-inside: avoid; }
th { background: #e2e8f0; text-align: left; font-weight: 700; }
th,td { border: 1px solid var(--line); padding: 3.5pt 6pt; vertical-align: top; }
tr:nth-child(even) td { background: #f8fafc; }
blockquote { margin: 6pt 0 9pt; padding: 5pt 10pt; border-left: 3pt solid var(--line); background: var(--bg2); color: #334155; font-size: 9.2pt; }
blockquote p:last-child { margin: 0; }
.callout { margin: 8pt 0 10pt; padding: 6pt 10pt 4pt; border-radius: 5pt; border-left: 4pt solid; break-inside: avoid; font-size: 9.4pt; }
.callout .ct { font: bold 8pt "Liberation Sans"; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 2pt; }
.callout.note { background: #eff6ff; border-color: #3b82f6; } .callout.note .ct { color: #1d4ed8; }
.callout.tip { background: #f0fdf4; border-color: #22c55e; } .callout.tip .ct { color: #15803d; }
.callout.warning,.callout.caution { background: #fffbeb; border-color: #f59e0b; } .callout.warning .ct,.callout.caution .ct { color: #b45309; }
.callout.important { background: #faf5ff; border-color: #a855f7; } .callout.important .ct { color: #7e22ce; }
img { max-width: 100%%; max-height: 120mm; display: block; margin: 6pt auto; border: 1px solid var(--line); border-radius: 4pt; break-inside: avoid; }
hr { border: none; border-top: 1px solid var(--line); margin: 12pt 0; }
/* sampul */
.cover { page: cover; width: 210mm; height: 297mm; padding: 28mm 22mm; color: #fff; display: flex; flex-direction: column; justify-content: space-between;
  background: radial-gradient(circle at 85%% 12%%, #3b82f6 0, transparent 38%%), radial-gradient(circle at 10%% 95%%, #f59e0b55 0, transparent 40%%), linear-gradient(160deg, #0b1b3f 0%%, #0f172a 100%%); break-after: page; }
.cover .kick { font: bold 10pt "Liberation Sans"; letter-spacing: .25em; text-transform: uppercase; color: #93c5fd; }
.cover h1 { font-size: 40pt; line-height: 1.08; margin: 10mm 0 6mm; color: #fff; }
.cover .sub { font-size: 14pt; color: #cbd5e1; max-width: 140mm; line-height: 1.4; }
.cover .badge { display: inline-block; margin-top: 10mm; padding: 4pt 12pt; border: 1px solid #93c5fd; border-radius: 20pt; font: bold 10pt "Liberation Sans"; color: #bfdbfe; }
.cover .glyph { font: 11pt/1.5 "DejaVu Sans Mono"; color: #7dd3fc; opacity: .85; }
.cover .foot { font-size: 9pt; color: #94a3b8; }
.legal { page-break-after: always; }
.legal h2 { border: none; font-size: 15pt; margin-top: 0; }
.legal p, .legal li { font-size: 9.2pt; }
/* daftar isi */
.toc { page-break-after: always; }
.toc h2 { border: none; font-size: 20pt; margin-top: 0; }
.toc .e { display: flex; align-items: baseline; gap: 4pt; font-size: 9.5pt; padding: 1.6pt 0; }
.toc .e a { color: var(--ink); }
.toc .e .dots { flex: 1; border-bottom: 1px dotted #94a3b8; transform: translateY(-2pt); }
.toc .e .pg { font-variant-numeric: tabular-nums; color: var(--mut); }
.toc .e.l1 { margin-top: 8pt; font-weight: 700; font-size: 10.5pt; color: var(--ink); }
.toc .e.l2 { padding-left: 14pt; }
.toc .e.l3 { padding-left: 28pt; font-size: 8.6pt; color: var(--mut); }
/* pembuka bagian */
.opener { page: opener; height: 247mm; display: flex; flex-direction: column; justify-content: center; break-before: page; break-after: page; position: relative; }
.opener .num { font: bold 110pt/1 "Liberation Sans"; color: var(--pc); opacity: .95; }
.opener h1 { font-size: 30pt; margin: 4mm 0 4mm; padding: 0; border: none; color: #0b1b3f; }
.opener .tag { font-size: 12pt; color: var(--mut); max-width: 130mm; }
.opener .bar { width: 40mm; height: 4pt; background: var(--pc); margin: 8mm 0; border-radius: 2pt; }
.opener .toc-mini { font-size: 9.5pt; color: var(--mut); columns: 2; column-gap: 10mm; margin-top: 6mm; }
.opener .toc-mini div { break-inside: avoid; padding: 1pt 0; }
/* buku solusi */
.ex { margin: 12pt 0 16pt; break-inside: auto; }
.ex h3 { margin-top: 18pt; }
.ex .stmt { margin: 0 0 4pt; }
.ex .label { font: bold 7.5pt "Liberation Sans"; letter-spacing: .08em; text-transform: uppercase; margin: 8pt 0 -3pt; break-after: avoid; }
.ex .label.sol { color: #1d4ed8; } .ex .label.out { color: #047857; } .ex .label.chk { color: #7c3aed; } .ex .label.hint { color: #b45309; }
pre.chk { background: #f5f3ff; color: #4c1d95; border-left: 3pt solid #8b5cf6; break-inside: avoid; }
.sec-note { color: var(--mut); font-size: 9.2pt; }
.gallery { display: grid; grid-template-columns: 1fr 1fr; gap: 6pt; }
.gallery img { max-height: 70mm; margin: 0; }
.src-title { font: bold 9pt "DejaVu Sans Mono"; color: var(--mut); margin: 10pt 0 -2pt; }
pre.code.src { font-size: 6.9pt; line-height: 1.38; }
''' % {'title': TITLE}

def page(title, body, extra_css=''):
    return f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>{esc(title)}</title><style>{CSS}{extra_css}</style></head><body>{body}</body></html>'

def cover(kicker, title, sub, badge, glyph, foot):
    return (f'<section class="cover"><div><div class="kick">{esc(kicker)}</div><h1>{title}</h1><div class="sub">{sub}</div>'
            f'<div class="badge">{esc(badge)}</div></div><div class="glyph">{glyph}</div><div class="foot">{foot}</div></section>')

def toc_html(entries, pages=None, title='Daftar Isi'):
    """entries: [(level, text, id)]; pages: {id: nomor halaman}"""
    out = [f'<section class="toc"><h2 style="break-before:avoid">{esc(title)}</h2>']
    for lv, text, hid in entries:
        pg = (pages or {}).get(hid, '00')
        out.append(f'<div class="e l{lv}"><a href="#{hid}">{esc(text)}</a><span class="dots"></span><span class="pg">{pg}</span></div>')
    out.append('</section>')
    return '\n'.join(out)

def opener(num, title, tagline, color, hid, sub_items=()):
    items = ''.join(f'<div>{esc(x)}</div>' for x in sub_items)
    return (f'<section class="opener" style="--pc:{color}"><div class="num">{esc(num)}</div><h1 id="{hid}">{esc(title)}</h1><div class="bar"></div>'
            f'<div class="tag">{esc(tagline)}</div>' + (f'<div class="toc-mini">{items}</div>' if items else '') + '</section>')
