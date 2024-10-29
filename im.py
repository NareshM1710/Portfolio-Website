import streamlit as st
from PIL import Image
import time
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Page Configuration
st.set_page_config(
    page_title="Naresh M - Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
local_css("style.css")

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
lottie_data = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_8npirptd.json")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=["About Me", "Experience", "Projects", "Contact"],
    icons=["person", "briefcase", "laptop", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#0083B8", "font-size": "20px"},
        "nav-link": {
            "font-size": "20px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#e0f7fa",
            "color": "black",
        },
        "nav-link-selected": {"background-color": "#0083B8", "color": "white"},
    }
)

# About Me Section
if selected == "About Me":
    st.markdown("<h1 style='text-align: center;'>Hello, I'm Naresh 👋</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Data Storyteller | Analytics Expert | Problem Solver
        I'm a passionate Data Analyst with 3 years of experience transforming complex data into actionable insights. 
        My journey in data analytics has been driven by curiosity and a desire to solve real-world problems through data.

        ### What I Do
        - 📊 Transform raw data into compelling stories
        - 💡 Develop interactive dashboards and reports
        - 🔍 Uncover patterns and trends in complex datasets
        - 📈 Drive business decisions through data-driven insights
        
        ### My Toolbox
        - **Data Analysis**: Power BI, Excel, SQL
        - **Visualization**: Advanced Charts, Custom Visuals
        - **Database**: MySQL, PostgreSQL
        - **Other Skills**: Python, ETL
        """)
    with col2:
        st_lottie(lottie_data, height=300, key="coding")

# Experience Section
elif selected == "Experience":
    st.markdown("<h1 style='text-align: center;'>Professional Journey</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        ### Data Analyst | Mitsogo
        - Implemented data validation processes, achieving a 95% accuracy rate.
        - Created dashboards from CRM data, delivering insights for sales and marketing.
        - Automated workflows using VBA Macros.
        """)
        st.success("""
        ### Data Processing Analyst | Nielsen IQ
        - Led key projects and maintained 90-95% data accuracy.
        - Collaborated with cross-functional teams and trained teams.
        - Automated tasks with Python, increasing efficiency by 95%.
        """)
    with col2:
        st.warning("""
        ### Skills & Expertise
        - **Technical Skills**: Power BI, SQL, Python, Advanced Excel, DAX
        - **Business Skills**: Data Storytelling, Problem Solving, Team Leadership
        """)

# Projects Section with Continuous Loop in Timed Slider
elif selected == "Projects":
    st.markdown("<h1 style='text-align: center;'>Featured Projects</h1>", unsafe_allow_html=True)
    
    # Power BI Projects Section with Continuous Timed Slider
    st.subheader("Power BI Dashboards")
    powerbi_projects = [
        {"title": "Airline Loyalty Program", "description": "Interactive dashboard tracking loyalty program", "image": "Airline Loyalty Program.jpg"},
        {"title": "Toy Store KPI Report", "description": "Tracks marketing ROI and KPI", "image": "Maven Toy Dashboard.jpg"},
        {"title": "Survey Dashboard", "description": "Analyzes demographics and Survey on Data Professional Jobs", "image": "Survey Dashboard.jpg"},
        {"title": "Uber Analytics Dashboard", "description": "Analyzes Rides Durations and Other KPI", "image": "Uber Analytics.jpg"},
        {"title": "Plant Co. Performance Dashboard", "description": "Analyzes Performance of Plant Co.", "image": "Plant Co. Dashboard.jpg"},
    ]
    
    slide_placeholder = st.empty()
    
    # Infinite loop for Power BI projects
    while True:
        for project in powerbi_projects:
            with slide_placeholder.container():
                st.markdown(f"### {project['title']}")
                st.write(project['description'])
                st.image(project['image'], use_column_width=True)
                time.sleep(3)  # Set delay for each slide
            slide_placeholder.empty()

# Excel Projects Section with Continuous Timed Slider
    st.subheader("Excel Projects")
    excel_projects = [
        {"title": "Excel Dashboard", "description": "Call Center Dashboard", "image": "Excel Dashboard.jpg"},
        {"title": "Excel Power Pivot", "description": "Power Pivot and Power Query Project", "image": "Excel PowerPivot.jpg"},
    ]
    
    slide_placeholder_excel = st.empty()
    
    # Infinite loop for Excel projects
    while True:
        for project in excel_projects:
            with slide_placeholder_excel.container():
                st.markdown(f"### {project['title']}")
                st.write(project['description'])
                st.image(project['image'], use_column_width=True)
                time.sleep(3)  # Set delay for each slide
            slide_placeholder_excel.empty()


# Contact Section
elif selected == "Contact":
    st.markdown("<h1 style='text-align: center;'>Let's Connect!</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Get in Touch
        - **LinkedIn**: [LinkedIn](http://www.linkedin.com/in/naresh-m-90796a141)
        - **GitHub**: [GitHub](your_github_url)
        - **Email**: 📧 nareshdharun17@gmail.com
        """)
    with col2:
        st_lottie(lottie_coding, height=300, key="contact")
        with open("Naresh_M_Resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download Resume", data=PDFbyte, file_name="Naresh_M_Resume.pdf", mime='application/octet-stream')

# Add custom CSS for styling
st.markdown("""
<style>
.main {background-color: #f0f2f6; padding: 2rem;}
h1 {color: #0083B8; font-family: 'Helvetica Neue', sans-serif;}
.stButton>button {background-color: #0083B8; color: white;}
.stButton>button:hover {background-color: #006491;}
img {border-radius: 10px;}
</style>
""", unsafe_allow_html=True)
