"""Capstone Modul 6 (v2) — Jalur A: EDA dataset publik Titanic.

Alur: load + inspeksi -> cleaning -> feature engineering -> analisis
(groupby / pivot / korelasi / uji statistik) -> visualisasi -> insight -> export.

Jalankan dari folder mana pun:
    python src/main.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # aman dijalankan tanpa layar (server/CI)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_CSV = BASE_DIR / "data" / "raw" / "titanic.csv"
SUMBER_URL = (
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
)
CLEAN_CSV = BASE_DIR / "data" / "processed" / "data_bersih.csv"
FIG_DIR = BASE_DIR / "figures"
REPORT_DIR = BASE_DIR / "output"

PERTANYAAN = [
    "1. Faktor apa (jenis kelamin, kelas tiket, usia, ukuran keluarga, harga tiket) yang paling berkaitan dengan keselamatan?",
    "2. Apakah kelas tiket dan jenis kelamin saling memperkuat atau berdiri sendiri?",
    "3. Apakah anak-anak dan keluarga kecil punya peluang selamat yang berbeda dari penumpang lain?",
]
BATASAN = [
    "Data observasional dari satu peristiwa: temuan menunjukkan asosiasi, bukan sebab-akibat.",
    "177 nilai usia (19,9%) diimputasi dengan median per kelas & jenis kelamin sehingga sebaran usia sedikit lebih sempit dari aslinya.",
    "Kolom deck 77% kosong sehingga tidak dipakai sebagai faktor analisis.",
    "107 baris identik dipertahankan karena tidak ada ID penumpang; jika sebenarnya duplikat, proporsi bisa bergeser tipis.",
    "Kelompok kecil (lansia n=22, keluarga >= 5 orang n=62) membuat persentasenya tidak stabil.",
    "Harga tiket (fare) berkorelasi kuat dengan kelas tiket, sehingga efeknya tidak independen.",
]

sns.set_theme(style="whitegrid", palette="muted")
WARNA = {"Selamat": "#2a9d8f", "Tidak selamat": "#e76f51"}


# --------------------------------------------------------------------------
# 1. Load + inspeksi
# --------------------------------------------------------------------------
def load_data(path=RAW_CSV, url=SUMBER_URL):
    """Baca CSV lokal; jika belum ada, unduh dari sumber lalu simpan."""
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"{path.name} belum ada, mengunduh dari sumber ...")
        df = pd.read_csv(url)
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)
        return df


def inspeksi(df):
    """Cetak ringkasan awal: shape, dtypes, missing, duplikat."""
    print("=" * 60)
    print("1. INSPEKSI AWAL")
    print("=" * 60)
    print("Shape:", df.shape)
    print("\nTipe data:")
    print(df.dtypes.to_string())
    miss = df.isna().sum()
    miss = miss[miss > 0]
    print("\nMissing values (jumlah, persen):")
    for kolom, n in miss.items():
        print(f"  {kolom:<12} {n:>4}  ({n / len(df):.1%})")
    print("\nBaris duplikat penuh:", int(df.duplicated().sum()))
    print("\nStatistik numerik:")
    print(df.describe().round(2).to_string())


# --------------------------------------------------------------------------
# 2. Cleaning + feature engineering
# --------------------------------------------------------------------------
def cleaning(df):
    """Bersihkan data dan kembalikan (df_bersih, catatan_cleaning)."""
    df = df.copy()
    catatan = []

    n_dup = int(df.duplicated().sum())
    catatan.append(
        f"{n_dup} baris identik terdeteksi tetapi TIDAK dihapus: dataset tidak "
        "punya ID penumpang, sehingga baris identik bisa jadi orang berbeda "
        "(mis. anggota keluarga dengan tiket sama)."
    )

    # age: isi dengan median per kombinasi kelas & jenis kelamin
    n_age = int(df["age"].isna().sum())
    df["age_imputed"] = df["age"].isna()
    df["age"] = df["age"].fillna(
        df.groupby(["pclass", "sex"])["age"].transform("median")
    )
    catatan.append(
        f"{n_age} nilai age kosong diisi median per (pclass, sex); "
        "kolom age_imputed menandai baris tersebut."
    )

    # embarked / embark_town: hanya 2 kosong -> modus
    for kolom in ("embarked", "embark_town"):
        df[kolom] = df[kolom].fillna(df[kolom].mode()[0])
    catatan.append("2 nilai embarked/embark_town kosong diisi modus (Southampton/S).")

    # deck: terlalu banyak kosong -> kategori 'Unknown'
    n_deck = int(df["deck"].isna().sum())
    df["deck"] = df["deck"].fillna("Unknown")
    catatan.append(
        f"{n_deck} nilai deck kosong ({n_deck / len(df):.0%}) diberi kategori "
        "'Unknown' (tidak diimputasi karena terlalu banyak)."
    )

    # kolom redundan
    df = df.drop(columns=["alive", "class"])
    catatan.append("Kolom alive & class dihapus (duplikasi dari survived & pclass).")

    # tipe data
    for kolom in ("sex", "embarked", "embark_town", "who", "deck"):
        df[kolom] = df[kolom].astype("category")
    catatan.append("Kolom teks dikonversi ke tipe category.")

    # feature engineering
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=["Anak (0-12)", "Remaja (13-18)", "Dewasa muda (19-35)",
                "Dewasa (36-60)", "Lansia (60+)"],
    )
    df["fare_quartile"] = pd.qcut(
        df["fare"], 4, labels=["Q1 termurah", "Q2", "Q3", "Q4 termahal"]
    )
    df["status"] = np.where(df["survived"] == 1, "Selamat", "Tidak selamat")
    catatan.append(
        "Fitur baru: family_size, age_group, fare_quartile, status."
    )

    assert df[["age", "fare", "embarked"]].isna().sum().sum() == 0
    return df, catatan


# --------------------------------------------------------------------------
# 3. Analisis
# --------------------------------------------------------------------------
def analisis(df):
    """Jalankan groupby, pivot, korelasi, dan uji statistik; kembalikan dict hasil."""
    hasil = {}
    hasil["overall"] = df["survived"].mean()
    hasil["by_sex"] = df.groupby("sex", observed=True)["survived"].agg(["count", "mean"])
    hasil["by_class"] = df.groupby("pclass")["survived"].agg(["count", "mean"])
    hasil["pivot_sex_class"] = df.pivot_table(
        values="survived", index="sex", columns="pclass",
        aggfunc="mean", observed=True,
    )
    hasil["by_age_group"] = df.groupby("age_group", observed=True)["survived"].agg(["count", "mean"])
    hasil["by_family"] = df.groupby("family_size")["survived"].agg(["count", "mean"])
    hasil["by_embark"] = df.groupby("embark_town", observed=True)["survived"].agg(["count", "mean"])
    hasil["fare_by_class"] = df.groupby("pclass")["fare"].agg(["median", "mean", "max"])
    hasil["korelasi"] = df[["survived", "pclass", "age", "sibsp", "parch", "fare", "family_size"]].corr()

    # uji statistik sederhana (stretch goal)
    tabel_sex = pd.crosstab(df["sex"], df["survived"])
    chi2, p_sex, _, _ = stats.chi2_contingency(tabel_sex)
    tabel_cls = pd.crosstab(df["pclass"], df["survived"])
    chi2_c, p_cls, _, _ = stats.chi2_contingency(tabel_cls)
    fare_sel = df.loc[df["survived"] == 1, "fare"]
    fare_tdk = df.loc[df["survived"] == 0, "fare"]
    u, p_fare = stats.mannwhitneyu(fare_sel, fare_tdk, alternative="two-sided")
    hasil["uji"] = pd.DataFrame(
        {
            "uji": ["Chi-square sex x survived", "Chi-square pclass x survived",
                    "Mann-Whitney fare (selamat vs tidak)"],
            "statistik": [chi2, chi2_c, u],
            "p_value": [p_sex, p_cls, p_fare],
        }
    )
    return hasil


# --------------------------------------------------------------------------
# 4. Visualisasi
# --------------------------------------------------------------------------
def _simpan(fig, nama):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_DIR / f"{nama}.png", dpi=150, bbox_inches="tight")


def _plot_sex_class(ax, df):
    sns.barplot(data=df, x="pclass", y="survived", hue="sex", errorbar=None, ax=ax)
    ax.set_title("Tingkat keselamatan per kelas & jenis kelamin")
    ax.set_xlabel("Kelas tiket"); ax.set_ylabel("Proporsi selamat")
    ax.set_ylim(0, 1); ax.legend(title="Jenis kelamin")
    for c in ax.containers:
        ax.bar_label(c, fmt="%.2f", padding=2)


def _plot_age(ax, df):
    for status, warna in WARNA.items():
        sns.histplot(df.loc[df["status"] == status, "age"], bins=25, kde=True,
                     stat="density", color=warna, alpha=0.45, label=status, ax=ax)
    ax.set_title("Distribusi usia berdasarkan keselamatan")
    ax.set_xlabel("Usia (tahun)"); ax.set_ylabel("Kepadatan"); ax.legend()


def _plot_fare(ax, df):
    sns.boxplot(data=df, x="pclass", y="fare", ax=ax, color="#8ecae6")
    ax.set_yscale("log")
    ax.set_title("Harga tiket per kelas (skala log)")
    ax.set_xlabel("Kelas tiket"); ax.set_ylabel("Fare (log)")


def _plot_corr(ax, hasil):
    sns.heatmap(hasil["korelasi"], annot=True, fmt=".2f", cmap="coolwarm",
                center=0, ax=ax, cbar=False, annot_kws={"size": 8})
    ax.set_title("Korelasi antar variabel numerik")


def _plot_family(ax, hasil):
    d = hasil["by_family"].reset_index()
    sns.barplot(data=d, x="family_size", y="mean", ax=ax, color="#457b9d")
    ax.set_title("Tingkat keselamatan menurut ukuran keluarga")
    ax.set_xlabel("Ukuran keluarga (termasuk diri sendiri)")
    ax.set_ylabel("Proporsi selamat"); ax.set_ylim(0, 1)
    for i, (n, m) in enumerate(zip(d["count"], d["mean"])):
        ax.text(i, m + 0.02, f"n={n}", ha="center", fontsize=8)


def _plot_age_sex(ax, df):
    sns.barplot(data=df, x="age_group", y="survived", hue="sex", errorbar=None, ax=ax)
    ax.set_title("Tingkat keselamatan per kelompok usia & jenis kelamin")
    ax.set_xlabel("Kelompok usia"); ax.set_ylabel("Proporsi selamat")
    ax.set_ylim(0, 1); ax.tick_params(axis="x", rotation=20); ax.legend(title="")


def visualisasi(df, hasil):
    """Buat 6 grafik terpisah + 1 dashboard 2x3 (PNG & PDF)."""
    plot_df = [
        ("01_keselamatan_kelas_sex", _plot_sex_class, (df,)),
        ("02_distribusi_usia", _plot_age, (df,)),
        ("03_harga_tiket_per_kelas", _plot_fare, (df,)),
        ("04_korelasi", _plot_corr, (hasil,)),
        ("05_ukuran_keluarga", _plot_family, (hasil,)),
        ("06_usia_dan_sex", _plot_age_sex, (df,)),
    ]
    for nama, fungsi, args in plot_df:
        fig, ax = plt.subplots(figsize=(8, 5))
        fungsi(ax, *args)
        fig.tight_layout()
        _simpan(fig, nama)
        plt.close(fig)

    fig, axes = plt.subplots(2, 3, figsize=(20, 11))
    for ax, (_, fungsi, args) in zip(axes.ravel(), plot_df):
        fungsi(ax, *args)
    fig.suptitle("Dashboard EDA Titanic (891 penumpang)", fontsize=18, y=1.0)
    fig.tight_layout()
    _simpan(fig, "00_dashboard")
    fig.savefig(FIG_DIR / "00_dashboard.pdf", bbox_inches="tight")
    plt.close(fig)


# --------------------------------------------------------------------------
# 5. Insight + export
# --------------------------------------------------------------------------
def tulis_insight(df, hasil):
    """Susun insight berbasis angka hasil analisis (ditulis ke insights.md)."""
    s = hasil["by_sex"]["mean"]
    c = hasil["by_class"]["mean"]
    pv = hasil["pivot_sex_class"]
    ag = hasil["by_age_group"]
    fam = hasil["by_family"]
    uji = hasil["uji"].set_index("uji")["p_value"]
    kor = hasil["korelasi"]["survived"].drop("survived").sort_values()
    sendiri = fam.loc[1, "mean"]
    kecil = df.loc[df["family_size"].between(2, 4), "survived"].mean()
    besar = df.loc[df["family_size"] >= 5, "survived"].mean()
    n_besar = int((df["family_size"] >= 5).sum())

    baris = [
        f"1. **Jenis kelamin adalah pembeda terkuat.** {s['female']:.1%} penumpang "
        f"perempuan selamat, dibanding {s['male']:.1%} laki-laki "
        f"(selisih {(s['female'] - s['male']) * 100:.0f} poin persentase; "
        f"chi-square p = {uji['Chi-square sex x survived']:.1e}).",
        f"2. **Kelas tiket memengaruhi peluang selamat.** Kelas 1: {c[1]:.1%}, "
        f"kelas 2: {c[2]:.1%}, kelas 3: {c[3]:.1%} "
        f"(chi-square p = {uji['Chi-square pclass x survived']:.1e}). "
        f"Korelasi pclass dengan survived = {kor['pclass']:.2f}.",
        f"3. **Efek kelas dan jenis kelamin saling menguatkan.** Perempuan kelas 1 "
        f"selamat {pv.loc['female', 1]:.1%}, sedangkan laki-laki kelas 3 hanya "
        f"{pv.loc['male', 3]:.1%}. Namun perempuan kelas 3 ({pv.loc['female', 3]:.1%}) "
        f"masih lebih baik daripada laki-laki kelas 1 ({pv.loc['male', 1]:.1%}).",
        f"4. **Anak-anak diprioritaskan.** Kelompok usia 0-12 tahun selamat "
        f"{ag.loc['Anak (0-12)', 'mean']:.1%} (n={int(ag.loc['Anak (0-12)', 'count'])}), "
        f"lebih tinggi daripada dewasa muda 19-35 tahun "
        f"({ag.loc['Dewasa muda (19-35)', 'mean']:.1%}) dan lansia 60+ "
        f"({ag.loc['Lansia (60+)', 'mean']:.1%}).",
        f"5. **Ukuran keluarga berhubungan non-linier dengan keselamatan.** "
        f"Penumpang sendirian selamat {sendiri:.1%}, keluarga 2-4 orang {kecil:.1%}, "
        f"dan keluarga >= 5 orang hanya {besar:.1%} (n={n_besar}).",
        f"6. **Harga tiket berkorelasi positif dengan keselamatan.** Median fare "
        f"kelas 1 = {hasil['fare_by_class'].loc[1, 'median']:.1f} vs kelas 3 = "
        f"{hasil['fare_by_class'].loc[3, 'median']:.1f}; penumpang yang selamat "
        f"membayar lebih mahal (Mann-Whitney p = {uji['Mann-Whitney fare (selamat vs tidak)']:.1e}; "
        f"korelasi fare-survived = {kor['fare']:.2f}).",
    ]
    return "\n\n".join(baris) + "\n"


def export(df, hasil, catatan, insight):
    """Simpan data bersih, tabel ringkasan, Excel multi-sheet, dan teks insight."""
    CLEAN_CSV.parent.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEAN_CSV, index=False)

    ringkasan = hasil["by_class"].join(
        hasil["fare_by_class"], rsuffix="_fare"
    ).rename(columns={"count": "jumlah", "mean": "proporsi_selamat"})
    ringkasan.round(4).to_csv(REPORT_DIR / "ringkasan.csv")
    hasil["pivot_sex_class"].round(4).to_csv(REPORT_DIR / "pivot_sex_kelas.csv")

    with pd.ExcelWriter(REPORT_DIR / "laporan_titanic.xlsx") as xl:
        ringkasan.round(4).to_excel(xl, sheet_name="Per kelas")
        hasil["by_sex"].round(4).to_excel(xl, sheet_name="Per sex")
        hasil["pivot_sex_class"].round(4).to_excel(xl, sheet_name="Pivot sex x kelas")
        hasil["by_age_group"].round(4).to_excel(xl, sheet_name="Per usia")
        hasil["by_family"].round(4).to_excel(xl, sheet_name="Per keluarga")
        hasil["korelasi"].round(3).to_excel(xl, sheet_name="Korelasi")
        hasil["uji"].to_excel(xl, sheet_name="Uji statistik", index=False)
        pd.DataFrame({"catatan_cleaning": catatan}).to_excel(
            xl, sheet_name="Catatan cleaning", index=False
        )
    teks = insight.replace("**", "") + "\nBatasan:\n" + "\n".join(f"- {b}" for b in BATASAN) + "\n"
    (REPORT_DIR / "insight.txt").write_text(teks, encoding="utf-8")


def main():
    print("PERTANYAAN ANALISIS")
    print("\n".join(PERTANYAAN))
    print()
    df_raw = load_data()
    inspeksi(df_raw)

    print("\n" + "=" * 60 + "\n2. CLEANING\n" + "=" * 60)
    df, catatan = cleaning(df_raw)
    for c in catatan:
        print("-", c)
    print("Shape setelah cleaning:", df.shape)

    print("\n" + "=" * 60 + "\n3. ANALISIS\n" + "=" * 60)
    hasil = analisis(df)
    print(f"Tingkat keselamatan keseluruhan: {hasil['overall']:.1%}")
    for kunci in ("by_sex", "by_class", "pivot_sex_class", "by_age_group",
                  "by_family", "by_embark", "fare_by_class", "uji"):
        print(f"\n[{kunci}]")
        if kunci == "uji":
            print(hasil[kunci].to_string(
                formatters={"statistik": "{:.2f}".format, "p_value": "{:.2e}".format}))
        else:
            print(hasil[kunci].round(4).to_string())

    visualisasi(df, hasil)
    insight = tulis_insight(df, hasil)
    export(df, hasil, catatan, insight)

    print("\n" + "=" * 60 + "\n4. INSIGHT\n" + "=" * 60)
    print(insight)
    print("Batasan:")
    print("\n".join(f"- {b}" for b in BATASAN))
    print("\nSelesai. File tersimpan di data/processed/, figures/, dan output/.")


if __name__ == "__main__":
    main()
