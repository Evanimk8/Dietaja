def rekomendasi_page():
    st.markdown("<div class='title fade-in-text'>🍒 Rekomendasi Makanan Sehat</div>", unsafe_allow_html=True)

    bmi = st.session_state.bmi
    status = st.session_state.status
    goal = st.session_state.goal
    age = st.session_state.age

    st.write(f"**Tujuan:** {goal}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Status:** {status}")
    st.write(f"**Usia:** {age} tahun")

    st.subheader("🍴 Makanan Disarankan:")

    col1, col2 = st.columns(2)

    if goal == "Turun Berat Badan":
        with col1:
            st.markdown("### 🥗")
            st.write("Gado-gado")
            st.markdown("### 🍚")
            st.write("Nasi Merah + Sayur Bening")
        with col2:
            st.markdown("### 🐟")
            st.write("Ikan Bakar")
            st.markdown("### 🍌")
            st.write("Buah Segar")

    else:
        with col1:
            st.markdown("### 🍛")
            st.write("Nasi + Tempe Tahu")
            st.markdown("### 🥜")
            st.write("Pecel")
        with col2:
            st.markdown("### 🍶")
            st.write("Susu Kedelai / Jus Alpukat")
            st.markdown("### 🍞")
            st.write("Roti Gandum + Selai Kacang")

    st.markdown("<div class='left-button'>", unsafe_allow_html=True)
    if st.button("← Kembali"):
        st.session_state.page = "bmi"
    st.markdown("</div>", unsafe_allow_html=True)

