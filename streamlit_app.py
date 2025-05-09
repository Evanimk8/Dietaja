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
        body, .stApp, .title, .fade-in-text, .stMarkdown, label, .stNumberInput label, .stTextInput label {
            color: black !important;
            font-weight: bold;
        }

        input {
            color: black !important;
        }

        html, body {
            font-size: 18px !important;
        }

        @media only screen and (max-width: 600px) {
            .title {
                font-size: 28px !important;
            }
            label, .stMarkdown, .stButton > button {
                font-size: 16px !important;
            }
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

        .fade-in-text {
            opacity: 0;
            animation: fadeIn 3s forwards;
        }

        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
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
    berat = st.number_input("Berat badan (kg)", value=70.0)
    tinggi = st.number_input("Tinggi badan (cm)", value=170.0)

    st.session_state.age = usia

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

        st.session_state.page = "hasil"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 4: Hasil BMI
def hasil_page():
    st.markdown("<div class='title fade-in-text'>🍎 Hasil Perhitungan BMI</div>", unsafe_allow_html=True)
    st.write(f"**BMI Anda:** {st.session_state.bmi}")
    st.write(f"**Status Kesehatan:** {st.session_state.status}")

    st.success("Tetap semangat dan jaga pola hidup sehat! 💪")

    st.markdown("<div class='right-button'>", unsafe_allow_html=True)
    if st.button("🍽 Rekomendasi Makanan"):
        st.session_state.page = "rekomendasi"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 5: Rekomendasi Makanan & Minuman
def rekomendasi_page():
    goal = st.session_state.goal
    st.markdown("<div class='title fade-in-text'>🥗 Rekomendasi Makanan & Minuman</div>", unsafe_allow_html=True)

    if goal == "Turun Berat Badan":
        st.subheader("🍽 Makanan:")
        st.markdown("""
        - Gado-gado (1 mangkuk) - ~300 kalori  
        - Ikan bakar (150g) - ~250 kalori  
        - Nasi merah & sayur bening - ~350 kalori  
        - Buah pisang atau pepaya - ~100 kalori  
        - Sup sayur bening - ~120 kalori  
        - Oatmeal dengan buah - ~250 kalori  
        - Bakso kuah tanpa mie - ~180 kalori (3 butir)
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - Air putih  
        - Infused water (lemon, mint)  
        - Teh hijau tanpa gula  
        - Jus buah segar tanpa gula - ~90 kalori  
        - Air kelapa murni - ~50 kalori  
        """)
    else:
        st.subheader("🍽 Makanan:")
        st.markdown("""
        - Nasi putih + tempe & tahu goreng - ~450 kalori  
        - Pecel (sayur + bumbu kacang) - ~400 kalori  
        - Jus alpukat dengan susu - ~250 kalori  
        - Roti gandum + selai kacang - ~350 kalori  
        - Telur dadar + nasi + sambal - ~400 kalori  
        - Bakso dengan mie & tahu - ~450 kalori (5 butir)  
        """)
        st.subheader("🥤 Minuman:")
        st.markdown("""
        - Susu full cream  
        - Jus alpukat atau pisang  
        - Smoothies (susu + buah)  
        - Susu kedelai - ~150 kalori  
        """)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "hasil"
    st.markdown("</div>", unsafe_allow_html=True)

# Routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "goal":
    goal_page()
elif st.session_state.page == "bmi":
    bmi_page()
elif st.session_state.page == "hasil":
    hasil_page()
elif st.session_state.page == "rekomendasi":
    rekomendasi_page()
