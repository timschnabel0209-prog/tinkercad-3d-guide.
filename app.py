from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Tinkercad 3D – Anleitung",
    page_icon="🧊",
    layout="centered",
)

BASE_DIR = Path(__file__).parent
KNOWLEDGE_DIR = BASE_DIR / "wissen"

st.markdown("""
<style>
    .block-container {max-width: 900px; padding-top: 2.2rem; padding-bottom: 4rem;}
    h1, h2, h3 {letter-spacing: -0.02em;}
    .intro {color: #666; font-size: 1.05rem;}
    a {text-decoration: none;}
</style>
""", unsafe_allow_html=True)

st.title("Tinkercad 3D – Anleitung")
st.markdown(
    '<p class="intro">Eine übersichtliche deutschsprachige Anleitung für '
    'Autodesk Tinkercad 3D Design – vom ersten Objekt bis zum Export.</p>',
    unsafe_allow_html=True,
)

st.info(
    "Diese Website ist ein Lernleitfaden zu Tinkercad 3D Design. "
    "Die Oberfläche kann sich durch Updates leicht verändern. "
    "Wenn eine Schaltfläche anders heißt oder an einer anderen Stelle liegt, "
    "orientiere dich an ihrer Funktion."
)

docs = sorted(KNOWLEDGE_DIR.glob("*.md"))
if not docs:
    st.warning("Noch keine Wissensartikel gefunden. Lege Markdown-Dateien im Ordner „wissen“ ab.")
else:
    st.subheader("Inhaltsübersicht")
    for doc in docs:
        title = doc.stem.replace("_", " ").replace("-", " ").title()
        st.markdown(f"- [{title}](#{doc.stem})")

    st.divider()
    for doc in docs:
        content = doc.read_text(encoding="utf-8")
        st.markdown(f'<div id="{doc.stem}"></div>', unsafe_allow_html=True)
        st.markdown(content)
        st.divider()

st.subheader("Offizielle Lernressourcen")
st.markdown(
    "- [Tinkercad – offizielle 3D-Design-Tutorials](https://www.tinkercad.com/learn/designs)\n"
    "- [Tinkercad – Startseite](https://www.tinkercad.com/)"
)

st.caption(
    "Unabhängiger Lernleitfaden. Nicht von Autodesk erstellt oder unterstützt. "
    "Tinkercad und Autodesk sind Marken ihrer jeweiligen Inhaber."
)
