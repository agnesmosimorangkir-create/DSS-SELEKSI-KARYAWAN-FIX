
import streamlit as st
import plotly.express as px
from modules.ev_eol import calculate_ev_eol

def show_ev_eol():

    st.title("💎 EV & EOL Analysis")

    st.markdown("""
    **Expected Value (EV)** mengukur nilai harapan kandidat dengan mempertimbangkan
    probabilitas tiap kondisi perusahaan. **EOL** mengukur kerugian kesempatan
    jika kita tidak memilih kandidat terbaik.
    """)

    st.markdown("---")
    st.subheader("📐 Rumus EV & EOL")
    st.code("""
EV(i)  = 0.30×Payoff_S1 + 0.40×Payoff_S2 + 0.30×Payoff_S3
EOL(i) = EV_max - EV(i)

P(S1)=0.30  P(S2)=0.40  P(S3)=0.30  → Total=1.00
    """, language="text")
    st.warning("""
    **Asumsi:**
    - Probabilitas berlaku SAMA untuk semua kandidat
    - Kandidat EV tertinggi = EOL = 0 (kandidat terbaik)
    - Semakin kecil EOL semakin baik
    """)

    st.markdown("---")

    if "payoff" not in st.session_state:
        st.warning("⚠️ Generate Payoff Matrix terlebih dahulu.")
        return

    df = st.session_state["payoff"]

    if st.button("💎 Hitung EV dan EOL", type="primary"):

        hasil = calculate_ev_eol(df)
        st.session_state["ev_eol"] = hasil
        st.success("✅ EV dan EOL berhasil dihitung!")

        st.dataframe(
            hasil[["ID_Kandidat","Nama","EV","EOL","Rank_EV"]]
            .sort_values("EV", ascending=False).reset_index(drop=True),
            use_container_width=True
        )

        tab1, tab2, tab3 = st.tabs(["🏆 Top 15 EV","📉 Top 15 EOL","📊 Distribusi"])

        with tab1:
            top15 = hasil.nlargest(15,"EV")
            fig = px.bar(top15, x="Nama", y="EV", color="EV",
                         color_continuous_scale="Blues", text=top15["EV"].round(4))
            fig.update_traces(textposition="outside")
            fig.update_layout(xaxis_tickangle=-30)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            top15e = hasil.nsmallest(15,"EOL")
            fig2 = px.bar(top15e, x="Nama", y="EOL", color="EOL",
                          color_continuous_scale="Reds", text=top15e["EOL"].round(4))
            fig2.update_traces(textposition="outside")
            fig2.update_layout(xaxis_tickangle=-30)
            st.plotly_chart(fig2, use_container_width=True)

        with tab3:
            fig3 = px.histogram(hasil, x="EV", nbins=20,
                                color_discrete_sequence=["steelblue"])
            fig3.add_vline(x=hasil["EV"].mean(), line_dash="dash",
                           line_color="red",
                           annotation_text=f"Mean={hasil['EV'].mean():.4f}")
            st.plotly_chart(fig3, use_container_width=True)

        st.info("✅ Lanjutkan ke menu **📈 Uncertainty Analysis**.")
