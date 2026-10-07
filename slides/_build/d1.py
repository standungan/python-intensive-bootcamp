from lib import *
from runner import run, run_err

def build():
    S = []
    S.append(title_slide(1, 'Python Fundamentals', 'Variabel, control flow, dan struktur data — dari nol sampai menu interaktif',
        ['6 jam', 'Pemula', 'Modul 1', 'Buku Kerja Hari 1'], glyphs='x = 42<br>if x &gt; 0:<br>&nbsp;&nbsp;print("halo")',
        notes='<b>Pembukaan (±5 menit).</b> Sapa peserta, jelaskan format: instruktur demo singkat → peserta langsung coba di buku kerja Jupyter. Tunjukkan pintasan slide: tekan <b>?</b>.'))
    S.append(slide(h2('Agenda Hari 1'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Opening + setup', 'm': 40}, {'t': 'Variabel & I/O', 'm': 45}, {'t': 'Control flow', 'm': 60},
        {'t': 'Rehat', 'm': 25, 'c': '#64748b'}, {'t': 'Struktur data', 'm': 85}, {'t': 'Mini project', 'm': 75, 'c': 'var(--ok)'}, {'t': 'Rekap', 'm': 30}]}),
        p('Total ±6 jam. Setiap blok: <b>demo singkat → peserta coba sendiri</b> di buku kerja.', 'mut', step=8),
        notes='Klik tiap langkah untuk memunculkan segmen agenda. Total 360 menit. Tekankan: setiap blok teori diikuti latihan buku kerja.', title='Agenda'))
    S.append(slide(h2('Setelah hari ini Anda bisa…'), chk([
        'menyiapkan environment Python (venv + Jupyter)', 'memakai variabel, tipe data, operator, dan f-string',
        'membuat logika dengan <code class="i">if</code>, <code class="i">for</code>, <code class="i">while</code>',
        'memilih <b>list / tuple / dict / set</b> yang tepat', 'membuat menu interaktif data mahasiswa (Mini Project)']),
        notes='Bacakan singkat. Hubungkan ke hasil akhir: mini project menu data mahasiswa.', title='Tujuan'))

    S.append(section('A', 'Variabel, Tipe Data & I/O', 'Menyimpan nilai, memahami tipe, membaca input', notes='Blok 45 menit: setup (10) + variabel (10) + tipe (10) + operator (5) + I/O (10).'))
    S.append(slide(h2('Menyiapkan lingkungan', 'Setup'),
        row(code('$ python --version\nPython 3.11.x\n$ python -m venv .venv\n$ source .venv/bin/activate \n(.venv) $ pip install notebook pandas\n(.venv) $ jupyter notebook',
                 lang='bash', size='sm', reveal=[1, 1, 2, 3, 4, 5], style='flex:1.6'),
            col(callout('<b>Cek:</b> prompt berawalan <code class="i">(.venv)</code> berarti environment aktif.', step=4),
                callout('Tanpa venv, paket antar-proyek bisa bentrok.', 'warn', step=5)), gap=22),
        notes='Demo langsung di terminal instruktur. Pastikan semua peserta lolos <b>python --version</b> dan bisa membuka Jupyter sebelum lanjut (±10 menit). Bantu yang macet.', title='Setup environment'))
    S.append(slide(h2('Variabel = nama yang menunjuk ke nilai', 'Konsep'),
        row(code('nama = "Siti"\numur = 20\nipk = 3.67\naktif = True\numur = umur + 1',
                 reveal=[1, 2, 3, 4, 5], focus={5: [4]}, style='flex:1.1'),
            widget('boxes', {'items': [
                {'name': 'nama', 'val': '"Siti"', 'type': 'str', 'at': 1}, {'name': 'umur', 'val': '20', 'type': 'int', 'at': 2, 'changes': [{'at': 5, 'val': '21'}]},
                {'name': 'ipk', 'val': '3.67', 'type': 'float', 'at': 3}, {'name': 'aktif', 'val': 'True', 'type': 'bool', 'at': 4}]}), gap=24),
        notes='Klik satu per satu. Tekankan: tipe mengikuti <b>nilai</b>, bukan nama. Pada langkah terakhir nilai <code>umur</code> berubah dari 20 ke 21.', title='Variabel'))
    src = 'print(type("Python"), type(21), type(3.14), type(True))\nprint(int("42") + 8)\nprint(float("3.5") * 2)\nprint(int(3.9))        # dipotong, bukan dibulatkan\nprint(bool(0), bool(""), bool("teks"))'
    S.append(slide(h2('Tipe data & casting', 'Konsep'),
        code(src, size='sm', reveal=[1, 2, 3, 4, 5], focus={1: [0], 2: [1], 3: [2], 4: [3], 5: [4]}),
        out(run(src), start=1),
        callout('<code class="i">input()</code> selalu menghasilkan <b>str</b> → ubah dengan <code class="i">int()</code> / <code class="i">float()</code>.', 'warn', step=6),
        notes='Peragakan tiap baris, minta peserta menebak output sebelum klik. Poin: <b>int(3.9) = 3</b> (truncasi). Nilai "falsy": 0, "", [], None.', title='Tipe data & casting'))
    src = 'print(17 // 5, 17 % 5, 2 ** 8, 7 / 2)\nprint(60 <= 78 <= 90)\nprint(78 >= 70 and 3.6 >= 3.5)\ntotal = 10\ntotal += 5\nprint(total)'
    S.append(slide(h2('Operator', 'Konsep'),
        row(code(src, size='sm', reveal=[1, 2, 3, 4, 5, 6], focus={1: [0], 2: [1], 3: [2], 4: [3, 4, 5]}, style='flex:1.2'),
            col(table(['Operator', 'Arti'], [['<code class="i">//</code>', 'pembagian bulat'], ['<code class="i">%</code>', 'sisa bagi'], ['<code class="i">**</code>', 'pangkat'], ['<code class="i">and or not</code>', 'logika']], start=1)), gap=24),
        out(run(src), start=1, style='margin-top:14px'),
        notes='Fokus: <b>//</b> vs <b>/</b>, perbandingan berantai <code>60 &lt;= x &lt;= 90</code>, dan operator penugasan <code>+=</code>.', title='Operator'))
    S.append(slide(h2('f-string & input()', 'Konsep'),
        code('nama = input("Nama: ")\nnilai = float(input("Nilai: "))\nprint(f"{nama} mendapat {nilai:.1f}")', reveal=[1, 2, 3], focus={3: [2]}),
        out(run('nama = input("Nama: ")\nnilai = float(input("Nilai: "))\nprint(f"{nama} mendapat {nilai:.1f}")', ['Rina', '88.5']), start=3),
        callout('<code class="i">{nilai:.1f}</code> = 1 angka desimal. Pada contoh ini input yang diketik: <b>Rina</b> dan <b>88.5</b>.', step=4),
        notes='Demo live di Jupyter: minta peserta mengetik input mereka sendiri.', title='f-string & input'))
    S.append(work(['L1', 'L2', 'L3', 'L4', 'L5'], 15, 'Buka <b>workbook/hari1-python-fundamentals.ipynb</b> → Bagian A',
        'Jalankan sel Periksa jawaban (✅/❌) setelah menulis kode. Buka 💡 Petunjuk bila buntu.',
        notes='15 menit. Keliling kelas. Kesalahan umum: lupa mengubah tipe (str vs int), memakai <b>=</b> bukan <b>==</b>.'))

    S.append(section('B', 'Control Flow', 'Memilih cabang dan mengulang pekerjaan', notes='Blok 60 menit: if (15) + for (15) + while (15) + latihan (15).'))
    code_if = 'nilai = 78\nif nilai >= 85:\n    grade = "A"\nelif nilai >= 70:\n    grade = "B"\nelse:\n    grade = "C"\nprint(grade)'
    S.append(slide(h2('if / elif / else — satu jalur dipilih', 'Percabangan'),
        row(code(code_if, size='sm', focus={1: [0], 2: [1], 3: [3], 4: [4], 5: [7]}, style='flex:.8'),
            widget('flow', {'w': 620, 'h': 400, 'nodes': [
                {'id': 's', 'x': 170, 'y': 0, 'w': 220, 'h': 50, 't': 'nilai = 78', 'k': 'c', 'at': 1},
                {'id': 'd1', 'x': 150, 'y': 80, 'w': 260, 'h': 56, 't': 'nilai ≥ 85 ?', 'k': 'd', 'at': 2},
                {'id': 'A', 'x': 450, 'y': 83, 'w': 150, 'h': 50, 't': 'grade = A', 'k': 'c'},
                {'id': 'd2', 'x': 150, 'y': 175, 'w': 260, 'h': 56, 't': 'nilai ≥ 70 ?', 'k': 'd', 'at': 3},
                {'id': 'B', 'x': 450, 'y': 178, 'w': 150, 'h': 50, 't': 'grade = B', 'k': 'c', 'at': 4},
                {'id': 'C', 'x': 150, 'y': 270, 'w': 260, 'h': 50, 't': 'grade = C', 'k': 'c'},
                {'id': 'e', 'x': 170, 'y': 350, 'w': 220, 'h': 50, 't': 'print(grade)', 'k': 'c', 'at': 5}],
                'edges': [{'a': 's', 'b': 'd1', 'at': 2}, {'a': 'd1', 'b': 'A', 'l': 'ya'}, {'a': 'd1', 'b': 'd2', 'l': 'tidak', 'at': 3},
                          {'a': 'd2', 'b': 'B', 'l': 'ya', 'at': 4}, {'a': 'd2', 'b': 'C', 'l': 'tidak'}, {'a': 'B', 'b': 'e', 'at': 5, 'bend': -60}]}), gap=24),
        notes='Klik mengikuti alur untuk <b>nilai = 78</b>: 78 ≥ 85? tidak → 78 ≥ 70? ya → grade = "B". Hanya <b>satu</b> cabang yang dijalankan. Urutan cek: dari batas tertinggi.', title='if / elif / else'))
    code_for = 'for i in range(1, 6):\n    print(i * i)'
    S.append(slide(h2('for — ulangi untuk setiap elemen', 'Perulangan'),
        code(code_for, focus={s: [0, 1] for s in range(1, 6)}),
        col(p('<span class="mut">range(1, 6)</span> menghasilkan', 'sm'),
            widget('grid', {'rows': [[1, 2, 3, 4, 5]], 'cw': 84, 'hl': [h for s in range(1, 6) for h in ([{'at': s, 'cells': [[0, s - 2]], 'cls': 'g'}] if s > 1 else []) + [{'at': s, 'cells': [[0, s - 1]], 'cls': 'b'}]]}),
            p('<span class="mut">i * i</span> pada tiap putaran', 'sm'),
            widget('grid', {'rows': [['·'] * 5], 'cw': 84, 'hl': [{'at': s, 'cells': [[0, s - 1]], 'cls': 'g'} for s in range(1, 6)],
                            'vals': [{'at': s, 'cells': [[0, s - 1]], 'text': str((s) ** 2)} for s in range(1, 6)]})),
        notes='Setiap klik = satu putaran. Kotak oranye = nilai <b>i</b> saat ini. Kotak bawah menampilkan hasil <code>i * i</code>. Ingat: <b>range(1, 6)</b> berhenti di 5 (akhir eksklusif).', title='for loop'))
    S.append(slide(h2('while — ulangi selama kondisi benar', 'Perulangan'),
        row(col(code('sisa = 3\nwhile sisa > 0:\n    print(sisa)\n    sisa -= 1\nprint("selesai")', size='sm', focus={1: [0], 2: [1], 3: [2, 3], 4: [1], 5: [2, 3], 6: [1], 7: [2, 3], 8: [1], 9: [4]}),
                row(widget('boxes', {'items': [{'name': 'sisa', 'val': '3', 'type': 'int', 'at': 1, 'changes': [{'at': 3, 'val': '2'}, {'at': 5, 'val': '1'}, {'at': 7, 'val': '0'}]}]}),
                    out(['3', '2', '1', 'selesai'], start=3, style='margin-top:0;flex:1'), gap=18), style='flex:1'),
            col(widget('flow', {'w': 520, 'h': 270, 'nodes': [
                {'id': 'i', 'x': 0, 'y': 0, 'w': 170, 'h': 50, 't': 'sisa = 3', 'k': 'c', 'at': 1},
                {'id': 'c', 'x': 0, 'y': 110, 'w': 190, 'h': 56, 't': 'sisa > 0 ?', 'k': 'd', 'at': [2, 4, 6, 8]},
                {'id': 'b', 'x': 290, 'y': 112, 'w': 220, 'h': 52, 't': 'print(sisa)\nsisa -= 1', 'k': 'c', 'at': [3, 5, 7]},
                {'id': 'e', 'x': 0, 'y': 220, 'w': 190, 'h': 50, 't': 'selesai', 'k': 'c', 'at': 9}],
                'edges': [{'a': 'i', 'b': 'c', 'at': 2}, {'a': 'c', 'b': 'b', 'l': 'ya', 'at': 3, 'bend': 30}, {'a': 'b', 'b': 'c', 'at': 4, 'bend': 30}, {'a': 'c', 'b': 'e', 'l': 'tidak', 'at': 9}]}),
                callout('Tanpa <code class="i">sisa -= 1</code> → <b>loop tak berhenti</b>!', 'bad', step=9), style='flex:1'), gap=24),
        notes='Ikuti satu putaran demi satu: cek kondisi → jalankan badan → cek lagi. Pada langkah akhir kondisi False → keluar. Tunjukkan bahaya loop tak-hingga (tekan Ctrl+C / Interrupt kernel).', title='while loop'))
    S.append(work(['L6', 'L7', 'L8', 'L9', 'L10'], 15, 'Buka <b>workbook/hari1-python-fundamentals.ipynb</b> → Bagian B',
        'Grade, bilangan genap, diskon kasir, tebak angka, pola bintang.', notes='15 menit. Minta peserta yang cepat membantu teman di sebelah. Jawaban L9 memakai <b>while True</b> + <b>break</b>.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 25}, style='margin-top:40px;align-self:center'),
        p('Kembali tepat waktu — berikutnya: <b>struktur data</b>.', 'mut center', anim='up'),
        notes='25 menit. Tekan <b>C</b> atau klik Mulai untuk menjalankan timer.', layout='content work', title='Rehat'))

    S.append(section('C', 'Struktur Data', 'List, tuple, dictionary, set, dan list of dict', notes='Blok 85 menit: list (15) tuple (10) dict (20) set (10) list of dict (15) latihan (15).'))
    code_l = 'nilai = [80, 90, 75, 88]\nprint(nilai[0])\nprint(nilai[-1])\nprint(nilai[1:3])\nnilai.append(95)\nprint(nilai)'
    S.append(slide(h2('List — urutan yang bisa diubah', 'Struktur data'),
        row(code(code_l, size='sm', reveal=[1, 1, 2, 3, 4, 5], focus={1: [0], 2: [1], 3: [2], 4: [3], 5: [4], 6: [5]}, style='flex:1.15'),
            col(widget('grid', {'rows': [[80, 90, 75, 88, '']], 'head': ['0', '1', '2', '3', '4'], 'cw': 82,
                                'hl': [{'at': 0, 'cells': [[0, 4]], 'cls': 'x'}, {'at': 2, 'cells': [[0, 0]], 'cls': 'b'}, {'at': 3, 'cells': [[0, 3]], 'cls': 'b'},
                                       {'at': 4, 'cells': [[0, 1], [0, 2]], 'cls': 'a'}, {'at': 5, 'cells': [[0, 4]], 'cls': 'g'}],
                                'vals': [{'at': 5, 'cells': [[0, 4]], 'text': '95'}]}),
                out(['80', '88', '[90, 75]', '[80, 90, 75, 88, 95]'], start=2), p('<span class="mut sm">indeks dimulai dari 0; <b>-1</b> = elemen terakhir; irisan <code class="i">[1:3]</code> = indeks 1 dan 2</span>', step=4)), gap=24),
        notes='Kunci: indeks mulai <b>0</b>, indeks negatif dari belakang, irisan akhir <b>eksklusif</b>. Langkah terakhir: append menambah di ujung.', title='List'))
    S.append(slide(h2('Tuple & unpacking', 'Struktur data'),
        row(col(code('koordinat = (-6.2, 106.8)\nlat, lon = koordinat\nprint(lat, lon)', size='sm', reveal=[1, 2, 3], focus={2: [1], 3: [2]}),
                out(run('koordinat = (-6.2, 106.8)\nlat, lon = koordinat\nprint(lat, lon)'), start=3),
                callout('Tuple <b>tidak bisa diubah</b> setelah dibuat — cocok untuk data yang tetap.', step=4)),
            col(widget('grid', {'rows': [['-6.2', '106.8']], 'head': ['0', '1'], 'cw': 120, 'hl': [{'at': 2, 'cells': [[0, 0]], 'cls': 'b'}, {'at': 2, 'cells': [[0, 1]], 'cls': 'a'}]}),
                p('↓', 'big mut center'), widget('boxes', {'items': [{'name': 'lat', 'val': '-6.2', 'at': 2}, {'name': 'lon', 'val': '106.8', 'at': 2}]}, step=2)), gap=30),
        notes='Unpacking: setiap elemen tuple masuk ke satu variabel, urut.', title='Tuple'))
    S.append(slide(h2('Dictionary — pasangan key → value', 'Struktur data'),
        row(code('mhs = {\n    "nama": "Budi",\n    "nim": "2201",\n    "ipk": 3.6,\n}\nprint(mhs["nama"])\nprint(mhs.get("prodi", "belum diisi"))\nmhs["prodi"] = "Informatika"\nmhs["ipk"] = 3.7', size='sm', reveal=[1, 1, 1, 1, 1, 2, 3, 4, 5], focus={1: [0, 1, 2, 3, 4], 2: [5], 3: [6], 4: [7], 5: [8]}, style='flex:1.1'),
            col(widget('grid', {'rows': [['"nama"', '"Budi"'], ['"nim"', '"2201"'], ['"ipk"', '3.6']], 'head': ['key', 'value'], 'cw': 140,
                                'hl': [{'at': 2, 'cells': ['r:0'], 'cls': 'b'}, {'at': 3, 'cells': ['r:0'], 'cls': 'x'}, {'at': 5, 'cells': [[2, 1]], 'cls': 'g'}],
                                'append': [{'at': 4, 'row': ['"prodi"', '"Informatika"']}], 'vals': [{'at': 5, 'cells': [[2, 1]], 'text': '3.7'}]}),
                out(['Budi', 'belum diisi'], start=2)), gap=24),
        callout('Akses langsung <code class="i">mhs["prodi"]</code> yang belum ada → <b>KeyError</b>; <code class="i">.get(key, default)</code> aman.', 'warn', step=6),
        notes='Pada langkah 3 kunci "prodi" tidak ada → <b>.get</b> memberi nilai default (tidak error). Langkah 4: menambah key baru. Langkah 5: mengubah nilai ipk.', title='Dictionary'))
    S.append(slide(h2('Set — unik & operasi himpunan', 'Struktur data'),
        row(col(code('a = {"baca", "musik", "olahraga"}\nb = {"musik", "gaming", "olahraga"}\nprint(a | b)   # gabungan\nprint(a & b)   # irisan\nprint(a - b)   # hanya di a', size='sm', reveal=[1, 1, 2, 3, 4], focus={2: [2], 3: [3], 4: [4]}),
                callout('Hapus duplikat: <code class="i">list(set([1, 2, 2, 3]))</code> → <code class="i">[1, 2, 3]</code>', step=5)),
            widget('venn', {'w': 520, 'h': 270, 'a': {'n': 'a', 'only': ['baca']}, 'b': {'n': 'b', 'only': ['gaming']}, 'both': ['musik', 'olahraga'],
                            'steps': [{'at': 2, 'hl': 'union', 'label': 'a | b  → <b>gabungan</b>'}, {'at': 3, 'hl': 'both', 'label': 'a &amp; b  → <b>irisan</b>'}, {'at': 4, 'hl': 'a_only', 'label': 'a - b  → <b>hanya di a</b>'}]}), gap=24),
        notes='Venn: kiri = hanya a, tengah = irisan, kanan = hanya b. Set tidak berurutan & tidak punya duplikat.', title='Set'))
    code_ld = 'mahasiswa = [\n    {"nama": "Ani",  "ipk": 3.5, "prodi": "IF"},\n    {"nama": "Budi", "ipk": 3.9, "prodi": "SI"},\n    {"nama": "Cici", "ipk": 3.2, "prodi": "IF"},\n]\nif_only = [m for m in mahasiswa if m["prodi"] == "IF"]\nterbaik = max(mahasiswa, key=lambda m: m["ipk"])'
    S.append(slide(h2('List of dict — pola data mahasiswa', 'Struktur data'),
        row(code(code_ld, size='xs', reveal=[1, 1, 1, 1, 1, 2, 3], focus={2: [5], 3: [6]}, style='flex:1.45'),
            col(widget('grid', {'rows': [['Ani', '3.5', 'IF'], ['Budi', '3.9', 'SI'], ['Cici', '3.2', 'IF']], 'head': ['nama', 'ipk', 'prodi'], 'cw': 100, 'gf': 23,
                                'hl': [{'at': 2, 'cells': ['r:0', 'r:2'], 'cls': 'g'}, {'at': 2, 'cells': ['r:1'], 'cls': 'x'}, {'at': 3, 'clear': True}, {'at': 3, 'cells': ['r:1'], 'cls': 'b'}]}),
                out(['IF  → Ani, Cici', 'ipk tertinggi → Budi'], start=2)), gap=22),
        notes='Ini struktur utama mini project. List = kumpulan baris, setiap dict = satu mahasiswa. Filter dengan list comprehension; <b>max(..., key=lambda ...)</b> untuk nilai tertinggi.', title='List of dict'))
    S.append(slide(h2('Memilih struktur yang tepat'), table(['Struktur', 'Pakai bila…', 'Contoh'], [
        ['<code class="i">list</code>', 'urutan penting, boleh berubah', 'daftar nilai, daftar MK'],
        ['<code class="i">tuple</code>', 'data tetap / return beberapa nilai', 'koordinat, (nim, nama)'],
        ['<code class="i">dict</code>', 'butuh label / lookup cepat', 'profil mahasiswa, map MK→nilai'],
        ['<code class="i">set</code>', 'unik & operasi himpunan', 'hobi, deduplikasi']], start=1),
        notes='Ringkas pilihan struktur. Minta 1–2 peserta memberi contoh dari kehidupan kampus.', title='Memilih struktur'))
    S.append(work(['L11', 'L12', 'L13', 'L14', 'L15', 'L16'], 20, 'Buka <b>workbook/hari1-python-fundamentals.ipynb</b> → Bagian C',
        'List, dictionary, filter nilai lulus, tuple unpacking, set, dan list of dict.', notes='20 menit. L16 menggabungkan dict + list comprehension — dampingi yang kesulitan.'))
    S.append(slide(h2('Gaya penulisan — PEP 8', 'Praktik baik'),
        row(col(p('Kurang baik', 'bad big', step=1), code('def H(x,y):\n  return x+y\nHasil=H(1,2)', size='sm', step=1)),
            col(p('Lebih baik', 'ok big', step=2), code('def hitung_jumlah(a, b):\n    return a + b\n\nhasil = hitung_jumlah(1, 2)', size='sm', step=2)), gap=26),
        ul(['indentasi <b>4 spasi</b>, nama <code class="i">snake_case</code> yang bermakna', 'spasi di sekitar operator &amp; setelah koma', 'konstanta <code class="i">HURUF_BESAR</code>, class <code class="i">PascalCase</code>'], start=3, cls='sm'),
        notes='Singkat saja (5 menit). Aktifkan formatter di editor (Black/autopep8).', title='PEP 8'))

    S.append(section('D', 'Mini Project', 'Sistem data mahasiswa & sistem nilai', notes='Blok 75 menit: briefing (10) + coding (55) + diskusi (10).'))
    S.append(slide(h2('Alur menu interaktif', 'Mini Project 1'),
        widget('flow', {'w': 1100, 'h': 330, 'nodes': [
            {'id': 'm', 'x': 0, 'y': 120, 'w': 290, 'h': 80, 't': 'Tampilkan menu\ninput("Pilih: ")', 'k': 'c', 'at': [1, 4, 7]},
            {'id': 'n1', 'x': 430, 'y': 0, 'w': 300, 'h': 52, 't': '1  tambah(data, …)', 'k': 'c', 'at': 2}, {'id': 'n2', 'x': 430, 'y': 66, 'w': 300, 'h': 52, 't': '2  tampilkan(data)', 'k': 'c'},
            {'id': 'n3', 'x': 430, 'y': 132, 'w': 300, 'h': 52, 't': '3  cari(data, nim)', 'k': 'c', 'at': 5}, {'id': 'n4', 'x': 430, 'y': 198, 'w': 300, 'h': 52, 't': '4  hapus(data, nim)', 'k': 'c'},
            {'id': 'n5', 'x': 430, 'y': 264, 'w': 300, 'h': 52, 't': '5  ipk_tertinggi(data)', 'k': 'c'}, {'id': 'x', 'x': 880, 'y': 120, 'w': 220, 'h': 80, 't': '6  Keluar\n(break)', 'k': 'o', 'at': 8}],
            'edges': [{'a': 'm', 'b': 'n1', 'at': 2}, {'a': 'm', 'b': 'n2'}, {'a': 'm', 'b': 'n3', 'at': 5}, {'a': 'm', 'b': 'n4'}, {'a': 'm', 'b': 'n5'},
                      {'a': 'n1', 'b': 'x', 'bend': 0}, {'a': 'm', 'b': 'x', 'at': 8, 'bend': 150, 'l': 'pilih 6'}]}),
        callout('<b>Function terpisah</b> untuk tiap fitur + <code class="i">while True</code> untuk menu. Validasi: IPK 0–4, NIM tidak boleh ganda.', step=9),
        notes='Jelaskan alur satu putaran menu: tampilkan → pilih → panggil function → kembali ke menu, sampai pilih 6 (break). Workbook memberi function bertanda TODO + pemeriksa otomatis.', title='Alur menu'))
    S.append(work(['P1', 'P2'], 35, 'Buka <b>workbook/hari1-python-fundamentals.ipynb</b> → Bagian D',
        'Lengkapi function sampai ✅. Setelah itu coba menu interaktif di sel terakhir.', notes='35 menit pertama. Setelah itu diskusi 10 menit: apa yang paling sulit? Tampilkan satu solusi peserta.'))
    err1 = run_err('print(nama)'); err2 = run_err('print("Nilai: " + 80)'); err3 = run_err('mhs = {"nama": "Ani"}\nmhs["nim"]')
    S.append(slide(h2('Jebakan yang paling sering', 'Troubleshooting'),
        grid(3, card(code('print(nama)', size='sm', step=1, anim=None) + out(err1, err=True, step=2, style='font-size:19px'), 'NameError', anim=None),
                card(code('print("Nilai: " + 80)', size='sm', step=3, anim=None) + out(err2, err=True, step=4, style='font-size:19px;white-space:pre-wrap'), 'TypeError', anim=None),
                card(code('mhs["nim"]', size='sm', step=5, anim=None) + out(err3, err=True, step=6, style='font-size:19px'), 'KeyError', anim=None)),
        callout('Baca pesan error dari <b>baris paling bawah</b> ke atas: jenis error → apa yang salah → di baris mana.', 'ok', step=7),
        notes='Pesan error di atas adalah output asli Python. Biasakan peserta membaca error sebelum bertanya.', title='Jebakan umum'))
    S.append(slide(h2('Rekap Hari 1'), chk(['Variabel & tipe: <code class="i">int float str bool</code>, casting, f-string',
        'Percabangan <code class="i">if/elif/else</code> dan perulangan <code class="i">for</code> / <code class="i">while</code>',
        'Struktur data: list, tuple, dict, set, <b>list of dict</b>', 'Mini project: menu data mahasiswa dengan function', 'Semua latihan buku kerja ✅ (rekap skor di sel terakhir)']),
        p('<b>Besok (Hari 2):</b> Functions, Modules &amp; File Handling', 'acc big', step=6),
        notes='Minta peserta menjalankan sel <b>Rekap hasil latihan</b> dan mengisi lembar Rekap di notebook. Info besok: function, module, error handling, file CSV.', title='Rekap'))
    return S
