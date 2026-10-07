from lib import *
from runner import run, run_err, run_tmp

def build():
    S = []
    S.append(title_slide(2, 'Functions, Modules & File Handling', 'Menyusun kode yang bisa dipakai ulang, menangani error, dan menyimpan data ke file',
        ['6 jam', 'Modul 2', 'Buku Kerja Hari 2'], glyphs='def hitung(x):<br>&nbsp;&nbsp;return x * 2',
        notes='<b>Pembukaan (±5 menit).</b> Ulas singkat Hari 1 (tanya 2–3 peserta: apa yang paling diingat?). Format sama: demo singkat → peserta coba di buku kerja Hari 2.'))
    S.append(slide(h2('Agenda Hari 2'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Opening', 'm': 15}, {'t': 'Functions', 'm': 80}, {'t': 'Lambda & comp.', 'm': 40}, {'t': 'Rehat', 'm': 20, 'c': '#64748b'},
        {'t': 'Modules', 'm': 35}, {'t': 'Error handling', 'm': 50}, {'t': 'File', 'm': 50}, {'t': 'Mini project', 'm': 60, 'c': 'var(--ok)'}, {'t': 'Rekap', 'm': 10}]}),
        p('Total ±6 jam. Setiap blok: <b>demo singkat → peserta coba sendiri</b>.', 'mut', step=10),
        notes='Klik tiap langkah untuk memunculkan segmen agenda. Jumlah: 360 menit.', title='Agenda'))
    S.append(slide(h2('Setelah hari ini Anda bisa…'), chk([
        'menulis function dengan parameter, default, <code class="i">*args</code>/<code class="i">**kwargs</code>, dan return',
        'memahami scope local vs global', 'memakai lambda, map/filter, dan comprehension',
        'membuat module sendiri dan meng-<code class="i">import</code>-nya',
        'menangani error dengan <code class="i">try/except</code> dan <code class="i">raise</code>',
        'membaca &amp; menulis file teks dan CSV — lalu membuat pencatat yang menyimpan data']),
        notes='Tujuan hari ini; hubungkan ke mini project pencatat kegiatan yang persisten.', title='Tujuan'))

    S.append(section('A', 'Functions', 'Bungkus logika agar bisa dipakai berulang', notes='Blok 80 menit: konsep (35) + latihan L1–L8 (45).'))
    S.append(slide(h2('Anatomi function', 'Function'),
        row(code('def sapa(nama, sapaan="Halo"):\n    """Mengembalikan kalimat sapaan."""\n    return f"{sapaan}, {nama}!"\n\npesan = sapa("Rina")\nprint(pesan)', size='sm',
                 focus={1: [0], 2: [1], 3: [2], 4: [4], 5: [5]}, style='flex:1.15'),
            widget('flow', {'w': 440, 'h': 330, 'nodes': [
                {'id': 'a', 'x': 80, 'y': 0, 'w': 280, 'h': 50, 't': 'sapa("Rina")', 'k': 'c', 'at': 4},
                {'id': 'f', 'x': 40, 'y': 130, 'w': 360, 'h': 70, 't': 'def sapa(nama, sapaan="Halo")', 'k': 'c', 'at': 1},
                {'id': 'r', 'x': 80, 'y': 280, 'w': 280, 'h': 50, 't': '"Halo, Rina!"', 'k': 'o', 'at': 3}],
                'edges': [{'a': 'a', 'b': 'f', 'l': 'argumen', 'at': 4}, {'a': 'f', 'b': 'r', 'l': 'return', 'at': 3}]}), gap=24),
        out(run('def sapa(nama, sapaan="Halo"):\n    return f"{sapaan}, {nama}!"\nprint(sapa("Rina"))'), start=5, style='margin-top:12px'),
        notes='Urutan klik: <b>def</b> (parameter, nilai default) → docstring → return → panggilan → hasil. Bedakan <b>parameter</b> (di def) dan <b>argumen</b> (saat memanggil).', title='Anatomi function'))
    c1 = 'def kuadrat_print(x):\n    print(x * x)\n\ndef kuadrat_return(x):\n    return x * x\n\na = kuadrat_print(4)\nb = kuadrat_return(4)\nprint(a, b + 1)'
    S.append(slide(h2('print ≠ return', 'Function'),
        code(c1, size='sm', focus={1: [0, 1], 2: [3, 4], 3: [6], 4: [7], 5: [8]}),
        out(run(c1), start=3),
        callout('Function tanpa <code class="i">return</code> mengembalikan <b>None</b> — hasilnya tidak bisa dipakai untuk hitungan lanjut.', 'warn', step=6),
        notes='Jebakan klasik pemula. <code>print</code> hanya menampilkan; <code>return</code> mengirim nilai ke pemanggil. Tanya: kenapa <code>a</code> bernilai None?', title='print vs return'))
    c2 = 'def rata_rata(*angka):\n    return sum(angka) / len(angka)\n\ndef profil(**data):\n    for k, v in data.items():\n        print(f"{k}: {v}")\n\nprint(rata_rata(80, 90, 70))\nprofil(nama="Ani", prodi="IF")'
    S.append(slide(h2('*args & **kwargs', 'Function'),
        row(code(c2, size='sm', focus={1: [0, 1], 2: [7], 3: [3, 4, 5], 4: [8]}, style='flex:1.3'),
            col(card(p('<code class="i">*angka</code> → tuple', 'sm') + p('<code class="i">(80, 90, 70)</code>', 'acc'), 'Posisi bebas', step=2, anim='left'),
                card(p('<code class="i">**data</code> → dict', 'sm') + p('<code class="i">{"nama": "Ani", "prodi": "IF"}</code>', 'acc sm'), 'Keyword bebas', step=4, anim='left')), gap=24),
        out(run(c2), start=2, style='margin-top:10px'),
        notes='<b>*args</b> menampung argumen posisi berlebih sebagai tuple; <b>**kwargs</b> menampung keyword sebagai dict.', title='args & kwargs'))
    c3 = 'x = 10\n\ndef ubah():\n    x = 99\n    print("dalam:", x)\n\nubah()\nprint("luar:", x)'
    S.append(slide(h2('Scope — local vs global', 'Function'),
        row(code(c3, size='sm', focus={1: [0], 2: [2, 3], 3: [4], 4: [6], 5: [7]}, style='flex:1'),
            widget('nest', {'levels': [{'t': 'Global', 'at': 1, 'vars': [{'t': 'x = 10', 'at': 1, 'hl': 5}]},
                                       {'t': 'Lokal: ubah()', 'at': 2, 'hl': [3], 'vars': [{'t': 'x = 99', 'at': 2, 'hl': 3}]}]}), gap=28),
        out(run(c3), start=4, style='margin-top:12px'),
        callout('Mengubah variabel global dari dalam function? Pakai <b>return</b> (lebih aman) — bukan <code class="i">global</code>.', step=6),
        notes='<code>x = 99</code> di dalam function membuat variabel <b>baru</b> yang lokal; x global tetap 10. Pada langkah 5 lihat kotak Global menyala.', title='Scope'))
    S.append(work(['L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8'], 25, 'Buka <b>workbook/hari2-functions-modules-file-handling.ipynb</b> → Bagian A',
        'Function dasar, default, *args/**kwargs, multiple return, docstring.', notes='25 menit. Kesalahan umum: print di dalam function padahal diminta return; lupa menaruh docstring.'))

    S.append(section('B', 'Lambda, map, filter & Comprehension', 'Ringkas tanpa kehilangan kejelasan', notes='Blok 40 menit: demo (20) + latihan L9–L13 (20).'))
    S.append(slide(h2('map & filter dengan lambda', 'Fungsional'),
        row(col(code('kuadrat = list(map(lambda x: x * x, [1, 2, 3, 4]))', size='sm', step=1), widget('conv', {'items': ['1', '2', '3', '4'], 'fn': 'lambda x: x * x', 'out': ['1', '4', '9', '16'], 'lin': 'map: input', 'lout': 'hasil'}, step=1)),
            col(code('lulus = list(filter(lambda n: n >= 60, [80, 55, 90, 45]))', size='sm', step=1), widget('conv', {'items': ['80', '55', '90', '45'], 'fn': 'lambda n: n >= 60', 'keep': [True, False, True, False], 'out': ['80', '90'], 'lin': 'filter: input', 'lout': 'lolos'}, step=1)), gap=30),
        notes='Klik berulang: tiap klik memproses satu elemen. <b>map</b> mengubah setiap elemen; <b>filter</b> menyaring (merah = ditolak).', title='map & filter'))
    c4 = 'nilai = [80, 55, 90, 45, 70]\nlulus = [n for n in nilai if n >= 60]\nbonus = [n + 5 for n in nilai]\npeta = {n: ("lulus" if n >= 60 else "remedi") for n in nilai}\nurut = sorted(nilai, key=lambda n: -n)\nprint(lulus)\nprint(bonus)\nprint(peta)\nprint(urut)'
    S.append(slide(h2('Comprehension & sorted(key=…)', 'Fungsional'),
        code(c4, size='sm', focus={1: [1], 2: [2], 3: [3], 4: [4]}),
        out(run(c4), start=1),
        notes='Empat pola: list comprehension dengan filter, transformasi, dict comprehension dengan ekspresi kondisional, dan sorted dengan key lambda.', title='Comprehension'))
    S.append(work(['L9', 'L10', 'L11', 'L12', 'L13'], 20, 'Buka <b>workbook/hari2-functions-modules-file-handling.ipynb</b> → Bagian B',
        'Kuadrat 1–20, bonus nilai lulus, filter + lambda, dict comprehension, urutkan dengan lambda.', notes='20 menit.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 20}, style='margin-top:40px;align-self:center'),
        p('Berikutnya: <b>module &amp; error handling</b>.', 'mut center', anim='up'), notes='20 menit.', layout='content work', title='Rehat'))

    S.append(section('C', 'Modules', 'Memecah program ke beberapa file', notes='Blok 35 menit: demo (15) + latihan L14–L15 (20).'))
    S.append(slide(h2('Module = file .py yang bisa di-import', 'Modules'),
        row(widget('tree', {'nodes': [{'t': 'proyek/', 'k': 'dir', 'at': 1}, {'t': 'konversi.py', 'd': 1, 'at': 2, 'n': 'module buatan sendiri'},
                                      {'t': 'main.py', 'd': 1, 'at': 3, 'n': 'program utama'}, {'t': '__pycache__/', 'k': 'dir', 'd': 1, 'at': 5, 'n': 'dibuat otomatis'}]}),
            col(code('# konversi.py\ndef c_ke_f(c):\n    return c * 9 / 5 + 32', size='sm', step=2),
                code('# main.py\nimport konversi\nfrom konversi import c_ke_f\n\nprint(konversi.c_ke_f(100), c_ke_f(0))', size='sm', step=3),
                out(['212.0 32.0'], step=4)), gap=26),
        notes='Pastikan kedua file berada di <b>folder yang sama</b>. Jebakan: beri nama file seperti module bawaan (mis. <code>random.py</code>) → menimpa module standar.', title='Module'))
    S.append(slide(h2('Gaya import', 'Modules'), table(['Sintaks', 'Dipakai sebagai', 'Catatan'], [
        ['<code class="i">import math</code>', '<code class="i">math.sqrt(9)</code>', 'namespace jelas — paling aman'],
        ['<code class="i">from math import sqrt</code>', '<code class="i">sqrt(9)</code>', 'singkat, hindari bentrok nama'],
        ['<code class="i">import numpy as np</code>', '<code class="i">np.array([1])</code>', 'alias konvensional'],
        ['<code class="i">from m import *</code>', '—', '<span class="bad">hindari</span>']], start=1),
        out(run('import math\nfrom math import sqrt\nprint(math.pi, sqrt(9))\nprint(__name__)'), start=5),
        notes='Tunjukkan juga <code>if __name__ == "__main__":</code> — kode di dalamnya hanya jalan jika file dieksekusi langsung.', title='Gaya import'))
    S.append(work(['L14', 'L15'], 20, 'Buka <b>workbook/hari2-functions-modules-file-handling.ipynb</b> → Bagian C', 'Membuat module <code>konversi.py</code> dan <code>string_utils.py</code>, lalu meng-import-nya.', notes='20 menit.'))

    S.append(section('D', 'Error Handling', 'Program tidak crash saat sesuatu salah', notes='Blok 50 menit: konsep (25) + latihan L16–L18 (25).'))
    S.append(slide(h2('try / except / else / finally', 'Error'),
        row(code('def bagi_aman(a, b):\n    try:\n        hasil = a / b\n    except ZeroDivisionError:\n        return None\n    else:\n        return round(hasil, 2)\n    finally:\n        print("selesai dihitung")', size='xs',
                 focus={1: [1, 2], 2: [3, 4], 3: [5, 6], 4: [7, 8]}, style='flex:1.1'),
            widget('flow', {'w': 520, 'h': 420, 'nodes': [
                {'id': 't', 'x': 130, 'y': 0, 'w': 260, 'h': 56, 't': 'try:  a / b', 'k': 'c', 'at': 1},
                {'id': 'd', 'x': 130, 'y': 110, 'w': 260, 'h': 56, 't': 'ada error ?', 'k': 'd', 'at': 1},
                {'id': 'e', 'x': 0, 'y': 230, 'w': 230, 'h': 60, 't': 'except\nZeroDivisionError', 'k': 'c', 'at': 2},
                {'id': 'o', 'x': 290, 'y': 230, 'w': 230, 'h': 60, 't': 'else:\nreturn hasil', 'k': 'c', 'at': 3},
                {'id': 'f', 'x': 130, 'y': 360, 'w': 260, 'h': 56, 't': 'finally: selalu jalan', 'k': 'o', 'at': 4}],
                'edges': [{'a': 't', 'b': 'd', 'at': 1}, {'a': 'd', 'b': 'e', 'l': 'ya', 'at': 2}, {'a': 'd', 'b': 'o', 'l': 'tidak', 'at': 3}, {'a': 'e', 'b': 'f', 'at': 4}, {'a': 'o', 'b': 'f', 'at': 4}]}), gap=26),
        notes='Klik 2 = jalur error; klik 3 = jalur sukses. <b>finally</b> selalu berjalan di kedua jalur (cocok untuk menutup resource).', title='try/except'))
    c5 = 'def bagi_aman(a, b):\n    try:\n        hasil = a / b\n    except ZeroDivisionError:\n        return None\n    else:\n        return round(hasil, 2)\n    finally:\n        print("selesai dihitung")\n\nprint(bagi_aman(10, 4))\nprint(bagi_aman(1, 0))'
    S.append(slide(h2('Hasil nyata bagi_aman', 'Error'), code('print(bagi_aman(10, 4))\nprint(bagi_aman(1, 0))', size='sm', reveal=[1, 2], focus={1: [0], 2: [1]}),
        out(run(c5), start=1), callout('Tangkap <b>error yang spesifik</b> (<code class="i">ZeroDivisionError</code>), jangan <code class="i">except:</code> kosong.', 'warn', step=3),
        notes='Perhatikan "selesai dihitung" tercetak pada kedua pemanggilan.', title='Hasil bagi_aman'))
    c6 = 'def validasi_umur(umur):\n    if not isinstance(umur, int):\n        raise TypeError("umur harus int")\n    if umur < 0:\n        raise ValueError("umur tidak boleh negatif")\n    return umur\n\nfor u in (25, -3, "dua"):\n    try:\n        print(validasi_umur(u))\n    except (TypeError, ValueError) as e:\n        print(type(e).__name__, "->", e)'
    S.append(slide(h2('raise — membuat error sendiri', 'Error'),
        code(c6, size='xs', focus={1: [1, 2], 2: [3, 4], 3: [7, 8, 9, 10, 11]}), out(run(c6), start=3),
        notes='<b>raise</b> menghentikan function & melempar error ke pemanggil; <b>except … as e</b> menangkapnya. Cocok untuk validasi input.', title='raise'))
    S.append(work(['L16', 'L17', 'L18'], 25, 'Buka <b>workbook/hari2-functions-modules-file-handling.ipynb</b> → Bagian D', '<code>bagi_aman</code>, <code>input_angka</code> (ulangi sampai valid), validasi dengan <code>raise</code>.', notes='25 menit.'))

    S.append(section('E', 'File Handling', 'Teks dan CSV — data yang bertahan', notes='Blok 50 menit: demo (25) + latihan (25).'))
    c7 = 'from pathlib import Path\np = Path("catatan.txt")\np.write_text("baris 1\\nbaris 2\\n", encoding="utf-8")\nwith open(p, "a", encoding="utf-8") as f:\n    f.write("baris 3\\n")\nfor no, baris in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):\n    print(no, baris)\nprint(p.exists(), p.suffix)'
    S.append(slide(h2('File teks: with open & pathlib', 'File'),
        code(c7, size='xs', focus={1: [0, 1], 2: [2], 3: [3, 4], 4: [5, 6], 5: [7]}), out(run_tmp(c7), start=4),
        callout('Selalu pakai <code class="i">with</code> (file otomatis tertutup) dan <code class="i">encoding="utf-8"</code>.', step=6),
        notes='Mode <b>"w"</b> menimpa, <b>"a"</b> menambah, <b>"r"</b> membaca.', title='File teks'))
    c8 = 'import csv\nwith open("nilai.csv", "w", newline="", encoding="utf-8") as f:\n    w = csv.DictWriter(f, fieldnames=["nama", "nilai"])\n    w.writeheader()\n    w.writerows([{"nama": "Ani", "nilai": 85},\n                 {"nama": "Budi", "nilai": 70}])\nwith open("nilai.csv", newline="", encoding="utf-8") as f:\n    for baris in csv.DictReader(f):\n        print(baris["nama"], int(baris["nilai"]) + 5)'
    S.append(slide(h2('CSV dengan DictWriter / DictReader', 'File'),
        row(code(c8, size='xs', focus={1: [1, 2, 3, 4, 5], 2: [6, 7, 8]}, style='flex:1.4'),
            col(widget('grid', {'rows': [['Ani', '85'], ['Budi', '70']], 'head': ['nama', 'nilai'], 'cw': 120, 'hl': [{'at': 1, 'cells': ['r:0', 'r:1'], 'cls': 'g'}, {'at': 2, 'cells': ['r:0', 'r:1'], 'cls': 'b'}]}),
                out(run_tmp(c8), start=2)), gap=24),
        callout('Nilai dari CSV selalu <b>str</b> → ubah dengan <code class="i">int()</code>; <code class="i">newline=""</code> saat menulis agar tidak ada baris kosong (Windows).', 'warn', step=3),
        notes='Tabel kanan = isi file setelah ditulis (klik 1) dan dibaca baris demi baris (klik 2).', title='CSV'))

    S.append(section('F', 'Mini Project', 'Pencatat kegiatan akademik yang menyimpan datanya', notes='Blok 60 menit: briefing (10) + coding (40) + diskusi (10).'))
    S.append(slide(h2('Alur Pencatat Kegiatan', 'Mini Project'),
        widget('flow', {'w': 1100, 'h': 300, 'nodes': [
            {'id': 'a', 'x': 0, 'y': 110, 'w': 200, 'h': 70, 't': 'muat_csv()\nsaat mulai', 'k': 'c', 'at': 1},
            {'id': 'b', 'x': 270, 'y': 110, 'w': 200, 'h': 70, 't': 'menu\ntambah / lihat / filter', 'k': 'd', 'at': 2},
            {'id': 'c', 'x': 560, 'y': 20, 'w': 240, 'h': 60, 't': 'tambah_kegiatan()', 'k': 'c', 'at': 3},
            {'id': 'd', 'x': 560, 'y': 210, 'w': 240, 'h': 60, 't': 'tampilkan / filter', 'k': 'c', 'at': 4},
            {'id': 'e', 'x': 880, 'y': 20, 'w': 220, 'h': 60, 't': 'simpan_csv()', 'k': 'c', 'at': 5}],
            'edges': [{'a': 'a', 'b': 'b', 'at': 2}, {'a': 'b', 'b': 'c', 'at': 3}, {'a': 'b', 'b': 'd', 'at': 4}, {'a': 'c', 'b': 'e', 'at': 5}]}),
        callout('Data tersimpan di <code class="i">kegiatan.csv</code> → tetap ada saat program dijalankan lagi.', step=6),
        notes='Jelaskan: <b>muat</b> di awal, <b>simpan</b> setiap perubahan. Workbook memakai function <code>simpan_csv</code> dan <code>muat_csv</code> (latihan L19–L20) sebagai fondasi.', title='Alur mini project'))
    S.append(work(['L19', 'L20'], 40, 'Buka <b>workbook/hari2-functions-modules-file-handling.ipynb</b> → Bagian E–F', 'Lengkapi <code>simpan_csv</code> dan <code>muat_csv</code>, lalu bangun menu pencatat kegiatan.', notes='40 menit coding + 10 menit diskusi.'))
    e1 = run_err('def f(a, b):\n    return a + b\nf(1)'); e2 = run_err('x = 1\ndef f():\n    x += 1\nf()'); e3 = run_err('open("tidak_ada.txt")')
    S.append(slide(h2('Jebakan yang paling sering', 'Troubleshooting'),
        grid(3, card(code('f(1)', size='sm', step=1, anim=None) + out(e1, err=True, step=2, style='font-size:18px'), 'TypeError', anim=None),
                card(code('x += 1   # di dalam f()', size='sm', step=3, anim=None) + out(e2, err=True, step=4, style='font-size:18px'), 'UnboundLocalError', anim=None),
                card(code('open("tidak_ada.txt")', size='sm', step=5, anim=None) + out(e3, err=True, step=6, style='font-size:18px'), 'FileNotFoundError', anim=None)),
        callout('Periksa path dengan <code class="i">Path(...).exists()</code>; path relatif bergantung pada <b>folder tempat program dijalankan</b>.', 'ok', step=7),
        notes='Output adalah pesan error asli Python. Tunjukkan juga <b>ModuleNotFoundError</b> dan <b>UnicodeDecodeError</b> bila waktu ada.', title='Jebakan umum'))
    S.append(slide(h2('Rekap Hari 2'), chk(['Function: parameter, default, <code class="i">*args/**kwargs</code>, return vs print, scope',
        'Lambda, <code class="i">map/filter</code>, comprehension, <code class="i">sorted(key=)</code>', 'Module &amp; import; <code class="i">try/except/else/finally</code> dan <code class="i">raise</code>',
        'File teks &amp; CSV dengan <code class="i">with</code> + <code class="i">pathlib</code>', 'Mini project pencatat kegiatan yang persisten']),
        p('<b>Besok (Hari 3):</b> Object-Oriented Programming', 'acc big', step=6),
        notes='Minta peserta menjalankan sel <b>Rekap hasil latihan</b> di akhir notebook.', title='Rekap'))
    return S
