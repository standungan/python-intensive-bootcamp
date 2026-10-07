from lib import *
from runner import run, run_err

def build():
    S = []
    S.append(title_slide(3, 'Object-Oriented Programming', 'Class, object, inheritance, encapsulation, dan special methods',
        ['6 jam', 'Modul 3', 'Buku Kerja Hari 3'], glyphs='class Mahasiswa:<br>&nbsp;&nbsp;def __init__(self):',
        notes='<b>Pembukaan (±5 menit).</b> Ulas Hari 2: function, error handling, file. Hari ini: membungkus data + perilaku dalam class.'))
    S.append(slide(h2('Agenda Hari 3'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Opening', 'm': 25}, {'t': 'Class & object', 'm': 70}, {'t': 'Inheritance', 'm': 60}, {'t': 'Rehat', 'm': 20, 'c': '#64748b'},
        {'t': 'Encapsulation & special', 'm': 70}, {'t': 'Jebakan', 'm': 20}, {'t': 'Mini project', 'm': 80, 'c': 'var(--ok)'}, {'t': 'Rekap', 'm': 15}]}),
        p('Total ±6 jam. Demo singkat → peserta coba di buku kerja.', 'mut', step=9), notes='Total 360 menit.', title='Agenda'))
    S.append(slide(h2('Setelah hari ini Anda bisa…'), chk([
        'menjelaskan class vs object, attribute vs method', 'menulis <code class="i">__init__</code> dan memakai <code class="i">self</code>',
        'membedakan class attribute dan instance attribute', 'memakai inheritance, <code class="i">super()</code>, dan override',
        'menjaga data lewat encapsulation, <code class="i">@property</code>, dan special methods (<code class="i">__str__</code>, <code class="i">__eq__</code>)',
        'membangun mini project berbasis class']), notes='Tujuan hari ini.', title='Tujuan'))

    S.append(section('A', 'Class & Object', 'Cetak biru dan benda nyata', notes='Blok 70 menit: konsep (35) + latihan L1–L3 (35).'))
    S.append(slide(h2('Class = cetak biru, object = benda', 'OOP'),
        row(code('class Mahasiswa:\n    def __init__(self, nama, ipk):\n        self.nama = nama\n        self.ipk = ipk\n\n    def info(self):\n        return f"{self.nama} (IPK {self.ipk})"\n\nm1 = Mahasiswa("Ani", 3.7)\nm2 = Mahasiswa("Budi", 3.2)\nprint(m1.info())', size='xs',
                 focus={1: [0], 2: [1, 2, 3], 3: [5, 6], 4: [8], 5: [9], 6: [10]}, style='flex:1;min-width:0'),
            widget('cards', {'bp': {'t': 'class Mahasiswa', 'attrs': ['nama', 'ipk'], 'methods': ['info()']},
                             'ins': [{'t': 'm1', 'vals': [['nama', '"Ani"'], ['ipk', '3.7']], 'at': 4}, {'t': 'm2', 'vals': [['nama', '"Budi"'], ['ipk', '3.2']], 'at': 5}]}, style='zoom:.62'), gap=24),
        out(run('class Mahasiswa:\n    def __init__(self, nama, ipk):\n        self.nama = nama\n        self.ipk = ipk\n    def info(self):\n        return f"{self.nama} (IPK {self.ipk})"\nprint(Mahasiswa("Ani", 3.7).info())'), start=6, style='margin-top:10px'),
        notes='Klik: class (cetak biru) → <code>__init__</code> → method → object <b>m1</b> dan <b>m2</b> muncul di kanan, masing-masing punya data sendiri. <b>self</b> = object yang sedang dipakai.', title='Class & object'))
    c1 = 'class Siswa:\n    sekolah = "SMA 1"        # class attribute\n    jumlah = 0\n\n    def __init__(self, nama):\n        self.nama = nama     # instance attribute\n        Siswa.jumlah += 1\n\na, b = Siswa("Ani"), Siswa("Budi")\nprint(a.nama, b.nama, a.sekolah, Siswa.jumlah)'
    S.append(slide(h2('Class attribute vs instance attribute', 'OOP'),
        code(c1, size='xs', focus={1: [1, 2], 2: [5], 3: [6, 7], 4: [9]}),
        out(run(c1), start=4), callout('Class attribute: <b>dibagi</b> semua object (mis. penghitung). Instance attribute: <b>milik</b> object masing-masing.', step=5),
        notes='Penghitung <code>Siswa.jumlah</code> bertambah setiap object dibuat — contoh umum class attribute.', title='Class vs instance attribute'))
    S.append(work(['L1', 'L2', 'L3'], 35, 'Buka <b>workbook/hari3-oop.ipynb</b> → Bagian A', 'Class dasar, class attribute sebagai penghitung, dan <code>RekeningBank</code>.', notes='35 menit. Kesalahan umum: lupa <b>self</b>.'))

    S.append(section('B', 'Inheritance & Polimorfisme', 'Mewarisi dan menimpa perilaku', notes='Blok 60 menit: konsep (25) + latihan L4–L5 (35).'))
    c2 = 'class Hewan:\n    def __init__(self, nama):\n        self.nama = nama\n    def suara(self):\n        return "..."\n\nclass Kucing(Hewan):\n    def suara(self):\n        return "meong"\n\nclass Anjing(Hewan):\n    def __init__(self, nama, ras):\n        super().__init__(nama)\n        self.ras = ras\n    def suara(self):\n        return "guk"\n\nfor h in (Kucing("Mimi"), Anjing("Rex", "Husky")):\n    print(h.nama, h.suara())'
    S.append(slide(h2('Inheritance & override', 'OOP'),
        row(code(c2, size='xs', focus={1: [0, 1, 2, 3, 4], 2: [6, 7, 8], 3: [10, 11, 12, 13], 4: [14, 15], 5: [17, 18]}, style='flex:1.2'),
            col(widget('tree', {'nodes': [{'t': 'Hewan', 'k': 'cls', 'at': 1, 'n': 'nama, suara()'}, {'t': 'Kucing', 'k': 'cls', 'd': 1, 'at': 2, 'n': 'override suara()'}, {'t': 'Anjing', 'k': 'cls', 'd': 1, 'at': 3, 'n': '+ ras, super().__init__'}]}),
                out(run(c2), start=5)), gap=24),
        notes='<b>Hewan</b> = induk. <b>Kucing</b> menimpa <code>suara()</code>. <b>Anjing</b> menambah attribute <code>ras</code> dan memanggil <code>super().__init__</code>. Loop akhir = <b>polimorfisme</b>: pemanggilan sama, perilaku berbeda.', title='Inheritance'))
    S.append(slide(h2('Memakai super()', 'OOP'),
        row(col(p('Lupa memanggil <code class="i">super().__init__()</code>', 'bad big', step=1),
                code('class Anjing(Hewan):\n    def __init__(self, nama, ras):\n        self.ras = ras     # nama?', size='sm', step=1),
                out([run_err('class H:\n    def __init__(self,n): self.nama=n\nclass A(H):\n    def __init__(self,n,r): self.ras=r\nprint(A("x","y").nama)')], err=True, step=2)),
            col(p('Benar', 'ok big', step=3), code('class Anjing(Hewan):\n    def __init__(self, nama, ras):\n        super().__init__(nama)\n        self.ras = ras', size='sm', step=3),
                out(['Rex Husky'], step=4)), gap=26),
        notes='Jebakan nomor 1 pada inheritance: attribute induk "kosong" karena <b>super().__init__()</b> tidak dipanggil.', title='super()'))
    S.append(work(['L4', 'L5'], 35, 'Buka <b>workbook/hari3-oop.ipynb</b> → Bagian B', 'Inheritance, <code>super()</code>, override, dan polimorfisme.', notes='35 menit.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 20}, style='margin-top:40px;align-self:center'),
        p('Berikutnya: <b>encapsulation &amp; special methods</b>.', 'mut center', anim='up'), notes='20 menit.', layout='content work', title='Rehat'))

    S.append(section('C', 'Encapsulation, Special Methods & Context Manager', 'Menjaga data dan membuat object "berperilaku Python"', notes='Blok 70 menit: konsep (35) + latihan L6–L9 (35).'))
    c3 = 'class Rekening:\n    def __init__(self, saldo=0):\n        self._saldo = saldo\n\n    @property\n    def saldo(self):\n        return self._saldo\n\n    def setor(self, jumlah):\n        if jumlah <= 0:\n            raise ValueError("jumlah harus > 0")\n        self._saldo += jumlah\n\nr = Rekening(100)\nr.setor(50)\nprint(r.saldo)'
    err_s = run_err(c3 + '\nr.setor(-5)')
    S.append(slide(h2('Encapsulation — pintu resmi', 'OOP'),
        row(code(c3, size='xs', focus={1: [2], 2: [4, 5, 6], 3: [8, 9, 10, 11], 4: [13, 14, 15]}, style='flex:1.25;min-width:0'),
            col(card(p('Data <code class="i">_saldo</code> dilindungi.', 'sm') + p('Ubah lewat <code class="i">setor()</code> yang <b>memvalidasi</b>.', 'sm'), 'Mengapa?', step=3, anim='left'), out(run(c3), start=4),
                out(['r.setor(-5)  →  ' + err_s], err=True, step=5, style='font-size:19px')), gap=24),
        notes='Awalan <code>_</code> = "jangan sentuh langsung". <code>@property</code> membuat <code>r.saldo</code> bisa dibaca seperti attribute tapi tidak diubah sembarangan. Setoran negatif ditolak oleh <b>setor()</b>.', title='Encapsulation'))
    c4 = 'class Buku:\n    def __init__(self, judul, tahun):\n        self.judul, self.tahun = judul, tahun\n    def __str__(self):\n        return f"{self.judul} ({self.tahun})"\n    def __repr__(self):\n        return f"Buku({self.judul!r}, {self.tahun})"\n    def __eq__(self, other):\n        return self.judul == other.judul\n\nb1, b2 = Buku("Python", 2024), Buku("Python", 2024)\nprint(b1)\nprint(repr(b1))\nprint(b1 == b2, b1 is b2)'
    S.append(slide(h2('Special methods', 'OOP'),
        row(code(c4, size='xs', focus={1: [3, 4], 2: [5, 6], 3: [7, 8], 4: [11], 5: [12], 6: [13]}, style='flex:1.2'),
            col(table(['Method', 'Dipanggil saat'], [['<code class="i">__str__</code>', '<code class="i">print(obj)</code>'], ['<code class="i">__repr__</code>', 'debug / <code class="i">repr()</code>'], ['<code class="i">__eq__</code>', '<code class="i">a == b</code>']], start=1), out(run(c4), start=4)), gap=24),
        callout('<code class="i">__str__</code> harus <b>return</b> string — bukan <code class="i">print</code>.', 'warn', step=7),
        notes='Tanpa <code>__str__</code>, <code>print(obj)</code> hanya menampilkan alamat memori.', title='Special methods'))
    c5 = 'class FileCatatan:\n    def __init__(self, nama):\n        self.nama = nama\n    def __enter__(self):\n        print("buka", self.nama)\n        return self\n    def __exit__(self, tipe, nilai, tb):\n        print("tutup", self.nama)\n\nwith FileCatatan("log.txt") as f:\n    print("bekerja dengan", f.nama)'
    S.append(slide(h2('Context manager — with', 'OOP'),
        row(code(c5, size='xs', focus={1: [9], 2: [3, 4, 5], 3: [10], 4: [6, 7]}, style='flex:1.3'),
            widget('flow', {'w': 380, 'h': 330, 'nodes': [
                {'id': 'a', 'x': 60, 'y': 0, 'w': 260, 'h': 56, 't': '__enter__()', 'k': 'c', 'at': 2}, {'id': 'b', 'x': 60, 'y': 130, 'w': 260, 'h': 56, 't': 'isi blok with', 'k': 'c', 'at': 3},
                {'id': 'c', 'x': 60, 'y': 260, 'w': 260, 'h': 56, 't': '__exit__()', 'k': 'o', 'at': 4}], 'edges': [{'a': 'a', 'b': 'b', 'at': 3}, {'a': 'b', 'b': 'c', 'at': 4}]}), gap=26),
        out(run(c5), start=4, style='margin-top:10px'),
        notes='<b>__exit__</b> selalu dipanggil — walau terjadi error di dalam blok. Itulah alasan <code>with open(...)</code> aman.', title='Context manager'))
    S.append(work(['L6', 'L7', 'L8', 'L9'], 35, 'Buka <b>workbook/hari3-oop.ipynb</b> → Bagian C', 'Encapsulation, special methods pada <code>Buku</code>, <code>Titik</code> + jarak, context manager.', notes='35 menit.'))

    S.append(section('D', 'Jebakan Umum', 'Kesalahan klasik OOP', notes='20 menit.'))
    c6x = None
    c6 = 'class Keranjang:\n    def __init__(self, isi=[]):\n        self.isi = isi\n\na, b = Keranjang(), Keranjang()\na.isi.append("apel")\nprint(b.isi)'
    S.append(slide(h2('Mutable default argument', 'Jebakan'),
        row(code(c6, size='sm', focus={1: [1, 2], 2: [4], 3: [5], 4: [6]}, style='flex:1.1'),
            col(out(run(c6), start=4), p('Semua object <b>berbagi list yang sama</b>!', 'bad', step=4), code('def __init__(self, isi=None):\n    self.isi = isi or []', size='sm', step=5), p('Perbaikan: default <code class="i">None</code>', 'ok sm', step=5)), gap=24),
        notes='Default dievaluasi <b>sekali</b> saat function didefinisikan, bukan setiap dipanggil.', title='Mutable default'))
    e1 = run_err('class A:\n    def __init__(self, x):\n        self.x = x\nA()'); e2 = run_err('class A:\n    def f():\n        pass\nA().f()'); e3 = run_err('class A:\n    pass\nA().nama')
    S.append(slide(h2('Error yang paling sering', 'Troubleshooting'),
        grid(3, card(code('A()', size='sm', step=1, anim=None) + out(e1, err=True, step=2, style='font-size:17px'), '__init__ kurang argumen', anim=None),
                card(code('def f():', size='sm', step=3, anim=None) + out(e2, err=True, step=4, style='font-size:17px'), 'Lupa self', anim=None),
                card(code('A().nama', size='sm', step=5, anim=None) + out(e3, err=True, step=6, style='font-size:17px'), 'AttributeError', anim=None)),
        notes='Pesan error asli Python.', title='Error umum'))

    S.append(section('E', 'Mini Project', 'Sistem perpustakaan / inventaris berbasis class', notes='Blok 80 menit: briefing (10) + coding (60) + diskusi (10).'))
    S.append(slide(h2('Rancang class sebelum coding', 'Mini Project'),
        row(widget('tree', {'nodes': [{'t': 'Buku', 'k': 'cls', 'at': 1, 'n': 'judul, penulis, tersedia'}, {'t': 'Perpustakaan', 'k': 'cls', 'at': 2, 'n': 'daftar_buku (list of Buku)'},
                                      {'t': 'tambah(buku)', 'd': 1, 'at': 3}, {'t': 'pinjam(judul)', 'd': 1, 'at': 4, 'n': 'validasi tersedia'}, {'t': 'kembalikan(judul)', 'd': 1, 'at': 5}, {'t': 'cari(kata)', 'd': 1, 'at': 6}]}),
            col(callout('Tanya dulu: <b>object apa</b> yang ada? <b>data</b> apa yang dimiliki? <b>aksi</b> apa yang dilakukan?', step=1),
                callout('Pakai <code class="i">__str__</code> agar tampilan buku rapi dan <code class="i">raise</code> untuk aksi yang tidak valid.', 'ok', step=7)), gap=26),
        notes='Ajak peserta menggambar class di kertas dulu. Workbook memuat dua mini project berbasis class dengan pemeriksa otomatis (P1, P2).', title='Rancang class'))
    S.append(work(['P1', 'P2'], 60, 'Buka <b>workbook/hari3-oop.ipynb</b> → Bagian E', 'Bangun mini project berbasis class hingga ✅.', notes='60 menit coding + 10 menit diskusi.'))
    S.append(slide(h2('Rekap Hari 3'), chk(['Class, object, <code class="i">__init__</code>, <code class="i">self</code>; class vs instance attribute', 'Inheritance, <code class="i">super()</code>, override, polimorfisme',
        'Encapsulation, <code class="i">@property</code>, <code class="i">__str__/__repr__/__eq__</code>, context manager', 'Jebakan: mutable default, lupa <code class="i">self</code>/<code class="i">super()</code>', 'Mini project berbasis class']),
        p('<b>Besok (Hari 4):</b> NumPy &amp; Pandas', 'acc big', step=6), notes='Minta peserta menjalankan sel Rekap hasil latihan.', title='Rekap'))
    return S
