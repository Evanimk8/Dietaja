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
            color: black;
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
            justify-content: flex-end;
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
        input, .stNumberInput input, .stTextInput input, textarea {
            color: black !important;
            background-color: white !important;
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
    if st.button("🍌 Turun Berat Badan"):
        st.session_state.goal = "Turun Berat Badan"
        st.session_state.page = "bmi"
    if st.button("🍇 Naik Berat Badan"):
        st.session_state.goal = "Naik Berat Badan"
        st.session_state.page = "bmi"
    if st.button("← Kembali"):
        st.session_state.page = "home"

# Halaman 3
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

# Halaman 4
def hasil_bmi_page():
    st.markdown("<div class='title fade-in-text'>📊 Hasil BMI Kamu</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:black;'>BMI: {st.session_state.bmi} ({st.session_state.status})</h3>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color:black;'>💡 Tetap semangat! Setiap langkah kecil berarti untuk kesehatanmu 💪</h4>", unsafe_allow_html=True)

    st.markdown("<div class='right-button'>", unsafe_allow_html=True)
    if st.button("🍽 Rekomendasi Makanan"):
        st.session_state.page = "rekomendasi"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 5
def rekomendasi_page():
    goal = st.session_state.goal
    st.markdown("<div class='title fade-in-text'>🍱 Rekomendasi Makanan & Minuman</div>", unsafe_allow_html=True)

    if goal == "Turun Berat Badan":
        st.subheader("🍋 Makanan:")
        st.markdown("""
        - 🥗 Gado-gado – *250 kalori / 1 mangkuk sedang*
        - 🐟 Ikan kukus/bakar (tanpa minyak) – *150 kalori / 100g*
        - 🍚 Nasi merah + sayur bening – *200 kalori / piring*
        - 🍠 Ubi rebus – *90 kalori / 100g* (1–2 potong)
        - 🥣 Sup sayur bening – *100 kalori / mangkuk*
        - 🥬 Tumis bayam atau kangkung – *80 kalori / 1 porsi kecil*
        - 🍳 Telur rebus – *70 kalori / butir*
        - 🍌 Pisang – *90 kalori / buah*
        - 🥒 Salad sayuran dengan dressing rendah kalori – *120 kalori / mangkuk*
        """)

        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 💧 Air putih – *0 kalori* (wajib 8 gelas/hari)
        - 🍵 Teh hijau tanpa gula – *2 kalori / cangkir*
        - 🥒 Infused water (mentimun/lemon) – *0–5 kalori*
        - 🥥 Air kelapa murni – *45 kalori / 200 ml*
        - 🍉 Jus semangka tanpa gula – *50 kalori / gelas*
        """)

    else:  # Naik Berat Badan
        st.subheader("🍎 Makanan:")
        st.markdown("""
        - 🍛 Nasi putih + tempe/tahu goreng – *400–500 kalori / porsi*
        - 🥜 Pecel (sayur + bumbu kacang) – *350 kalori / porsi*
        - 🍜 Bakso (4–5 butir sedang) – *300 kalori*
        - 🍗 Ayam goreng – *250 kalori / potong*
        - 🥪 Roti gandum + selai kacang – *250 kalori / potong*
        - 🥔 Kentang goreng/rebus – *300 kalori / 200g*
        - 🍲 Bubur ayam – *350 kalori / mangkuk*
        - 🍳 Telur dadar – *120 kalori / butir*
        - 🥖 Roti isi telur dan keju – *400 kalori / porsi*
        """)

        st.subheader("🥤 Minuman:")
        st.markdown("""
        - 🥛 Susu full cream – *150 kalori / gelas*
        - 🥑 Jus alpukat dengan susu – *250–300 kalori / gelas*
        - 🍫 Cokelat panas manis – *180 kalori / gelas*
        - 🥤 Smoothie pisang + yogurt – *250 kalori*
        - 🧋 Susu kedelai manis – *140 kalori / gelas*
        - 🥥 Air kelapa + madu – *90–120 kalori*
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



