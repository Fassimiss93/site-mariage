import sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from datetime import date, datetime, timezone, timedelta
from utils.styles import CSS, WEDDING_DATE_STR, COUPLE, LOCATION

def _img_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

_couple_img = _img_b64(os.path.join(os.path.dirname(__file__), "assets", "couple.jpg"))

st.set_page_config(
    page_title="Adakou & Ata-Sé — 29 Août 2026",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(CSS, unsafe_allow_html=True)

# ── COMPTE À REBOURS ──────────────────────────────────────────────────────────
LOME_TZ = timezone(timedelta(hours=0))  # Lomé = UTC+0, pas d'heure d'été
wedding  = date(2026, 8, 29)
now      = datetime.now(tz=LOME_TZ)
delta    = wedding - now.date()
jours   = max(0, delta.days)
heures  = 23 - now.hour
minutes = 59 - now.minute

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero" style="position:relative;overflow:hidden;">
    <img src="data:image/jpeg;base64,{_couple_img}"
         style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
                filter:blur(3px) brightness(0.45);opacity:0.6;transform:scale(1.05);"/>
    <div style="position:relative;z-index:1;">
        <p class="hero-eyebrow">Vous êtes cordialement invités au mariage traditionnel de</p>
        <h1 class="hero-names" style="line-height:1.2;">
            Adakou<br>
            <span class="hero-amp">&amp;</span><br>
            Ata-Sé
        </h1>
        <div class="hero-ornament">✦ &nbsp; ✦ &nbsp; ✦</div>
        <p class="hero-date">Le {WEDDING_DATE_STR} &nbsp;·&nbsp; {LOCATION}</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── COUNTDOWN ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="countdown-wrap">
    <div class="cd-box">
        <span class="cd-num">{jours}</span>
        <span class="cd-lbl">Jours</span>
    </div>
    <div class="cd-box">
        <span class="cd-num">{heures}</span>
        <span class="cd-lbl">Heures</span>
    </div>
    <div class="cd-box">
        <span class="cd-num">{minutes}</span>
        <span class="cd-lbl">Minutes</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── MESSAGE D'ACCUEIL ─────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <h2 class="section-title">Bienvenue</h2>
    <div class="section-orn">✦</div>
    <p class="section-text">
        C'est avec une immense joie et un cœur plein d'amour que nous vous convions<br>
        à partager avec nous l'un des plus beaux jours de notre vie.<br><br>
        Votre présence à nos côtés fera de cette célébration un souvenir inoubliable.
    </p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:860px; margin: 0 auto; padding: 0 24px 60px;">
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(150px,1fr)); gap:16px;">
""", unsafe_allow_html=True)

simple_nav = [
    ("📅", "Programme", "pages/1_Programme"),
    ("💌", "RSVP",      "pages/5_RSVP"),
]

col_prog, col_infos, col_rsvp = st.columns([1, 1.4, 1])

with col_prog:
    st.markdown("""
    <div class="nav-card" style="background:white;border-radius:12px;padding:26px 12px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #d5872d;">
        <span style="font-size:2rem;display:block;margin-bottom:10px;">📅</span>
        <span style="font-family:'Raleway',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#7b7551;">Programme</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_Programme.py", label="→ Programme", use_container_width=True)

with col_infos:
    st.markdown("""
    <div class="nav-card" style="background:white;border-radius:12px;padding:22px 16px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #7b7551;">
        <span style="font-size:2rem;display:block;margin-bottom:6px;">ℹ️</span>
        <span style="font-family:'Raleway',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#7b7551;">Infos pratiques</span>
        <div style="margin-top:12px;font-family:'Raleway',sans-serif;font-size:0.8rem;
                    color:#5a5040;line-height:2;">
            👗 Dress Code<br>
            🏨 Hébergement<br>
            📍 Comment nous rejoindre<br>
            ❓ FAQ
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/4_Infos_pratiques.py", label="→ Infos pratiques", use_container_width=True)

with col_rsvp:
    st.markdown("""
    <div class="nav-card" style="background:white;border-radius:12px;padding:26px 12px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #d5872d;">
        <span style="font-size:2rem;display:block;margin-bottom:10px;">💌</span>
        <span style="font-family:'Raleway',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#7b7551;">RSVP</span>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/5_RSVP.py", label="→ RSVP", use_container_width=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="site-footer">
    Adakou &amp; Ata-Sé &nbsp;·&nbsp; {WEDDING_DATE_STR} &nbsp;·&nbsp; {LOCATION}<br>
    <span style="font-size:1.1rem; color:#d5872d;">💍</span>
</div>
""", unsafe_allow_html=True)
