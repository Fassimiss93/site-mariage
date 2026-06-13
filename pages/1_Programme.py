import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from utils.styles import CSS, WEDDING_DATE_STR, COUPLE, LOCATION, nav_bar

st.set_page_config(page_title="Programme — Adakou & Ata-Sé", page_icon="📅", layout="wide", initial_sidebar_state="collapsed")
st.markdown(CSS, unsafe_allow_html=True)
nav_bar()

st.markdown("""
<div class="hero" style="padding:50px 24px 40px;">
    <p class="hero-eyebrow">Le déroulé de notre grand jour</p>
    <h1 class="hero-names" style="font-size:clamp(2rem,6vw,4rem);">Programme</h1>
    <div class="hero-ornament">✦</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="max-width:760px;margin:0 auto;padding:40px 24px;">', unsafe_allow_html=True)

st.markdown("""
<div class="event-card">
    <p class="event-day">Samedi 29 août 2026</p>
    <h3 class="event-name">Cérémonie de mariage traditionnel</h3>
    <p class="event-detail">
        🕣 À partir de 8h30<br>
        📍 Attiegou, Lomé (Togo)<br><br>
        Suivi de la réception au même lieu.
    </p>
    <a href="https://www.google.com/maps/search/?api=1&query=6.19304,1.26689"
       target="_blank"
       style="display:inline-block;margin-top:14px;padding:8px 20px;background:#d5872d;
              color:white;border-radius:50px;font-family:Raleway,sans-serif;font-size:0.78rem;
              font-weight:600;letter-spacing:0.1em;text-decoration:none;text-transform:uppercase;">
        📍 Voir sur la carte
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── AJOUTER AU CALENDRIER ─────────────────────────────────────────────────────
st.markdown("""
<div class="section" style="padding-top:20px;">
    <h2 class="section-title">Ne l'oublie pas !</h2>
    <div class="section-orn">✦</div>
    <p class="section-text">Enregistre la date dans ton calendrier pour ne rien manquer.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Lien Google Calendar
    gcal = "https://calendar.google.com/calendar/r/eventedit?text=Mariage+Ata-S%C3%A9+%26+Adakou&dates=20260829/20260830&location=Lom%C3%A9,+Togo"
    st.markdown(f"""
    <div style="text-align:center;margin-top:10px;">
        <a href="{gcal}" target="_blank"
           style="display:inline-block;padding:14px 36px;
                  background:linear-gradient(135deg,#d5872d,#c07020);
                  color:white;border-radius:50px;text-decoration:none;
                  font-family:'Raleway',sans-serif;font-size:0.85rem;
                  font-weight:600;letter-spacing:0.15em;text-transform:uppercase;">
            📅 Ajouter à Google Calendar
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="site-footer">Adakou &amp; Ata-Sé &nbsp;·&nbsp; {WEDDING_DATE_STR} &nbsp;·&nbsp; {LOCATION}</div>
""", unsafe_allow_html=True)
