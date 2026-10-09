"""Membuat data nilai mahasiswa buatan sendiri (sintetis, reproducible).

Data ini FIKTIF — dibuat dengan seed tetap agar hasil analisis dapat diulang.
Jalankan: python src/generate_data.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUT = BASE_DIR / "data" / "raw" / "nilai_mahasiswa.csv"

MATKUL = ["pemrograman", "basis_data", "jaringan", "statistika", "matematika_diskrit"]
PRODI = {
    # bonus rata-rata nilai per mata kuliah (urutan = MATKUL)
    "Informatika": [6, 3, 0, 0, 2],
    "Sistem Informasi": [0, 6, 0, 3, -3],
    "Teknik Elektro": [-4, -3, 6, 2, 5],
}
DEPAN = ["Ani", "Budi", "Citra", "Dedi", "Eka", "Fajar", "Gita", "Hadi", "Indah", "Joko",
         "Kiki", "Lina", "Made", "Nina", "Oki", "Putri", "Rangga", "Sari", "Tono", "Umar"]
BELAKANG = ["Pratama", "Wijaya", "Santoso", "Lestari", "Hidayat", "Saputra", "Kusuma",
            "Nugroho", "Rahayu", "Setiawan"]


def buat_data(n_per_prodi=40, seed=2026):
    """Hasilkan DataFrame nilai: kemampuan dasar + bonus prodi + noise."""
    rng = np.random.default_rng(seed)
    baris = []
    nomor = 1
    for prodi, bonus in PRODI.items():
        for _ in range(n_per_prodi):
            dasar = rng.normal(70, 8)  # kemampuan umum mahasiswa
            nilai = np.clip(dasar + np.array(bonus) + rng.normal(0, 6, len(MATKUL)), 0, 100)
            baris.append({
                "nim": f"26{nomor:04d}",
                "nama": f"{rng.choice(DEPAN)} {rng.choice(BELAKANG)}",
                "prodi": prodi,
                "kelas": rng.choice(["A", "B"]),
                **dict(zip(MATKUL, nilai.round(1))),
            })
            nomor += 1
    return pd.DataFrame(baris)


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df = buat_data()
    df.to_csv(OUT, index=False)
    print(f"{len(df)} baris disimpan ke {OUT}")
