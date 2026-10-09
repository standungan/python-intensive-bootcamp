def latihan(day, nb, ids, mnt, bagian):
    return [(f"Sekarang giliran Anda. Buka buku kerja Hari {day}, bagian {bagian}, dan kerjakan {ids}. Waktunya {mnt} menit. Jalankan sel Periksa jawaban setelah menulis kode; kalau buntu, buka petunjuk. Jeda video ini dan lanjutkan setelah selesai.",
             f"Jeda video. Tampilkan notebook workbook/{nb}.ipynb dan jalankan timer {mnt} menit (tekan Mulai).")]

def rehat(mnt, next_):
    return [(f"Waktunya istirahat sekitar {mnt} menit. Setelah ini kita lanjut ke {next_}.", "Jeda video; tampilkan timer istirahat.")]
