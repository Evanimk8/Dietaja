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

# CSS Styling
st.markdown("""
    <style>
        * {
            color: black !important;
        }
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
        .right-button {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
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
            color: white !important;
            border: none;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
            margin-top: 10px;
        }
        input, .stNumberInput input, .stTextInput input, textarea {
            background-color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Halaman 1 - Home
def home_page():
    st.markdown("<div class='title fade-in-text'>🍓 Jagalah Tubuh Anda dengan Diet Sehat!!</div>", unsafe_allow_html=True)

    st.markdown("<div class='center-button'>", unsafe_allow_html=True)
    if st.button("🍊 Lanjut", key="Yuk Diet!_home"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

    # Kalkulator Kalori Harian
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

    st.markdown("<div class='title fade-in-text'>🍽 Kalkulator Kalori Harian</div>", unsafe_allow_html=True)
    st.subheader("Pilih makanan dan minuman yang kamu konsumsi:")

    food_choices = st.multiselect("Pilih Makanan dan Minuman", list(food_calories.keys()), key="selected_foods")

    if st.button("🍴 Lihat Hasil", key="lihat_hasil"):
        total_calories = sum([food_calories[food] for food in food_choices])
        st.markdown(f"<h3 style='color:black;'>🔥 Total Kalori: {total_calories} kalori</h3>", unsafe_allow_html=True)

# Halaman 2 - Tujuan Diet
def goal_page():
    st.markdown("<div class='title fade-in-text'>🍍 Apa tujuan diet kamu?</div>", unsafe_allow_html=True)
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
    st.markdown("<div class='title fade-in-text'>🍉 Masukkan Berat, Tinggi Badan & Usia</div>", unsafe_allow_html=True)
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
    st.markdown("<div class='title fade-in-text'>📊 Hasil BMI Kamu</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:black;'>BMI: {st.session_state.bmi} ({st.session_state.status})</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:black;'>💡 Tetap semangat! Setiap langkah kecil berarti untuk kesehatanmu 💪</h4>", unsafe_allow_html=True)

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
    st.markdown("<div class='title fade-in-text'>🍱 Rekomendasi Makanan & Minuman</div>", unsafe_allow_html=True)

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
    st.markdown("<div class='title fade-in-text'>🏋️‍♀️ Rekomendasi Olahraga</div>", unsafe_allow_html=True)
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
