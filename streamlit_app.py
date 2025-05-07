import streamlit as st

import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Diet Sehat", page_icon="🍇", layout="centered")

# CSS untuk background gradasi dan style teks
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #5dade2, #d2b4de);
        }
        .title {
            text-align: center;
            color: black;
            font-size: 36px;
            font-weight: bold;
            margin-top: 50px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Halaman Utama
def home_page():
    # Judul Halaman Utama
    st.markdown("<div class='title'>Jagalah Tubuh Anda dengan Diet yang Sehat!</div>", unsafe_allow_html=True)

    # Tombol "Lanjut"
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    lanjut = st.button("Lanjut")
    st.markdown("</div>", unsafe_allow_html=True)

    # Aksi ketika tombol ditekan
    if lanjut:
        st.session_state.page = "next_page"  # Menentukan halaman berikutnya setelah klik Lanjut
        st.experimental_rerun()  # Untuk reload dan pindah ke halaman berikutnya

# Halaman Selanjutnya (Pilih Tujuan Diet)
def next_page():
    # Judul Halaman
    st.markdown("<div class='title'>Apa yang ingin kamu capai?</div>", unsafe_allow_html=True)

    # Menambahkan dua tombol untuk pilihan tujuan
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Turun Berat Badan"):
            st.session_state.page = "bmi_input"  # Halaman untuk input BMI
            st.session_state.goal = "Turun Berat Badan"
            st.experimental_rerun()

    with col2:
        if st.button("Naik Berat Badan"):
            st.session_state.page = "bmi_input"  # Halaman untuk input BMI
            st.session_state.goal = "Naik Berat Badan"
            st.experimental_rerun()

# Halaman untuk Input Indeks Massa Tubuh (BMI)
def bmi_input_page():
    # Judul untuk halaman BMI
    st.markdown("<div class='title'>Masukkan Berat dan Tinggi Badan</div>", unsafe_allow_html=True)

    # Input untuk berat badan dan tinggi badan
    berat = st.number_input("Berat badan (kg)", min_value=30.0, max_value=200.0, value=70.0)
    tinggi = st.number_input("Tinggi badan (cm)", min_value=100.0, max_value=250.0, value=170.0)

    if berat > 0 and tinggi > 0:
        tinggi_m = tinggi / 100
        bmi = round(berat / (tinggi_m ** 2), 2)

        st.markdown(f"### BMI Anda: **{bmi}**")

        # Interpretasi BMI
        if bmi < 18.5:
            status = "Kurus"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        elif 25 <= bmi < 30:
            status = "Gemuk"
        else:
            status = "Obesitas"

        st.success(f"Status: {status}")
        st.write(f"Tujuan Anda: {st.session_state.goal}")

# Logika untuk halaman yang ditampilkan
if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "next_page":
    next_page()
elif st.session_state.page == "bmi_input":
    bmi_input_page()
