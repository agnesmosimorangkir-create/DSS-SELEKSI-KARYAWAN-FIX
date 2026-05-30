
import pandas as pd

def load_and_prepare_data(df):

    kriteria = [
        "Skor_Pendidikan",
        "Pengalaman_Tahun",
        "Tes_Teknis",
        "Wawancara",
        "Soft_Skills",
        "Kedisiplinan"
    ]

    for k in kriteria:
        df[k+"_Norm"] = (
            (df[k] - df[k].min())
            /
            (df[k].max() - df[k].min())
        )

    return df
