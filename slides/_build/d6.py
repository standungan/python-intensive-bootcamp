from lib import *
from runner import run, run_err

def build():
    S = []
    S.append(title_slide(6, 'Capstone Project', 'Membangun proyek analisis data utuh dari Modul 1–5',
        ['6 jam', 'Individual', 'Buku Kerja Hari 6'], glyphs='load → clean →<br>analyze → visualize<br>→ insight',
        notes='<b>Pembukaan.</b> Hari ini peserta bekerja mandiri hampir sepanjang hari. Peran instruktur: pembimbing, bukan penceramah. Tunjukkan agenda dan format showcase di awal.'))
    S.append(slide(h2('Agenda Hari 6'), widget('timeline', {'unit': 'mnt', 'items': [
        {'t': 'Briefing + topik', 'm': 20}, {'t': 'Perencanaan', 'm': 40}, {'t': 'Pengerjaan capstone', 'm': 180, 'c': 'var(--ok)'}, {'t': 'Rehat', 'm': 20, 'c': '#64748b'},
        {'t': 'Finalisasi + dokumentasi', 'm': 60}, {'t': 'Showcase', 'm': 40}]}),
        p('Total 360 menit — setengah hari penuh untuk <b>mengerjakan</b>.', 'mut', step=7), notes='Sesuai agenda Modul Hari 6.', title='Agenda'))
    S.append(slide(h2('Tujuan hari ini'), chk([
        'mengintegrasikan skill Modul 1–5 dalam satu proyek utuh', 'merancang alur: data → cleaning → analisis → visualisasi → insight',
        'menulis kode terstruktur (function / class) dan mengikuti PEP 8', 'menyajikan hasil dengan visualisasi &amp; dokumentasi yang jelas']),
        notes='Tujuan pembelajaran dari modul.', title='Tujuan'))

    S.append(section('1', 'Briefing & Pilih Jalur', 'Tiga jalur, satu pipeline', notes='20 menit.'))
    S.append(slide(h2('Pilih satu jalur capstone', 'Briefing'),
        grid(3, card(p('Analisis dataset publik (Student Performance, Titanic, Penguins, Gapminder)', 'sm') + p('Level menengah', 'acc sm'), 'Jalur A — EDA', step=1, anim='up'),
                card(p('Pipeline data dari API / arXiv: ambil, bersihkan, analisis, visualisasi', 'sm') + p('Menengah–tinggi', 'acc sm'), 'Jalur B — API / arXiv', step=2, anim='up'),
                card(p('Mini aplikasi analisis nilai / data akademik dengan class &amp; CSV', 'sm') + p('Tinggi', 'acc sm'), 'Jalur C — Aplikasi', step=3, anim='up')),
        callout('Boleh mengusulkan ide sendiri — dengan persetujuan instruktur.', step=4),
        notes='Bantu peserta memilih sesuai level & minat. Ingatkan: lebih baik <b>selesai &amp; rapi</b> daripada ambisius tapi tak selesai.', title='Pilih jalur'))
    S.append(slide(h2('Skill yang harus terintegrasi', 'Briefing'), table(['Modul', 'Skill yang dipakai'], [
        ['Modul 1–2', 'variabel, control flow, function, error handling, file I/O'], ['Modul 3', 'class / OOP (opsional, dianjurkan)'],
        ['Modul 4', 'NumPy &amp; Pandas — <b>wajib</b>: cleaning, filter, groupby, merge/pivot'], ['Modul 5', 'Matplotlib/Seaborn + API atau scraping — <b>wajib</b> ada visualisasi']], start=1),
        notes='Peta skill tiap modul ke capstone.', title='Skill terintegrasi'))

    S.append(section('2', 'Perencanaan', 'Pertanyaan analisis dan struktur proyek', notes='40 menit: pertanyaan analisis (15) + struktur folder (10) + rencana waktu (15).'))
    S.append(slide(h2('Mulai dari pertanyaan analisis', 'Perencanaan'),
        row(col(p('Pertanyaan yang baik', 'ok big', step=1), ul(['spesifik &amp; bisa dijawab dengan data', '"Apakah jam belajar berpengaruh pada nilai?"', '"Prodi mana dengan rata-rata IPK tertinggi?"'], start=1, steps=False)),
            col(p('Pertanyaan yang lemah', 'bad big', step=2), ul(['terlalu umum: "Analisis data ini"', 'tidak bisa diukur: "Mana yang bagus?"'], start=2, steps=False)), gap=30),
        callout('Tulis <b>3–5 pertanyaan</b> sebelum menulis kode — itu menentukan grafik dan insight.', step=3),
        notes='Peserta menulis pertanyaan di workbook (L1).', title='Pertanyaan analisis'))
    S.append(slide(h2('Struktur folder proyek', 'Perencanaan'),
        row(widget('tree', {'nodes': [{'t': 'capstone_nama_anda/', 'k': 'dir', 'at': 1}, {'t': 'data/', 'k': 'dir', 'd': 1, 'at': 2, 'n': 'raw/ · processed/'}, {'t': 'src/', 'k': 'dir', 'd': 1, 'at': 3, 'n': 'kode .py'},
                                      {'t': 'notebooks/', 'k': 'dir', 'd': 1, 'at': 3, 'n': 'bila pakai Jupyter'}, {'t': 'output/', 'k': 'dir', 'd': 1, 'at': 4, 'n': 'figures/ · reports/'},
                                      {'t': 'requirements.txt', 'd': 1, 'at': 5}, {'t': 'README.md', 'd': 1, 'at': 5}]}),
            col(callout('Pisahkan <b>data mentah</b> dari <b>data hasil olahan</b> — data mentah tidak pernah diubah.', step=2),
                callout('Path relatif tergantung folder tempat program dijalankan → pakai <code class="i">Path(__file__)</code>.', 'warn', step=4)), gap=28),
        notes='Struktur folder yang direkomendasikan modul. Peserta membuatnya di workbook (L2).', title='Struktur folder'))
    S.append(work(['L1', 'L2'], 40, 'Buka <b>workbook/hari6-capstone-project.ipynb</b> → Bagian A–B', 'Pilih jalur &amp; topik, tulis pertanyaan analisis, siapkan struktur folder.', notes='40 menit perencanaan.'))

    S.append(section('3', 'Pengerjaan Capstone', 'Clean → Analyze → Visualize → Insight', notes='180 menit coding mandiri. Keliling, bantu yang buntu, jangan memberi solusi penuh.'))
    S.append(slide(h2('Saran alokasi waktu coding (180 mnt)', 'Pengerjaan'),
        widget('timeline', {'unit': 'mnt', 'items': [{'t': 'Load + inspeksi', 'm': 20}, {'t': 'Cleaning', 'm': 25}, {'t': 'Analisis', 'm': 40}, {'t': 'Visualisasi', 'm': 45}, {'t': 'Insight + export', 'm': 25}, {'t': 'Buffer', 'm': 25, 'c': '#64748b'}]}),
        callout('Jangan terlalu lama di <b>cleaning</b>. Cukup baik &gt; sempurna tapi kehabisan waktu. Kerjakan visualisasi terpenting dulu. Simpan sesering mungkin.', 'warn', step=7),
        notes='Tips manajemen waktu dari modul.', title='Alokasi waktu'))
    S.append(slide(h2('Pipeline yang rapi: satu function, satu tugas', 'Pengerjaan'),
        row(code('def muat_data(path): ...\ndef bersihkan(df): ...\ndef analisis(df): ...\ndef buat_grafik(df, out_dir): ...\ndef main():\n    df = bersihkan(muat_data(PATH))\n    hasil = analisis(df)\n    buat_grafik(df, OUT)\n\nif __name__ == "__main__":\n    main()', size='xs', focus={1: [0], 2: [1], 3: [2], 4: [3], 5: [4, 5, 6, 7], 6: [9, 10]}, style='flex:1.2;min-width:0'),
            col(callout('Function kecil lebih mudah <b>diuji &amp; diperbaiki</b>.', step=2), callout('Sertakan <b>docstring</b> singkat + <b>error handling</b> pada baca file / panggil API.', 'ok', step=4),
                callout('Kode harus bisa dijalankan <b>dari atas ke bawah tanpa error</b>.', step=6)), gap=24),
        notes='Standar kualitas kode: nama bermakna, function/class, docstring, PEP 8, error handling.', title='Struktur kode'))
    S.append(work(['L3', 'L4', 'L5', 'L6'], 180, 'Buka <b>workbook/hari6-capstone-project.ipynb</b> → Bagian C + proyek Anda sendiri', 'Bangun pipeline pada proyekmu. Workbook menyediakan pola &amp; pemeriksa untuk cleaning, analisis, visualisasi, insight.',
        notes='180 menit. Checkpoint: menit ke-60 data bersih; menit ke-120 minimal 3 grafik; menit ke-170 insight pertama.'))
    S.append(slide(h2('Rehat ☕', 'Rehat'), widget('timer', {'m': 20}, style='margin-top:40px;align-self:center'),
        p('Berikutnya: <b>finalisasi &amp; dokumentasi</b>.', 'mut center', anim='up'), notes='20 menit.', layout='content work', title='Rehat'))

    S.append(section('4', 'Finalisasi & Dokumentasi', 'Membuat proyek siap dipakai orang lain', notes='60 menit: README (20) + cek deliverable (20) + polesan (20).'))
    S.append(slide(h2('Deliverables yang dikumpulkan', 'Finalisasi'), chk([
        'kode sumber (<code class="i">.py</code> / <code class="i">.ipynb</code>) yang dapat dijalankan', 'file data atau instruksi cara mendapatkannya',
        'minimal <b>4–5 visualisasi</b> (PNG/PDF)', 'dokumentasi capstone (judul, masalah, data, metode, hasil, insight, kesimpulan)', '<code class="i">README.md</code> dan <code class="i">requirements.txt</code>']),
        notes='Deliverables dari modul (Bagian 6.2). Sel pemeriksa deliverable ada di workbook (L7).', title='Deliverables'))
    S.append(slide(h2('Kerangka README.md', 'Finalisasi'),
        row(code('# Capstone: [Judul Project]\n\n## Opsi Project\n## Deskripsi Singkat\n## Sumber Data\n## Cara Menjalankan\n## Hasil Utama / Insight\n## Struktur Folder\n## Pengembangan Selanjutnya', lang='md', size='sm', reveal=[1, 1, 2, 3, 4, 5, 6, 7, 8], focus={4: [4], 5: [5]}, style='flex:1.1'),
            col(callout('<b>Cara Menjalankan</b>: orang lain harus bisa menjalankan proyekmu hanya dari README.', step=5), callout('<b>Insight</b>: tulis temuan dalam kalimat, bukan hanya angka.', 'ok', step=6)), gap=26),
        notes='Template README dari modul.', title='README'))
    S.append(work(['L7', 'L8', 'L9'], 60, 'Buka <b>workbook/hari6-capstone-project.ipynb</b> → Bagian D–F', 'Pemeriksa deliverable, pola khusus Jalur B/C, self-review.', notes='60 menit finalisasi.'))

    S.append(section('5', 'Showcase', 'Presentasikan hasilmu', notes='40 menit. Sekitar 4–5 menit per peserta bila kelas kecil; untuk kelas besar pilih sukarelawan / lakukan dalam kelompok.'))
    S.append(slide(h2('Format showcase (±5 menit)', 'Showcase'),
        widget('timeline', {'unit': 'mnt', 'items': [{'t': 'Masalah', 'm': 1}, {'t': 'Data & metode', 'm': 1}, {'t': 'Hasil (grafik)', 'm': 2}, {'t': 'Insight', 'm': 1}]}),
        callout('Siapkan <b>satu grafik terbaik</b> dan <b>satu temuan</b> yang paling mengejutkan.', step=5),
        notes='Beri umpan balik singkat: apa yang sudah baik + satu saran perbaikan.', title='Format showcase'))
    S.append(slide(h2('Checklist review sejawat', 'Showcase'), chk([
        'pertanyaan analisis jelas dan terjawab', 'grafik punya judul, label sumbu, satuan', 'kode berjalan dari atas ke bawah tanpa error',
        'ada function/class + docstring &amp; error handling', 'README memungkinkan orang lain menjalankan proyek']),
        notes='Checklist diambil dari ekspektasi kualitas kode & deliverables modul.', title='Review sejawat'))
    S.append(slide(h2('Selamat — Anda menyelesaikan bootcamp 🎉'), chk(['Python dasar → function → OOP', 'NumPy &amp; Pandas untuk data', 'Visualisasi, API, scraping', 'Capstone: proyek analisis data end-to-end']),
        p('<b>Langkah berikutnya:</b> perluas capstone (stretch goals), simpan di portofolio GitHub, dan terus latihan dengan dataset baru.', 'acc', step=5),
        notes='Penutup: apresiasi peserta, bagikan materi lanjutan dan tautan repositori.', title='Penutup'))
    return S
