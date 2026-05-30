
import streamlit as st
import pandas as pd
import plotly.express as px
from modules.payoff import calculate_payoff

def show_payoff_workflow():

    st.title("⚙️ Payoff Matrix")

    st.markdown("""
    Payoff matrix menunjukkan **nilai kesesuaian setiap kandidat
    terhadap setiap kondisi perusahaan (state of nature)**.
    """)

    st.markdown("---")
    st.subheader("📐 Rumus Payoff")
    st.code("""
Payoff(kandidat_i, state_j) =
    Σ (Nilai_Norm_kriteria × Bobot_kriteria_di_state_j)

S1 Growth:     0.10×Pend + 0.30×Exp + 0.30×Teknis + 0.10×Waw + 0.10×Soft + 0.10×Disiplin
S2 Balanced:   0.15×Pend + 0.15×Exp + 0.20×Teknis + 0.20×Waw + 0.15×Soft + 0.15×Disiplin
S3 Efficiency: 0.10×Pend + 0.10×Exp + 0.10×Teknis + 0.20×Waw + 0.25×Soft + 0.25×Disiplin
    """, language="text")
    st.warning("""
    **Asumsi:**
    - Total bobot tiap state = 1.0
    - Matriks hasil berukuran 100×3, setiap sel nilainya unik
    - Semakin tinggi payoff → kandidat makin cocok di kondisi tersebut
    """)

    st.markdown("---")

    if "preprocessed" not in st.session_state:
        st.warning("⚠️ Lakukan preprocessing terlebih dahulu.")
        return

    df = st.session_state["preprocessed"]

    if st.button("⚙️ Generate Payoff Matrix", type="primary"):

        df_payoff = calculate_payoff(df)
        st.session_state["payoff"] = df_payoff
        st.success("✅ Payoff Matrix berhasil dihitung!")

        st.dataframe(
            df_payoff[["ID_Kandidat","Nama","Payoff_S1","Payoff_S2","Payoff_S3"]],
            use_container_width=True
        )

        tab1, tab2, tab3 = st.tabs(["S1 Growth","S2 Balanced","S3 Efficiency"])
        for tab, col, scale in zip(
            [tab1, tab2, tab3],
            ["Payoff_S1","Payoff_S2","Payoff_S3"],
            ["Blues","Greens","Oranges"]
        ):
            with tab:
                top10 = df_payoff.nlargest(10, col)
                fig = px.bar(top10, x="Nama", y=col, color=col,
                             color_continuous_scale=scale,
                             text=top10[col].round(4))
                fig.update_traces(textposition="outside")
                fig.update_layout(xaxis_tickangle=-30)
                st.plotly_chart(fig, use_container_width=True)

        st.info("✅ Lanjutkan ke menu **💎 EV & EOL**.")
