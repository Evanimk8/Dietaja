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

# CSS untuk background dan tombol
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

        st.session_state.page = "hasil"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "goal"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 4: Hasil BMI dan semangat
def hasil_page():
    st.markdown("<div class='title fade-in-text'>🍒 Hasil BMI Kamu</div>", unsafe_allow_html=True)

    bmi = st.session_state.bmi
    status = st.session_state.status

    st.markdown(f"""
    <div style='font-size:24px; font-weight:bold; color:black; text-align:center;'>
    ✅ BMI: {bmi} — Status: {status}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:20px; font-weight:bold; color:black; text-align:center;'>
    Tetap semangat dalam menjalani pola hidup sehat! 💪💚
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='right-button'>", unsafe_allow_html=True)
    if st.button("🍽️ Lihat Rekomendasi Makanan"):
        st.session_state.page = "rekomendasi"
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman 5: Rekomendasi Makanan
def rekomendasi_page():
    st.markdown("<div class='title fade-in-text'>🍽️ Rekomendasi Makanan Sehat</div>", unsafe_allow_html=True)

    goal = st.session_state.goal

    if goal == "Turun Berat Badan":
        st.subheader("🔽 Makanan Rendah Kalori:")
        st.markdown("""
        - 🥗 Salad sayur (selada, wortel, tomat) – 100 kalori  
        - 🥚 Putih telur rebus (3 butir) – 51 kalori  
        - 🐟 Tuna kaleng tanpa minyak (85g) – 120 kalori  
        - 🍄 Tumis jamur tiram + bawang putih – 90 kalori  
        - 🍲 Sop ayam tanpa kulit + sayur – 180 kalori  
        - 🍵 Smoothie hijau (bayam, timun, apel hijau) – 110 kalori  
        - 🌽 Jagung rebus – 120 kalori  
        - 🍠 Singkong rebus – 150 kalori  
        - 🥬 Gado-gado tanpa kerupuk – 250 kalori  
        - 🍌 Buah segar seperti pisang atau pepaya – 100 kalori  
        - 🍜 **Bakso** (1 mangkuk kecil, tanpa mie) – 200 kalori  
        """)
    else:
        st.subheader("🔼 Makanan Tinggi Kalori Sehat:")
        st.markdown("""
        - 🍛 Nasi uduk + telur dadar + tempe – 550 kalori  
        - 🥑 Alpukat utuh + madu – 250 kalori  
        - 🥜 Kacang tanah sangrai (1 genggam) – 170 kalori  
        - 🧆 Perkedel kentang + telur – 300 kalori  
        - 🧈 Oatmeal + susu full cream + madu – 400 kalori  
        - 🧃 Smoothie pisang + susu + kacang almond – 350 kalori  
        - 🍗 Dada ayam panggang + minyak zaitun – 250 kalori  
        - 🍞 Pisang + roti tawar + selai kacang – 350 kalori  
        - 🥜 Pecel + nasi – 450 kalori  
        - 🧀 Roti gandum + keju + susu – 400 kalori  
        - 🍜 **Bakso** (1 mangkuk besar) – 400 kalori  
        """)

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "hasil"
    st.markdown("</div>", unsafe_allow_html=True)

# Routing halaman
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


