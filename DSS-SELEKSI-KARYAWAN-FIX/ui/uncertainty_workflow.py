
import streamlit as st
import pandas as pd
import plotly.express as px
from modules.uncertainty import calculate_uncertainty

def show_uncertainty():

    st.title("📈 Uncertainty Analysis")

    st.markdown("""
    Analisis keputusan **tanpa asumsi probabilitas pasti** menggunakan
    4 kriteria keputusan: Maximax, Maximin, Laplace, dan Hurwicz.
    """)

    st.markdown("---")
    st.subheader("📐 Rumus Uncertainty")
    st.code("""
Maximax  = max(Payoff_S1, Payoff_S2, Payoff_S3)   → optimistis
Maximin  = min(Payoff_S1, Payoff_S2, Payoff_S3)   → pesimistis
Laplace  = (Payoff_S1 + Payoff_S2 + Payoff_S3) / 3
Hurwicz  = 0.6×Maximax + 0.4×Maximin              → α=0.6
    """, language="text")
    st.warning("""
    **Asumsi:**
    - α = 0.6 → pengambil keputusan cenderung optimis
    - Hurwicz adalah kompromi antara Maximax dan Maximin
    """)

    st.markdown("---")

    if "ev_eol" not in st.session_state:
        st.warning("⚠️ Hitung EV & EOL terlebih dahulu.")
        return

    df = st.session_state["ev_eol"]

    if st.button("📈 Analisis Uncertainty", type="primary"):

        hasil = calculate_uncertainty(df)
        st.session_state["uncertainty"] = hasil
        st.success("✅ Uncertainty Analysis berhasil!")

        st.dataframe(
            hasil[["ID_Kandidat","Nama","Maximax","Maximin","Laplace","Hurwicz"]]
            .sort_values("Hurwicz", ascending=False).reset_index(drop=True),
            use_container_width=True
        )

        tab1, tab2, tab3, tab4 = st.tabs(["Maximax","Maximin","Laplace","Hurwicz"])
        for tab, col, scale in zip(
            [tab1, tab2, tab3, tab4],
            ["Maximax","Maximin","Laplace","Hurwicz"],
            ["Blues","Reds","Greens","Oranges"]
        ):
            with tab:
                top10 = hasil.nlargest(10, col)
                fig = px.bar(top10, x="Nama", y=col, color=col,
                             color_continuous_scale=scale,
                             text=top10[col].round(4))
                fig.update_traces(textposition="outside")
                fig.update_layout(xaxis_tickangle=-30)
                st.plotly_chart(fig, use_container_width=True)

        st.info("✅ Lanjutkan ke menu **⚖️ Utility Analysis**.")
