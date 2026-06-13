import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from utils.styles import CSS, WEDDING_DATE_STR, LOCATION, nav_bar

st.set_page_config(page_title="Infos pratiques — Adakou & Ata-Sé", page_icon="ℹ️", layout="wide", initial_sidebar_state="collapsed")
st.markdown(CSS, unsafe_allow_html=True)
nav_bar()

st.markdown("""
<div class="hero" style="padding:50px 24px 40px;">
    <p class="hero-eyebrow">Tout ce que vous devez savoir</p>
    <h1 class="hero-names" style="font-size:clamp(2rem,6vw,4rem);">Infos pratiques</h1>
    <div class="hero-ornament">✦</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="max-width:760px;margin:0 auto;padding:40px 24px;">', unsafe_allow_html=True)

# ── DRESS CODE ────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:white;border-radius:14px;padding:32px 36px;
            box-shadow:0 2px 16px rgba(0,0,0,0.07);margin-bottom:24px;
            border-top:4px solid #d5872d;">
    <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;
               font-weight:400;color:#2c2416;margin-bottom:6px;">
        👗 Dress Code
    </h3>
    <div style="width:30px;height:2px;background:#d5872d;margin-bottom:16px;"></div>
    <p style="font-family:'Raleway',sans-serif;font-weight:300;color:#5a5040;
              font-size:0.95rem;line-height:1.8;">
        <strong style="color:#2c2416;">Tenue blanche avec un tabla.</strong><br><br>
        Le tissu du tabla est disponible à la vente auprès des mariés :<br>
        <strong style="color:#d5872d;">Femme :</strong> 3 000 FCFA &nbsp;·&nbsp;
        <strong style="color:#d5872d;">Homme :</strong> 1 500 FCFA
    </p>
</div>
""", unsafe_allow_html=True)

# ── COMMENT NOUS REJOINDRE ────────────────────────────────────────────────────
st.markdown("""
<div style="background:white;border-radius:14px;padding:32px 36px;
            box-shadow:0 2px 16px rgba(0,0,0,0.07);margin-bottom:32px;
            border-top:4px solid #d5872d;">
    <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;
               font-weight:400;color:#2c2416;margin-bottom:6px;">
        📍 Comment nous rejoindre
    </h3>
    <div style="width:30px;height:2px;background:#d5872d;margin-bottom:16px;"></div>
    <p style="font-family:'Raleway',sans-serif;font-weight:300;color:#5a5040;
              font-size:0.95rem;line-height:1.8;">
        <strong style="color:#2c2416;">Attiegou — Lomé (Togo)</strong><br>
        Non loin du Lycée Attiegou (ex CEG Attiegou)<br>
        et du Château d'eau d'Attiegougan.<br><br>
        <a href="https://www.google.com/maps/search/?api=1&query=6.19304,1.26689"
           target="_blank"
           style="display:inline-block;margin-top:8px;padding:10px 22px;
                  background:#d5872d;color:white;border-radius:8px;
                  font-family:'Raleway',sans-serif;font-weight:600;font-size:0.88rem;
                  letter-spacing:0.05em;text-decoration:none;">
            📍 Voir la localisation sur Maps
        </a>
    </p>
</div>
""", unsafe_allow_html=True)

# ── FAQ ───────────────────────────────────────────────────────────────────────
st.markdown("""
<h2 style="font-family:'Cormorant Garamond',serif;font-size:2rem;
           font-weight:400;color:#2c2416;text-align:center;margin-bottom:6px;">
    Questions fréquentes
</h2>
<div style="text-align:center;color:#d5872d;margin-bottom:24px;">✦</div>
""", unsafe_allow_html=True)

faqs = [
    ("Comment confirmer ma présence ?",
     "Rendez-vous dans l'onglet RSVP de ce site et remplissez le formulaire de confirmation. Merci de confirmer votre présence avant le <strong style='color:#d5872d;'>1er Août 2026</strong>."),
    ("Puis-je venir avec mes enfants ?",
     "Oui, les enfants sont les bienvenus ! Merci toutefois de le mentionner lors de votre confirmation de présence afin que nous puissions prévoir les dispositions nécessaires pour les accueillir dans les meilleures conditions."),
    ("Puis-je offrir un cadeau ?",
     "Votre présence est, à nos yeux, le plus beau des cadeaux. Cependant, si vous souhaitez nous faire un présent, nous vous serions reconnaissants de privilégier une enveloppe, pour des raisons pratiques de logistique. Merci infiniment pour votre générosité."),
    ("Vous avez d'autres questions ?",
     "Pour toute question complémentaire, nous vous invitons à vous rapprocher directement des mariés qui se feront un plaisir de vous répondre."),
]

for q, a in faqs:
    st.markdown(f"""
    <div class="faq-item">
        <p class="faq-q">❓ {q}</p>
        <p class="faq-a">{a}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(f"""
<div class="site-footer">Adakou &amp; Ata-Sé &nbsp;·&nbsp; {WEDDING_DATE_STR} &nbsp;·&nbsp; {LOCATION}</div>
""", unsafe_allow_html=True)
