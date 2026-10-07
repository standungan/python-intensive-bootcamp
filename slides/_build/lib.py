"""DSL kecil untuk menyusun slide HTML (dipakai oleh build.py)."""
import html, json

def esc(s): return html.escape(str(s), quote=False)
def _j(o): return html.escape(json.dumps(o, ensure_ascii=False, separators=(',', ':')), quote=True)

def _step(step, anim=None, extra=''):
    a = ''
    if anim: a += f' data-anim="{anim}"'
    if step is not None: a += f' data-step="{step}"'
    return a + extra

def h2(text, tag=None):
    t = f'<span class="tag">{esc(tag)}</span>' if tag else ''
    return f'<h2 data-anim="up">{t}{text}</h2>'

def p(text, cls='', step=None, anim='up'):
    return f'<p class="{cls}"{_step(step, anim)}>{text}</p>'

def ul(items, start=1, steps=True, cls='', ordered=False, anim=None):
    tag = 'ol' if ordered else 'ul'
    out = []
    for i, it in enumerate(items):
        st = (start + i) if steps else None
        out.append(f'<li{_step(st, anim)}>{it}</li>')
    return f'<{tag} class="{cls}">' + ''.join(out) + f'</{tag}>'

def chk(items, start=1):
    return '<ul class="chk">' + ''.join(f'<li data-step="{start+i}"><span>{t}</span></li>' for i, t in enumerate(items)) + '</ul>'

def code(src, lang='py', focus=None, reveal=None, size='', step=None, anim='up', style=''):
    d = f' data-lang="{lang}"'
    if focus: d += f' data-focus="{_j({str(k): v for k, v in focus.items()})}"'
    if reveal: d += f' data-reveal="{_j(reveal)}"'
    cls = 'code' + (' term' if lang == 'bash' else '') + (f' {size}' if size else '')
    st = f' style="{style}"' if style else ''
    return f'<pre class="{cls}"{d}{_step(step, anim)}{st}><code>{esc(src)}</code></pre>'

def out(lines, start=None, err=False, step=None, style=''):
    """lines: str atau list; jika start diberikan, baris ke-i muncul di langkah start+i."""
    cls = 'out err' if err else 'out'
    st = f' style="{style}"' if style else ''
    if isinstance(lines, str): lines = [lines]
    if start is None:
        return f'<div class="{cls}"{_step(step)}{st}>' + '\n'.join(esc(l) for l in lines) + '</div>'
    body = ''.join(f'<span data-step="{start+i}">{esc(l)}</span>' for i, l in enumerate(lines))
    return f'<div class="{cls}"{st}>{body}</div>'

def callout(text, kind='', step=None, anim='up'):
    return f'<div class="callout {kind}"{_step(step, anim)}>{text}</div>'

def card(body, title=None, step=None, anim='up', cls=''):
    t = f'<h3>{title}</h3>' if title else ''
    return f'<div class="card {cls}"{_step(step, anim)}>{t}{body}</div>'

def widget(name, cfg, step=None, style=''):
    st = f' style="{style}"' if style else ''
    return f'<div class="w" data-w="{name}" data-cfg="{_j(cfg)}"{_step(step)}{st}></div>'

def row(*cols, gap=None, cls=''):
    st = f' style="gap:{gap}px"' if gap is not None else ''
    return f'<div class="row {cls}"{st}>' + ''.join(cols) + '</div>'

def col(*items, cls='', style=''):
    st = f' style="{style}"' if style else ''
    return f'<div class="col {cls}"{st}>' + ''.join(items) + '</div>'

def grid(n, *cards, style=''):
    st = f' style="{style}"' if style else ''
    return f'<div class="grid{n} stagger"{st}>' + ''.join(cards) + '</div>'

def table(head, rows, start=None):
    th = ''.join(f'<th>{h}</th>' for h in head)
    body = ''
    for i, r in enumerate(rows):
        st = f' data-step="{start+i}"' if start is not None else ''
        body += f'<tr{st}>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return f'<table class="t" data-anim="up"><tr>{th}</tr>{body}</table>'

def slide(*parts, layout='content', notes='', title=None, transition=None):
    a = f' data-title="{html.escape(title, quote=True)}"' if title else ''
    if transition: a += f' data-transition="{transition}"'
    n = f'<aside class="notes">{notes}</aside>' if notes else ''
    return f'<section class="slide {layout}"{a}>' + ''.join(parts) + n + '</section>'

def title_slide(day, title, sub, pills, glyphs='', notes=''):
    body = ('<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>'
            f'<div class="kicker" data-anim="up">Python Intensive Bootcamp · Hari {day}</div>'
            f'<h1 data-anim="up" style="--d:.1s">{title}</h1>'
            f'<div class="sub" data-anim="up" style="--d:.2s">{sub}</div>'
            '<div class="meta" data-anim="up" style="--d:.35s">' + ''.join(f'<span class="pill">{esc(x)}</span>' for x in pills) + '</div>'
            + (f'<div class="glyphs" data-anim="left" style="--d:.5s">{glyphs}</div>' if glyphs else ''))
    return slide(body, layout='title', notes=notes, title=title, transition='zoom')

def section(num, title, sub='', notes=''):
    body = (f'<div class="num" data-anim="zoom">{num}</div><h1 data-anim="up" style="--d:.15s">{title}</h1>'
            + (f'<p class="mut big" data-anim="up" style="--d:.25s">{sub}</p>' if sub else ''))
    return slide(body, layout='section', notes=notes, title=f'{num}. {title}', transition='rise')

def work(ids, minutes, where, text='', notes='', title='Sekarang coba!'):
    body = ('<div class="badge" data-anim="pop">SEKARANG COBA!</div>'
            f'<h1 data-anim="up" style="--d:.1s">{title if title!="Sekarang coba!" else "Kerjakan di buku kerja"}</h1>'
            '<div class="ids" data-anim="up" style="--d:.2s">' + ''.join(f'<span>{esc(i)}</span>' for i in ids) + '</div>'
            f'<div class="how" data-anim="up" style="--d:.3s">{where}</div>'
            + (f'<p class="mut" data-anim="up" style="--d:.35s">{text}</p>' if text else '')
            + widget('timer', {'m': minutes}, style='margin-top:14px'))
    return slide(body, layout='work', notes=notes, title=f'Latihan: {", ".join(ids)}', transition='zoom')

def page(day, title, slides, accent='#38bdf8', accent_light='#0b7bbd', css_path='assets/deck.css', js_path='assets/deck.js'):
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hari {day} — {esc(title)} · Python Intensive Bootcamp</title>
<link rel="stylesheet" href="{css_path}">
<style>:root{{--acc:{accent}}}html.light{{--acc:{accent_light}}}</style></head>
<body><div id="stage"><div id="deck" data-transition="slide">
{chr(10).join(slides)}
</div></div>
<script src="{js_path}"></script></body></html>
'''
