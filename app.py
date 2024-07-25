from pathlib import Path

import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Paulo_Augusto_Giavoni_CV_EN_.pdf"
profile_pic = current_dir / "assets" / "personalfoto.png"
mickey_pic = current_dir / "assets" / "mickey.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Paulo Giavoni"
PAGE_ICON = ":wave:"
NAME = "Paulo Giavoni"
DESCRIPTION = """
2D/3D CAD Specialist, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "paulo.giavoni@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/paulogiavoni/",
    "ResearchGate": "https://www.researchgate.net/publication/374950113_BIM_METHODOLOGY_APPLIED_TO_THE_DIGITALIZATION_AND_MODERNIZATION_OF_THE_PAULO_AFONSO_IV_POWER_PLANT_CHESF_BAHIA",
}
PROJECTS = {
    "🏆 BIM Methodology Applied to the Digitalization and Modernization of the Paulo Afonso IV Power Plant (CHESF, Bahia)": "https://www.researchgate.net/publication/374950113_BIM_METHODOLOGY_APPLIED_TO_THE_DIGITALIZATION_AND_MODERNIZATION_OF_THE_PAULO_AFONSO_IV_POWER_PLANT_CHESF_BAHIA",
}

# --- PAGE SETTINGS ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)
mickey_pic = Image.open(mickey_pic)

# --- SIDEBAR MENU ---
st.sidebar.title("Navigation")
menu = ["Home", "Projects", "Contact", "Testimonials", "Education"]
choice = st.sidebar.radio("Go to", menu)

# --- PAGE CONTENT ---
if choice == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - ✔️ Specialized in advanced BIM methodologies and applications in engineering and construction projects
        - ✔️ Strong hands-on experience and knowledge in Revit, Dynamo, Navisworks, and Inventor
        - ✔️ Excellent team player with a strong sense of initiative on tasks
        """
    )

    # --- LINKEDIN WIDGET ---
    st.subheader("My Linkedin Feed")
    components.html(
        """
        <script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
        <div class="elfsight-app-89d4b5f4-c11b-4309-ada1-25893ce1745c" data-elfsight-app-lazy></div>
        """,
        height=600
    )

    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")

    # --- SKILLS ---
    st.write('\n')
    st.subheader("Technical Skills")
    st.write(
        """
        - 👩‍💻 Software: Revit Architecture, Revit MEP, Navisworks, Dynamo, Inventor
        - 📊 Languages: Italian, English, Portuguese
        """
    )

    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1 ---
    st.write("🚧", "**Electrical Designer - Revit | Norhart Inc**")
    st.write("Jan 2024 - Jun 2024 | Remote - Minnesota, US")
    st.write(
        """
        - ► Lead the electrical design for multi-residential buildings utilizing Revit and Dynamo in compliance with the NEC Code (US).
        - ► Support lighting calculations and cable sizing through advanced programming techniques.
        - ► Conduct regular check-in meetings to present progress and deliverables to supervisors, ensuring project alignment and deadlines are met.
        """
    )

    # --- JOB 2 ---
    st.write('\n')
    st.write("🚧", "**BIM Specialist | Voith Hydro Latam**")
    st.write("Apr 2021 - Dec 2023 | Hybrid - Brazil")
    st.write(
        """
        - ► Spearheaded the implementation of BIM methodologies, significantly optimizing modernization processes for hydroelectric power plants.
        - ► Managed and coordinated the 3D scanning and modeling of the Paulo Afonso IV Hydroelectric Plant.
        - ► Provided international modeling support for projects in Australia, Germany, and the USA.
        - ► Led training programs and development sessions, enhancing team proficiency in BIM.
        """
    )

    # --- JOB 3 ---
    st.write('\n')
    st.write("🚧", "**BIM Specialist | Adecco - Latam**")
    st.write("May 2019 - Mar 2021 | Remote - Brazil")
    st.write(
        """
        - ► Contracted through Adecco to deliver BIM modeling services for GE GridACS in São Paulo, Brazil.
        - ► Acted as a training leader in Revit, Navisworks, and Dynamo across the LATAM region.
        - ► Standardized 3D elements for electrical substations, ensuring consistency and efficiency.
        - ► Developed BIM models for 230kV and 500kV substations, enhancing project accuracy and detail.
        """
    )

elif choice == "Projects":
    st.subheader("Projects & Accomplishments")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")

elif choice == "Contact":
    st.subheader("Contact")
    st.write("---")
    st.write("Feel free to reach out via email or phone:")
    st.write("📫", EMAIL)
    st.write("📞 +55 11 96524-8049")

elif choice == "Testimonials":
    st.subheader("Testimonials")
    st.write("---")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(mickey_pic, width=100)
    with col2:
        st.write(
            """
            "Paulo is a highly professional and effective Electrical Designer. In only a few months, he had created an entirely new way to present electrical construction drawing information. A client requested fully detailed electrical drawings with material take-offs. Paulo created and implemented the system to deliver an exceptional set of electrical drawings. His BIM background clearly shines in his work, and he’s constantly seeking the best possible ways to complete any task. Paulo did a great job in balancing BIM automation customizations with the schedule of deliverables to ensure projects stayed on track. I would recommend Paulo as an Electrical Designer and any other BIM role."
            """
        )
        st.write("— [Mickey Halverson, PE, SE, Director of Architecture & Engineering](https://www.linkedin.com/in/mickey-halverson-pe-se-b69b34ba/)")

elif choice == "Education":
    st.subheader("Education")
    st.write("---")
    st.write("### Master's in Building Information Modeling (BIM)")
    st.write("**Polytechnic School, University of São Paulo (USP)**")
    st.write("2021 – 2023 | São Paulo, Brazil")
    st.write("- Specialized in advanced BIM methodologies and applications in engineering and construction projects.")
    st.write('\n')
    st.write("### Postgraduate in Digital Architecture and Parametric Design")
    st.write("**Centro Universitário Belas Artes**")
    st.write("2020 – 2021 | São Paulo, Brazil")
    st.write("- Focused on digital tools and parametric design techniques to enhance architectural workflows.")
    st.write('\n')
    st.write("### Bachelor in Electrical Engineering")
    st.write("**Faculdade de Engenharia de São Paulo (FESP)**")
    st.write("2013 – 2016 | São Paulo, Brazil")
    st.write("- Comprehensive study in electrical engineering principles, with a focus on practical applications in various sectors.")
    st.write('\n')
    st.write("### Technologist in Electrical Systems")
    st.write("**Instituto Federal de São Paulo (IFSP)**")
    st.write("2010 – 2012 | São Paulo, Brazil")
    st.write("- Emphasis on the development and maintenance of electrical systems.")
    st.write('\n')
    st.write("### Technician in Civil Construction")
    st.write("**Instituto Federal de São Paulo (IFSP)**")
    st.write("2005 – 2007 | São Paulo, Brazil")
    st.write("- Gained foundational knowledge in civil construction, preparing for further specialization in engineering.")

# --- BACKGROUND STYLE ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
        position: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
