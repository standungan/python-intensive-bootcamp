"""Membuat data SAMPEL FIKTIF berformat Atom arXiv (untuk mode offline).

PENTING: seluruh judul, penulis, dan tanggal di berkas ini dibuat secara acak
(seed tetap) hanya untuk mendemonstrasikan pipeline ketika API arXiv tidak
dapat dijangkau. Ini BUKAN hasil pencarian arXiv yang sebenarnya; tautan memakai
domain example.org agar tidak tertukar dengan paper asli.

Jalankan: python src/buat_sampel.py
"""
import random
from pathlib import Path
from xml.sax.saxutils import escape

BASE_DIR = Path(__file__).resolve().parent.parent
OUT = BASE_DIR / "data" / "raw" / "arxiv_sample.xml"

METODE = ["Transformer Models", "Graph Neural Networks", "Deep Learning", "Reinforcement Learning",
          "Federated Learning", "Self-Supervised Learning", "Explainable Machine Learning",
          "Large Language Models", "Bayesian Methods", "Convolutional Networks"]
TUGAS = ["Student Dropout Prediction", "Adaptive Tutoring", "Learning Analytics", "Automated Essay Scoring",
         "Knowledge Tracing", "Course Recommendation", "Programming Education", "Exam Performance Forecasting"]
KONTEKS = ["Higher Education", "Online Courses", "Low-Resource Settings", "Primary Schools",
           "Massive Open Courses", "Engineering Programs"]
PENULIS = ["A. Prakoso", "B. Santika", "C. Wirawan", "D. Anggraini", "E. Mahendra", "F. Kurniawan",
           "G. Pertiwi", "H. Saragih", "I. Nasution", "J. Hartono", "K. Lukito", "L. Rahmani"]
# bobot tahun: lebih banyak paper pada tahun-tahun terbaru
TAHUN = {2019: 2, 2020: 3, 2021: 4, 2022: 5, 2023: 7, 2024: 8, 2025: 9, 2026: 4}


def buat(seed=7):
    rng = random.Random(seed)
    entri = []
    nomor = 1
    for tahun, n in TAHUN.items():
        for _ in range(n):
            bulan = rng.randint(1, 12 if tahun < 2026 else 9)
            judul = f"{rng.choice(METODE)} for {rng.choice(TUGAS)} in {rng.choice(KONTEKS)}"
            penulis = rng.sample(PENULIS[:4], 1) + rng.sample(PENULIS, rng.randint(1, 3))
            penulis = list(dict.fromkeys(penulis))
            entri.append((nomor, tahun, bulan, rng.randint(1, 28), judul, penulis))
            nomor += 1
    entri.sort(key=lambda e: (e[1], e[2], e[3]), reverse=True)   # terbaru dulu, seperti sortBy=submittedDate desc
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom">',
           "  <title>DATA SAMPEL FIKTIF - bukan hasil pencarian arXiv</title>"]
    for no, th, bl, tg, judul, pen in entri:
        xml.append("  <entry>")
        xml.append(f"    <id>https://example.org/sampel/{no:03d}</id>")
        xml.append(f"    <title>{escape(judul)}</title>")
        xml.append(f"    <summary>Ringkasan sampel fiktif nomor {no} (data buatan untuk demonstrasi).</summary>")
        xml.append(f"    <published>{th}-{bl:02d}-{tg:02d}T09:00:00Z</published>")
        for a in pen:
            xml.append(f"    <author><name>{escape(a)}</name></author>")
        xml.append(f'    <link href="https://example.org/sampel/{no:03d}"/>')
        xml.append("  </entry>")
    xml.append("</feed>")
    return "\n".join(xml) + "\n", len(entri)


if __name__ == "__main__":
    teks, n = buat()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(teks, encoding="utf-8")
    print(f"{n} entri sampel fiktif ditulis ke {OUT}")
