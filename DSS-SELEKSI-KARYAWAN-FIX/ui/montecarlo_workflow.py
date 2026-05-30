 
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from modules.montecarlo import run_monte_carlo
 
def show_montecarlo_workflow():
 
    st.title("🎲 Monte Carlo Simulation")
 
    st.markdown("""
    Monte Carlo Simulation menguji **kestabilan keputusan** dengan menjalankan
    1000 skenario di mana probabilitas state divariasikan secara acak menggunakan
    distribusi Dirichlet. Kandidat yang paling sering menang di berbagai skenario
    adalah kandidat yang paling **robust** dan layak direkomendasikan.
    """)
 
    st.markdown("---")
    st.subheader("📐 Rumus Monte Carlo")
    st.info("**Distribusi Dirichlet digunakan untuk mengacak probabilitas state secara proporsional**")
    st.code("""
Setiap iterasi (diulang 1000x):
  [P(S1), P(S2), P(S3)] ~ Dirichlet([3, 4, 3])
  → menghasilkan probabilitas acak yang tetap sum = 1.0
  → proporsional dengan nilai asli (0.30, 0.40, 0.30)
 
  EV_sim(i) = P_sim(S1) × Payoff_S1
            + P_sim(S2) × Payoff_S2
            + P_sim(S3) × Payoff_S3
 
  Winner = kandidat dengan EV_sim tertinggi di iterasi tersebut
 
Hasil akhir:
  Win_Rate(i) = Jumlah_Menang(i) / 1000 × 100%
    """, language="text")
    st.warning("""
    **Asumsi:**
    - Dirichlet([3,4,3]) menjaga proporsi asli namun dengan variasi alami
    - Kandidat dengan win rate tinggi = unggul di berbagai kondisi
    - Win rate rendah = kandidat hanya bagus di kondisi tertentu saja
    """)
 
    st.markdown("---")
 
    if "utility" not in st.session_state:
        st.warning("⚠️ Hitung Utility terlebih dahulu.")
        return
 
    df = st.session_state["utility"]
 
    n_sim = st.selectbox("Jumlah Simulasi", [100, 500, 1000, 5000], index=2)
 
    if st.button("🎲 Run Monte Carlo", type="primary"):
 
        with st.spinner(f"Menjalankan {n_sim} simulasi..."):
            hasil = run_monte_carlo(df, n_simulation=n_sim)
 
        st.session_state["mc_result"] = hasil
        st.success(f"✅ Monte Carlo selesai — {n_sim} simulasi!")
        st.markdown("---")
 
        terbaik_mc   = hasil.iloc[0]
        terbaik_info = df[df["ID_Kandidat"] == terbaik_mc["ID_Kandidat"]].iloc[0]
 
        st.subheader("🔢 Kandidat Paling Sering Menang")
        col1, col2, col3 = st.columns(3)
        col1.metric("Kandidat",     terbaik_info["Nama"])
        col2.metric("Jumlah Menang", int(terbaik_mc["Jumlah_Menang"]))
        col3.metric("Win Rate",     f"{terbaik_mc['Persentase']:.1f}%")
 
        st.markdown("---")
        st.subheader("📊 Hasil Monte Carlo")
        st.dataframe(
            hasil.merge(df[["ID_Kandidat","Nama"]], on="ID_Kandidat", how="left")
            [["ID_Kandidat","Nama","Jumlah_Menang","Persentase"]],
            use_container_width=True
        )
 
        st.markdown("---")
        st.subheader("📊 Visualisasi")
 
        tab1, tab2 = st.tabs(["🏆 Win Rate Top 15", "📊 Distribusi"])
 
        with tab1:
            top15 = hasil.head(15).merge(df[["ID_Kandidat","Nama"]], on="ID_Kandidat")
            fig = px.bar(
                top15, x="Nama", y="Persentase",
                title=f"Top 15 Win Rate Monte Carlo ({n_sim} Simulasi)",
                color="Persentase", color_continuous_scale="Greens",
                text=top15["Persentase"].round(1),
                labels={"Persentase": "Win Rate (%)", "Nama": "Kandidat"}
            )
            fig.update_traces(textposition="outside")
            fig.update_layout(xaxis_tickangle=-30)
            st.plotly_chart(fig, use_container_width=True)
 
        with tab2:
            fig2 = px.histogram(
                hasil, x="Persentase", nbins=20,
                title="Distribusi Win Rate Seluruh Kandidat",
                color_discrete_sequence=["mediumseagreen"],
                labels={"Persentase": "Win Rate (%)", "count": "Jumlah Kandidat"}
            )
            st.plotly_chart(fig2, use_container_width=True)
 
        st.info("✅ Lanjutkan ke menu **🏆 Final Recommendation**.")
