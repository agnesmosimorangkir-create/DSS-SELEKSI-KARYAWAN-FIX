
import streamlit as st
import pandas as pd

def show_upload():

    st.title("📂 Upload Dataset Kandidat")

    uploaded_file = st.file_uploader(
        "Upload File Kandidat",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ Dataset berhasil diupload!")
        st.dataframe(df, use_container_width=True)
        st.session_state["data"] = df
        return df

    return None
