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
st.set_page_config(page_title="Diet Sehat", page_icon="🌊", layout="centered")

# CSS untuk tema air dan animasi
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #a2d4f4, #0077be);
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
            animation: fadeIn 2s ease-in-out;
        }
        .big-button {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }
        .stButton > button {
            font-size: 20px;
            padding: 0.75em 2em;
            border-radius: 10px;
            background-color: #0099cc;
            color: white;
            border: none;
        }
        /* Animasi fadeIn */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .fade-in-text {
            opacity: 0;
            animation: fadeIn 3s forwards;
        }
    </style>
""", unsafe_allow_html=True)

# Halaman 1: Home
def home_page():
    st.markdown("<div class='title fade-in-text'>💧 Jagalah Tubuh Anda dengan Diet yang Sehat! 🌊</div>", unsafe_allow_html=True)
    st.markdown("<div class='big-button'>", unsafe_allow_html=True)
    if st.button("Lanjut"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 2: Pilih Tujuan
def goal_page():
    st.markdown("<div class='title fade-in-text'>🌴 Apa yang ingin kamu capai? 🌊</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Turun Berat Badan"):
            st.session_state.goal = "Turun Berat Badan"
            st.session_state.page = "bmi"
    with col2:
        if st.button("Naik Berat Badan"):
            st.session_state.goal = "Naik Berat Badan"
            st.session_state.page = "bmi"
    if st.button("← Kembali"):
        st.session_state.page = "home"

# Halaman 3: Input BMI + Usia
def bmi_page():
    st.markdown("<div class='title fade-in-text'>💦 Masukkan Berat, Tinggi Badan, dan Usia Anda 🐠</div>", unsafe_allow_html=True)
    usia = st.number_input("Usia (tahun)", min_value=1, max_value=120, value=25)
    st.session_state.age = usia
    berat = st.number_input("Berat badan (kg)", value=70.0)
    tinggi = st.number_input("Tinggi badan (cm)", value=170.0)

    if st.button("Lihat Hasil"):
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

    if st.button("← Kembali"):
        st.session_state.page = "goal"

# Halaman 4: Rekomendasi Makanan
def rekomendasi_page():
    st.markdown("<div class='title fade-in-text'>🍽️ Rekomendasi Makanan Sehat 🧊</div>", unsafe_allow_html=True)
    bmi = st.session_state.bmi
    status = st.session_state.status
    goal = st.session_state.goal
    age = st.session_state.age

    st.write(f"**Tujuan:** {goal}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Status:** {status}")
    st.write(f"**Usia:** {age} tahun")

    if goal == "Turun Berat Badan":
        st.subheader("🌿 Makanan untuk Turun Berat Badan:")
        st.markdown(""" 
        - 🥦 **Sayuran Hijau**: 1 porsi (sekitar 1 cangkir)
        - 🍗 **Dada Ayam**: 100-150g
        - 🥣 **Oatmeal**: 1/2 cangkir
        - 🐟 **Ikan Kukus**: 100-150g
        - 🍎 **Buah Segar**: 1 buah kecil (misalnya apel, pisang)
        """)
    else:
        st.subheader("🍞 Makanan untuk Naik Berat Badan:")
        st.markdown("""
        - 🥛 **Susu**: 1 gelas (250ml)
        - 🍚 **Nasi & Kentang**: 1-1.5 cangkir nasi/kentang
        - 🍞 **Roti Gandum**: 2 iris
        - 🥑 **Smoothie**: 1 gelas (300ml)
        """)

    if st.button("← Kembali"):
        st.session_state.page = "bmi"

# Routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "goal":
    goal_page()
elif st.session_state.page == "bmi":
    bmi_page()
elif st.session_state.page == "rekomendasi":
    rekomendasi_page()

