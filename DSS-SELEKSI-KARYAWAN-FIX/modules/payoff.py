
def calculate_payoff(df):

    df["Payoff_S1"] = (
        0.10 * df["Skor_Pendidikan_Norm"]
        + 0.30 * df["Pengalaman_Tahun_Norm"]
        + 0.30 * df["Tes_Teknis_Norm"]
        + 0.10 * df["Wawancara_Norm"]
        + 0.10 * df["Soft_Skills_Norm"]
        + 0.10 * df["Kedisiplinan_Norm"]
    )

    df["Payoff_S2"] = (
        0.15 * df["Skor_Pendidikan_Norm"]
        + 0.15 * df["Pengalaman_Tahun_Norm"]
        + 0.20 * df["Tes_Teknis_Norm"]
        + 0.20 * df["Wawancara_Norm"]
        + 0.15 * df["Soft_Skills_Norm"]
        + 0.15 * df["Kedisiplinan_Norm"]
    )

    df["Payoff_S3"] = (
        0.10 * df["Skor_Pendidikan_Norm"]
        + 0.10 * df["Pengalaman_Tahun_Norm"]
        + 0.10 * df["Tes_Teknis_Norm"]
        + 0.20 * df["Wawancara_Norm"]
        + 0.25 * df["Soft_Skills_Norm"]
        + 0.25 * df["Kedisiplinan_Norm"]
    )

    return df
