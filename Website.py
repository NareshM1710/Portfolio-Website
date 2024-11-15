import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu
from streamlit_card import card
from streamlit_carousel import carousel
import requests
from streamlit_lottie import st_lottie
import time

# Page Configuration
st.set_page_config(
    page_title="Naresh M - Data Analyst Portfolio",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for styling
def local_css(file_name):
    with open(file_name, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
local_css("im.css")

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
    options=["About Me", "Experience", "Projects",  "Certifications", "Contact"],
    icons=["person", "briefcase", "laptop", "briefcase", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#010324", "font-size": "20px"},
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
        - **Data Analysis**: Power BI, Excel, SQL, Looker Studio
        - **Visualization**: Advanced Charts, Custom Visuals
        - **Database**: MySQL, SQL
        - **Other Skills**: Python, ETL, GA4
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
        - Looker Studio
        - Google Analytics
        

        #### Business Skills
        - Data Storytelling
        - Problem Solving
        - Team Leadership
        - Project Management
        - Team Collaboration
        """)

# Projects Section
elif selected == "Projects":
    st.subheader("Power BI Dashboards")

    powerbi_projects = [
        {"title": "Airline Loyalty Program", "description": "Interactive dashboard tracking loyalty program", "img": "Airline Loyalty Program.jpg"},
        {"title": "Toy Store KPI Report", "description": "Tracks marketing ROI and KPI", "img": "Maven Toy Dashboard.jpg"},
        {"title": "Survey Dashboard", "description": "Analyzes demographics and Survey on Data Professional Jobs", "img": "Survey Dashboard.jpg"},
        {"title": "Uber Analytics Dashboard", "description": "Analyzes Rides Durations and Other KPI", "img": "Uber Analytics.jpg"},
        {"title": "Plant Co. Performance Dashboard", "description": "Analyzes Performance of Plant Co.", "img": "Plant Co. Dashboard.jpg"},
    ]

    powerbi_carousel_data = []
    for project in powerbi_projects:
        powerbi_carousel_data.append({
            "img": project["img"],
            "title": project["title"],
            "text": f"### {project['title']}\n{project['description']}"
        })

    carousel(
        items=powerbi_carousel_data,
        interval=4000,  # Interval between slides (5 seconds)
    )

    st.markdown("---")

    st.subheader("Excel Dashboards")

    excel_projects = [
        {"title": "Excel Dashboard", "description": "Call Center Dashboard", "img": "Excel Dashboard.jpg"},
        {"title": "Excel Power Pivot", "description": "Power Pivot and Power Query Project", "img": "Excel PowerPivot.jpg"},
    ]

    excel_carousel_data = []
    for project in excel_projects:
        excel_carousel_data.append({
            "title": project["title"],
            "img": project["img"],
            "text": f"### {project['title']}\n{project['description']}"
        })

    carousel(
        items=excel_carousel_data,
        interval=4000,  # Interval between slides (5 seconds)
    )
    
    st.markdown("---")

    st.subheader("SQL Projects")

    sql_projects = [
        {"title": "EDA Data Analysis", "github": "https://github.com/NareshM1710/Sales-EDA-SQL"},
       
    ]

    for project in sql_projects:
        st.markdown(f"**[ {project['title']} ]** - [GitHub Link]({project['github']})")

# Certifications Section
elif selected == "Certifications":
    st.markdown("<h1 style='text-align: center;'>Certifications</h1>", unsafe_allow_html=True)

    certifications = [
        {"title": "Power BI Desktop - Maven Analytics", "link": ""},
        {"title": "Advanced Power BI Desktop (DAX) - LinkedIn", "link": ""},
        {"title": "SQL for Data Analysis - LinkedIn ", "link": ""},
        {"title": "Google Analytics 4 - Google", "link": ""},
    ]

    for cert in certifications:
        st.markdown(f"**[ {cert['title']} ]** - [View Certification]({cert['link']})")

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


# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-family: Comic Sans MS, sans-serif; font-size: 1.2em; color: #0083B8;'>2024 Naresh M. All Rights Reserved.</p>", unsafe_allow_html=True)
