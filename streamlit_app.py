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

# Mendapatkan tema yang aktif
is_dark_mode = st.markdown('<style>body {background-color: #1c1c1c; color: white;}</style>', unsafe_allow_html=True)

# CSS Styling (dark mode friendly)
if is_dark_mode:
    st.markdown("""
    <style>
        .stApp {
            background-color: #2b2b2b;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
            color: #fff;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput input, .stNumberInput input {
            background-color: #333;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .stApp {
            background-color: #fefefe;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
        }
        .stButton > button {
            background-color: #ff90b3;
            color: white;
        }
        .stTextInput input, .stNumberInput input {
            background-color: #fff;
        }
    </style>
    """, unsafe_allow_html=True)

# Halaman 1 - Home
def home_page():
    st.markdown("<div class='title'>🍓 Jagalah Tubuh Anda dengan Diet Sehat!!</div>", unsafe_allow_html=True)

    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍊 Lanjut", key="Yuk Diet!_home"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

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
    usia = st.number_input("🧒 Usia (tahun)", min_value=1, max_value=120, value=25, key="usia")
    berat = st.number_input("⚖ Berat badan (kg)", value=70.0, key="berat")
    tinggi = st.number_input("📏 Tinggi badan (cm)", value=170.0, key="tinggi")
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
    st.markdown(f"<h3>BMI: {st.session_state.bmi} ({st.session_state.status})</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4>💡 Tetap semangat! Setiap langkah kecil berarti untuk kesehatanmu 💪</h4>", unsafe_allow_html=True)

    st.markdown("<div class='right-button'>", unsafe_allow_html=True)
    if st.button("🍽 Rekomendasi Makanan"):
        st.session_state.page = "rekomendasi"
    if st.button("🏃‍♂️ Rekomendasi Olahraga"):
        st.session_state.page = "olahraga"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 5 - Rekomendasi Makanan
def rekomendasi_page():
    goal = st.session_state.goal
    st.markdown("<div class='title'>🍱 Rekomendasi Makanan & Minuman</div>", unsafe_allow_html=True)

    if goal == "Turun Berat Badan":
        st.subheader("🍋 Makanan:")
        st.markdown("""
        - 🥗 Gado-gado – *250 kalori / 1 mangkuk sedang*
        - 🐟 Ikan kukus/bakar (tanpa minyak) – *150 kalori / 100g*
        - 🍚 Nasi merah + sayur bening – *200 kalori / piring*
        - 🍠 Ubi rebus – *90 kalori / 100g*
        - 🥣 Sup sayur bening – *100 kalori / mangkuk*
        - 🥬 Tumis bayam – *80 kalori / porsi kecil*
        - 🍳 Telur rebus – *70 kalori / butir*
        - 🍌 Pisang – *90 kalori / buah*
        - 🥒 Salad sayuran – *120 kalori / mangkuk*
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 💧 Air putih – *0 kalori*
        - 🍵 Teh hijau tanpa gula – *2 kalori*
        - 🥒 Infused water – *0–5 kalori*
        - 🥥 Air kelapa – *45 kalori / 200ml*
        - 🍉 Jus semangka tanpa gula – *50 kalori*
        """)
    else:
        st.subheader("🍎 Makanan:")
        st.markdown("""
        - 🍛 Nasi putih + tempe/tahu – *400–500 kalori*
        - 🥜 Pecel – *350 kalori*
        - 🍜 Bakso – *300 kalori*
        - 🍗 Ayam goreng – *250 kalori*
        - 🥪 Roti gandum + selai kacang – *250 kalori*
        - 🥔 Kentang goreng – *300 kalori*
        - 🍲 Bubur ayam – *350 kalori*
        - 🍳 Telur dadar – *120 kalori*
        - 🥖 Roti isi telur & keju – *400 kalori*
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 🥛 Susu full cream – *150 kalori*
        - 🥑 Jus alpukat + susu – *250–300 kalori*
        - 🍫 Cokelat panas manis – *180 kalori*
        - 🥤 Smoothie pisang + yogurt – *250 kalori*
        - 🧋 Susu kedelai manis – *140 kalori*
        - 🥥 Air kelapa + madu – *90–120 kalori*
        """)

    if st.button("← Kembali"):
        st.session_state.page = "hasil"

# Halaman 6 - Rekomendasi Olahraga
def rekomendasi_olahraga_page():
    st.markdown("<div class='title'>🏋️‍♀️ Rekomendasi Olahraga</div>", unsafe_allow_html=True)
    if st.session_state.goal == "Turun Berat Badan":
        st.subheader("🔥 Untuk Menurunkan Berat Badan:")
        st.markdown("""
        - 🏃‍♂️ Jogging 30–45 menit (3–5x/minggu)
        - 🚴‍♀️ Bersepeda ringan
        - 🧘‍♂️ Yoga/pilates
        - 🏊‍♂️ Berenang
        - 🏋️‍♀️ Latihan kekuatan ringan
        """)
    else:
        st.subheader("💪 Untuk Menaikkan Berat Badan:")
        st.markdown("""
        - 🏋️‍♂️ Latihan angkat beban
        - 🤸‍♂️ Push-up, sit-up, dan plank
        - 🏃‍♂️ Jogging ringan (20–30 menit)
        - 🍽 Kombinasikan dengan asupan tinggi kalori sehat
        """)

    if st.button("← Kembali"):
        st.session_state.page = "hasil"

# Routing Halaman
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "goal":
    goal_page()
elif st.session_state.page == "bmi":
    bmi_page()
elif st.session_state.page == "hasil":
    hasil_bmi_page()
elif st.session_state.page == "rekomendasi":
    rekomendasi_page()
elif st.session_state.page == "olahraga":
    rekomendasi_olahraga_page()

# Watermark
st.markdown("""
    <hr style="margin-top: 50px;" />
    <div style='text-align: center; font-family: "Comic Sans MS", cursive, sans-serif; color: #cc3aad; font-size: 15px; background-color: #fff0f5; padding: 12px; border-radius: 12px; border: 2px dotted #ff90b3;'>
        🍓 dibuat oleh <u>Evani Mahesa</u>, <u>R. Devina</u>, <u>Muhazzib Raiffan</u>, <u>Aisyah</u>, dan <u>Zahra Aulia</u> ✨ – <strong>Kelompok 11</strong> 🍉
    </div>
""", unsafe_allow_html=True)
