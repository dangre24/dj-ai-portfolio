import streamlit as st

st.set_page_config(
    page_title="Daniel (DJ) Greene Jr | Projects",
    page_icon="🧬",
    layout="centered"
)
st.markdown("""
<style>

/* REMOVE STREAMLIT HEADER */
header {
    visibility: hidden;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

[data-testid="stStatusWidget"] {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Georgia&display=swap');

.stApp {
    background: linear-gradient(135deg, #071a1f 0%, #0b2d2e 45%, #102a43 100%);
    color: #f5f7fa;
}

html, body, [class*="css"], [data-testid="stMarkdownContainer"] {
    font-family: Georgia, serif !important;
}

/* Main container */
.block-container {
    padding-top: 3rem;
    max-width: 850px;
}

/* Header box */
.hero {
    text-align: center;
    padding: 35px 25px;
    border-radius: 25px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(120, 255, 214, 0.25);
    box-shadow: 0 0 30px rgba(0, 255, 200, 0.12);
    margin-bottom: 30px;
}

/* Main name */
.hero h1 {
    font-size: 45px;
    color: #eafff8;
    margin-bottom: 5px;
}

/* Subtitle */
.hero h3 {
    color: #7fffd4;
    font-weight: normal;
}

/* Project cards */
.project-card {
    background: rgba(255, 255, 255, 0.09);
    border: 1px solid rgba(127, 255, 212, 0.25);
    border-radius: 22px;
    padding: 24px;
    margin: 18px 0;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
    transition: 0.25s ease;
}

.project-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 28px rgba(127, 255, 212, 0.25);
    border-color: #7fffd4;
}

.project-title {
    font-size: 25px;
    font-weight: bold;
    color: #ffffff;
}

.project-description {
    font-size: 16px;
    color: #d6e4e5;
    margin-top: 8px;
    margin-bottom: 18px;
}

/* Link buttons */
.stLinkButton a {
    background: linear-gradient(90deg, #00c9a7, #00b4d8) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 0.65rem 1.2rem !important;
    font-weight: bold !important;
    border: none !important;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 35px;
    padding: 20px;
    color: #d6e4e5;
    font-size: 15px;
}

a {
    color: #7fffd4 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🧬 Daniel (DJ) Greene Jr</h1>
    <h3>Project Portfolio</h3>
    <p>Healthcare, laboratory science, biotech, and legal AI tools built with Python, and OpenAI APIs.</p>
</div>
""", unsafe_allow_html=True)

links = [
    {
        "title": "🧪 Lab Folks AI",
        "description": "AI-powered laboratory analysis assistant for PCR, HPLC, ELISA, LC-MS, and GC-MS workflows.",
        "url": "https://labfolksai.streamlit.app"
    },
    {
        "title": "💊 Rx Insight AI",
        "description": "AI healthcare application for medication interaction review, lifestyle factors, and biochemical risk analysis.",
        "url": "https://rxinsightai.streamlit.app"
    },
    {
        "title": "⚖️ ConstitutionAI",
        "description": "AI constitutional rights and law education tool for search-and-seizure, Miranda rights, and due process scenarios.",
        "url": "https://constitutionai.streamlit.app/"
    },
    {
        "title": "CRISPR Guide RNA Designer",
        "description": "A Python-based CRISPR guide RNA design tool that detects PAM sites, ranks candidate guides, predicts off-target risk, and visualizes potential genome edits.",
        "url": "https://crispr-ytmd.onrender.com/"
    },
]

for link in links:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{link["title"]}</div>
        <div class="project-description">{link["description"]}</div>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("Open Project", link["url"])

st.markdown("""
<div class="footer">
    <p>📧 djgreenedj@gmail.com</p>
    <p>📞 317-760-6807</p>
    <p>🔗 GitHub: <a href="https://github.com/dangre24" target="_blank">github.com/dangre24</a></p>
</div>
""", unsafe_allow_html=True)

# streamlit run app.py
