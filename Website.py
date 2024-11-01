import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu
from streamlit_card import card
from streamlit_carousel import carousel
import requests
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
        ### Data Analytics | Visualization  | Manipulation
        
       Data Analyst with 2.8+ years of experience in data validation, analysis, and visualization, with a strong focus on 
       automation to streamline repetitive tasks. Proficient in Excel and skilled in transforming complex data into actionable 
       insights to support business decisions. Experienced in data collection, market research, and marketing analytics. Open 
       to new opportunities and passionate about optimizing processes through data-driven solutions. 

        ### What I Do
        - 📊 Transform raw data into compelling stories
        - 💡 Develop interactive dashboards and reports
        - 🔍 Uncover patterns and trends in complex datasets
        - 📈 Drive business decisions through data-driven insights
        
        ### My Toolbox
        - **Skills**: Power BI, DAX, Excel, SQL, Python, MS Power Automate, MS Suite, HubSpot, Zendesk.
        - **Domain Knowledge**:  FMCG, Marketing Analytics  
        - **Core Competencies**: Data Analysis & Validation, Data Visualization, Automation & Process Optimization, 
                                 Market Research & Reporting, Cross-Functional Collaboration.
        - **Other Skills**: Automation , ETL
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
        #### Jul-2023 - Present
        - Implemented data validation processes resulting in a 95% proficiency rate, ensuring accurate analytics on lead conversion rates.
        - Designed and created dashboards from HubSpot CRM and Zendesk ticket data, delivering insights to the SEM and sales teams to enhance ad performance.
        - Provided daily analytics reports to the CMO, showcasing key metrics and actionable insights for informed decision-making.
        - Utilized Power Query (DAX) and Excel for advanced data visualization, creating visually appealing dashboards that facilitate data interpretation.
        - Optimized processes and presented insights through data visualization, contributing to improved ad campaigns and lead conversion rates.
        - Automated tasks using Excel VBA Macros, streamlining workflows, and enhancing accuracy in data processing.

        """)
        
        st.success("""
        ### Data Processing Analyst | Nielsen IQ
        #### Feb-2022 - Jul-2023
        - Led key projects, trained teams to enhance competency, excelled as an OGRDS Specialist in MS Excel reporting, and standardized local retail codes to global standards.
        - Achieved 90-95% accuracy in data management, earning awards from major clients and driving successful platform transitions for team success.
        - Achieved highest accuracy in day-to-day operations, earning recognition as a top coder.
        - Proficient in data collection, cleaning, analysis, and visualization using Python, Pandas, MySQL, and VBA macros.
        - Conducted market research, delivered sales forecasts, and prepared daily, weekly, and monthly MIS reports for clients. 
        - Developed and implemented processes in Python, optimizing data processing efficiency by 95%.
        - Demonstrated automation skills with Python, automating tasks, GIC mapping, and developing text classifiers, PLU tools, and Web Automation bots.

        """)
    
    with col2:
        st.warning("""
        ### Skills & Expertise
        
        #### Technical Skills
        - Power BI
        - SQL
        - Python
        - Advanced Excel
        - Power Query 
        - Power Pivot
        - DAX
        
        #### Business Skills
        - Data Storytelling
        - Problem Solving
        - Team Leadership
        - Project Management
        - Team Collaboration 
        """)

# Projects Section
if selected == "Projects":
    st.markdown("<h1 style='text-align: center;'>Featured Projects</h1>", unsafe_allow_html=True)
    
    # Power BI Projects Section
    st.subheader("Power BI Dashboards")
    powerbi_projects = [
        {"title": "Airline Loyalty Program", "description": "Interactive dashboard tracking loyalty program", "image": "Airline Loyalty Program.jpg"},
        {"title": "Toy Store KPI Report", "description": "Tracks marketing ROI and KPI", "image": "Maven Toy Dashboard.jpg"},
        {"title": "Survey Dashboard", "description": "Analyzes demographics and Survey on Data Professional Jobs", "image": "Survey Dashboard.jpg"},
        {"title": "Uber Analytics Dashboard", "description": "Analyzes Rides Durations and Other KPI", "image": "Uber Analytics.jpg"},
        {"title": "Plant Co. Performance Dashboard", "description": "Analyzes Performance of Plant Co.", "image": "Plant Co. Dashboard.jpg"},
    ]
    
    # Power BI Slider with forward and backward buttons
    powerbi_index = 0
    powerbi_slider_placeholder = st.empty()
    
    # Navigation for Power BI projects
    if st.button("◀ Previous Power BI Project"):
        powerbi_index = (powerbi_index - 1) % len(powerbi_projects)
    if st.button("▶ Next Power BI Project"):
        powerbi_index = (powerbi_index + 1) % len(powerbi_projects)

    # Display selected Power BI project
    with powerbi_slider_placeholder.container():
        st.markdown(f"### {powerbi_projects[powerbi_index]['title']}")
        st.write(powerbi_projects[powerbi_index]['description'])
        st.image(powerbi_projects[powerbi_index]['image'], use_column_width=True)
    
    # Separator between sections
    st.markdown("---")
    
    # Excel Projects Section
    st.subheader("Excel Projects")
    excel_projects = [
        {"title": "Excel Dashboard", "description": "Call Center Dashboard", "image": "Excel Dashboard.jpg"},
        {"title": "Excel Power Pivot", "description": "Power Pivot and Power Query Project", "image": "Excel PowerPivot.jpg"},
    ]
    
    # Excel Slider with forward and backward buttons
    excel_index = 0
    excel_slider_placeholder = st.empty()
    
    # Navigation for Excel projects
    if st.button("◀ Previous Excel Projec"):
        excel_index = (excel_index - 1) % len(excel_projects)
    if st.button("▶ Next Excel Project"):
        excel_index = (excel_index + 1) % len(excel_projects)

    # Display selected Excel project
    with excel_slider_placeholder.container():
        st.markdown(f"### {excel_projects[excel_index]['title']}")
        st.write(excel_projects[excel_index]['description'])
        st.image(excel_projects[excel_index]['image'], use_column_width=True)

# Contact Section
elif selected == "Contact":
    st.markdown("<h1 style='text-align: center;'>Let's Connect!</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Get in Touch
        I'm always interested in hearing about new opportunities and collaborations.
        
        ### Connect with me on:
        - [LinkedIn](https://www.linkedin.com/in/naresh-m-90796a141/)
        - [GitHub](https://github.com/NareshM1710)
        
        ### Email
        📧  nareshdharun17@gmail.com
        """)
        
    with col2:
        st_lottie(lottie_coding, height=300, key="contact")
        
        with open("Naresh_M_Resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        
        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="Naresh_M_Resume.pdf",
            mime='application/octet-stream'
        )

# Add custom CSS for styling
st.markdown("""
<style>
/* Main page styling */
.main {
    background-color: #f0f2f6;
    padding: 2rem;
}
h1 {
    color: #0083B8;
    font-family: 'Helvetica Neue', sans-serif;
}
.stButton>button {
    background-color: #0083B8;
    color: white;
}
.stButton>button:hover {
    background-color: #006491;
}
img {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
