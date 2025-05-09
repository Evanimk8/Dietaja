import streamlit as st

# Inisialisasi session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'goal' not in st.session_state:
    st.session_state.goal = ''
if 'bmi' not in st.session_state:
    st.session_state.bmi = 0.0
if 'status' not in st.session_state:
    st.session_state.status = ''
if 'age' not in st.session_state:
    st.session_state.age = 0

# Konfigurasi halaman
st.set_page_config(page_title="Diet Sehat", page_icon="🍉", layout="centered")

# CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #fefefe;
            background-image: radial-gradient(#ffd6d6 2px, transparent 2px),
                              radial-gradient(#d6ffe7 2px, transparent 2px),
                              radial-gradient(#d6e0ff 2px, transparent 2px);
            background-size: 40px 40px;
            background-position: 0 0, 20px 20px, 10px 10px;
            background-attachment: fixed;
        }
        .title {
            text-align: center;
            color: #444;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .fade-in-text {
            opacity: 0;
            animation: fadeIn 3s forwards;
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .left-button {
            display: flex;
            justify-content: flex-start;
            margin: 20px 0;
        }
        .right-button {
            display: flex;
            justify-content: flex-end;
            margin: 20px 0;
        }
        .stButton > button {
            font-size: 20px;
            padding: 0.75em 2em;
            border-radius: 12px;
            background-color: #ff90b3;
            color: white;
            border: none;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Halaman 1
def home_page():
    st.markdown("<div class='title fade-in-text'>🍓 Jagalah Tubuh Anda dengan Diet Sehat!!</div>", unsafe_allow_html=True)
    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍊 Lanjut"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 2
def goal_page():
    st.markdown("<div class='title fade-in-text'>🍍 Apa tujuan diet kamu?</div>", unsafe_allow_html=True)
    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍌 Turun Berat Badan"):
        st.session_state.goal = "Turun Berat Badan"
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍇 Naik Berat Badan"):
        st.session_state.goal = "Naik Berat Badan"
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "home"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 3
def bmi_page():
    st.markdown("<div class='title fade-in-text'>🍉 Masukkan Berat, Tinggi Badan & Usia</div>", unsafe_allow_html=True)
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
    st.session_state.age = usia
    berat = st.number_input("Berat badan (kg)", value=70.0)
    tinggi = st.number_input("Tinggi badan (cm)", value=170.0)
    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍏 Lihat Hasil"):
        tinggi_m = tinggi / 100
        bmi = round(berat / (tinggi_m ** 2), 2)
        st.session_state.bmi = bmi
        if bmi < 18.5:
            st.session_state.status = "Kurus"
        elif 18.5 <= bmi < 25:
            st.session_state.status = "Normal"
        elif 25 <= bmi < 30:
            st.session_state.status = "Gemuk"
        else:
            st.session_state.status = "Obesitas"
        st.session_state.page = "rekomendasi"
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 4
def rekomendasi_page():
    st.markdown("<div class='title fade-in-text'>📊 Hasil BMI Kamu</div>", unsafe_allow_html=True)
    bmi = st.session_state.bmi
    status = st.session_state.status
    st.subheader(f"📏 BMI Anda: **{bmi}**")
    st.subheader(f"🩺 Status: **{status}**")

    st.success("💪 Tetap semangat! Dengan pola makan sehat dan gaya hidup aktif, kamu bisa capai tujuanmu!")

    st.markdown("<div class='right-button'>", unsafe_allow_html=True)
    if st.button("🍽️ Lihat Rekomendasi Makanan"):
        st.session_state.page = "makanan"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 5
def makanan_page():
    goal = st.session_state.goal
    st.markdown("<div class='title fade-in-text'>🍽️ Rekomendasi Makanan Sehat</div>", unsafe_allow_html=True)

    if goal == "Turun Berat Badan":
        st.subheader("Untuk Menurunkan Berat Badan:")
        st.markdown("""
        **🍱 Makanan Utama:**
        - 🥗 Gado-gado tanpa kerupuk (200 gr) – *Kalori: ~300 kcal*
        - 🍲 Sup sayur bening (1 mangkok) – *Kalori: ~100 kcal*
        - 🐟 Ikan panggang (100 gr) – *Kalori: ~120 kcal*
        - 🍚 Nasi merah (100 gr) – *Kalori: ~110 kcal*
        - 🍳 Telur rebus (1 butir) – *Kalori: ~70 kcal*
        - 🍗 Dada ayam tanpa kulit (100 gr) – *Kalori: ~165 kcal*

        **🥒 Camilan Sehat:**
        - 🍎 Apel (1 buah) – *Kalori: ~95 kcal*
        - 🍌 Pisang sedang – *Kalori: ~105 kcal*
        - 🥒 Mentimun potong – *Kalori: ~15 kcal*
        - 🍿 Popcorn tanpa mentega (1 cup) – *Kalori: ~30 kcal*

        **🥤 Minuman:**
        - 💧 Air putih – *0 kcal*
        - 🍵 Teh hijau tanpa gula – *Kalori: ~2 kcal*
        - 🍶 Infused water (lemon, timun) – *Kalori: ~5 kcal*
        """)
    else:
        st.subheader("Untuk Menaikkan Berat Badan:")
        st.markdown("""
        **🍱 Makanan Utama:**
        - 🍛 Nasi putih + ayam goreng + tempe (1 porsi) – *Kalori: ~700 kcal*
        - 🍲 Sup krim ayam (1 mangkok) – *Kalori: ~200 kcal*
        - 🧆 Perkedel kentang (1 buah) – *Kalori: ~150 kcal*
        - 🍞 Roti gandum + selai kacang (2 lembar) – *Kalori: ~300 kcal*
        - 🍝 Mie rebus + telur (1 porsi) – *Kalori: ~450 kcal*

        **🥜 Camilan Tinggi Kalori:**
        - 🥜 Kacang tanah sangrai (1 genggam) – *Kalori: ~160 kcal*
        - 🍌 Pisang goreng (1 buah) – *Kalori: ~180 kcal*
        - 🍯 Roti tawar + madu (1 lembar) – *Kalori: ~130 kcal*
        - 🧀 Keju slice (1 lembar) – *Kalori: ~80 kcal*

        **🥤 Minuman:**
        - 🥛 Susu full cream (1 gelas) – *Kalori: ~150 kcal*
        - 🥤 Jus alpukat + susu kental (1 gelas) – *Kalori: ~250–300 kcal*
        - 🍶 Smoothie pisang + susu + selai kacang – *Kalori: ~350 kcal*
        """)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "rekomendasi"
    st.markdown("</div>", unsafe_allow_html=True)

# Routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "goal":
    goal_page()
elif st.session_state.page == "bmi":
    bmi_page()
elif st.session_state.page == "rekomendasi":
    rekomendasi_page()
elif st.session_state.page == "makanan":
    makanan_page()



