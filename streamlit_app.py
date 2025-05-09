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

# Halaman 1: Home
def home_page():
    st.markdown("<div class='title fade-in-text'>🍓 Jagalah Tubuh Anda dengan Diet Sehat!!</div>", unsafe_allow_html=True)
    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍊 Lanjut"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 2: Pilih Tujuan
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

# Halaman 3: Input BMI
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

# Halaman 4: Hasil BMI
def rekomendasi_page():
    st.markdown("<div class='title fade-in-text'>📊 Hasil BMI Kamu</div>", unsafe_allow_html=True)
    bmi = st.session_state.bmi
    status = st.session_state.status
    st.subheader(f"📏 BMI Anda: **{bmi}**")
    st.subheader(f"🩺 Status: **{status}**")
    st.success("💪 Tetap semangat! Dengan pola makan sehat dan gaya hidup aktif, kamu bisa capai tujuanmu!")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Kembali"):
            st.session_state.page = "bmi"
    with col2:
        if st.button("🍽️ Lihat Rekomendasi Makanan"):
            st.session_state.page = "makanan"

# Halaman 5: Rekomendasi Makanan
def makanan_page():
    st.markdown("<div class='title fade-in-text'>🍱 Rekomendasi Makanan Sehat</div>", unsafe_allow_html=True)

    if st.session_state.goal == "Turun Berat Badan":
        st.subheader("🍋 Makanan Disarankan (Rendah Kalori):")
        st.markdown("""
        - 🥗 **Gado-gado**: Sayur + bumbu kacang (200 kalori per mangkuk)
        - 🐟 **Ikan kukus/bakar**: 100-150g (180 kalori)
        - 🍚 **Nasi merah + sayur bening**: (250 kalori)
        - 🍌 **Buah segar (pisang/pepaya/apel)**: (80-100 kalori per buah)
        - 🍲 **Sup bening sayur + tahu**: (150 kalori)
        - 🥚 **Telur rebus**: 1 butir (78 kalori)
        - 🍠 **Ubi rebus**: 1 buah sedang (120 kalori)
        - 🥬 **Tumis kangkung tanpa minyak berlebih**: (100 kalori)
        """)
    else:
        st.subheader("🍎 Makanan Disarankan (Tinggi Kalori Sehat):")
        st.markdown("""
        - 🍛 **Nasi putih + tempe goreng**: (400 kalori)
        - 🥜 **Pecel (sayur + bumbu kacang)**: (350 kalori)
        - 🍶 **Jus alpukat tanpa gula**: (200 kalori)
        - 🍞 **Roti gandum + selai kacang**: (300 kalori)
        - 🍗 **Ayam panggang + kentang rebus**: (450 kalori)
        - 🧀 **Omelet telur + keju**: (350 kalori)
        - 🥣 **Bubur kacang hijau santan**: (250 kalori)
        - 🥛 **Susu full cream**: 1 gelas (150 kalori)
        """)

    if st.button("← Kembali"):
        st.session_state.page = "rekomendasi"

# Routing halaman
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
