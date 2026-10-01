"""Unit test sederhana untuk AnalisisNilai (jalankan: python -m unittest discover -s tests)."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from analisis_nilai import MATKUL, AnalisisNilai, DataTidakValidError  # noqa: E402
from generate_data import buat_data  # noqa: E402


def app_contoh():
    tmp = Path(tempfile.mkdtemp()) / "data.csv"
    buat_data(n_per_prodi=10, seed=1).to_csv(tmp, index=False)
    return AnalisisNilai(tmp)


class TestAnalisisNilai(unittest.TestCase):
    def test_jumlah_dan_rata_rata(self):
        app = app_contoh()
        self.assertEqual(len(app), 30)
        baris = app.df.iloc[0]
        self.assertAlmostEqual(baris["rata_rata"], round(baris[MATKUL].mean(), 2))

    def test_tambah_valid_dan_nim_berurutan(self):
        app = app_contoh()
        nim = app.tambah_mahasiswa("Tes", "Informatika", "a", dict.fromkeys(MATKUL, 80))
        self.assertEqual(nim, "260031")
        self.assertEqual(len(app), 31)
        self.assertEqual(app.df.iloc[-1]["kelas"], "A")

    def test_tambah_tidak_valid(self):
        app = app_contoh()
        with self.assertRaises(DataTidakValidError):
            app.tambah_mahasiswa("Tes", "Informatika", "A", dict.fromkeys(MATKUL, 101))
        with self.assertRaises(DataTidakValidError):
            app.tambah_mahasiswa("  ", "Informatika", "A", dict.fromkeys(MATKUL, 80))
        with self.assertRaises(DataTidakValidError):
            app.tambah_mahasiswa("Tes", "Informatika", "A", {"pemrograman": 80})
        self.assertEqual(len(app), 30)

    def test_filter_dan_ranking(self):
        app = app_contoh()
        hasil = app.filter(prodi="Informatika")
        self.assertTrue((hasil["prodi"] == "Informatika").all())
        top = app.ranking(5)
        self.assertEqual(len(top), 5)
        self.assertTrue(top["rata_rata"].is_monotonic_decreasing)

    def test_state_bolak_balik(self):
        app = app_contoh()
        path = Path(tempfile.mkdtemp()) / "state.json"
        app.simpan_state(path)
        baru = AnalisisNilai.muat_state(path)
        self.assertEqual(len(baru), len(app))
        self.assertTrue((baru.df["rata_rata"].values == app.df["rata_rata"].values).all())

    def test_file_tidak_ada(self):
        with self.assertRaises(FileNotFoundError):
            AnalisisNilai("tidak_ada.csv")

    def test_bandingkan_prodi(self):
        app = app_contoh()
        hasil = app.bandingkan_prodi("Informatika", "Teknik Elektro")
        self.assertIn("p_value", hasil.columns)
        self.assertEqual(len(hasil), len(MATKUL) + 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
