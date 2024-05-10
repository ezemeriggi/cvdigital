from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic(3).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV Digital | Ezequiel Meriggi"
PAGE_ICON = ":hospital:"
NAME = "Ezequiel Meriggi"
DESCRIPTION = """
Médico y Data Analyst.
"""
EMAIL = "ezequielmeriggi@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/",
    "🏆 Income and Expense Tracker - ": "https://youtu.be/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Aptitudes & Cualidades")
st.write(
    """
- ✔️ Capacidad para analizar problemas complejos y formular soluciones prácticas.
- ✔️ Trabajo en equipo e iniciativa para hacer más eficiente el uso de recursos y del personal de trabajo.
- ✔️ Buen manejo de conceptos estadísticos básicos y sus aplicaciones
- ✔️ Experiencia en la supervisión remota del flujo financiero de múltiples sucursales
- ✔️ Experiencia en categorización y análisis de gastos empresariales y optimización de recursos.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programación: SQL, Phyton (básico)
- 📊 Visualización de datos: PowerBi, MS Excel, Tableau (aprendiendo)
- 📚 Estadística: Regresión logística, regresión lineal, árboles de decisión
- 🗄️ Databases: MySQL
"""
)

# --- IDIOMAS ---
st.write('\n')
st.subheader("IDIOMAS")
st.write(
    """
- 🇦🇷  Español: Nativo
- 🇺🇸  🇬🇧  Inglés: C1
- 🇫🇷  Francés: A2 (en curso)
- 🇩🇪  🇦🇹  Alemán: A1.2
"""
)

# --- Educación ---
st.write('\n')
st.subheader("Educación")
st.write("---")

# --- Grado
st.write("🎓", "Médico: UNIVERSIDAD NACIONAL DE LA PLATA")
st.write("2014 - 2023")
st.write("🎓", "Licenciatura en Sistemas Informáticos: UNIVERSIDAD NACIONAL DE LA PLATA")
st.write("2023 - actualidad (15%)"
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia Laboral")
st.write("---")

# --- JOB 1
st.write("🛒 ", "Biston Global SRL (Bahía Blanca, Buenos Aires)")
st.write("2016 - actualidad")
st.write(
    """
- ► Auditoría y control de flujo de dinero en las 6 sucursales.
- ► Creación de guías y algoritmos de manejo de distintas áreas de la empresa.
- ► Trabajo en conjunto con la empresa desarrolladora del software de ventas y stock.
- ► Uso de PowerBI, MS Excel y SQL para:
    - Rediseñar el modelo de base de datos.
    - Categorizar y registrar cada gasto.
    - Analizar la rentabilidad de la empresa en general y de áreas específicas.
"""
)

# --- JOB 2
st.write('\n')
st.write("🏥 ", "Pre-residente de Clínica (Hospital San Martín, La Plata, Buenos Aires)")
st.write("Programa de becas de la provincia de Buenos Aires")
st.write(" 03/2024 - 05/2024")
st.write(
    """
- ► Rotativo por salas de internación del área de Clínica del hospital San Martín de La Plata.
"""
)

# --- INTERCAMBIOS Y VOLUNTARIADO ---
st.write('\n')
st.subheader("Intercambio Universitario y voluntariado")
st.write("---")

# --- INTERCAMBIO
st.write('\n')
st.write("🇦🇹 ", "INTERNATIONAL FEDERATION OF MEDICAL STUDENTS' ASSOCIATIONS (IFMSA)")
st.write("Intercambio rotativo en “Salzburger Landeskliniken (SALK)” en Salzburg, Austria.")
st.write("2019")
st.write(
    """
- ► Intercambio bilateral, estuve en el área de cirugía del departamento de Urología.
"""
)

# --- VOLUNTARIADO
st.write('\n')
st.write("🙌 ", "R.E.D.E.S (realizando derechos para una externación sustentable)")
st.write("Hospital Dr. Alejandro Korn, Melchor Romero, Buenos Aires")
st.write("2017 - 2021")
st.write(
    """
- ► Rol de extensionista universitario en tareas de desarrollo del lazo social con pacientes internados en el servicio de salud mental.
- ► Trabajo interdisciplinario.
- ► Presentación en congresos de salud mental comunitaria.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Proyectos")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
