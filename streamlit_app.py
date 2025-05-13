from streamlit_lottie import st_lottie
import requests
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# fungsi lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Pengaturan halaman
st.set_page_config(
    page_title="Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Fungsi untuk setiap halaman
def homepage():
    st.markdown("""
    <style>
        .main {
            background-color: #eeeeee;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            color: #4a4a4a;
        }
        .stButton button {
            background-color: #5a5a5a;
            color: white;
        }
        .info-box {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #999999;
            margin-bottom: 20px;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.title("🧪 Aplikasi Perhitungan Kadar Metode Spektrofotometri UV-Vis")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gambar dan penjelasan dalam layout kolom
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(
            "https://lsi.fleischhacker-asia.biz/wp-content/uploads/2022/05/Spektrofotometer-UV-VIS-Fungsi-Prinsip-Kerja-dan-Cara-Kerjanya.jpg", 
            caption="🖼️ Alat Spektrofotometer (sumber: PT. Laboratorium Solusi Indonesia)", 
            use_container_width=True
        )
        st.info("🔍 Gambar di atas adalah alat spektrofotometer yang digunakan untuk analisis UV-Vis.")
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.subheader("📖 Tentang Spektrofotometri UV-Vis")
        st.write("""
        Spektrofotometri UV-Vis adalah teknik analisis 💡 untuk mengukur seberapa banyak cahaya ☀️
        diserap oleh suatu senyawa pada panjang gelombang ultraviolet dan tampak.

        **🔧 Komponen utama:**
        - 💡 Sumber cahaya (deuterium untuk UV, tungsten untuk Vis)
        - 🎯 Monokromator (memilih panjang gelombang)
        - 🧫 Kuvet (tempat sampel)
        - 🎛️ Detektor (mengubah sinyal cahaya menjadi data)

        Teknik ini banyak digunakan untuk analisis kuantitatif dan kualitatif bahan kimia, air, obat, dan lainnya 🧪.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.subheader("⚙️ Fitur Aplikasi")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("📏 **Perhitungan Kadar**")
        st.write("Menghitung kadar senyawa berdasarkan nilai absorbansi")

    with col2:
        st.markdown("🔄 **Perhitungan %RPD**")
        st.write("Evaluasi kehandalan pengukuran duplikat")

    with col3:
        st.markdown("🎯 **Perhitungan %Recovery**")
        st.write("Mengukur akurasi metode melalui nilai %REC")
    
    st.markdown("---")
    st.markdown("© 2025 🧪 Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis | Kelompok 4 1F")

# Fungsi c terukur
def c_terukur():
    st.title("🔬 Perhitungan C Terukur")

    # Load animasi dari URL
    lottie_url = "https://lottie.host/e79a2339-95d9-4ef3-a88c-b1f366cee77e/KZcPl75CcB.lottie"
    lottie_json = load_lottieurl(lottie_url)

    # Tampilkan animasi (di bawah judul)
    if lottie_json:
        st_lottie(lottie_json, height=300, key="c_terukur_anim")

    # Pilih jumlah perhitungan
    n = st.slider("Jumlah perhitungan sampel", min_value=1, max_value=3, value=1, help="Pilih 1–3 sampel sekaligus")

    # Tempat menyimpan hasil
    results = []

    for i in range(1, n+1):
        st.markdown(f"### Sampel #{i}")
        nama = st.text_input(f"Nama Sampel #{i}", value=f"Sample {i}", key=f"nama_{i}")
        absorban = st.number_input(f"Absorbansi (A) Sampel #{i}", format="%.4f",
                                   min_value=0.0, step=0.0001, key=f"a_{i}")
        intercept = st.number_input(f"Intercept (b) Sampel #{i}", format="%.4f",
                                    min_value=0.0, step=0.0001, key=f"b_{i}")
        slope = st.number_input(f"Slope (m) Sampel #{i}", format="%.4f",
                                min_value=0.0001, step=0.0001, key=f"m_{i}")

        # Hitung segera, tapi tampilin nanti
        c_ukur = (absorban - intercept) / slope
        # Simpan nama + hasil rounded 4 desimal
        results.append((nama, round(c_ukur, 4)))

        st.markdown("---")

    # Tampilkan semua hasil
    if st.button("Hitung Semua C Terukur"):
        for nama, nilai in results:
            st.success(f"Konsentrasi/C terukur pada '{nama}' = {nilai:.4f} mg/L (ppm)")
# Fungsi Kadar
def kadar():
    st.title("Perhitungan Kadar")

    # Pilih tipe perhitungan
    tipe = st.radio("Pilih jenis perhitungan:",
                    ("A. Tanpa Bobot Sample (ppm/mg·L⁻¹)",
                     "B. Dengan Bobot Sample (mg·kg⁻¹)"))

    # Jumlah sampel (1–3)
    n = st.slider("Jumlah sampel", 1, 3, 1)

    results = []

    for i in range(1, n+1):
        st.markdown(f"---\n### Sampel #{i}")
        nama = st.text_input(f"Nama Sampel #{i}", f"Sample {i}", key=f"k_nama_{i}")

        if tipe.startswith("A"):
            # A: tanpa bobot sample
            c_ukur = st.number_input(
                f"C terukur (mg/L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_c_{i}"
            )
            blanko = st.number_input(
                f"C terukur blanko (mg/L)(koreksi) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_b_{i}"
            )
            faktor = st.number_input(
                f"Faktor Pengenceran #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kA_f_{i}"
            )

            nilai = (c_ukur - blanko) * faktor
            satuan = "mg/L (ppm)"

        else:
            # B: dengan bobot sample
            c_ukur = st.number_input(
                f"C terukur (mg/L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_c_{i}"
            )
            vol = st.number_input(
                f"Volume labu takar awal (L) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_v_{i}"
            )
            bobot = st.number_input(
                f"Bobot sample (kg) #{i}",
                min_value=0.0, value=0.0, step=0.0000001,
                format="%.7f",
                key=f"kB_w_{i}"
            )

            nilai = (c_ukur * vol) / bobot if bobot != 0 else 0.0
            satuan = "mg/kg"

        # simpan tanpa membulatkan—kita bulatkan saat tampil
        results.append((nama, nilai, satuan))

    # tombol hitung
    if st.button("Hitung Kadar"):
        st.markdown("## Hasil Perhitungan")
        for nama, nilai, satuan in results:
            st.success(f"Kadar pada '{nama}' = {nilai:.7f} {satuan}")
            
# Fungsi RPD
def rpd():
    st.title("% RPD")

    # Keterangan sebelum input
    st.markdown(
        "C1 dan C2 setiap perhitungan suatu kadar berbeda-beda, "
        "tergantung metode yang digunakan saat preparasi."
    )

    # Input C1 & C2
    c1 = st.number_input(
        "Masukkan C1", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c1"
    )
    c2 = st.number_input(
        "Masukkan C2", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c2"
    )

    # Hitung
    if st.button("Hitung %RPD"):
        # Numerator = |C1 - C2|
        num = abs(c1 - c2)
        # Denominator = rata-rata (C1 + C2)/2
        den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1  # hindari div/0
        rpd_val = num / den * 100

        # Tampilkan hasil dengan 7 desimal
        st.success(f"%RPD = {rpd_val:.7f} %")

        # Keterangan batas 5%
        if rpd_val < 5:
            st.info("Hasil oke")
        else:
            st.warning("Hasil tidak oke")
# Fungsi REC
def rec():
    st.title("% REC")

    # Keterangan sebelum input
    st.markdown(
        "C1, C2, dan C3 setiap perhitungan suatu kadar berbeda-beda, "
        "tergantung metode yang digunakan saat preparasi!"
    )

    # Input C1, C2 & C3
    c1 = st.number_input(
        "Masukkan C1", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c1"
    )
    c2 = st.number_input(
        "Masukkan C2", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c2"
    )
    c3 = st.number_input(
        "Masukkan C3", 
        min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c3"
    )

    # Hitung
    if st.button("Hitung %REC"):
        # Rumus: (C3 - C1) / C2 * 100
        den = c2 if c2 != 0 else 1
        rec_val = (c3 - c1) / den * 100

        # Tampilkan hasil dengan 7 desimal
        st.success(f"%REC = {rec_val:.7f} %")

        # Keterangan rentang 80–120%
        if 80 <= rec_val <= 120:
            st.info("Hasil oke")
        else:
            st.warning("Hasil tidak oke")


# --- Fungsi placeholder ---
def blank_page(title):
    st.title(title)
    st.write("Sedang dikembangkan…")

# --- Sidebar & Routing ---
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Homepage", "C Terukur", "kadar", "%RPD", "%REC"])

if page == "Homepage":
    homepage()
elif page == "C Terukur":
    c_terukur()
elif page == "kadar":
    kadar()
elif page == "%RPD":
    rpd()
elif page == "%REC":
    rec()
