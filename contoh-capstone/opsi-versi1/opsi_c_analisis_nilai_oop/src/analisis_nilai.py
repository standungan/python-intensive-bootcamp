"""Kelas AnalisisNilai — mini sistem analisis data akademik (OOP + Pandas).

Fitur: tambah data, statistik, filter, ranking, perbandingan dua prodi,
visualisasi, export CSV/Excel, serta simpan/muat state aplikasi (JSON).
"""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

MATKUL = ["pemrograman", "basis_data", "jaringan", "statistika", "matematika_diskrit"]
KOLOM_ID = ["nim", "nama", "prodi", "kelas"]
sns.set_theme(style="whitegrid", palette="muted")


class DataTidakValidError(ValueError):
    """Dilempar saat input data mahasiswa tidak memenuhi aturan validasi."""


class AnalisisNilai:
    """Mengelola data nilai mahasiswa dan menghasilkan analisis serta laporan.

    Attributes:
        df (pd.DataFrame): data nilai (kolom id + satu kolom per mata kuliah).
        matkul (list[str]): daftar mata kuliah yang dianalisis.
    """

    def __init__(self, data_path=None, matkul=None):
        self.matkul = list(matkul or MATKUL)
        if data_path:
            self.df = self._baca_csv(Path(data_path))
        else:
            self.df = pd.DataFrame(columns=KOLOM_ID + self.matkul)
        self._hitung_rata()

    # ------------------------------------------------------------------
    # Pemuatan & validasi
    # ------------------------------------------------------------------
    def _baca_csv(self, path):
        """Baca CSV dan validasi kolom serta rentang nilai (0-100)."""
        try:
            df = pd.read_csv(path, dtype={"nim": str})
        except FileNotFoundError as err:
            raise FileNotFoundError(f"File data tidak ditemukan: {path}") from err
        hilang = set(KOLOM_ID + self.matkul) - set(df.columns)
        if hilang:
            raise DataTidakValidError(f"Kolom wajib tidak ada: {sorted(hilang)}")
        if df["nim"].duplicated().any():
            raise DataTidakValidError("NIM duplikat ditemukan pada file data.")
        nilai = df[self.matkul]
        if nilai.isna().any().any() or ((nilai < 0) | (nilai > 100)).any().any():
            raise DataTidakValidError("Nilai harus terisi dan berada pada rentang 0-100.")
        return df

    def _hitung_rata(self):
        """Hitung kolom rata_rata dan predikat dari nilai mata kuliah."""
        if self.df.empty:
            self.df["rata_rata"] = pd.Series(dtype=float)
            self.df["predikat"] = pd.Series(dtype=str)
            return
        self.df["rata_rata"] = self.df[self.matkul].mean(axis=1).round(2)
        self.df["predikat"] = pd.cut(
            self.df["rata_rata"], bins=[-0.01, 54.99, 69.99, 84.99, 100],
            labels=["D", "C", "B", "A"]).astype(str)

    # ------------------------------------------------------------------
    # Tambah data
    # ------------------------------------------------------------------
    def tambah_mahasiswa(self, nama, prodi, kelas, nilai):
        """Tambah satu mahasiswa; `nilai` berupa dict {matkul: angka 0-100}.

        Mengembalikan NIM yang dibuat otomatis. Melempar DataTidakValidError
        jika nama kosong, mata kuliah tidak lengkap, atau nilai di luar 0-100.
        """
        if not str(nama).strip():
            raise DataTidakValidError("Nama tidak boleh kosong.")
        if set(nilai) != set(self.matkul):
            raise DataTidakValidError(f"Nilai harus lengkap untuk: {self.matkul}")
        for mk, angka in nilai.items():
            if not isinstance(angka, (int, float)) or not 0 <= angka <= 100:
                raise DataTidakValidError(f"Nilai {mk}={angka!r} harus angka 0-100.")
        nomor = 1 if self.df.empty else int(self.df["nim"].str[2:].astype(int).max()) + 1
        nim = f"26{nomor:04d}"
        baris = {"nim": nim, "nama": nama.strip(), "prodi": prodi.strip(),
                 "kelas": kelas.strip().upper(), **nilai}
        self.df = pd.concat([self.df, pd.DataFrame([baris])], ignore_index=True)
        self._hitung_rata()
        return nim

    # ------------------------------------------------------------------
    # Statistik, filter, ranking
    # ------------------------------------------------------------------
    def statistik(self):
        """Statistik deskriptif per mata kuliah (+ rata_rata)."""
        kolom = self.matkul + ["rata_rata"]
        return self.df[kolom].agg(["count", "mean", "median", "std", "min", "max"]).T.round(2)

    def statistik_per_prodi(self):
        """Rata-rata tiap mata kuliah per program studi."""
        return self.df.groupby("prodi")[self.matkul + ["rata_rata"]].mean().round(2)

    def filter(self, prodi=None, kelas=None, min_rata=None, predikat=None):
        """Kembalikan salinan DataFrame yang memenuhi semua kriteria yang diberikan."""
        hasil = self.df
        if prodi is not None:
            hasil = hasil[hasil["prodi"] == prodi]
        if kelas is not None:
            hasil = hasil[hasil["kelas"] == kelas.upper()]
        if min_rata is not None:
            hasil = hasil[hasil["rata_rata"] >= min_rata]
        if predikat is not None:
            hasil = hasil[hasil["predikat"] == predikat.upper()]
        return hasil.copy()

    def ranking(self, n=10, prodi=None):
        """n mahasiswa dengan rata-rata tertinggi (opsional per prodi)."""
        data = self.filter(prodi=prodi)
        top = data.sort_values(["rata_rata", "nim"], ascending=[False, True]).head(n)
        top = top[["nim", "nama", "prodi", "rata_rata", "predikat"]].reset_index(drop=True)
        top.index += 1
        top.index.name = "peringkat"
        return top

    def bandingkan_prodi(self, prodi_a, prodi_b):
        """Bandingkan rata-rata dua prodi per mata kuliah (Welch t-test + selisih)."""
        baris = []
        for mk in self.matkul + ["rata_rata"]:
            a = self.df.loc[self.df["prodi"] == prodi_a, mk]
            b = self.df.loc[self.df["prodi"] == prodi_b, mk]
            if len(a) < 2 or len(b) < 2:
                raise DataTidakValidError("Setiap prodi perlu minimal 2 mahasiswa.")
            t, p = stats.ttest_ind(a, b, equal_var=False)
            baris.append({"matkul": mk, f"rata_{prodi_a}": a.mean(),
                          f"rata_{prodi_b}": b.mean(), "selisih": a.mean() - b.mean(),
                          "t": t, "p_value": p, "signifikan_5%": p < 0.05})
        hasil = pd.DataFrame(baris).set_index("matkul")
        kolom_bulat = [c for c in hasil.columns if c not in ("p_value", "signifikan_5%")]
        hasil[kolom_bulat] = hasil[kolom_bulat].round(3)
        return hasil

    # ------------------------------------------------------------------
    # Visualisasi
    # ------------------------------------------------------------------
    def visualisasi(self, folder):
        """Simpan 6 grafik + dashboard 2x3 ke `folder`; kembalikan daftar nama file."""
        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)
        panel = [
            ("01_distribusi_rata_rata", self._p_hist),
            ("02_boxplot_per_prodi", self._p_box),
            ("03_rata_matkul_per_prodi", self._p_bar),
            ("04_korelasi_matkul", self._p_corr),
            ("05_top10", self._p_top),
            ("06_predikat_per_prodi", self._p_predikat),
        ]
        for nama, fungsi in panel:
            fig, ax = plt.subplots(figsize=(8, 5))
            fungsi(ax)
            fig.tight_layout()
            fig.savefig(folder / f"{nama}.png", dpi=150, bbox_inches="tight")
            plt.close(fig)
        fig, axes = plt.subplots(2, 3, figsize=(20, 11))
        for ax, (_, fungsi) in zip(axes.ravel(), panel):
            fungsi(ax)
        fig.suptitle(f"Dashboard Nilai Mahasiswa ({len(self.df)} mahasiswa)", fontsize=18, y=1.0)
        fig.tight_layout()
        fig.savefig(folder / "00_dashboard.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        return ["00_dashboard.png"] + [f"{n}.png" for n, _ in panel]

    def _p_hist(self, ax):
        sns.histplot(self.df["rata_rata"], bins=20, kde=True, ax=ax, color="#457b9d")
        ax.axvline(self.df["rata_rata"].mean(), color="red", ls="--",
                   label=f"rata-rata = {self.df['rata_rata'].mean():.1f}")
        ax.set_title("Distribusi rata-rata nilai"); ax.set_xlabel("Rata-rata nilai"); ax.legend()

    def _p_box(self, ax):
        sns.boxplot(data=self.df, x="prodi", y="rata_rata", ax=ax)
        ax.set_title("Rata-rata nilai per program studi")
        ax.set_xlabel(""); ax.set_ylabel("Rata-rata nilai"); ax.tick_params(axis="x", rotation=10)

    def _p_bar(self, ax):
        d = self.df.melt(id_vars="prodi", value_vars=self.matkul, var_name="matkul", value_name="nilai")
        sns.barplot(data=d, x="matkul", y="nilai", hue="prodi", errorbar=None, ax=ax)
        ax.set_title("Rata-rata nilai per mata kuliah & prodi")
        ax.set_xlabel(""); ax.set_ylabel("Rata-rata nilai"); ax.set_ylim(50, 90)
        ax.tick_params(axis="x", rotation=20); ax.legend(title="", fontsize=8)

    def _p_corr(self, ax):
        sns.heatmap(self.df[self.matkul].corr(), annot=True, fmt=".2f", cmap="coolwarm",
                    center=0, ax=ax, cbar=False, annot_kws={"size": 8})
        ax.set_title("Korelasi antar mata kuliah"); ax.tick_params(axis="x", rotation=30)

    def _p_top(self, ax):
        top = self.ranking(10).reset_index()
        sns.barplot(data=top, y="nama", x="rata_rata", hue="prodi", dodge=False, ax=ax)
        ax.set_title("10 mahasiswa dengan rata-rata tertinggi")
        ax.set_xlabel("Rata-rata nilai"); ax.set_ylabel("")
        ax.set_xlim(top["rata_rata"].min() - 5, 100); ax.legend(title="", fontsize=8)

    def _p_predikat(self, ax):
        tab = pd.crosstab(self.df["prodi"], self.df["predikat"]).reindex(
            columns=["A", "B", "C", "D"], fill_value=0)
        tab.plot(kind="bar", stacked=True, ax=ax, colormap="RdYlGn_r")
        ax.set_title("Sebaran predikat per program studi")
        ax.set_xlabel(""); ax.set_ylabel("Jumlah mahasiswa"); ax.tick_params(axis="x", rotation=10)
        ax.legend(title="Predikat")

    # ------------------------------------------------------------------
    # Export & state
    # ------------------------------------------------------------------
    def export(self, path_csv, path_xlsx=None):
        """Export data ke CSV; jika path_xlsx diberikan, buat laporan multi-sheet."""
        path_csv = Path(path_csv)
        path_csv.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(path_csv, index=False)
        if path_xlsx:
            with pd.ExcelWriter(path_xlsx) as xl:
                self.df.to_excel(xl, sheet_name="Data", index=False)
                self.statistik().to_excel(xl, sheet_name="Statistik")
                self.statistik_per_prodi().to_excel(xl, sheet_name="Per prodi")
                self.ranking(20).to_excel(xl, sheet_name="Top 20")
                self.df["predikat"].value_counts().rename("jumlah").to_frame().to_excel(
                    xl, sheet_name="Predikat")

    def simpan_state(self, path):
        """Simpan seluruh state (data + daftar matkul) ke file JSON."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        state = {"matkul": self.matkul, "data": self.df.drop(columns=["rata_rata", "predikat"])
                 .to_dict(orient="records")}
        path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")

    @classmethod
    def muat_state(cls, path):
        """Muat state dari JSON hasil simpan_state() dan kembalikan objek baru."""
        state = json.loads(Path(path).read_text(encoding="utf-8"))
        obj = cls(matkul=state["matkul"])
        obj.df = pd.DataFrame(state["data"], dtype=object)
        obj.df["nim"] = obj.df["nim"].astype(str)
        for mk in obj.matkul:
            obj.df[mk] = obj.df[mk].astype(float)
        obj._hitung_rata()
        return obj

    def __len__(self):
        return len(self.df)

    def __repr__(self):
        return f"AnalisisNilai({len(self)} mahasiswa, {len(self.matkul)} mata kuliah)"
