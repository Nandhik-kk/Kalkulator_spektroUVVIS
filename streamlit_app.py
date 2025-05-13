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
    
    # Load semua animasi terlebih dahulu
    lottie_kadar = load_lottieurl("https://lottie.host/765b6ca4-5e8a-4baf-b1f8-703bc83b6e12/eKBFeaUGKE.json")
    lottie_rpd = load_lottieurl("https://lottie.host/3404aaaa-4440-49d3-8015-a91ad8a5d529/hgcgSw6HUz.json")
    lottie_rec = load_lottieurl("https://lottie.host/c23cbd35-6d04-490e-8a28-162d08f97c2e/dgvwoV7Ytb.json")

    with col1:
        if lottie_kadar:
            st_lottie(lottie_kadar, height=140, key="kadar")
        st.markdown("📏 **Perhitungan C Terukur & Kadar**")
        st.write("Menghitung kadar senyawa berdasarkan nilai absorbansi")

    with col2:
        if lottie_rpd:
            st_lottie(lottie_rpd, height=140, key="rpd")
        st.markdown("🔄 **Perhitungan %RPD(Relative Percent Difference)**")
        st.write("Evaluasi kehandalan pengukuran duplikat")

    with col3:
        if lottie_rec:
            st_lottie(lottie_rec, height=140, key="rec")
        st.markdown("🎯 **Perhitungan %Recovery**")
        st.write("Mengukur akurasi metode melalui nilai %REC")
    
    st.markdown("---")
    st.markdown("© 2025 🧪 Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis | Kelompok 4 1F")

# Fungsi c terukur
def c_terukur():
    st.title("🔬 Perhitungan C Terukur")
    
    # Animasi Lottie di bawah judul
    lottie_url = "https://lottie.host/5ee6c7e7-3c7b-473f-b75c-df412fe210cc/kF9j77AAsG.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_c_terukur")


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
    st.title("📏Perhitungan Kadar")

    # Animasi lottie
    lottie_url = "https://lottie.host/765b6ca4-5e8a-4baf-b1f8-703bc83b6e12/eKBFeaUGKE.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_kadar")

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
    st.title("🔄% RPD")

    # Animasi lottie
    lottie_url = "https://lottie.host/3404aaaa-4440-49d3-8015-a91ad8a5d529/hgcgSw6HUz.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_kadar")

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
            st.info("✅Nilai %RPD yang kurang dari 5% menunjukkan bahwa hasil pengukuran sangat konsisten dan reprodusibel, sehingga dapat dianggap andal dan diterima secara analitis.")
        else:
            st.warning("⚠️Nilai %RPD yang melebihi 5% mengindikasikan adanya perbedaan yang cukup besar antara dua hasil pengukuran, sehingga menunjukkan kurangnya konsistensi atau kemungkinan adanya kesalahan dalam prosedur analisis.")
# Fungsi REC
def rec():
    st.title("🎯% REC")

     # Animasi lottie
    lottie_url = "https://lottie.host/c23cbd35-6d04-490e-8a28-162d08f97c2e/dgvwoV7Ytb.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_kadar")

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
            st.info("✅Nilai %Recovery yang berada dalam rentang 80–120% menunjukkan bahwa metode analisis memiliki akurasi yang baik, di mana jumlah analit yang terukur mendekati jumlah yang sebenarnya. Ini menandakan bahwa tidak ada kehilangan signifikan atau interferensi yang berarti selama proses analisis.")
        else:
            st.warning("⚠️Nilai %Recovery yang berada di luar rentang 80–120% mengindikasikan adanya ketidaksesuaian antara jumlah analit yang seharusnya dan yang terukur, sehingga menandakan akurasi yang buruk. Hal ini dapat disebabkan oleh kehilangan analit selama proses ekstraksi, kontaminasi, atau gangguan matriks lainnya.")


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
