import streamlit as st
import base64
import os

st.set_page_config(page_title="Perfil Netflix Style", layout="wide")

# FUNÇÃO BASE64
def get_base64_image(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# IMAGENS LOCAIS
foto = get_base64_image("foto 88.png")
zap = get_base64_image("whatsapp.png")

# =========================
# FUNDO ESCURO ESTILO NETFLIX
# =========================
st.markdown("""
<style>
body {
    background-color: #111 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOGO NETFLIX TOPO
# =========================
st.markdown("""
<div style="text-align:center; margin-bottom:30px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg"
         width="260">
</div>
""", unsafe_allow_html=True)

# =========================
# CARD PRINCIPAL
# =========================
st.markdown("""
<div style="
    background-color:#1c1c1c;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 0px 20px rgba(0,0,0,0.6);
">
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

# FOTO
with col1:
    if foto:
        st.image("foto 88.png", width=250)
    else:
        st.warning("Foto não encontrada")

# TEXTO
with col2:
    st.markdown("""
    <h2 style="color:white;">Rayane</h2>

    <p style="color:#ccc; font-size:18px; line-height:1.8;">
    Rayane é estudante do Ensino Médio no IFPB Campus Itabaiana,
    dedicada aos estudos e interessada em tecnologia.
    </p>
    """, unsafe_allow_html=True)

    st.link_button("🎬 Visitar Netflix", "https://www.netflix.com/br/")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# WHATSAPP FINAL
# =========================
st.markdown("<br><br>", unsafe_allow_html=True)

if zap:
    st.markdown(f"""
    <div style="text-align:center;">

        <a href="https://wa.me/5581997471583" target="_blank">

            <img src="data:image/png;base64,{zap}"
                 width="90"
                 style="transition:0.3s;">

        </a>

    </div>
    """, unsafe_allow_html=True)
else:
    st.warning("Imagem do WhatsApp não encontrada")
