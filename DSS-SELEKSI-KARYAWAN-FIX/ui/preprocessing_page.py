
import streamlit as st
from modules.preprocessing import load_and_prepare_data
import pandas as pd

def show_preprocessing():

    st.title("🔧 Preprocessing Data")

    st.markdown("""
    Sebelum data kandidat bisa diproses menggunakan metode DSS,
    semua nilai kriteria harus **dinormalisasi** terlebih dahulu.
    Ini dilakukan karena tiap kriteria memiliki skala yang berbeda-beda.
    """)

    st.markdown("---")
    st.subheader("📐 Rumus Normalisasi")
    st.info("**Metode: Min-Max Scaling**")
    st.code("""
Nilai_Norm = (nilai - nilai_min) / (nilai_max - nilai_min)

Contoh:
  Tes Teknis = 75, Min = 40, Max = 100
  Nilai_Norm = (75 - 40) / (100 - 40) = 0.583
    """, language="text")
    st.warning("""
    **Asumsi:**
    - Min dan max dihitung dari data aktual 100 kandidat
    - Hasil selalu di rentang 0.0 hingga 1.0
    - Nilai 1.0 = terbaik, nilai 0.0 = terburuk untuk kriteria itu
    """)

    st.markdown("---")

    if "data" not in st.session_state:
        st.warning("⚠️ Silakan upload dataset terlebih dahulu.")
        return

    df = st.session_state["data"]

    st.subheader("👀 Data Awal")
    st.dataframe(df.head(10), use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Kandidat", len(df))
    col2.metric("Total Kolom", len(df.columns))
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.markdown("---")

    if st.button("⚙️ Generate Normalisasi", type="primary"):

        df_norm = load_and_prepare_data(df)
        st.session_state["preprocessed"] = df_norm
        st.success("✅ Normalisasi berhasil!")

        kolom_norm = [c for c in df_norm.columns if c.endswith("_Norm")]
        st.subheader("✅ Data Setelah Normalisasi")
        st.dataframe(df_norm[["ID_Kandidat","Nama"] + kolom_norm].head(10), use_container_width=True)
        st.dataframe(df_norm[kolom_norm].describe().round(4), use_container_width=True)
        st.info("✅ Lanjutkan ke menu **⚙️ Payoff Matrix**.")
