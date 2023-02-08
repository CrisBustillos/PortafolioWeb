from pathlib import Path

import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portafolio Python - Excel - Streamlit - Anaconda Cristóbal Bustillos Contreras"
PAGE_ICON = ":wave:"
NAME = "Cristóbal Bustillos Contreras"
DESCRIPTION =  """ 
Joven profesional entusiasta y conocedor de la tecnología e informática y 
todos sus potenciales usos. La información es poder, y hoy más que nunca
tenemos las herramientas para dominar ese poder.
"""

EMAIL = "cris.bustillosc@gmail.com"
PROJECTS = {
	"💻 Aplicación de escritorio que permite la interconexión entre Python y Excel": "https://drive.google.com/file/d/1rCudAw7IErNmhohU6TWcSSuaMzo_6ELp/view?usp=share_link",
	"📲 Aplicación Web para el trabajo de base de datos de forma remota": "https://crisbustillos-appweb-app-fyyif9.streamlit.app",
	"🐍 Aplicación de comandos con Python para obtener NDVI en imagenes de cultivos (en progreso)": "https://drive.google.com/file/d/18EwvILW5NOfyW2GAUj_E8vNKIp2YSipG/view?usp=sharing",

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
		label="Descargar CV",
		data=PDFbyte,
		file_name=resume_file.name,
		mime="application/octet-stream",
	)
	st.write("📧", EMAIL)
	st.write("📱", "+56993663970")

# --- EXPERIENCE & QUALIFICATIONS ---

st.write("#")
st.subheader("👨‍💻 Conocimientos en programación y tecnologías")
st.write("---")
st.write(
	"""
	- 🏆 Conocimientos sólidos en uso del lenguaje de programación Python para trabajar con grandes volumenes de datos. Principalmente, he trabajado con Pandas, Matplotlib, Streamlit, Numpy, entre otros.
	- 🏆 Creación y gestión de base de datos con tecnologías como MySQL, SQLite3 y Excel.
	- 🏆 Conocimientos intermedio en uso de Excel.
	- 🏆 Uso avanzado de cmd y bash tanto en Windows como en Linux.
	"""
	)

# --- PROJECTS ---

st.write("#")
st.subheader("💡 Proyectos personales")
st.write("---")
for project, link in PROJECTS.items():
	st.write(f"[{project}]({link})")

