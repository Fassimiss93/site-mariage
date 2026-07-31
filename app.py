import sys, os, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import streamlit.components.v1 as components
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

# ── ENVELOPPE D'INTRODUCTION ─────────────────────────────────────────────────
# Purement en CSS (animation qui se joue toute seule + clic pour passer) afin que ça
# fonctionne toujours, même si un bloqueur de pub empêche le composant JS ci-dessous.
st.markdown("""
<input type="checkbox" id="env-toggle" class="env-checkbox">
<label for="env-toggle" class="env-overlay" id="env-overlay">
    <div class="envelope">
        <div class="env-back"></div>
        <div class="env-letter"><span class="env-letter-ornament">&#10022;</span></div>
        <div class="env-flap"></div>
        <div class="env-seal">
            <svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
                <text x="22" y="43" font-family="'Playfair Display', serif" font-style="italic"
                      font-weight="600" font-size="34" fill="#fdf6e8" text-anchor="middle">A</text>
                <text x="22" y="43" font-family="'Playfair Display', serif" font-style="italic"
                      font-weight="600" font-size="34" fill="#fdf6e8" text-anchor="middle"
                      opacity="0.5" transform="translate(64,0) scale(-1,1)">A</text>
            </svg>
        </div>
    </div>
</label>
""", unsafe_allow_html=True)

# Amélioration facultative : mémorise que l'enveloppe a déjà été vue pour ne pas la
# rejouer en revenant sur l'accueil. Best-effort — si bloqué, l'enveloppe fonctionne
# quand même (animation CSS garantie) mais se rejoue à chaque retour.
components.html("""
<script>
try {
    var doc = window.parent.document;
    var chk = doc.getElementById('env-toggle');
    var overlay = doc.getElementById('env-overlay');
    if (chk && overlay && !overlay.dataset.envInit) {
        overlay.dataset.envInit = '1';
        var storage = window.parent.sessionStorage;
        if (storage.getItem('envelope_opened') === '1') {
            overlay.classList.add('env-instant');
            chk.checked = true;
        } else {
            setTimeout(function () { storage.setItem('envelope_opened', '1'); }, 3300);
            chk.addEventListener('change', function () {
                if (chk.checked) { storage.setItem('envelope_opened', '1'); }
            });
        }
    }
} catch (e) {}
</script>
""", height=0, width=0)

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
    <h2 class="section-title">Woezon !</h2>
    <div class="section-orn">✦</div>
    <p class="section-text">
        Chez nous, un mariage ne célèbre pas seulement l'union de deux personnes,<br>
        mais celle de deux familles, de deux histoires et de tous ceux qui les entourent.<br><br>
        Nous sommes profondément heureux de vous convier à ce moment de bonheur<br>
        et de célébration de notre amour.<br><br>
        Votre présence à nos côtés fera de ce jour spécial, un souvenir inoubliable.
    </p>
</div>
""", unsafe_allow_html=True)

# ── NAVIGATION ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:860px; margin: 0 auto; padding: 0 24px 60px;">
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(150px,1fr)); gap:16px;">
""", unsafe_allow_html=True)

col_prog, col_infos, col_rsvp = st.columns([1, 1.4, 1])

with col_prog:
    st.markdown("""
    <a href="Programme" target="_self" class="nav-card-link">
    <div class="nav-card" style="background:white;border-radius:12px;padding:26px 12px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #d5872d;">
        <div class="cal-icon"><div class="cal-icon-top"></div><div class="cal-icon-day">29</div></div>
        <span style="font-family:'Poppins',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#5c5738;">Programme</span>
        <div class="nav-cta">→ Voir le programme</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col_infos:
    st.markdown("""
    <a href="Infos_pratiques" target="_self" class="nav-card-link">
    <div class="nav-card" style="background:white;border-radius:12px;padding:22px 16px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #7b7551;">
        <span style="font-size:2rem;display:block;margin-bottom:6px;">ℹ️</span>
        <span style="font-family:'Poppins',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#5c5738;">Infos pratiques</span>
        <div style="margin-top:12px;font-family:'Poppins',sans-serif;font-size:0.8rem;
                    color:#3d3527;line-height:2;">
            👗 Dress Code<br>
            📍 Comment nous rejoindre<br>
            ❓ FAQ
        </div>
        <div class="nav-cta">→ Voir les infos pratiques</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

with col_rsvp:
    st.markdown("""
    <a href="RSVP" target="_self" class="nav-card-link">
    <div class="nav-card" style="background:white;border-radius:12px;padding:26px 12px;
         text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);
         border-top:3px solid #d5872d;">
        <span style="font-size:2rem;display:block;margin-bottom:10px;">💌</span>
        <span style="font-family:'Poppins',sans-serif;font-size:0.82rem;font-weight:600;
              letter-spacing:0.1em;text-transform:uppercase;color:#5c5738;">RSVP</span>
        <div class="nav-cta">→ Confirmer ma présence</div>
    </div>
    </a>
    """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="site-footer">
    Adakou &amp; Ata-Sé &nbsp;·&nbsp; {WEDDING_DATE_STR} &nbsp;·&nbsp; {LOCATION}<br>
    <span style="font-size:1.1rem; color:#d5872d;">💍</span>
</div>
""", unsafe_allow_html=True)
