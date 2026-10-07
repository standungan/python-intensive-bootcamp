from lib import *
from runner import run, run_err, run_tmp

def blk(r0, r1, c0, c1):
    return [[r, c] for r in range(r0, r1 + 1) for c in range(c0, c1 + 1)]

def build():
    S = []
    S.append(title_slide(4, 'NumPy & Pandas', 'Mengolah data numerik dan tabular — dari array sampai laporan',
        ['6 jam', 'Modul 4', 'Buku Kerja Hari 4'], glyphs='df.groupby("prodi")<br>&nbsp;&nbsp;["ipk"].mean()',
        notes='<b>Pembukaan (±10 menit).</b> Ulas Hari 3. Hari ini kita beralih dari "program" ke "data": array untuk komputasi cepat, DataFrame untuk tabel.'))
    S.append(slide(h2('Agenda Hari 4'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Opening', 'm': 20}, {'t': 'NumPy', 'm': 90}, {'t': 'Rehat', 'm': 20, 'c': '#64748b'}, {'t': 'Pandas dasar', 'm': 70},
        {'t': 'Cleaning & operasi', 'm': 70}, {'t': 'Mini project', 'm': 70, 'c': 'var(--ok)'}, {'t': 'Rekap', 'm': 20}]}),
        p('Total ±6 jam. Demo singkat → peserta coba di buku kerja.', 'mut', step=8), notes='Total 360 menit.', title='Agenda'))
    S.append(slide(h2('Setelah hari ini Anda bisa…'), chk([
        'membuat &amp; mengiris array NumPy, boolean masking, broadcasting', 'menghitung statistik (mean, std, korelasi) dengan axis',
        'membuat Series &amp; DataFrame; seleksi dengan <code class="i">[]</code>, <code class="i">loc</code>, <code class="i">iloc</code>',
        'membersihkan data: missing values, duplikat, tipe data', 'meringkas data: <code class="i">groupby</code>, <code class="i">merge</code>, <code class="i">pivot_table</code>',
        'membuat laporan akhir dari dataset kotor']), notes='Tujuan hari ini.', title='Tujuan'))

    S.append(section('A', 'NumPy', 'Array, indexing, masking, dan broadcasting', notes='Blok 90 menit: konsep (55) + latihan L1–L9 (35).'))
    c1 = 'import numpy as np\nlist_a = [1, 2, 3]\narr = np.array([1, 2, 3])\nprint(list_a * 2)\nprint(arr * 2)\nprint(arr.dtype, arr.shape)'
    S.append(slide(h2('Mengapa array, bukan list?', 'NumPy'),
        code(c1, size='sm', reveal=[1, 1, 1, 2, 3, 4], focus={1: [1, 2], 2: [3], 3: [4], 4: [5]}), out(run(c1), start=2),
        callout('Operasi array berlaku untuk <b>seluruh elemen sekaligus</b> (vectorized) — lebih ringkas dan jauh lebih cepat.', step=5),
        notes='<code>list * 2</code> menggandakan list; <code>array * 2</code> mengalikan tiap elemen.', title='List vs array'))
    c2 = 'import numpy as np\narr = np.arange(12).reshape(3, 4)\nprint(arr[1, 2])\nprint(arr[:, 1])\nprint(arr[0:2, 1:3])'
    S.append(slide(h2('Indexing & slicing 2D', 'NumPy'),
        row(code(c2, size='sm', focus={1: [1], 2: [2], 3: [3], 4: [4]}, style='flex:1.1'),
            col(widget('grid', {'rows': [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 'head': ['0', '1', '2', '3'], 'idx': ['0', '1', '2'], 'cw': 84,
                                'hl': [{'at': 2, 'cells': [[1, 2]], 'cls': 'b'}, {'at': 3, 'cells': ['c:1'], 'cls': 'a'}, {'at': 4, 'cells': blk(0, 1, 1, 2), 'cls': 'g'}]}),
                out(run(c2), start=2)), gap=26),
        notes='Format: <code>arr[baris, kolom]</code>. <code>:</code> = semua. <code>0:2</code> = baris 0 dan 1 (akhir eksklusif).', title='Slicing'))
    c3 = 'import numpy as np\nnilai = np.array([55, 80, 45, 90, 70])\nlulus = nilai >= 60\nprint(lulus)\nprint(nilai[lulus])\nprint(np.where(nilai >= 60, "lulus", "remedi"))'
    S.append(slide(h2('Boolean masking & np.where', 'NumPy'),
        row(col(code(c3, size='xs', focus={1: [2], 2: [3], 3: [4], 4: [5]}), out(run(c3), start=2)),
            widget('conv', {'items': ['55', '80', '45', '90', '70'], 'fn': 'nilai >= 60', 'keep': [False, True, False, True, True], 'out': ['80', '90', '70'], 'lin': 'nilai', 'lout': 'nilai[mask]'}, step=2), gap=26),
        notes='Mask berisi True/False per elemen; <code>nilai[mask]</code> mengambil yang True. <code>np.where</code> = if-else untuk seluruh array.', title='Masking'))
    c4 = 'import numpy as np\nm = np.array([[1, 2, 3], [4, 5, 6]])\nprint(m.sum(axis=0))\nprint(m.mean(axis=1))\nprint(m + np.array([10, 20, 30]))'
    S.append(slide(h2('Agregasi per axis & broadcasting', 'NumPy'),
        row(code(c4, size='xs', focus={1: [2], 2: [3], 3: [4]}, style='flex:1.1'),
            col(widget('grid', {'rows': [[1, 2, 3], [4, 5, 6]], 'head': ['kol 0', 'kol 1', 'kol 2'], 'idx': ['b0', 'b1'], 'cw': 100, 'hl': [{'at': 1, 'cells': ['c:0', 'c:1', 'c:2'], 'cls': 'b'}, {'at': 2, 'cells': ['r:0', 'r:1'], 'cls': 'g'}, {'at': 3, 'cells': ['all'], 'cls': 'a'}]}),
                out(run(c4), start=1)), gap=26),
        callout('<b>axis=0</b> → turun per kolom · <b>axis=1</b> → menyamping per baris. Broadcasting: vektor 3 elemen "ditarik" ke kedua baris.', step=4),
        notes='Klik 1: axis=0 (biru, per kolom). Klik 2: axis=1 (hijau, per baris). Klik 3: broadcasting menambah vektor ke setiap baris.', title='Axis & broadcasting'))
    S.append(work(['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9'], 35, 'Buka <b>workbook/hari4-numpy-pandas.ipynb</b> → Bagian A', 'Array, indexing, masking, <code>np.where</code>, normalisasi min-max, korelasi, diagonal.', notes='35 menit.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 20}, style='margin-top:40px;align-self:center'),
        p('Berikutnya: <b>Pandas</b>.', 'mut center', anim='up'), notes='20 menit.', layout='content work', title='Rehat'))

    S.append(section('B', 'Pandas — Series & DataFrame', 'Tabel data dengan label', notes='Blok 70 menit: konsep (40) + latihan L10–L14 (30).'))
    c5 = 'import pandas as pd\ndf = pd.DataFrame({\n    "nama": ["Ani", "Budi", "Cici", "Dedi"],\n    "prodi": ["IF", "SI", "IF", "SI"],\n    "ipk": [3.5, 3.9, 3.2, 3.6],\n})\nprint(df)\nprint(df.shape)\nprint(df.dtypes)'
    S.append(slide(h2('DataFrame — tabel di Python', 'Pandas'),
        row(code(c5, size='xs', focus={1: [1, 2, 3, 4, 5, 6], 2: [7], 3: [8], 4: [9]}, style='flex:1.1'), out(run(c5), start=2, style='flex:.9;margin-top:0'), gap=24),
        notes='Kolom = Series. <code>shape</code> = (baris, kolom). <code>dtypes</code> menunjukkan tipe tiap kolom (pandas 3: teks bertipe <code>str</code>).', title='DataFrame'))
    c6 = 'import pandas as pd\ndf = pd.DataFrame({"nama": ["Ani", "Budi", "Cici", "Dedi"], "prodi": ["IF", "SI", "IF", "SI"], "ipk": [3.5, 3.9, 3.2, 3.6]})\nprint(df["ipk"].mean())\nprint(df.loc[1, "nama"])\nprint(df.iloc[0:2, 1:3])\nprint(df[df["ipk"] >= 3.5])'
    S.append(slide(h2('Seleksi: [], loc, iloc, filter', 'Pandas'),
        row(col(code('df["ipk"].mean()\ndf.loc[1, "nama"]\ndf.iloc[0:2, 1:3]\ndf[df["ipk"] >= 3.5]', size='sm', focus={1: [0], 2: [1], 3: [2], 4: [3]}),
                out(run(c6), start=1, style='font-size:19px')),
            widget('grid', {'rows': [['Ani', 'IF', '3.5'], ['Budi', 'SI', '3.9'], ['Cici', 'IF', '3.2'], ['Dedi', 'SI', '3.6']], 'head': ['nama', 'prodi', 'ipk'], 'idx': ['0', '1', '2', '3'], 'cw': 110,
                            'hl': [{'at': 1, 'cells': ['c:2'], 'cls': 'b'}, {'at': 2, 'cells': [[1, 0]], 'cls': 'a'}, {'at': 3, 'cells': blk(0, 1, 1, 2), 'cls': 'g'}, {'at': 4, 'cells': ['r:0', 'r:1', 'r:3'], 'cls': 'b'}]}), gap=26),
        notes='<b>loc</b> pakai label, <b>iloc</b> pakai posisi. Filter: kondisi boolean di dalam <code>df[...]</code>.', title='Seleksi'))
    c7 = 'import pandas as pd\ndf = pd.DataFrame({"nama": ["Ani", "Budi", "Cici", "Dedi"], "ipk": [3.5, 3.9, 3.2, 3.6]})\ndf["status"] = df["ipk"].apply(lambda x: "cumlaude" if x >= 3.5 else "reguler")\nprint(df.sort_values("ipk", ascending=False).head(3))'
    S.append(slide(h2('Kolom baru, sort, head', 'Pandas'),
        code('df["status"] = df["ipk"].apply(lambda x: "cumlaude" if x >= 3.5 else "reguler")\ndf.sort_values("ipk", ascending=False).head(3)', size='xs', reveal=[1, 2], focus={1: [0], 2: [1]}), out(run(c7), start=2),
        notes='Tambah kolom turunan dengan <code>apply</code> / operasi vektor; urutkan dengan <code>sort_values</code>.', title='Kolom baru'))
    S.append(work(['L10', 'L11', 'L12', 'L13', 'L14'], 30, 'Buka <b>workbook/hari4-numpy-pandas.ipynb</b> → Bagian B', 'Series, DataFrame, seleksi, kolom status &amp; grade, sorting.', notes='30 menit.'))

    S.append(section('C', 'Cleaning & Operasi Lanjutan', 'Missing values, groupby, merge, pivot', notes='Blok 70 menit: konsep (40) + latihan L15–L19 (30).'))
    c8 = 'import pandas as pd, numpy as np\ndf = pd.DataFrame({"nama": ["Ani", "Budi", "Budi", "Cici"], "nilai": [80, np.nan, np.nan, 70]})\nprint(df.isna().sum())\ndf = df.drop_duplicates()\ndf["nilai"] = df["nilai"].fillna(df["nilai"].mean())\nprint(df)'
    S.append(slide(h2('Missing values & duplikat', 'Cleaning'),
        row(col(code(c8, size='xs', focus={1: [1], 2: [2], 3: [3], 4: [4, 5]}), out(run(c8), start=1, style='font-size:17px')),
            widget('grid', {'rows': [['Ani', '80'], ['Budi', 'NaN'], ['Budi', 'NaN'], ['Cici', '70']], 'head': ['nama', 'nilai'], 'idx': ['0', '1', '2', '3'], 'cw': 110,
                            'hl': [{'at': 1, 'cells': [[1, 1], [2, 1]], 'cls': 'x'}, {'at': 2, 'cells': ['r:2'], 'cls': 'x'}, {'at': 3, 'clear': True}, {'at': 3, 'cells': [[1, 1]], 'cls': 'g'}],
                            'vals': [{'at': 3, 'cells': [[1, 1]], 'text': '75.0'}]}), gap=24),
        notes='Klik: temukan NaN → hapus duplikat (baris 2) → isi NaN dengan rata-rata (75.0).', title='Missing & duplikat'))
    c9 = 'import pandas as pd\ndf = pd.DataFrame({"prodi": ["IF", "SI", "IF", "SI"], "ipk": [3.5, 3.9, 3.2, 3.6]})\nprint(df.groupby("prodi")["ipk"].agg(["mean", "count"]))'
    S.append(slide(h2('groupby — pisah, hitung, gabung', 'Pandas'),
        row(col(code('df.groupby("prodi")["ipk"]\n  .agg(["mean", "count"])', size='sm', step=1), out(run(c9), start=2),
                p('Split → Apply → Combine', 'acc big', step=3)),
            widget('chart', {'kind': 'bar', 'labels': ['IF', 'SI'], 'series': [{'name': 'rata-rata IPK', 'data': [3.35, 3.75]}], 'w': 520, 'h': 330, 'ymax': 4, 'title': 'Rata-rata IPK per prodi', 'yl': 'IPK'}, step=2), gap=24),
        notes='IF: (3.5+3.2)/2 = 3.35. SI: (3.9+3.6)/2 = 3.75. Grafik muncul bertahap saat Anda klik.', title='groupby'))
    c10 = 'import pandas as pd\nmhs = pd.DataFrame({"nim": [1, 2, 3], "nama": ["Ani", "Budi", "Cici"]})\nnilai = pd.DataFrame({"nim": [1, 2, 4], "skor": [90, 80, 70]})\nprint(mhs.merge(nilai, on="nim", how="left"))'
    S.append(slide(h2('merge — gabung tabel lewat kunci', 'Pandas'),
        widget('merge', {'left': {'t': 'mhs', 'head': ['nim', 'nama'], 'rows': [['1', 'Ani'], ['2', 'Budi'], ['3', 'Cici']], 'key': 0},
                         'right': {'t': 'nilai', 'head': ['nim', 'skor'], 'rows': [['1', '90'], ['2', '80'], ['4', '70']], 'key': 0},
                         'res': {'t': 'how="left"', 'head': ['nim', 'nama', 'skor'], 'rows': [['1', 'Ani', '90'], ['2', 'Budi', '80'], ['3', 'Cici', 'NaN']]}, 'matches': [[0, 0], [1, 1]]}),
        out(run(c10), start=4, style='margin-top:10px;font-size:18px'),
        callout('<b>how="left"</b> mempertahankan semua baris kiri; yang tak punya pasangan → <b>NaN</b>. Tipe kolom kunci harus sama!', 'warn', step=4),
        notes='Klik 1: kolom kunci. Klik 2: baris yang cocok (hijau) vs tidak (redup). Klik 3: hasil gabungan.', title='merge'))
    c11 = 'import pandas as pd\ndf = pd.DataFrame({"prodi": ["IF", "IF", "SI", "SI"], "angkatan": [2023, 2024, 2023, 2024], "ipk": [3.5, 3.2, 3.9, 3.6]})\nprint(df.pivot_table(index="prodi", columns="angkatan", values="ipk", aggfunc="mean"))'
    S.append(slide(h2('pivot_table — ringkasan dua dimensi', 'Pandas'),
        code('df.pivot_table(index="prodi", columns="angkatan",\n               values="ipk", aggfunc="mean")', size='sm', step=1), out(run(c11), start=2),
        notes='Baris = prodi, kolom = angkatan, isi = rata-rata ipk.', title='pivot_table'))
    S.append(work(['L15', 'L16', 'L17', 'L18', 'L19'], 30, 'Buka <b>workbook/hari4-numpy-pandas.ipynb</b> → Bagian C', 'Missing &amp; duplikat, konversi tipe, GroupBy, Merge, Pivot + CSV.', notes='30 menit.'))

    S.append(section('D', 'Mini Project', 'Dari data kotor ke laporan', notes='Blok 70 menit: briefing (10) + coding (50) + diskusi (10).'))
    S.append(slide(h2('Pipeline analisis data', 'Mini Project'),
        widget('flow', {'w': 1100, 'h': 150, 'nodes': [
            {'id': 'a', 'x': 0, 'y': 40, 'w': 190, 'h': 66, 't': 'Load\nread_csv', 'k': 'c', 'at': 1}, {'id': 'b', 'x': 225, 'y': 40, 'w': 190, 'h': 66, 't': 'Cleaning\nNaN & tipe', 'k': 'c', 'at': 2},
            {'id': 'c', 'x': 450, 'y': 40, 'w': 190, 'h': 66, 't': 'Merge\ngabung tabel', 'k': 'c', 'at': 3}, {'id': 'd', 'x': 675, 'y': 40, 'w': 190, 'h': 66, 't': 'Analisis\ngroupby, pivot', 'k': 'c', 'at': 4},
            {'id': 'e', 'x': 900, 'y': 40, 'w': 190, 'h': 66, 't': 'Laporan\nto_csv', 'k': 'o', 'at': 5}],
            'edges': [{'a': 'a', 'b': 'b', 'at': 2}, {'a': 'b', 'b': 'c', 'at': 3}, {'a': 'c', 'b': 'd', 'at': 4}, {'a': 'd', 'b': 'e', 'at': 5}]}),
        ul(['<b>P1</b> Kalkulator nilai akhir (dasar)', '<b>P3</b> Merge multi-tabel', '<b>P4</b> Pivot &amp; reporting'], start=6, cls='sm'),
        callout('Pola yang sama dipakai lagi di <b>Capstone (Hari 6)</b>.', step=9),
        notes='Pipeline yang sama dipakai di semua mini project dan capstone. Setiap proyek di workbook punya pemeriksa otomatis.', title='Pipeline'))
    S.append(work(['P1', 'P3', 'P4'], 50, 'Buka <b>workbook/hari4-numpy-pandas.ipynb</b> → Bagian D', 'Kalkulator nilai akhir, merge multi-tabel, pivot &amp; reporting.', notes='50 menit coding + 10 menit diskusi.'))
    e1 = run_err('import pandas as pd\ndf = pd.DataFrame({"nama": ["a"]})\ndf["Nama"]')
    e2 = run_err('import pandas as pd\ndf = pd.DataFrame({"x": [1, 5]})\ndf[df["x"] > 1 and df["x"] < 9]')
    e3 = run_err('import numpy as np\nnp.ones((2, 3)) + np.ones((2,))')
    S.append(slide(h2('Jebakan yang paling sering', 'Troubleshooting'),
        grid(3, card(code('df["Nama"]', size='sm', step=1, anim=None) + out([e1], err=True, step=2, style='font-size:18px'), 'KeyError (nama kolom)', anim=None),
                card(code('df[a > 1 and a < 9]', size='sm', step=3, anim=None) + out([e2[:90] + '…'], err=True, step=4, style='font-size:18px'), 'and / or pada filter', anim=None),
                card(code('shape (2,3) + (2,)', size='sm', step=5, anim=None) + out([e3], err=True, step=6, style='font-size:18px'), 'Broadcasting', anim=None)),
        callout('Perbaikan: <code class="i">df["x"].str.strip()</code> untuk nama kolom · <code class="i">(a &gt; 1) &amp; (a &lt; 9)</code> · samakan shape dengan <code class="i">reshape</code>.', 'ok', step=7),
        notes='Pesan error asli. Juga bahas <b>chained assignment</b>: gunakan <code>.loc</code> atau <code>.copy()</code> (pandas 3 memakai Copy-on-Write).', title='Jebakan umum'))
    S.append(slide(h2('Rekap Hari 4'), chk(['NumPy: array, slicing, masking, <code class="i">np.where</code>, axis, broadcasting', 'Pandas: Series/DataFrame, <code class="i">loc/iloc</code>, filter, kolom baru, sort',
        'Cleaning: missing values, duplikat, <code class="i">to_numeric</code>', 'Ringkasan: <code class="i">groupby</code>, <code class="i">merge</code>, <code class="i">pivot_table</code>', 'Mini project pipeline data end-to-end']),
        p('<b>Besok (Hari 5):</b> Visualisasi, API &amp; Scraping', 'acc big', step=6), notes='Minta peserta menjalankan sel Rekap hasil latihan.', title='Rekap'))
    return S
