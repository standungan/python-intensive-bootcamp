from lib import *
from runner import run, run_err, run_tmp

def build():
    S = []
    S.append(title_slide(5, 'Visualisasi, API & Scraping', 'Mengubah data menjadi grafik, dan mengambil data dari web dengan etis',
        ['6 jam', 'Modul 5', 'Buku Kerja Hari 5'], glyphs='plt.plot(x, y)<br>requests.get(url)',
        notes='<b>Pembukaan (±10 menit).</b> Ulas Hari 4 (pipeline data). Hari ini: menyajikan data dengan grafik dan mengambil data dari API/web. Catatan: bila jaringan terbatas, buku kerja memakai data contoh/fallback.'))
    S.append(slide(h2('Agenda Hari 5'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Opening', 'm': 15}, {'t': 'Matplotlib', 'm': 60}, {'t': 'Seaborn', 'm': 40}, {'t': 'Rehat', 'm': 20, 'c': '#64748b'},
        {'t': 'API & JSON', 'm': 60}, {'t': 'Scraping & arXiv', 'm': 50}, {'t': 'Mini project', 'm': 100, 'c': 'var(--ok)'}, {'t': 'Rekap', 'm': 15}]}),
        p('Total ±6 jam. Demo singkat → peserta coba di buku kerja.', 'mut', step=9), notes='Total 360 menit.', title='Agenda'))
    S.append(slide(h2('Setelah hari ini Anda bisa…'), chk([
        'membuat line, bar, scatter, histogram, dan subplot dengan Matplotlib', 'memakai Seaborn untuk distribusi, relasi, dan heatmap',
        'memanggil API dengan <code class="i">requests</code> dan mengolah JSON', 'menangani error jaringan (timeout, 404, 429)',
        'melakukan scraping secara etis dengan BeautifulSoup &amp; membaca feed arXiv', 'membangun dashboard dan pipeline data mini']),
        notes='Tujuan hari ini.', title='Tujuan'))

    S.append(section('A', 'Matplotlib', 'Grafik dasar yang jelas dan jujur', notes='Blok 60 menit: konsep (30) + latihan L1–L5 (30).'))
    S.append(slide(h2('Anatomi grafik Matplotlib', 'Matplotlib'),
        row(code('import matplotlib.pyplot as plt\n\nhari = ["Sen", "Sel", "Rab", "Kam", "Jum"]\nsuhu = [30, 32, 31, 29, 33]\n\nfig, ax = plt.subplots()\nax.plot(hari, suhu, marker="o")\nax.set_title("Suhu Harian")\nax.set_xlabel("Hari")\nax.set_ylabel("°C")\nplt.show()', size='xs',
                 focus={1: [5], 2: [6], 3: [7, 8, 9], 4: [10]}, style='flex:1.05;min-width:0'),
            widget('chart', {'kind': 'line', 'labels': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'], 'series': [{'name': 'suhu', 'data': [30, 32, 31, 29, 33]}], 'w': 560, 'h': 360, 'ymax': 40, 'title': 'Suhu Harian', 'xl': 'Hari', 'yl': '°C'}, style='zoom:.85'), gap=22),
        notes='Klik 1: kerangka sumbu. Klik 2: garis digambar. Klik 3: judul &amp; label. Selalu beri <b>judul, label sumbu, satuan</b>.', title='Anatomi grafik'))
    S.append(slide(h2('Pilih jenis grafik sesuai pertanyaan', 'Matplotlib'), table(['Pertanyaan', 'Grafik', 'Fungsi'], [
        ['Bagaimana perubahan dari waktu ke waktu?', 'Line', '<code class="i">ax.plot</code>'], ['Bandingkan antar kategori?', 'Bar', '<code class="i">ax.bar</code>'],
        ['Apakah dua variabel berhubungan?', 'Scatter', '<code class="i">ax.scatter</code>'], ['Bagaimana sebaran nilai?', 'Histogram', '<code class="i">ax.hist</code>'],
        ['Bagian dari keseluruhan (sedikit kategori)?', 'Pie', '<code class="i">ax.pie</code>']], start=1),
        notes='Mulai dari <b>pertanyaan</b>, bukan dari jenis grafik.', title='Memilih grafik'))
    S.append(slide(h2('Bar, scatter, histogram', 'Matplotlib'),
        row(widget('chart', {'kind': 'bar', 'labels': ['IF', 'SI', 'TI'], 'series': [{'name': 'ipk', 'data': [3.4, 3.7, 3.1]}], 'w': 400, 'h': 300, 'ymax': 4, 'title': 'Bar', 'yl': 'IPK'}, step=1, style='zoom:.8'),
            widget('chart', {'kind': 'scatter', 'xs': [2, 4, 5, 7, 8, 9], 'xmax': 10, 'series': [{'name': 'nilai', 'data': [55, 62, 70, 78, 85, 92]}], 'w': 400, 'h': 300, 'ymax': 100, 'title': 'Scatter', 'xl': 'jam belajar'}, step=2, style='zoom:.8'),
            widget('chart', {'kind': 'hist', 'labels': ['50', '60', '70', '80', '90'], 'series': [{'name': 'n', 'data': [2, 5, 9, 6, 3]}], 'w': 400, 'h': 300, 'ymax': 10, 'title': 'Histogram', 'xl': 'nilai'}, step=3, style='zoom:.8'), gap=10),
        code('ax.bar(prodi, ipk)      ax.scatter(jam, nilai)      ax.hist(nilai, bins=5)', size='xs', step=4),
        notes='Tiga grafik muncul bergantian. Bar = kategori, scatter = hubungan, histogram = sebaran.', title='Bar, scatter, histogram'))
    S.append(slide(h2('Subplot & simpan grafik', 'Matplotlib'),
        row(code('fig, axes = plt.subplots(2, 2, figsize=(8, 6))\naxes[0, 0].plot(x, y)\naxes[0, 1].bar(k, v)\naxes[1, 0].hist(data)\naxes[1, 1].scatter(a, b)\nfig.tight_layout()\nfig.savefig("dashboard.png", dpi=150)', size='xs', focus={1: [0], 2: [1], 3: [2], 4: [3], 5: [4], 6: [5, 6]}, style='flex:1.2;min-width:0'),
            widget('grid', {'rows': [['plot', 'bar'], ['hist', 'scatter']], 'cw': 150, 'ch': 90, 'hl': [{'at': 2, 'cells': [[0, 0]], 'cls': 'b'}, {'at': 3, 'cells': [[0, 1]], 'cls': 'g'}, {'at': 4, 'cells': [[1, 0]], 'cls': 'a'}, {'at': 5, 'cells': [[1, 1]], 'cls': 'x'}]}), gap=26),
        callout('Di skrip <code class="i">.py</code> / server tanpa layar, <code class="i">plt.show()</code> tidak tampil → gunakan <code class="i">savefig()</code>.', 'warn', step=7),
        notes='<code>axes[baris, kolom]</code> — mirip indexing array NumPy.', title='Subplot'))
    S.append(work(['L1', 'L2', 'L3', 'L4', 'L5'], 30, 'Buka <b>workbook/hari5-visualisasi-api-scraping.ipynb</b> → Bagian A', 'Line, bar, histogram + garis rata-rata, dashboard 2×2, simpan ke file.', notes='30 menit.'))

    S.append(section('B', 'Seaborn', 'Grafik statistik dengan sedikit kode', notes='Blok 40 menit: konsep (20) + latihan L6–L8 (20).'))
    S.append(slide(h2('Seaborn — langsung dari DataFrame', 'Seaborn'),
        row(code('import seaborn as sns\n\nsns.histplot(df, x="nilai", kde=True)\nsns.boxplot(data=df, x="hari", y="tip")\nsns.scatterplot(data=df, x="jam", y="nilai", hue="prodi")\nsns.heatmap(df.corr(numeric_only=True), annot=True)', size='xs', focus={1: [2], 2: [3], 3: [4], 4: [5]}, style='flex:1.3;min-width:0'),
            col(table(['Grafik', 'Untuk'], [['histplot', 'distribusi'], ['boxplot', 'sebaran + outlier'], ['scatterplot', 'relasi + hue'], ['heatmap', 'korelasi']], start=1)), gap=24),
        callout('Seaborn bekerja <b>di atas Matplotlib</b>: judul/label tetap diatur dengan <code class="i">plt.title()</code> dsb.', step=5),
        notes='Beri nama kolom persis seperti di DataFrame — salah ketik = <b>ValueError</b>.', title='Seaborn'))
    S.append(work(['L6', 'L7', 'L8'], 20, 'Buka <b>workbook/hari5-visualisasi-api-scraping.ipynb</b> → Bagian B', 'Boxplot per hari, heatmap korelasi, countplot &amp; barplot.', notes='20 menit.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 20}, style='margin-top:40px;align-self:center'),
        p('Berikutnya: <b>API &amp; JSON</b>.', 'mut center', anim='up'), notes='20 menit.', layout='content work', title='Rehat'))

    S.append(section('C', 'API & JSON', 'Meminta data dari server', notes='Blok 60 menit: konsep (35) + latihan L9–L11 (25).'))
    S.append(slide(h2('Alur request → response', 'API'),
        widget('seq', {'w': 900, 'h': 270, 'actors': [{'n': 'Program Anda', 'x': 150}, {'n': 'Server API', 'x': 750}],
                       'msgs': [{'f': 0, 't': 1, 'l': 'GET /users?limit=3', 'y': 50, 'at': 1}, {'f': 1, 't': 0, 'l': '200 OK  +  JSON', 'y': 115, 'at': 2}, {'f': 0, 't': 1, 'l': 'GET /halaman-tidak-ada', 'y': 180, 'at': 3, 'bad': True}, {'f': 1, 't': 0, 'l': '404 Not Found', 'y': 235, 'at': 4, 'bad': True}]}, style='align-self:center'),
        code('r = requests.get(url, params={"limit": 3}, timeout=10)\nr.raise_for_status()      # error bila 4xx/5xx\ndata = r.json()', size='xs', step=5),
        notes='Selalu pakai <b>timeout</b> dan <b>raise_for_status()</b>. Kode status: 2xx sukses, 4xx salah di klien, 5xx salah di server, 429 = terlalu sering.', title='Request-response'))
    c1 = 'import json, pandas as pd\nraw = \'{"data": [{"id": 1, "nama": "Ani", "kota": {"nama": "Bandung"}}, {"id": 2, "nama": "Budi", "kota": {"nama": "Medan"}}]}\'\nd = json.loads(raw)\nprint(d["data"][0]["kota"]["nama"])\ndf = pd.json_normalize(d["data"])\nprint(df)'
    S.append(slide(h2('JSON → dict → DataFrame', 'API'),
        row(code(c1.replace('\'{"data": [{"id": 1, "nama": "Ani", "kota": {"nama": "Bandung"}}, {"id": 2, "nama": "Budi", "kota": {"nama": "Medan"}}]}\'', 'respons_json'), size='xs', focus={1: [2], 2: [3], 3: [4, 5]}, style='flex:1.2;min-width:0'),
            out(run(c1), start=2, style='margin-top:0;flex:.9'), gap=24),
        callout('<code class="i">json_normalize</code> meratakan JSON bersarang jadi kolom: <code class="i">kota.nama</code>.', step=4),
        notes='Pada contoh ini <code>respons_json</code> adalah string JSON (dari <code>r.text</code>) berisi daftar pengguna dengan objek bersarang.', title='JSON'))
    c2 = 'import requests\ndef ambil(url):\n    try:\n        r = requests.get(url, timeout=5)\n        r.raise_for_status()\n        return r.json()\n    except requests.exceptions.RequestException as e:\n        print("Gagal:", type(e).__name__)\n        return None'
    S.append(slide(h2('Error handling jaringan', 'API'),
        row(code(c2, size='xs', focus={1: [3, 4, 5], 2: [6, 7, 8]}, style='flex:1.2;min-width:0'),
            col(table(['Kode', 'Arti'], [['200', 'OK'], ['404', 'tidak ditemukan'], ['429', 'terlalu sering — tunggu'], ['5xx', 'server bermasalah']], start=3),
                callout('Siapkan <b>fallback</b>: cache lokal / data contoh agar program tetap jalan offline.', 'ok', step=7)), gap=24),
        notes='Satu <code>except requests.exceptions.RequestException</code> menangkap Timeout, ConnectionError, HTTPError.', title='Error jaringan'))
    S.append(work(['L9', 'L10', 'L11'], 25, 'Buka <b>workbook/hari5-visualisasi-api-scraping.ipynb</b> → Bagian C', 'Struktur JSON, <code>json_normalize</code> + agregasi, mengolah respons cuaca.', notes='25 menit. Data contoh tersedia di notebook bila jaringan terblokir.'))

    S.append(section('D', 'Scraping & arXiv', 'Mengambil data dari halaman web & feed ilmiah', notes='Blok 50 menit: konsep (30) + latihan L12–L13 (20).'))
    S.append(slide(h2('Etika scraping', 'Scraping'), chk(['Baca <code class="i">robots.txt</code> dan Terms of Service situs', 'Beri jeda antar request (rate limit), jangan membanjiri server',
        'Utamakan <b>API resmi</b> bila tersedia', 'Jangan ambil data pribadi / yang dilindungi', 'Cantumkan sumber data pada laporan']),
        notes='Tekankan etika sebelum teknik.', title='Etika'))
    html = '<html><body><h1>Berita</h1><ul><li class="judul">Python 3.14 rilis</li><li class="judul">AI kampus</li></ul></body></html>'
    c3 = 'from bs4 import BeautifulSoup\nhtml = """<ul><li class="judul">Python 3.14 rilis</li><li class="judul">AI kampus</li></ul>"""\nsoup = BeautifulSoup(html, "html.parser")\nfor li in soup.select("li.judul"):\n    print(li.get_text())'
    S.append(slide(h2('BeautifulSoup — menelusuri HTML', 'Scraping'),
        row(widget('tree', {'nodes': [{'t': '<html>', 'k': 'node', 'at': 1}, {'t': '<body>', 'k': 'node', 'd': 1, 'at': 1}, {'t': '<ul>', 'k': 'node', 'd': 2, 'at': 1},
                                      {'t': '<li class="judul">', 'k': 'node', 'd': 3, 'at': 1, 'hl': 2, 'n': 'Python 3.14 rilis'}, {'t': '<li class="judul">', 'k': 'node', 'd': 3, 'at': 1, 'hl': 2, 'n': 'AI kampus'}]}),
            col(code('from bs4 import BeautifulSoup\nsoup = BeautifulSoup(html, "html.parser")\nfor li in soup.select("li.judul"):\n    print(li.get_text())', size='xs', focus={1: [1], 2: [2, 3]}), out(run(c3), start=2)), gap=26),
        notes='<code>soup.select("li.judul")</code> memilih semua &lt;li&gt; berkelas <i>judul</i> (menyala pada klik 2).', title='BeautifulSoup'))
    feed = '<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Paper A</title><published>2025-01-10T00:00:00Z</published></entry><entry><title>Paper B</title><published>2025-02-01T00:00:00Z</published></entry></feed>'
    c4 = 'import xml.etree.ElementTree as ET\nns = {"a": "http://www.w3.org/2005/Atom"}\nroot = ET.fromstring(feed_xml)\nfor e in root.findall("a:entry", ns):\n    print(e.find("a:title", ns).text, e.find("a:published", ns).text[:10])'
    out4 = run('import xml.etree.ElementTree as ET\nfeed_xml = %r\n' % feed + c4)
    S.append(slide(h2('arXiv API — metadata paper', 'arXiv'),
        widget('flow', {'w': 1100, 'h': 110, 'nodes': [
            {'id': 'a', 'x': 0, 'y': 20, 'w': 230, 'h': 64, 't': 'query\nsearch_query=all:LLM', 'k': 'c', 'at': 1}, {'id': 'b', 'x': 290, 'y': 20, 'w': 230, 'h': 64, 't': 'respons\nAtom XML', 'k': 'c', 'at': 2},
            {'id': 'c', 'x': 580, 'y': 20, 'w': 230, 'h': 64, 't': 'parse\nElementTree', 'k': 'c', 'at': 3}, {'id': 'd', 'x': 870, 'y': 20, 'w': 230, 'h': 64, 't': 'DataFrame\nanalisis', 'k': 'o', 'at': 4}],
            'edges': [{'a': 'a', 'b': 'b', 'at': 2}, {'a': 'b', 'b': 'c', 'at': 3}, {'a': 'c', 'b': 'd', 'at': 4}]}),
        code(c4, size='xs', step=5), out(out4, start=6),
        notes='Feed arXiv berformat <b>Atom XML</b> dengan namespace — itu sebabnya <code>ns</code> diperlukan. Notebook menyediakan sampel feed bila jaringan terblokir.', title='arXiv'))
    S.append(work(['L12', 'L13'], 20, 'Buka <b>workbook/hari5-visualisasi-api-scraping.ipynb</b> → Bagian D', 'Mengurai HTML dengan BeautifulSoup dan feed arXiv.', notes='20 menit.'))

    S.append(section('E', 'Mini Project', 'Dashboard, API + visualisasi, pipeline arXiv', notes='Blok 100 menit: briefing (10) + coding (80) + diskusi (10).'))
    S.append(slide(h2('Pilih tingkat tantangan', 'Mini Project'), table(['Project', 'Tema', 'Level'], [
        ['<b>P1</b>', 'Dashboard visualisasi nilai', 'Dasar'], ['<b>P2</b>', 'API + visualisasi', 'Menengah'], ['<b>P3</b>', 'Pipeline paper arXiv', 'Menengah–Tinggi'], ['<b>P4</b>', 'EDA lengkap dataset nyata', 'Tinggi']], start=1),
        callout('Semua proyek memakai pola <b>ambil → bersihkan → analisis → visualisasi → simpan</b>.', step=5),
        notes='Peserta memilih sesuai kemampuan; minimal selesaikan P1. Pemeriksa otomatis tersedia di workbook.', title='Pilih proyek'))
    S.append(work(['P1', 'P2', 'P3', 'P4'], 80, 'Buka <b>workbook/hari5-visualisasi-api-scraping.ipynb</b> → Bagian E', 'Mulai dari yang sesuai levelmu — tiap proyek ada pemeriksa ✅.', notes='80 menit coding + 10 menit diskusi.'))
    e1 = run_err('import matplotlib\nmatplotlib.use("Agg")\nimport matplotlib.pyplot as plt\nplt.plot([1, 2, 3], [4, 5])')
    e2 = run_err('import json\njson.loads("<html>bukan json</html>")')
    e3 = run_err('d = {"error": "rate limit"}\nd["data"]')
    S.append(slide(h2('Jebakan yang paling sering', 'Troubleshooting'),
        grid(3, card(code('plt.plot(x, y)', size='sm', step=1, anim=None) + out([e1], err=True, step=2, style='font-size:18px'), 'x dan y beda panjang', anim=None),
                card(code('json.loads("<html>…")', size='sm', step=3, anim=None) + out([e2], err=True, step=4, style='font-size:18px'), 'JSONDecodeError', anim=None),
                card(code('d["data"]', size='sm', step=5, anim=None) + out([e3], err=True, step=6, style='font-size:18px'), 'KeyError', anim=None)),
        callout('Periksa <code class="i">r.status_code</code> dan key <code class="i">"error"</code> sebelum membaca data; pastikan respons memang JSON.', 'ok', step=7),
        notes='Pesan error asli. Tambahan: 429 (terlalu sering) → beri jeda; Timeout → tambah timeout/retry.', title='Jebakan umum'))
    S.append(slide(h2('Rekap Hari 5'), chk(['Matplotlib: line/bar/scatter/hist, subplot, <code class="i">savefig</code>', 'Seaborn: histplot, boxplot, heatmap dari DataFrame',
        'API: <code class="i">requests</code>, JSON, <code class="i">json_normalize</code>, error handling', 'Scraping etis: BeautifulSoup &amp; feed arXiv', 'Mini project: dashboard &amp; pipeline data']),
        p('<b>Besok (Hari 6):</b> Capstone Project', 'acc big', step=6), notes='Minta peserta menjalankan sel Rekap hasil latihan. Ingatkan memilih jalur capstone malam ini.', title='Rekap'))
    return S
