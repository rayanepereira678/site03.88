import streamlit as st
import os

# CONFIG
st.set_page_config(page_title="Perfil Netflix Style", layout="wide")

# =========================
# FUNDO ESCURO
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
<div style="text-align:center; margin-bottom:25px;">
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
    box-shadow:0px 0px 20px rgba(0,0,0,0.7);
">
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

# FOTO PERFIL
with col1:
    if os.path.exists("foto 88.png"):
        st.image("foto 88.png", width=260)
    else:
        st.warning("Foto não encontrada")

# TEXTO PERFIL
with col2:
    st.markdown("""
    <h1 style="color:white;">Rayane</h1>

    <p style="color:#ccc; font-size:18px; line-height:1.8;">
    Rayane é estudante do Ensino Médio no IFPB Campus Itabaiana,
    dedicada aos estudos e interessada em tecnologia.
    Ama aprender coisas novas e desenvolver projetos criativos.
    </p>
    """, unsafe_allow_html=True)

    st.link_button("🎬 Visitar Netflix", "https://www.netflix.com/br/")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# WHATSAPP FINAL
# =========================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">
    <p style="color:white; font-size:18px;">Fale comigo no WhatsApp</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">
    <a href="https://wa.me/5581997471583" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg"
             width="80">
    </a>
</div>
""", unsafe_allow_html=True)
