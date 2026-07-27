CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Raleway:wght@300;400;500;600;700&display=swap');

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebarNav"] li:first-child { display: none; }
.block-container { padding-top: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { background: #2c2416 !important; }
section[data-testid="stSidebar"] * { color: #f4f4f8 !important; }

body, .stApp { background-color: #f4f4f8; font-family: 'Raleway', sans-serif; }

/* ── HERO ── */
.hero {
    background: linear-gradient(160deg, #2c2416 0%, #4a3728 60%, #7b7551 100%);
    padding: 80px 24px 60px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at 50% 40%, rgba(213,135,45,0.18) 0%, transparent 65%);
}
.hero-eyebrow {
    font-family: 'Raleway', sans-serif;
    font-size: 0.8rem; font-weight: 500;
    letter-spacing: 0.4em; text-transform: uppercase;
    color: rgba(244,244,248,0.65); margin-bottom: 20px;
    position: relative; z-index: 1;
}
.hero-names {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3.2rem, 9vw, 6.5rem);
    font-weight: 300; color: #d5872d !important;
    margin: 0; margin-right: -0.04em; letter-spacing: 0.04em; text-align: center !important;
    position: relative; z-index: 1; line-height: 1.1;
}
.hero-amp { color: #2c2416 !important; font-style: italic; margin: 0 0.12em; display: inline-block; }
.hero-ornament { color: #d5872d; font-size: 1.4rem; margin: 18px 0; position: relative; z-index: 1; }
.hero-date {
    font-family: 'Raleway', sans-serif;
    font-size: 0.95rem; font-weight: 400;
    letter-spacing: 0.35em; text-transform: uppercase;
    color: rgba(244,244,248,0.75);
    position: relative; z-index: 1;
}

/* ── COUNTDOWN ── */
.countdown-wrap {
    display: flex; justify-content: center; gap: 20px;
    margin: 40px auto 0; max-width: 480px; padding: 0 24px;
}
.cd-box {
    background: white; border-radius: 12px; padding: 18px 20px;
    text-align: center; flex: 1;
    box-shadow: 0 4px 20px rgba(213,135,45,0.12);
    border-bottom: 3px solid #d5872d;
}
.cd-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.8rem; font-weight: 600; color: #d5872d;
    line-height: 1; display: block;
}
.cd-lbl {
    font-family: 'Raleway', sans-serif;
    font-size: 0.62rem; font-weight: 600;
    letter-spacing: 0.2em; text-transform: uppercase;
    color: #7b7551; margin-top: 6px; display: block;
}

/* ── SECTIONS ── */
.section { max-width: 860px; margin: 0 auto; padding: 60px 24px; text-align: center; }
.section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem; font-weight: 400; color: #2c2416; margin-bottom: 6px;
}
.section-orn { color: #d5872d; font-size: 1.1rem; margin: 6px 0 22px; }
.section-text {
    font-family: 'Raleway', sans-serif;
    font-size: 1rem; font-weight: 300; color: #5a5040; line-height: 1.9;
}

/* ── CARDS ── */
.event-card {
    background: white; border-radius: 14px; padding: 32px 36px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    border-left: 4px solid #d5872d;
    margin-bottom: 20px; text-align: left;
}
.event-day {
    font-family: 'Raleway', sans-serif; font-size: 0.7rem;
    font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase;
    color: #d5872d; margin-bottom: 8px;
}
.event-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem; font-weight: 400; color: #2c2416;
}
.event-detail {
    font-family: 'Raleway', sans-serif; font-size: 0.9rem;
    font-weight: 400; color: #7b7551; margin-top: 10px; line-height: 1.7;
}

/* ── PERSON CARD ── */
.person-card {
    background: white; border-radius: 14px; padding: 24px 20px;
    text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    border-top: 3px solid #7b7551;
}
.person-avatar {
    width: 80px; height: 80px; border-radius: 50%;
    background: linear-gradient(135deg, #d5872d, #7b7551);
    margin: 0 auto 14px; display: flex; align-items: center;
    justify-content: center; font-size: 2rem;
}
.person-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.2rem; color: #2c2416;
}
.person-role {
    font-family: 'Raleway', sans-serif; font-size: 0.72rem;
    font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase;
    color: #d5872d; margin-top: 4px;
}

/* ── RSVP FORM ── */
.rsvp-wrap { max-width: 620px; margin: 0 auto; padding: 0 24px 60px; }
.rsvp-card {
    background: white; border-radius: 16px; padding: 40px 44px;
    box-shadow: 0 4px 30px rgba(0,0,0,0.08);
}
.stButton > button {
    background: linear-gradient(135deg, #d5872d, #c07020) !important;
    color: white !important; border: none !important;
    border-radius: 50px !important; padding: 12px 40px !important;
    font-family: 'Raleway', sans-serif !important;
    font-size: 0.9rem !important; font-weight: 600 !important;
    letter-spacing: 0.15em !important; text-transform: uppercase !important;
    width: 100% !important; margin-top: 12px !important;
}
.stButton > button:hover { opacity: 0.9 !important; }

/* ── FAQ ── */
.faq-item {
    background: white; border-radius: 12px; padding: 20px 26px;
    margin-bottom: 12px; border-left: 3px solid #7b7551;
    box-shadow: 0 1px 8px rgba(0,0,0,0.05);
}
.faq-q {
    font-family: 'Raleway', sans-serif; font-weight: 600;
    color: #2c2416; font-size: 0.95rem; margin-bottom: 8px;
}
.faq-a {
    font-family: 'Raleway', sans-serif; font-weight: 300;
    color: #5a5040; font-size: 0.9rem; line-height: 1.7;
}

/* ── CALENDAR ICON ── */
.cal-icon {
    width: 42px; height: 42px; margin: 0 auto 10px;
    border-radius: 7px; background: white; border: 2px solid #d5872d;
    display: flex; flex-direction: column; overflow: visible;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08); position: relative;
}
.cal-icon-top {
    height: 11px; background: #d5872d; border-radius: 4px 4px 0 0;
    position: relative;
}
.cal-icon-top::before, .cal-icon-top::after {
    content: ''; position: absolute; top: -3px; width: 4px; height: 8px;
    background: #7b7551; border-radius: 2px;
}
.cal-icon-top::before { left: 9px; }
.cal-icon-top::after { right: 9px; }
.cal-icon-day {
    flex: 1; display: flex; align-items: center; justify-content: center;
    font-family: 'Cormorant Garamond', serif; font-weight: 700;
    font-size: 1.25rem; color: #2c2416; line-height: 1;
}

/* ── ENVELOPE INTRO ── */
.env-checkbox { display: none; }
.env-overlay {
    position: fixed; inset: 0; z-index: 999999;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    background: linear-gradient(160deg, #2c2416 0%, #4a3728 55%, #7b7551 100%);
    cursor: pointer;
    transition: opacity 0.9s ease 0.65s, visibility 0.9s ease 0.65s;
}
.env-checkbox:checked + .env-overlay {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}
.envelope {
    position: relative; width: 260px; height: 175px; perspective: 1200px;
}
.envelope::before, .envelope::after {
    content: ''; position: absolute; bottom: 0; width: 0; height: 0;
    border-style: solid; z-index: 1;
}
.envelope::before {
    left: 0; border-width: 0 0 88px 130px;
    border-color: transparent transparent rgba(0,0,0,0.06) transparent;
}
.envelope::after {
    right: 0; border-width: 0 130px 88px 0;
    border-color: transparent transparent rgba(0,0,0,0.06) transparent;
}
.env-back {
    position: absolute; inset: 0; border-radius: 5px;
    background: linear-gradient(160deg, #f7efe0, #ecdfc3);
    box-shadow: 0 25px 60px rgba(0,0,0,0.45);
}
.env-letter {
    position: absolute; left: 12px; right: 12px; bottom: 6px; height: 82%;
    background: #fffdf8; border-radius: 4px;
    box-shadow: 0 -2px 14px rgba(0,0,0,0.1);
    display: flex; align-items: center; justify-content: center;
    transform: translateY(4px); transition: transform 0.7s ease 0.1s;
    z-index: 2;
}
.env-letter-ornament {
    font-family: 'Cormorant Garamond', serif; font-size: 1rem;
    color: rgba(213,135,45,0.55); letter-spacing: 0.5em;
}
.env-flap {
    position: absolute; top: 0; left: 0; width: 100%; height: 88px;
    background: linear-gradient(160deg, #f0e2c4, #e2cfa0);
    clip-path: polygon(0 0, 100% 0, 50% 100%);
    transform-origin: top center; transform-style: preserve-3d;
    transition: transform 0.8s ease-in-out; z-index: 3;
    filter: drop-shadow(0 6px 8px rgba(0,0,0,0.18));
}
.env-seal {
    position: absolute; top: 54px; left: 50%; transform: translate(-50%,-50%);
    width: 52px; height: 52px; border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #e6a13e, #b96a1a);
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.35), inset 0 1px 3px rgba(255,255,255,0.25),
                inset 0 -2px 4px rgba(0,0,0,0.25);
    z-index: 4;
    animation: env-pulse 2.4s ease-in-out infinite;
}
.env-seal svg { display: block; width: 30px; height: 30px; }
@keyframes env-pulse {
    0%, 100% { transform: translate(-50%,-50%) scale(1); }
    50% { transform: translate(-50%,-50%) scale(1.07); }
}
.env-checkbox:checked + .env-overlay .env-flap { transform: rotateX(180deg); }
.env-checkbox:checked + .env-overlay .env-letter {
    transform: translateY(-42px); transition: transform 0.7s ease 0.55s;
}
.env-overlay.env-instant,
.env-overlay.env-instant .env-flap,
.env-overlay.env-instant .env-letter {
    transition: none !important;
}
.env-hint {
    margin-top: 32px; font-family: 'Raleway', sans-serif; font-size: 0.75rem;
    font-weight: 500; letter-spacing: 0.3em; text-transform: uppercase;
    color: rgba(244,244,248,0.7);
}

/* ── FOOTER ── */
.site-footer {
    text-align: center; padding: 40px 24px;
    font-family: 'Raleway', sans-serif; font-size: 0.8rem;
    color: #9a8e80; letter-spacing: 0.1em;
    border-top: 1px solid rgba(123,117,81,0.2);
}
</style>
"""

WEDDING_DATE_STR = "29 Août 2026"
COUPLE = "Adakou & Ata-Sé"
LOCATION = "Lomé, Togo"


def nav_bar():
    import streamlit as st
    st.markdown("""
    <div style="background:white;border-bottom:1px solid rgba(213,135,45,0.2);
                padding:10px 24px;margin-bottom:0;">
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 8])
    with col1:
        st.page_link("app.py", label="← Accueil", use_container_width=True)
