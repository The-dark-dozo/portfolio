import streamlit as st
from datetime import date

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(
    page_title="Portfolio – Adaï Joseph Térence",
    page_icon="📊",
    layout="wide",
)

# ----------------------
# DATA / CONTENT
# ----------------------
PROFILE = {
    "name": "Adaï Joseph Térence",
    "title": "Data Scientist",
    "email": "josephterence84@gmail.com",
    "phone": "+225 07-12-45-05-86",
    "linkedin": "https://www.linkedin.com/in/joseph-ada%C3%AF-821986364/",
    "github": "https://github.com/The-dark-dozo",
    # Optionnel: ajoute le chemin d'un CV PDF hébergé (GitHub raw/Drive) pour activer le bouton de téléchargement
    "cv_url": None,
}

PROJECTS = [
    {
        "title": "Prédiction de l’Inclusion Financière en Afrique",
        "subtitle": "Application Streamlit avec modèle XGBoost",
        "description": (
            "Application interactive qui prédit si une personne possède un compte bancaire à partir de "
            "données socio‑démographiques. Intégration d’un modèle XGBoost et déploiement avec Streamlit."
        ),
        "skills": ["Python", "Streamlit", "XGBoost", "Scikit-learn", "Pandas", "NumPy"],
        "github_url": "https://github.com/The-dark-dozo/streamlit-financial-inclusion",
        "app_url": "https://app-financial-inclusion-abtlv8ahtjnrsgvx67jxmu.streamlit.app/",
        "value_add": [
            "Analyses prédictives appliquées à un cas business (inclusion financière)",
            "Dashboard interactif pour utilisateurs non techniques",
            "Chaîne complète: préparation des données ▶️ modélisation ▶️ déploiement",
        ],
    },
    {
        "title": "Music Streaming Database",
        "subtitle": "Modélisation de base de données PostgreSQL + requêtes d’analyse",
        "description": (
            "Schéma relationnel pour application de streaming musical (users, artists, albums, tracks, "
            "playlists, listening_history, subscriptions, comments). Inclut des requêtes d’insights métier."
        ),
        "skills": ["SQL", "PostgreSQL", "Modélisation", "Analyses SQL", "Git"],
        "github_url": "https://github.com/The-dark-dozo/music-streaming-db",
        "app_url": None,
        "value_add": [
            "Maîtrise de la conception SQL et requêtes analytiques",
            "Transformation de besoins métier en modèle exploitable",
            "Analyses: top chansons, temps d’écoute, playlists par utilisateur",
        ],
    },
    {
        "title": "Analyse Jumia CI – Ordinateurs Portables",
        "subtitle": "Web scraping + EDA + insights business",
        "description": (
            "Collecte (Selenium, BeautifulSoup), nettoyage (Pandas) et analyse du marché des laptops sur "
            "Jumia Côte d’Ivoire: marques, processeurs, RAM, stockage, avis."
        ),
        "skills": ["Selenium", "BeautifulSoup", "Pandas", "EDA", "Data Cleaning", "Git"],
        "github_url": "https://github.com/The-dark-dozo/Data_Jumia_analysis_laptop",
        "app_url": None,
        "value_add": [
            "Transformation de données non structurées en indicateurs actionnables",
            "Classements marques/configurations et préférences clients",
            "Prêt pour tableaux de bord Power BI / Excel",
        ],
    },
    {
        "title": "Analyse des Variations des Cryptomonnaies",
        "subtitle": "Automatisation via API CoinMarketCap + visualisations Plotly",
        "description": (
            "Collecte en temps réel (requests), nettoyage et suivi des variations (1h, 24h, 7j, 30j, 60j, 90j). "
            "Visualisations interactives avec Plotly, export CSV pour suivi."
        ),
        "skills": ["API", "Python", "Pandas", "Plotly", "Matplotlib", "Seaborn", "Git"],
        "github_url": "https://github.com/The-dark-dozo/Coinmarket_api_usecase",
        "app_url": None,
        "value_add": [
            "Connexion à des sources externes (API) et automatisation",
            "Suivi dynamique d’indicateurs temporels",
            "Communication claire via graphiques interactifs",
        ],
    },
    {
        "title": "Churn Prediction – Expresso",
        "subtitle": "Application Streamlit de prédiction du churn",
        "description": (
            "Application interactive pour estimer le risque de départ client et explorer les facteurs clés "
            "de churn pour un opérateur télécom."
        ),
        "skills": ["Streamlit", "ML", "Pandas", "Visualisation", "Segmentation"],
        "github_url": "https://github.com/The-dark-dozo/churn_app",
        "app_url": None,
        "value_add": [
            "Priorisation des segments clients à risque",
            "Aide à la décision pour la fidélisation",
            "Présentation d’insights complexes de façon simple",
        ],
    },
]

TAGS_COLORMAP = {
    # simple mapping to keep tags visually distinct
    "Python": "#166534", "Streamlit": "#065f46", "XGBoost": "#1d4ed8", "Scikit-learn": "#0f766e",
    "Pandas": "#4b5563", "NumPy": "#7c3aed", "SQL": "#334155", "PostgreSQL": "#1e293b",
    "Modélisation": "#ef4444", "Analyses SQL": "#dc2626", "Git": "#111827", "Selenium": "#6b21a8",
    "BeautifulSoup": "#15803d", "EDA": "#0ea5e9", "Data Cleaning": "#a16207", "API": "#7c2d12",
    "Plotly": "#1f2937", "Matplotlib": "#0b7285", "Seaborn": "#155e75", "ML": "#a21caf",
    "Visualisation": "#7c3aed", "Segmentation": "#334155",
}

# ----------------------
# HELPERS
# ----------------------
def tag_chip(label: str):
    color = TAGS_COLORMAP.get(label, "#334155")
    return f"""
    <span style='display:inline-block; padding:4px 10px; margin:2px; border-radius:999px; font-size:12px; background:{color}; color:white;'>
        {label}
    </span>
    """


def project_card(p: dict):
    with st.container(border=True):
        left, right = st.columns([0.72, 0.28], vertical_alignment="center")
        with left:
            st.subheader(p["title"])  # title
            st.caption(p.get("subtitle", ""))
            st.write(p["description"])  # description

            # tags
            tags = "".join([tag_chip(s) for s in p.get("skills", [])])
            st.markdown(tags, unsafe_allow_html=True)

            # value add bullets
            if v := p.get("value_add"):
                st.markdown("**Valeur ajoutée :**")
                for item in v:
                    st.markdown(f"- {item}")
        with right:
            st.markdown("#### Liens")
            st.link_button("GitHub", p["github_url"], use_container_width=True)
            if p.get("app_url"):
                st.link_button("Application", p["app_url"], use_container_width=True)


# ----------------------
# SIDEBAR NAV
# ----------------------
with st.sidebar:
    st.image("20210216_213621.jpg", use_container_width=True)
      # GitHub avatar (modifiable)
    st.markdown(f"### {PROFILE['name']}")
    st.markdown(f"**{PROFILE['title']}**")
    st.divider()
    nav = st.radio(
        "Navigation",
        ["🏠 Accueil", "📂 Projets", "📬 Contact"],
        index=0,
    )
    st.divider()
    st.markdown("**Liens rapides**")
    st.link_button("GitHub", PROFILE["github"], use_container_width=True)
    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    if PROFILE.get("cv_url"):
        st.link_button("Télécharger mon CV", PROFILE["cv_url"], use_container_width=True)


# ----------------------
# PAGES
# ----------------------
if nav == "🏠 Accueil":
    st.title("📊 Portfolio – Adaï Joseph Térence")
    st.markdown(f"#### {PROFILE['title']}")

    st.write(
        """
        Passionné par la *science des données*, je conçois et déploie des solutions allant de l’analyse exploratoire
        à la mise en production d’applications interactives. Mon objectif : transformer des données complexes en
        **informations stratégiques et exploitables** pour soutenir la prise de décision.
        """
    )

    # Quick highlights
    st.subheader("Compétences clés")
    cols = st.columns(4)
    highlights = [
        ("Analyse & EDA", "Pandas, statistiques descriptives, visualisation"),
        ("SQL & Modélisation", "PostgreSQL, requêtes analytiques"),
        ("ML & Prédiction", "Scikit-learn, XGBoost"),
        ("Apps & Déploiement", "Streamlit, Git/GitHub"),
    ]
    for (title, desc), c in zip(highlights, cols):
        with c:
            st.metric(label=title, value="✔︎")
            st.caption(desc)

    st.divider()
    st.subheader("Projets en vedette")
    for p in PROJECTS[:3]:  # show first three as featured
        project_card(p)

elif nav == "📂 Projets":
    st.title("📂 Projets")

    # Filters (par compétence)
    all_skills = sorted({s for p in PROJECTS for s in p.get("skills", [])})
    sel = st.multiselect("Filtrer par compétence :", options=all_skills)

    filtered = [p for p in PROJECTS if set(sel).issubset(set(p.get("skills", [])))] if sel else PROJECTS

    for p in filtered:
        project_card(p)

elif nav == "📬 Contact":
    st.title("📬 Contact")

    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        st.markdown(f"**Nom :** {PROFILE['name']}")
        st.markdown(f"**Titre :** {PROFILE['title']}")
        st.markdown(f"**Email :** [{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.markdown(f"**Téléphone :** {PROFILE['phone']}")
        st.markdown(f"**LinkedIn :** [{PROFILE['linkedin']}]({PROFILE['linkedin']})")
        st.markdown(f"**GitHub :** [{PROFILE['github']}]({PROFILE['github']})")
        if PROFILE.get("cv_url"):
            st.download_button("Télécharger mon CV", data=None, file_name="CV_Adaï_Joseph_Térence.pdf", disabled=True)
            st.caption("(Ajoute l’URL de ton CV dans PROFILE['cv_url'] pour activer un bouton dédié dans la barre latérale.)")

    with col2:
        st.info(
            "Disponible pour un **stage Business Analyst Junior (6 mois)** à partir du 01 septembre 2025.")
        st.write(":spiral_calendar: Dernière mise à jour : ", date.today().strftime('%d/%m/%Y'))

    st.divider()
    st.write("\nMerci pour votre visite ! N’hésitez pas à me contacter pour toute collaboration 🚀")
