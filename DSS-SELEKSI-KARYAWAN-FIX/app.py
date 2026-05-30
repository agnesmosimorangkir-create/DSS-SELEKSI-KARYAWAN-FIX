 
import streamlit as st
import pandas as pd
 
from ui.upload_page import show_upload
from ui.preprocessing_page import show_preprocessing
from ui.payoff_workflow import show_payoff_workflow
from ui.ev_eol_workflow import show_ev_eol
from ui.uncertainty_workflow import show_uncertainty
from ui.utility_workflow import show_utility_workflow
from ui.montecarlo_workflow import show_montecarlo_workflow
from ui.final_recommendation import show_final_recommendation
 
st.set_page_config(
    page_title="DSS Seleksi Karyawan",
    page_icon="🏆",
    layout="wide"
)
 
st.sidebar.title("🏆 DSS Talent Selection")
st.sidebar.markdown("---")
st.sidebar.markdown("**Agnes Monica Simorangkir**")
st.sidebar.markdown("NIM: 4233260018")
st.sidebar.markdown("---")
 
menu = st.sidebar.radio(
    "Navigasi",
    [
        "🏠 Beranda",
        "📂 Upload Dataset",
        "🔧 Preprocessing",
        "⚙️ Payoff Matrix",
        "💎 EV & EOL",
        "📈 Uncertainty Analysis",
        "⚖️ Utility Analysis",
        "🎲 Monte Carlo Simulation",
        "🏆 Final Recommendation"
    ]
)
 
# ============================================================
# BERANDA
# ============================================================
 
if menu == "🏠 Beranda":
 
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1e3a5f 0%, #2e86ab 100%);
                    padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem;'>
            <h1 style='color:white; margin:0; font-size:2rem;'>
                🏆 Sistem Pendukung Keputusan
            </h1>
            <h2 style='color:#a8d8ea; margin:0.3rem 0 1rem 0;
                       font-size:1.3rem; font-weight:400;'>
                Seleksi Karyawan Berbasis DSS
            </h2>
            <hr style='border-color: rgba(255,255,255,0.2); margin: 1rem 0;'>
            <p style='color:white; margin:0; font-size:1rem;'>
                👩‍🎓 <strong>Agnes Monica Simorangkir</strong>
                &nbsp;&nbsp;|&nbsp;&nbsp;
                🎓 NIM: <strong>4233260018</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)
 
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("👥 Kandidat", "100 Orang")
    c2.metric("🌐 State of Nature", "3 Kondisi")
    c3.metric("📊 Kriteria", "6 Kriteria")
    c4.metric("🎲 Simulasi MC", "1000 Iterasi")
 
    st.markdown("---")
 
    # --- Tentang Sistem ---
    st.subheader("📌 Tentang Sistem")
    st.markdown("""
    Sistem ini adalah **Decision Support System (DSS)** yang dirancang untuk membantu
    perusahaan memilih kandidat karyawan terbaik secara objektif dan terstruktur.
 
    DSS ini menggabungkan beberapa metode analisis keputusan yang mempertimbangkan
    **ketidakpastian kondisi bisnis** di masa depan, sehingga rekomendasi yang dihasilkan
    lebih **robust** dan **terpercaya** dibanding hanya mengandalkan satu metode tunggal.
    """)
 
    st.markdown("---")
 
    # --- Alur Sistem ---
    st.subheader("🔄 Alur Sistem DSS")
 
    col_a, col_b = st.columns([1, 2])
 
    with col_a:
        st.markdown("""
        | Langkah | Proses |
        |---|---|
        | 1️⃣ | Upload Dataset |
        | 2️⃣ | Preprocessing & Normalisasi |
        | 3️⃣ | Hitung Payoff Matrix |
        | 4️⃣ | Hitung EV & EOL |
        | 5️⃣ | Uncertainty Analysis |
        | 6️⃣ | Utility Analysis |
        | 7️⃣ | Monte Carlo Simulation |
        | 8️⃣ | Rekomendasi Final |
        """)
 
    with col_b:
        st.info("""
        **Mengapa perlu beberapa metode?**
 
        Tidak ada satu metode yang sempurna untuk semua situasi.
        Dengan menggabungkan EV, EOL, Utility, dan Monte Carlo,
        kita bisa melihat kandidat mana yang **konsisten unggul**
        dari berbagai sudut pandang analisis — bukan hanya dari
        satu perspektif saja.
        """)
 
    st.markdown("---")
 
    # --- State of Nature ---
    st.subheader("🌐 State of Nature")
    st.markdown("""
    State of nature adalah **kondisi perusahaan di masa depan** yang tidak bisa
    dikontrol pengambil keputusan, namun bisa diperkirakan probabilitasnya oleh manajemen.
    Probabilitas state berlaku **sama untuk semua kandidat**.
    """)
 
    col1, col2, col3 = st.columns(3)
 
    with col1:
        st.markdown("""
        <div style='background:#e8f4f8; padding:1.2rem; border-radius:12px;
                    border-left: 5px solid #2196F3;'>
            <h4 style='color:#1565C0; margin:0;'>🚀 S1 — Growth Mode</h4>
            <p style='margin:0.5rem 0 0 0; font-size:0.9rem;'>
                Perusahaan sedang berkembang pesat.
                Prioritas: <strong>pengalaman & teknis</strong>.
            </p>
            <p style='margin:0.8rem 0 0 0; color:#1565C0;
                      font-weight:bold; font-size:1.1rem;'>
                P(S1) = 0.30
            </p>
        </div>
        """, unsafe_allow_html=True)
 
    with col2:
        st.markdown("""
        <div style='background:#e8f5e9; padding:1.2rem; border-radius:12px;
                    border-left: 5px solid #4CAF50;'>
            <h4 style='color:#2E7D32; margin:0;'>⚖️ S2 — Balanced Mode</h4>
            <p style='margin:0.5rem 0 0 0; font-size:0.9rem;'>
                Kondisi perusahaan stabil.
                Semua kriteria <strong>seimbang</strong>.
            </p>
            <p style='margin:0.8rem 0 0 0; color:#2E7D32;
                      font-weight:bold; font-size:1.1rem;'>
                P(S2) = 0.40
            </p>
        </div>
        """, unsafe_allow_html=True)
 
    with col3:
        st.markdown("""
        <div style='background:#fff3e0; padding:1.2rem; border-radius:12px;
                    border-left: 5px solid #FF9800;'>
            <h4 style='color:#E65100; margin:0;'>💼 S3 — Efficiency Mode</h4>
            <p style='margin:0.5rem 0 0 0; font-size:0.9rem;'>
                Perusahaan fokus efisiensi.
                Prioritas: <strong>soft skills & disiplin</strong>.
            </p>
            <p style='margin:0.8rem 0 0 0; color:#E65100;
                      font-weight:bold; font-size:1.1rem;'>
                P(S3) = 0.30
            </p>
        </div>
        """, unsafe_allow_html=True)
 
    st.markdown("---")
 
    # --- Kriteria ---
    st.subheader("📋 Kriteria Penilaian & Bobot Per State")
    st.markdown("""
    Setiap kandidat dinilai dari **6 kriteria**. Bobot tiap kriteria
    **berbeda per state** karena prioritas perusahaan berbeda di tiap kondisi.
    """)
 
    df_kriteria = pd.DataFrame({
        "Kriteria": [
            "Skor Pendidikan",
            "Pengalaman Kerja",
            "Tes Teknis",
            "Wawancara",
            "Soft Skills",
            "Kedisiplinan"
        ],
        "Skala": [
            "1–4 (SMA=1, D3=2, S1=3, S2=4)",
            "0–10 tahun",
            "0–100",
            "0–100",
            "0–100",
            "0–100"
        ],
        "Bobot S1 Growth": [
            "0.10", "0.30", "0.30", "0.10", "0.10", "0.10"
        ],
        "Bobot S2 Balanced": [
            "0.15", "0.15", "0.20", "0.20", "0.15", "0.15"
        ],
        "Bobot S3 Efficiency": [
            "0.10", "0.10", "0.10", "0.20", "0.25", "0.25"
        ],
    })
 
    st.dataframe(df_kriteria, use_container_width=True, hide_index=True)
 
    st.markdown("---")
 
    # --- Rumus & Asumsi Per Metode ---
    st.subheader("🧮 Rumus & Asumsi Tiap Metode")
 
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📦 Payoff",
        "💎 EV",
        "📉 EOL",
        "📈 Uncertainty",
        "⚖️ Utility",
        "🎲 Monte Carlo"
    ])
 
    with tab1:
        st.markdown("### 📦 Payoff Matrix")
        st.info("""
        **Definisi:** Payoff adalah nilai kesesuaian kandidat terhadap
        suatu kondisi perusahaan tertentu.
        """)
        st.code("""
Langkah 1 — Normalisasi (Min-Max Scaling):
  Nilai_Norm = (nilai - nilai_min) / (nilai_max - nilai_min)
 
Langkah 2 — Hitung Payoff:
  Payoff(kandidat_i, state_j) =
      Σ (Nilai_Norm_kriteria × Bobot_kriteria_di_state_j)
 
Contoh S1:
  Payoff_S1 = 0.10×Pend_Norm + 0.30×Exp_Norm + 0.30×Teknis_Norm
            + 0.10×Wawancara_Norm + 0.10×Soft_Norm + 0.10×Disiplin_Norm
        """, language="text")
        st.warning("""
        **Asumsi:**
        - Bobot ditentukan manajemen berdasarkan prioritas bisnis per kondisi
        - Hasilnya matriks 100×3, setiap sel nilainya unik
        - Semakin tinggi payoff → kandidat makin cocok di kondisi tersebut
        """)
 
    with tab2:
        st.markdown("### 💎 Expected Value (EV)")
        st.info("""
        **Definisi:** Nilai harapan kandidat yang mempertimbangkan
        probabilitas tiap kondisi perusahaan.
        """)
        st.code("""
EV(i) = P(S1) × Payoff(i, S1)
      + P(S2) × Payoff(i, S2)
      + P(S3) × Payoff(i, S3)
 
EV(i) = 0.30 × Payoff_S1
      + 0.40 × Payoff_S2
      + 0.30 × Payoff_S3
        """, language="text")
        st.warning("""
        **Asumsi:**
        - Probabilitas state bersifat subjektif — ditentukan manajemen
        - Probabilitas berlaku SAMA untuk semua kandidat
        - Kandidat dengan EV tertinggi = paling direkomendasikan
        """)
 
    with tab3:
        st.markdown("### 📉 Expected Opportunity Loss (EOL)")
        st.info("""
        **Definisi:** Kerugian kesempatan jika kita tidak memilih
        kandidat terbaik.
        """)
        st.code("""
EOL(i) = EV_max - EV(i)
 
Keterangan:
  EV_max = nilai EV tertinggi dari seluruh kandidat
  EOL = 0  → kandidat ini adalah yang terbaik
  EOL besar → makin besar kerugian jika kandidat ini dipilih
        """, language="text")
        st.warning("""
        **Asumsi:**
        - EOL melengkapi EV — kandidat terbaik dari EV = EOL terkecil (0)
        - Semakin kecil EOL semakin baik
        """)
 
    with tab4:
        st.markdown("### 📈 Uncertainty Analysis")
        st.info("""
        **Definisi:** Analisis keputusan tanpa asumsi probabilitas pasti,
        menggunakan beberapa kriteria keputusan berbeda.
        """)
        st.code("""
Maximax = max(Payoff_S1, Payoff_S2, Payoff_S3)
          → Pilihan optimistis (ambil yang terbaik dari terbaik)
 
Maximin = min(Payoff_S1, Payoff_S2, Payoff_S3)
          → Pilihan pesimistis (lindungi dari skenario terburuk)
 
Laplace = (Payoff_S1 + Payoff_S2 + Payoff_S3) / 3
          → Semua state dianggap sama peluangnya
 
Hurwicz = α × Maximax + (1-α) × Maximin   [α = 0.6]
          → Kompromi antara optimis dan pesimis
        """, language="text")
        st.warning("""
        **Asumsi:**
        - α = 0.6 artinya pengambil keputusan cenderung optimis
        - Hurwicz adalah metode yang paling sering dipakai sebagai kompromi
        """)
 
    with tab5:
        st.markdown("### ⚖️ Utility Analysis")
        st.info("""
        **Definisi:** Transformasi payoff menggunakan fungsi utility
        untuk mencerminkan preferensi risiko pengambil keputusan.
        """)
        st.code("""
Utility(i, Sj) = √Payoff(i, Sj)
                 → Fungsi akar kuadrat = risk-averse
 
Expected_Utility(i) = P(S1) × Utility(i,S1)
                    + P(S2) × Utility(i,S2)
                    + P(S3) × Utility(i,S3)
 
Expected_Utility(i) = 0.30×√Payoff_S1
                    + 0.40×√Payoff_S2
                    + 0.30×√Payoff_S3
        """, language="text")
        st.warning("""
        **Asumsi:**
        - Fungsi akar kuadrat = pengambil keputusan bersifat risk-averse
        - Artinya: lebih menghargai peningkatan kecil di level rendah
          dibanding peningkatan besar di level tinggi
        - Kandidat dengan Expected Utility tertinggi = paling direkomendasikan
          dari perspektif manajemen risiko
        """)
 
    with tab6:
        st.markdown("### 🎲 Monte Carlo Simulation")
        st.info("""
        **Definisi:** Simulasi 1000 skenario dengan probabilitas state
        yang divariasikan secara acak menggunakan distribusi Dirichlet.
        """)
        st.code("""
Setiap iterasi (1000x):
  [P(S1), P(S2), P(S3)] ~ Dirichlet([3, 4, 3])
  → acak tapi tetap proporsional dengan probabilitas asli
 
  EV_sim(i) = P_sim(S1)×Payoff_S1
            + P_sim(S2)×Payoff_S2
            + P_sim(S3)×Payoff_S3
 
  Winner = kandidat dengan EV_sim tertinggi
 
Win Rate(i) = Jumlah_Menang(i) / 1000 × 100%
        """, language="text")
        st.warning("""
        **Asumsi:**
        - Dirichlet([3,4,3]) menjaga proporsi asli (0.3, 0.4, 0.3)
          namun dengan variasi alami antar simulasi
        - Win rate tinggi = kandidat unggul di berbagai kondisi
        - Kandidat yang konsisten menang = kandidat paling robust
        """)
 
    st.markdown("---")
    st.caption(
        "Sistem Pendukung Keputusan Seleksi Karyawan  |  "
        "Agnes Monica Simorangkir  |  NIM: 4233260018"
    )
 
# ============================================================
# HALAMAN LAIN
# ============================================================
 
elif menu == "📂 Upload Dataset":
    show_upload()
 
elif menu == "🔧 Preprocessing":
    show_preprocessing()
 
elif menu == "⚙️ Payoff Matrix":
    show_payoff_workflow()
 
elif menu == "💎 EV & EOL":
    show_ev_eol()
 
elif menu == "📈 Uncertainty Analysis":
    show_uncertainty()
 
elif menu == "⚖️ Utility Analysis":
    show_utility_workflow()
 
elif menu == "🎲 Monte Carlo Simulation":
    show_montecarlo_workflow()
 
elif menu == "🏆 Final Recommendation":
    show_final_recommendation()
 
