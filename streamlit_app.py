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

# CSS Styling dengan animasi & responsif
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
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            color: black;
            font-size: 32px;
            font-weight: bold;
            animation: fadeIn 2s ease-in-out;
        }
        .highlight {
            font-size: 24px;
            color: #ff5c8d;
            text-shadow: 0 0 10px #ff5c8d;
            animation: glow 2s infinite alternate;
            text-align: center;
        }
        .fade-in-text {
            animation: fadeIn 3s forwards;
        }
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        @keyframes glow {
            from {
                text-shadow: 0 0 5px #ff5c8d, 0 0 10px #ff5c8d;
            }
            to {
                text-shadow: 0 0 20px #ff2b75, 0 0 30px #ff2b75;
            }
        }
        .stButton > button {
            font-size: 18px;
            padding: 0.6em 1.5em;
            border-radius: 10px;
            background-color: #ff90b3;
            color: white;
            border: none;
            margin-top: 10px;
        }
        input, .stNumberInput input, .stTextInput input, textarea {
            color: black !important;
            background-color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Data kalori makanan
food_calories = {
    "Gado-gado": 250, "Ikan Kukus": 150, "Nasi Merah + Sayur Bening": 200,
    "Ubi Rebus": 90, "Sup Sayur Bening": 100, "Tumis Bayam": 80,
    "Telur Rebus": 70, "Pisang": 90, "Salad Sayuran": 120, "Nasi Goreng": 350,
    "Pecel": 350, "Bakso": 300, "Ayam Goreng": 250, "Kentang Goreng": 300,
    "Pizza": 280, "Burger": 350, "Sate Ayam": 200, "Ayam Geprek": 400,
    "Roti Gandum + Selai Kacang": 250, "Tacos": 200, "Bubur Ayam": 350,
    "Cumi Goreng Tepung": 250, "Sandwich": 350, "Susu Full Cream": 150,
    "Jus Alpukat": 300, "Cokelat Panas Manis": 180, "Smoothie Pisang + Yogurt": 250,
    "Susu Kedelai Manis": 140, "Air Kelapa + Madu": 120, "Teh Hijau": 2,
    "Air Putih": 0,
}

# Halaman 1 - Home
def home_page():
    st.markdown("<div class='title'>🍓 Jagalah Tubuh Anda dengan Diet Sehat!!</div>", unsafe_allow_html=True)

    st.markdown("### 🍽 Kalkulator Kalori Harian")
    st.subheader("Pilih makanan dan minuman yang kamu konsumsi:")
    food_choices = st.multiselect("Pilih Makanan dan Minuman", list(food_calories.keys()), key="selected_foods")
    
    if st.button("🍴 Lihat Hasil"):
        total_calories = sum([food_calories[food] for food in food_choices])
        st.markdown(f"<div class='highlight'>🔥 Total Kalori: {total_calories} kalori</div>", unsafe_allow_html=True)

    if st.button("🍊 Lanjut"):
        st.session_state.page = "goal"

# Halaman 2 - Tujuan Diet
def goal_page():
    st.markdown("<div class='title'>🍍 Apa tujuan diet kamu?</div>", unsafe_allow_html=True)
    if st.button("🍌 Turun Berat Badan"):
        st.session_state.goal = "Turun Berat Badan"
        st.session_state.page = "bmi"
    if st.button("🍇 Naik Berat Badan"):
        st.session_state.goal = "Naik Berat Badan"
        st.session_state.page = "bmi"
    if st.button("← Kembali"):
        st.session_state.page = "home"

# Halaman 3 - BMI
def bmi_page():
    st.markdown("<div class='title'>🍉 Masukkan Berat, Tinggi Badan & Usia</div>", unsafe_allow_html=True)
    usia = st.number_input("🧒 Usia (tahun)", min_value=1, max_value=120, value=25)
    berat = st.number_input("⚖ Berat badan (kg)", value=70.0)
    tinggi = st.number_input("📏 Tinggi badan (cm)", value=170.0)
    st.session_state.age = usia

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
        st.session_state.page = "hasil"
    if st.button("← Kembali"):
        st.session_state.page = "goal"

# Halaman 4 - Hasil BMI
def hasil_bmi_page():
    st.markdown("<div class='title'>📊 Hasil BMI Kamu</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='highlight'>BMI: {st.session_state.bmi} ({st.session_state.status})</div>", unsafe_allow_html=True)
    st.info("💡 Tetap semangat! Setiap langkah kecil berarti untuk kesehatanmu 💪")

    if st.button("🍽 Rekomendasi Makanan"):
        st.session_state.page = "rekomendasi"
    if st.button("🏃‍♂️ Rekomendasi Olahraga"):
        st.session_state.page = "olahraga"
    if st.button("← Kembali"):
        st.session_state.page = "bmi"

# Halaman 5 - Rekomendasi Makanan
def rekomendasi_page():
    goal = st.session_state.goal
    st.markdown("<div class='title'>🍱 Rekomendasi Makanan & Minuman</div>", unsafe_allow_html=True)

    if goal == "Turun Berat Badan":
        st.subheader("🍋 Makanan:")
        st.markdown("""
        - 🥗 Gado-gado – 250 kal
        - 🐟 Ikan kukus – 150 kal
        - 🍚 Nasi merah – 200 kal
        - 🍠 Ubi rebus – 90 kal
        - 🥬 Tumis bayam – 80 kal
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 💧 Air putih – 0 kal
        - 🍵 Teh hijau – 2 kal
        - 🥥 Air kelapa – 45 kal
        """)
    else:
        st.subheader("🍎 Makanan:")
        st.markdown("""
        - 🍛 Nasi + tempe – 400-500 kal
        - 🥪 Roti selai kacang – 250 kal
        - 🍜 Bakso – 300 kal
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 🥛 Susu full cream – 150 kal
        - 🧋 Jus alpukat – 300 kal
        - 🍫 Cokelat panas – 180 kal
        """)

    if st.button("← Kembali"):
        st.session_state.page = "hasil"

# Halaman 6 - Rekomendasi Olahraga
def rekomendasi_olahraga_page():
    st.markdown("<div class='title'>🏋️‍♀️ Rekomendasi Olahraga</div>", unsafe_allow_html=True)
    if st.session_state.goal == "Turun Berat Badan":
        st.markdown("""
        - 🏃‍♂️ Jogging 30–45 menit
        - 🚴‍♀️ Bersepeda ringan
        - 🧘 Yoga / pilates
        """)
    else:
        st.markdown("""
        - 🏋️‍♂️ Latihan angkat beban
        - 🤸 Push-up & sit-up
        - 🏃 Jogging ringan
        """)

    if st.button("← Kembali"):
        st.session_state.page = "hasil"

# Routing Halaman
pages = {
    "home": home_page,
    "goal": goal_page,
    "bmi": bmi_page,
    "hasil": hasil_bmi_page,
    "rekomendasi": rekomendasi_page,
    "olahraga": rekomendasi_olahraga_page,
}

pages[st.session_state.page]()
