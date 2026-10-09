from lib import *

OS3 = lambda w, m, l: table(['Sistem', 'Perintah'], [['Windows', w], ['macOS', m], ['Linux', l]], start=1)
C = lambda s: f'<code class="i">{s}</code>'

def build():
    S = []
    S.append(title_slide(0, 'Persiapan Lingkungan', 'Python, terminal, virtual environment (venv), dan Jupyter — siap sebelum Hari 1',
        ['±75 menit', 'Windows · macOS · Linux', 'Wajib sebelum Hari 1'], glyphs='python -m venv .venv<br>pip install notebook<br>jupyter notebook',
        notes='<b>Pembukaan (±3 menit).</b> Sesi ini menyamakan lingkungan semua peserta. Tanyakan sistem operasi tiap peserta di awal; siapkan jalur Windows, macOS, dan Linux. Target: setiap peserta bisa membuka sebuah notebook dari venv-nya sendiri.'))
    S.append(slide(h2('Agenda persiapan'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Instal Python', 'm': 15}, {'t': 'Terminal', 'm': 10}, {'t': 'venv', 'm': 15}, {'t': 'pip', 'm': 10}, {'t': 'Jupyter', 'm': 15}, {'t': 'Buku kerja', 'm': 10, 'c': 'var(--ok)'}]}),
        p('Total ±75 menit. Setiap bagian diakhiri <b>cek</b> — jangan lanjut sebelum cek berhasil.', 'mut', step=7),
        notes='Total 75 menit. Tekankan aturan: jangan lanjut bila langkah sebelumnya belum berhasil — masalah lingkungan menumpuk.', title='Agenda'))
    S.append(slide(h2('Setelah sesi ini Anda punya…'), chk([
        'Python 3.11 atau lebih baru yang terpasang dan dikenali terminal', 'folder proyek <code class="i">bootcamp/</code> dengan virtual environment <code class="i">.venv</code>',
        'paket yang dibutuhkan (pandas, numpy, matplotlib, …) di dalam venv', 'Jupyter Notebook yang berjalan dari venv tersebut', 'buku kerja Hari 1 yang bisa dibuka dan dijalankan']),
        notes='Hasil akhir yang diharapkan. Kembali ke slide ini di akhir sebagai daftar periksa.', title='Tujuan'))

    S.append(section('A', 'Instal Python', 'Cek dulu, instal bila perlu', notes='15 menit: cek versi (3) + instal per OS (8) + jebakan PATH (4).'))
    S.append(slide(h2('Cek: apakah Python sudah ada?', 'Python'),
        row(code('# Windows\npy --version\npython --version\n\n# macOS / Linux\npython3 --version', lang='bash', size='sm', reveal=[1, 1, 1, 1, 2, 3], focus={1: [1, 2], 2: [5]}, style='flex:1.1'),
            col(callout('Yang dicari: <b>Python 3.11</b> atau lebih baru (3.12, 3.13 juga baik).', step=3),
                callout('Muncul <i>"not recognized"</i> / <i>"command not found"</i> → Python belum terpasang atau belum masuk <b>PATH</b>. Lanjut ke slide berikutnya.', 'warn', step=4)), gap=24),
        notes='Minta semua peserta mengetik perintah dan menyebutkan hasilnya. Di macOS/Linux, <code>python</code> bisa tidak ada tetapi <code>python3</code> ada — itu normal.', title='Cek versi'))
    S.append(slide(h2('Instal Python sesuai sistem operasi', 'Python'),
        grid(3, card(ul(['unduh installer dari <b>python.org/downloads</b>', 'jalankan, <b>centang “Add python.exe to PATH”</b>', 'pilih Install Now'], start=1, steps=False, cls='sm'), 'Windows', step=1, anim='up'),
                card(ul(['unduh installer dari <b>python.org/downloads</b>', 'atau Homebrew: ' + C('brew install python')], start=1, steps=False, cls='sm'), 'macOS', step=2, anim='up'),
                card(ul(['Debian/Ubuntu:', C('sudo apt install python3 python3-venv python3-pip'), 'Fedora: ' + C('sudo dnf install python3')], start=1, steps=False, cls='sm'), 'Linux', step=3, anim='up')),
        callout('Setelah instal, <b>tutup dan buka lagi terminal</b>, lalu ulangi perintah cek versi.', 'ok', step=4),
        notes='Kotak “Add python.exe to PATH” di installer Windows adalah sumber masalah nomor satu — tunjukkan layar installer. Di Ubuntu, paket <b>python3-venv</b> diperlukan agar <code>python3 -m venv</code> berfungsi.', title='Instal Python'))
    S.append(slide(h2('Jebakan: Python terpasang tapi tidak ketemu', 'Python'),
        table(['Gejala', 'Penyebab', 'Solusi'], [
            ['Windows: <code class="i">python</code> tidak dikenali', 'belum centang <i>Add to PATH</i>', 'pakai <code class="i">py</code> (Python launcher) atau jalankan ulang installer → <i>Modify</i> → centang PATH'],
            ['Windows membuka Microsoft Store', 'alias bawaan Windows', 'instal dari python.org; matikan alias di <i>Manage app execution aliases</i>'],
            ['macOS/Linux: <code class="i">python</code> tidak ada', 'hanya tersedia <code class="i">python3</code>', 'pakai <code class="i">python3</code> (di dalam venv, <code class="i">python</code> otomatis ada)'],
            ['versi lama (mis. 3.8)', 'ada beberapa Python terpasang', 'panggil versi baru secara eksplisit: <code class="i">python3.11</code> atau <code class="i">py -3.11</code>']], start=1),
        notes='Jangan membahas semua baris panjang-panjang; fokus ke baris yang sedang dialami peserta. Setelah venv aktif, perintah <code>python</code> dan <code>pip</code> selalu menunjuk ke Python venv di semua sistem operasi.', title='Jebakan PATH'))

    S.append(section('B', 'Terminal Dasar', 'Berpindah folder dan membuat folder', notes='10 menit.'))
    S.append(slide(h2('Perintah terminal yang dipakai', 'Terminal'),
        table(['Tujuan', 'Windows (PowerShell)', 'macOS / Linux'], [
            ['di folder mana saya?', C('pwd') + ' / ' + C('cd'), C('pwd')], ['lihat isi folder', C('dir') + ' / ' + C('ls'), C('ls')],
            ['buat folder', C('mkdir bootcamp'), C('mkdir bootcamp')], ['masuk folder', C('cd bootcamp'), C('cd bootcamp')], ['naik satu level', C('cd ..'), C('cd ..')]], start=1),
        callout('Terminal Windows: <b>PowerShell</b> atau <b>Terminal</b> (Windows 11). Di VS Code: menu <i>Terminal → New Terminal</i>.', step=6),
        notes='Peragakan: buka terminal, <code>pwd</code>, <code>mkdir bootcamp</code>, <code>cd bootcamp</code>. Peserta yang belum pernah memakai terminal butuh waktu; jangan terburu-buru.', title='Terminal dasar'))
    S.append(slide(h2('Buat folder proyek', 'Terminal'),
        row(code('mkdir bootcamp\ncd bootcamp\npwd        # Windows: cd', lang='bash', size='sm', reveal=[1, 2, 3], focus={1: [0], 2: [1], 3: [2]}, style='flex:1'),
            widget('tree', {'nodes': [{'t': '~/', 'k': 'dir', 'at': 1}, {'t': 'bootcamp/', 'k': 'dir', 'd': 1, 'at': 1, 'hl': 2, 'n': 'folder kerja kita'}]}), gap=28),
        callout('Semua langkah berikutnya dijalankan <b>di dalam folder ini</b>.', step=4),
        notes='Pastikan semua peserta berada di folder <code>bootcamp</code> sebelum membuat venv.', title='Folder proyek'))

    S.append(section('C', 'Virtual Environment (venv)', 'Lingkungan terisolasi untuk tiap proyek', notes='15 menit: konsep (4) + buat & aktifkan (8) + jebakan PowerShell (3).'))
    S.append(slide(h2('Mengapa perlu venv?', 'venv'),
        widget('flow', {'w': 980, 'h': 270, 'nodes': [
            {'id': 'sys', 'x': 350, 'y': 0, 'w': 280, 'h': 64, 't': 'Python sistem\n(jangan diotak-atik)', 'k': 'c', 'at': 1},
            {'id': 'a', 'x': 0, 'y': 170, 'w': 300, 'h': 80, 't': 'proyek A  .venv\npandas 2.2', 'k': 'c', 'at': 2},
            {'id': 'b', 'x': 340, 'y': 170, 'w': 300, 'h': 80, 't': 'bootcamp  .venv\npandas 3.0', 'k': 'o', 'at': 3},
            {'id': 'c', 'x': 680, 'y': 170, 'w': 300, 'h': 80, 't': 'proyek C  .venv\nversi lain lagi', 'k': 'c', 'at': 4}],
            'edges': [{'a': 'sys', 'b': 'a', 'at': 2}, {'a': 'sys', 'b': 'b', 'at': 3}, {'a': 'sys', 'b': 'c', 'at': 4}]}),
        callout('Tiap proyek punya <b>paket sendiri</b> → tidak bentrok, mudah dihapus, mudah diulang di komputer lain.', step=5),
        notes='Analogi: satu kotak peralatan per proyek. Tanpa venv, memperbarui satu paket untuk proyek A bisa merusak proyek B.', title='Mengapa venv'))
    S.append(slide(h2('Buat dan aktifkan venv', 'venv'),
        col(p('1 · Buat (sekali saja)', 'acc big', step=1), code('python -m venv .venv      # macOS/Linux: python3 -m venv .venv', lang='bash', size='xs', step=1),
                p('2 · Aktifkan (setiap membuka terminal baru)', 'acc big', step=2),
                table(['Sistem', 'Perintah'], [['Windows PowerShell', C('.venv\\Scripts\\Activate.ps1')], ['Windows CMD', C('.venv\\Scripts\\activate.bat')], ['macOS / Linux', C('source .venv/bin/activate')]], start=3)),
        callout('Berhasil bila prompt berawalan <code class="i">(.venv)</code>, misalnya <code class="i">(.venv) PS C:\\bootcamp&gt;</code> atau <code class="i">(.venv) user@pc:~/bootcamp$</code>.', 'ok', step=6),
        notes='Demo langsung. Perintah <b>buat</b> hanya sekali per proyek; perintah <b>aktifkan</b> diulang setiap kali membuka terminal baru. Tunjukkan folder <code>.venv</code> yang muncul.', title='Buat & aktifkan venv'))
    S.append(slide(h2('Jebakan Windows: skrip dinonaktifkan', 'venv'),
        row(col(p('Gejala di PowerShell', 'bad big', step=1), out(['Activate.ps1 cannot be loaded because running scripts is disabled on this system.'], err=True, step=1, style='font-size:19px')),
            col(p('Solusi (pilih satu)', 'ok big', step=2), code('# A. izinkan skrip lokal untuk akun Anda\nSet-ExecutionPolicy -Scope CurrentUser RemoteSigned\n\n# B. atau pakai CMD\n.venv\\Scripts\\activate.bat', lang='bash', size='xs', step=2), style='flex:1.7;min-width:0'),
            gap=26),
        notes='Ini hanya terjadi di PowerShell Windows. Opsi A cukup dijalankan sekali; jawab Y bila diminta konfirmasi. Opsi B menghindari masalah dengan memakai CMD.', title='PowerShell policy'))
    S.append(slide(h2('Cek venv sudah aktif', 'venv'),
        row(code('python -c "import sys; print(sys.prefix)"\npython -m pip --version\ndeactivate', lang='bash', size='sm', reveal=[1, 2, 3], focus={1: [0], 2: [1], 3: [2]}, style='flex:1.8;min-width:0'),
            col(callout('Baris pertama harus menunjuk ke folder <b>.venv</b> di dalam bootcamp.', step=2), callout('Baris kedua menampilkan lokasi pip <b>di dalam .venv</b>.', step=3),
                callout('<code class="i">deactivate</code> keluar dari venv; prompt kembali normal.', 'warn', step=4)), gap=24),
        notes='Jika path tidak menunjuk ke .venv, venv belum aktif — kembali ke langkah aktivasi. Setelah deactivate, aktifkan lagi sebelum lanjut.', title='Cek venv'))

    S.append(section('D', 'pip & Paket', 'Memasang library yang dibutuhkan', notes='10 menit.'))
    S.append(slide(h2('Memasang paket dengan pip', 'pip'),
        row(code('python -m pip install --upgrade pip\npip install pandas\npip list\npip freeze > requirements.txt', lang='bash', size='sm', reveal=[1, 2, 3, 4], focus={1: [0], 2: [1], 3: [2], 4: [3]}, style='flex:1.1'),
            col(callout('Selalu pastikan <code class="i">(.venv)</code> aktif sebelum <code class="i">pip install</code>.', 'warn', step=1), callout('<code class="i">pip list</code> menampilkan paket di venv ini saja.', step=3), callout('<code class="i">freeze</code> menyimpan daftar paket + versinya.', step=4)), gap=24),
        notes='Jika <code>pip</code> tidak dikenali, pakai <code>python -m pip</code> — selalu berhasil karena memakai Python yang sedang aktif.', title='Pip dasar'))
    S.append(slide(h2('Satu perintah untuk semua kebutuhan bootcamp', 'pip'),
        row(code('# requirements.txt (ada di akar repositori)\nnotebook\nnumpy\npandas\nmatplotlib\nseaborn\nscipy\nopenpyxl\nrequests\nbeautifulsoup4\nfeedparser', lang='bash', size='xs', reveal=[1] + [2] * 10, style='flex:1'),
            col(code('pip install -r requirements.txt', lang='bash', size='sm', step=2), callout('Memasang semua paket sekaligus. Butuh internet dan beberapa menit.', step=3), callout('Pasang ulang di komputer lain = perintah yang sama.', 'ok', step=4)), gap=26),
        notes='File <code>requirements.txt</code> ada di akar repositori. Selama menunggu instalasi, jelaskan fungsi paket: numpy/pandas data, matplotlib/seaborn grafik, requests/beautifulsoup4 web, notebook = Jupyter.', title='requirements.txt'))

    S.append(section('E', 'Jupyter Notebook', 'Menulis dan menjalankan kode per sel', notes='15 menit: menjalankan (5) + antarmuka (5) + kernel venv (5).'))
    S.append(slide(h2('Menjalankan Jupyter', 'Jupyter'),
        row(code('jupyter notebook', lang='bash', size='sm', step=1, style='flex:.8'),
            widget('flow', {'w': 560, 'h': 330, 'nodes': [
                {'id': 't', 'x': 150, 'y': 0, 'w': 260, 'h': 60, 't': 'terminal (.venv)\njupyter notebook', 'k': 'c', 'at': 1},
                {'id': 's', 'x': 150, 'y': 130, 'w': 260, 'h': 60, 't': 'server lokal\nlocalhost:8888', 'k': 'c', 'at': 2},
                {'id': 'b', 'x': 150, 'y': 260, 'w': 260, 'h': 60, 't': 'browser\nhalaman Jupyter', 'k': 'o', 'at': 3}],
                'edges': [{'a': 't', 'b': 's', 'at': 2}, {'a': 's', 'b': 'b', 'at': 3}]}), gap=24),
        callout('Biarkan terminal tetap terbuka selama bekerja. Berhenti dengan <b>Ctrl+C</b> di terminal.', 'warn', step=4),
        callout('Browser tidak terbuka sendiri? Salin alamat <code class="i">http://localhost:8888/…</code> (lengkap dengan token) dari terminal.', step=5),
        notes='Jupyter berjalan sebagai server di komputer Anda sendiri; browser hanya antarmukanya. Jika port 8888 terpakai, Jupyter otomatis memakai 8889 dan seterusnya.', title='Menjalankan Jupyter'))
    S.append(slide(h2('Antarmuka & pintasan notebook', 'Jupyter'),
        table(['Aksi', 'Pintasan'], [['jalankan sel & pindah ke bawah', '<code class="i">Shift + Enter</code>'], ['mode perintah / mode edit', '<code class="i">Esc</code> / <code class="i">Enter</code>'],
                                      ['sisipkan sel di atas / bawah', '<code class="i">A</code> / <code class="i">B</code> (mode perintah)'], ['hapus sel', '<code class="i">D D</code>'], ['ubah ke Markdown / kode', '<code class="i">M</code> / <code class="i">Y</code>']], start=1),
        callout('Jika kode aneh/error tak masuk akal: menu <b>Kernel → Restart Kernel and Run All Cells</b>.', 'ok', step=6),
        notes='Ada dua jenis sel: kode dan Markdown. Variabel hidup di kernel, jadi urutan menjalankan sel penting. Tunjukkan satu sel kode <code>print("halo")</code>.', title='Pintasan notebook'))
    S.append(slide(h2('Pastikan kernel memakai venv', 'Jupyter'),
        code('# di terminal, venv aktif\npip install ipykernel\npython -m ipykernel install --user --name bootcamp --display-name "Python (bootcamp)"', lang='bash', size='xs', reveal=[1, 2, 3], focus={1: [1], 2: [2]}),
        callout('Jupyter yang dijalankan <b>dari venv</b> otomatis memakai venv itu.', step=1),
        callout('Perintah kedua mendaftarkan venv sebagai kernel yang bisa dipilih: <i>Kernel → Change kernel → Python (bootcamp)</i>.', step=3),
        callout('Cek di sel: <code class="i">import sys; sys.executable</code> → harus menunjuk ke folder <b>.venv</b>.', 'ok', step=4),
        notes='Penyebab klasik ModuleNotFoundError di notebook: kernel yang dipakai bukan venv (paket terpasang di venv, tetapi notebook jalan di Python lain). Tanpa --display-name, kernel baru akan bernama generik sehingga membingungkan.', title='Kernel venv'))

    S.append(section('F', 'Ambil Materi & Buku Kerja', 'Dari repositori ke notebook Hari 1', notes='10 menit.'))
    S.append(slide(h2('Ambil buku kerja dan buka Hari 1', 'Buku kerja'),
        code('git clone https://github.com/standungan/python-intensive-bootcamp\ncd python-intensive-bootcamp\npip install -r requirements.txt\njupyter notebook workbook/', lang='bash', size='sm', focus={1: [0], 2: [1], 3: [2], 4: [3]}),
        callout('Tanpa Git: tombol hijau <b>Code → Download ZIP</b> di GitHub, ekstrak, lalu buka terminal di folder hasil ekstrak.', step=5),
        callout('Di Jupyter buka <code class="i">hari1-python-fundamentals.ipynb</code>; jalankan <b>sel pertama (setup)</b> lebih dulu.', 'ok', step=6),
        notes='Peserta tanpa Git memakai Download ZIP. Ingatkan: buat venv sebelum <code>pip install -r requirements.txt</code>. Sel pertama notebook (setup) wajib dijalankan sebelum latihan.', title='Buka buku kerja'))
    S.append(work(['Python', 'venv', 'pip', 'Jupyter'], 10, 'Terminal Anda + <b>workbook/hari1-python-fundamentals.ipynb</b>',
        'Cek 4 hal: <code>python --version</code>, prompt <code>(.venv)</code>, <code>pip list</code> menampilkan pandas, dan sel pertama notebook Hari 1 berjalan tanpa error.', notes='10 menit. Keliling dan bantu yang tertinggal. Catat kendala umum untuk slide berikutnya.', title='Cek akhir'))
    S.append(slide(h2('Pemecahan masalah cepat', 'Troubleshooting'), table(['Pesan / gejala', 'Penyebab', 'Solusi'], [
        ['<code class="i">pip</code> tidak dikenali', 'venv belum aktif / PATH', '<code class="i">python -m pip …</code> setelah mengaktifkan venv'],
        ['<code class="i">ModuleNotFoundError: pandas</code>', 'paket di venv lain / kernel salah', 'aktifkan venv, <code class="i">pip install</code>, pilih kernel venv'],
        ['<code class="i">jupyter</code> tidak dikenali', 'notebook belum terpasang di venv', '<code class="i">pip install notebook</code>'],
        ['Port 8888 sibuk', 'Jupyter lain masih berjalan', '<code class="i">jupyter notebook --port 8889</code>'],
        ['<i>running scripts is disabled</i>', 'kebijakan PowerShell', 'lihat slide PowerShell policy / pakai CMD'],
        ['instalasi pip sangat lambat/gagal', 'koneksi / proxy', 'ulangi; cek koneksi; minta jaringan lain']], start=1),
        notes='Slide rujukan; tinggalkan di layar saat peserta mengerjakan cek akhir. Untuk kendala lain, mulailah dari: venv aktif? kernel benar? paket terpasang di venv?', title='Troubleshooting'))
    S.append(slide(h2('Alternatif jika instalasi lokal bermasalah'), table(['Opsi', 'Kelebihan', 'Catatan'], [
        ['<b>VS Code</b> + ekstensi Python & Jupyter', 'editor + terminal + notebook dalam satu jendela', 'tetap butuh Python &amp; venv di komputer'],
        ['<b>Google Colab</b>', 'tanpa instal, jalan di browser', 'butuh akun Google &amp; internet; unggah notebook dari <code class="i">workbook/</code>; berkas hilang saat sesi berakhir']], start=1),
        notes='Colab adalah jalan keluar bagi peserta yang komputernya tidak bisa dipasangi Python. Materi hari 1–5 bisa berjalan di Colab; latihan yang menulis file sebaiknya diunduh hasilnya.', title='Alternatif'))
    S.append(slide(h2('Rekap persiapan'), chk(['Python 3.11+ terpasang; <code class="i">python --version</code> / <code class="i">python3 --version</code> berhasil', 'folder <code class="i">bootcamp/</code> dan venv <code class="i">.venv</code> (aktif: prompt <code class="i">(.venv)</code>)',
        'paket terpasang dengan <code class="i">pip install -r requirements.txt</code>', 'Jupyter berjalan dari venv; kernel benar', 'buku kerja Hari 1 terbuka dan sel pertama berjalan']),
        p('<b>Selanjutnya (Hari 1):</b> Python Fundamentals', 'acc big', step=6), notes='Pastikan semua peserta lolos sebelum Hari 1. Peserta yang belum lolos diberi waktu pendampingan sebelum sesi dimulai.', title='Rekap'))
    return S
