
import streamlit as st
import plotly.express as px
import numpy as np
from modules.utility import calculate_utility

def show_utility_workflow():

    st.title("⚖️ Utility Analysis")

    st.markdown("""
    Utility Analysis mengubah payoff menggunakan **fungsi akar kuadrat**
    yang mencerminkan sikap **risk-averse** — menghindari risiko.
    """)

    st.markdown("---")
    st.subheader("📐 Rumus Utility")
    st.code("""
Utility(i, Sj)      = √Payoff(i, Sj)

Expected_Utility(i) = 0.30×√Payoff_S1
                    + 0.40×√Payoff_S2
                    + 0.30×√Payoff_S3
    """, language="text")
    st.warning("""
    **Asumsi:**
    - Fungsi √x = risk-averse (menghindari risiko)
    - Karena payoff di 0–1, maka √Payoff ≥ Payoff selalu
    - Probabilitas sama dengan EV: 0.30 / 0.40 / 0.30
    """)

    st.markdown("---")

    if "uncertainty" not in st.session_state:
        st.warning("⚠️ Lakukan Uncertainty Analysis terlebih dahulu.")
        return

    df = st.session_state["uncertainty"]

    if st.button("⚖️ Hitung Utility", type="primary"):

        hasil = calculate_utility(df)
        st.session_state["utility"] = hasil
        st.success("✅ Expected Utility berhasil dihitung!")

        st.dataframe(
            hasil[["ID_Kandidat","Nama","Utility_S1","Utility_S2",
                   "Utility_S3","Expected_Utility"]]
            .sort_values("Expected_Utility", ascending=False).reset_index(drop=True),
            use_container_width=True
        )

        tab1, tab2 = st.tabs(["🏆 Top 15","📊 Distribusi"])

        with tab1:
            top15 = hasil.nlargest(15,"Expected_Utility")
            fig = px.bar(top15, x="Nama", y="Expected_Utility",
                         color="Expected_Utility", color_continuous_scale="Greens",
                         text=top15["Expected_Utility"].round(4))
            fig.update_traces(textposition="outside")
            fig.update_layout(xaxis_tickangle=-30)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            fig2 = px.histogram(hasil, x="Expected_Utility", nbins=20,
                                color_discrete_sequence=["mediumseagreen"])
            fig2.add_vline(x=hasil["Expected_Utility"].mean(), line_dash="dash",
                           line_color="red",
                           annotation_text=f"Mean={hasil['Expected_Utility'].mean():.4f}")
            st.plotly_chart(fig2, use_container_width=True)

        st.info("✅ Lanjutkan ke menu **🎲 Monte Carlo Simulation**.")
