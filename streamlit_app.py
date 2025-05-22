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
    
    # Load animasi
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
    
    # Animasi Lottie
    lottie_url = "https://lottie.host/5ee6c7e7-3c7b-473f-b75c-df412fe210cc/kF9j77AAsG.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_c_terukur")


    # Pilih jumlah perhitungan
    n = st.number_input("Jumlah perhitungan sampel (maks. 50)", min_value=1, max_value=50, value=1, step=1)

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
    n = st.number_input("Jumlah sampel (maks. 50)", min_value=1, max_value=50, value=1, step=1)

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
        st_lottie(lottie_json, height=250, key="anim_rpd")

    # Pilihan jenis perhitungan
    tipe = st.radio("Pilih jenis perhitungan RPD:",
                    ("A. Single RPD", "B. Multiple RPD"))

    # Keterangan edukatif
    st.info("✅Nilai %RPD yang kurang dari 5% menunjukkan bahwa hasil pengukuran sangat konsisten dan reprodusibel, sehingga dapat dianggap andal dan diterima secara analitis.")
    st.warning("⚠️Nilai %RPD yang melebihi 5% mengindikasikan adanya perbedaan yang cukup besar antara dua hasil pengukuran, sehingga menunjukkan kurangnya konsistensi atau kemungkinan adanya kesalahan dalam prosedur analisis.")

    rpd_results = []

    if tipe.startswith("A"):
        # SINGLE RPD
        c1 = st.number_input("Masukkan C1", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c1")
        c2 = st.number_input("Masukkan C2", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c2")

        if st.button("Hitung %RPD", key="btn_rpd_single"):
            num = abs(c1 - c2)
            den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1
            rpd_val = num / den * 100

            st.success(f"%RPD = {rpd_val:.7f} %")
            if rpd_val < 5:
                st.info("✅Hasil pengukuran konsisten dan dapat diterima.")
            else:
                st.warning("⚠️Hasil pengukuran tidak konsisten atau kurang andal.")

    else:
        # MULTIPLE RPD
        n = st.number_input("Jumlah perhitungan RPD (maks. 50)", min_value=1, max_value=50, value=1, step=1)
        
        for i in range(1, n + 1):
            st.markdown(f"---\n### Perhitungan RPD #{i}")
            c1 = st.number_input(f"C1 untuk RPD #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rpd_m_c1_{i}")
            c2 = st.number_input(f"C2 untuk RPD #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rpd_m_c2_{i}")

            num = abs(c1 - c2)
            den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1
            rpd_val = num / den * 100

            rpd_results.append((i, rpd_val))

        if st.button("Hitung Semua RPD", key="btn_rpd_multiple"):
            st.markdown("## Hasil Perhitungan %RPD")
            all_consistent = True

            for i, val in rpd_results:
                st.write(f"🔹 %RPD #{i} = {val:.7f} %")
                if val < 5:
                    st.info(f"✅ RPD #{i} menunjukkan hasil konsisten")
                else:
                    st.warning(f"⚠️ RPD #{i} menunjukkan hasil tidak konsisten")
                    all_consistent = False

            # Kesimpulan akhir
            st.markdown("---")
            if all_consistent:
                st.success("✅ **Kesimpulan:** Semua hasil perhitungan menunjukkan %RPD < 5%, sehingga dapat disimpulkan bahwa hasil analisis RPD konsisten dan dapat diterima.")
            else:
                st.error("❌ **Kesimpulan:** Terdapat hasil perhitungan dengan %RPD ≥ 5%, sehingga dapat disimpulkan bahwa analisis RPD tidak sepenuhnya konsisten.")

# Fungsi REC
def rec():
    st.title("🎯% REC")

    # Animasi lottie
    lottie_url = "https://lottie.host/c23cbd35-6d04-490e-8a28-162d08f97c2e/dgvwoV7Ytb.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_rec")

    # Pilihan jenis perhitungan
    tipe = st.radio("Pilih jenis perhitungan Recovery:",
                    ("A. Single REC", "B. Multiple REC"))

    # Keterangan edukatif
    st.info("✅Nilai %Recovery yang berada dalam rentang 80–120% menunjukkan bahwa metode analisis memiliki akurasi yang baik, di mana jumlah analit yang terukur mendekati jumlah yang sebenarnya. Ini menandakan bahwa tidak ada kehilangan signifikan atau interferensi yang berarti selama proses analisis.")
    st.warning("⚠️Nilai %Recovery yang berada di luar rentang 80–120% mengindikasikan adanya ketidaksesuaian antara jumlah analit yang seharusnya dan yang terukur, sehingga menandakan akurasi yang buruk.")

    rec_results = []

    if tipe.startswith("A"):
        # SINGLE REC
        c1 = st.number_input("Masukkan C1", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c1")
        c2 = st.number_input("Masukkan C2", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c2")
        c3 = st.number_input("Masukkan C3", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c3")

        if st.button("Hitung %REC", key="btn_rec_single"):
            den = c2 if c2 != 0 else 1
            rec_val = (c3 - c1) / den * 100

            st.success(f"%REC = {rec_val:.7f} %")

            if 80 <= rec_val <= 120:
                st.info("✅Hasil menunjukkan akurasi yang baik.")
            else:
                st.warning("⚠️Hasil menunjukkan akurasi yang buruk atau ada gangguan dalam analisis.")

    else:
        # MULTIPLE REC
        n = st.number_input("Jumlah perhitungan REC (maks. 50)", min_value=1, max_value=50, value=1, step=1)
        
        for i in range(1, n + 1):
            st.markdown(f"---\n### Perhitungan REC #{i}")
            c1 = st.number_input(f"C1 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c1_{i}")
            c2 = st.number_input(f"C2 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c2_{i}")
            c3 = st.number_input(f"C3 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c3_{i}")

            den = c2 if c2 != 0 else 1
            rec_val = (c3 - c1) / den * 100

            rec_results.append((i, rec_val))

        if st.button("Hitung Semua REC", key="btn_rec_multiple"):
            st.markdown("## Hasil Perhitungan %REC")
            all_accurate = True

            for i, val in rec_results:
                st.write(f"📊 %REC #{i} = {val:.7f} %")
                if 80 <= val <= 120:
                    st.info(f"✅ REC #{i} menunjukkan akurasi baik")
                else:
                    st.warning(f"⚠️ REC #{i} menunjukkan akurasi kurang baik")
                    all_accurate = False

            st.markdown("---")
            # Kesimpulan akhir
            if all_accurate:
                st.success("✅ **Kesimpulan:** Semua hasil %Recovery berada dalam rentang 80–120%, artinya metode analisis memiliki akurasi yang baik.")
            else:
                st.error("❌ **Kesimpulan:** Terdapat hasil %Recovery di luar rentang 80–120%, menunjukkan adanya ketidakakuratan dalam analisis.")


# Fungsi tentang
def about():
    st.title("📘 Tentang Aplikasi")
    
     # Animasi lottie
    lottie_url = "https://lottie.host/be2a3ab6-87e7-4cb9-b0e6-3c06148a80ae/QxYr1rJcW9.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_tentang")
        
    st.markdown("""
    Aplikasi ini dibuat untuk membantu proses perhitungan kadar senyawa berdasarkan metode Spektrofotometri UV-Vis.

    **👨‍🔬 Fitur Utama:**
    - Perhitungan konsentrasi (C terukur)
    - Perhitungan kadar senyawa
    - Evaluasi keandalan hasil (%RPD)
    - Evaluasi akurasi metode (%Recovery)

    **🛠️ Dibuat dengan:**
    - Python
    - Streamlit
    - Lottie Animations
    - NumPy & Pandas

    **📅 Tahun:** 2025  
    **👥 Pengembang:** Kelompok 4, Kelas 1F
    """)

    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=200)



# --- Sidebar & Routing ---
st.sidebar.title("Navigasi")

# Animasi Lottie
    lottie_url = "https://lottie.host/2ffc614e-2618-4900-98ad-e2e3265b3fdc/wViAtE1rnJ.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, height=250, key="anim_c_navigasi")
        
page = st.sidebar.radio("Pilih Halaman:", ["Homepage", "C Terukur", "kadar", "%RPD", "%REC","Tentang"])

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
elif page == "Tentang":
    about()
