# Projects Section
if selected == "Projects":
    st.markdown("<h1 style='text-align: center;'>Featured Projects</h1>", unsafe_allow_html=True)

    # Power BI Projects Section
    st.subheader("Power BI Dashboards")
    powerbi_projects = [
        {"title": "Airline Loyalty Program", "description": "Interactive dashboard tracking loyalty program", "image": "Airline Loyalty Program.jpg", "url": "https://example.com/airline"},
        {"title": "Toy Store KPI Report", "description": "Tracks marketing ROI and KPI", "image": "Maven Toy Dashboard.jpg", "url": "https://example.com/toy-store"},
        {"title": "Survey Dashboard", "description": "Analyzes demographics and Survey on Data Professional Jobs", "image": "Survey Dashboard.jpg", "url": "https://example.com/survey"},
        {"title": "Uber Analytics Dashboard", "description": "Analyzes Rides Durations and Other KPI", "image": "Uber Analytics.jpg", "url": "https://example.com/uber"},
        {"title": "Plant Co. Performance Dashboard", "description": "Analyzes Performance of Plant Co.", "image": "Plant Co. Dashboard.jpg", "url": "https://example.com/plant-co"},
    ]

    # Auto Slide for Power BI Projects
    powerbi_index = 0
    powerbi_slider_placeholder = st.empty()

    while True:
        with powerbi_slider_placeholder.container():
            st.markdown(f"### {powerbi_projects[powerbi_index]['title']}")
            st.write(powerbi_projects[powerbi_index]['description'])
            # Make image clickable with a link
            st.markdown(
                f"<a href='{powerbi_projects[powerbi_index]['url']}' target='_blank'><img src='{powerbi_projects[powerbi_index]['image']}' style='width: 100%; border-radius: 10px;'/></a>",
                unsafe_allow_html=True
            )
            time.sleep(3)  # Automatic slide change every 3 seconds
        powerbi_index = (powerbi_index + 1) % len(powerbi_projects)

    # Separator
    st.markdown("---")

    # Excel Projects Section
    st.subheader("Excel Projects")
    excel_projects = [
        {"title": "Excel Dashboard", "description": "Call Center Dashboard", "image": "Excel Dashboard.jpg", "url": "https://example.com/excel-dashboard"},
        {"title": "Excel Power Pivot", "description": "Power Pivot and Power Query Project", "image": "Excel PowerPivot.jpg", "url": "https://example.com/power-pivot"},
    ]

    # Auto Slide for Excel Projects
    excel_index = 0
    excel_slider_placeholder = st.empty()

    while True:
        with excel_slider_placeholder.container():
            st.markdown(f"### {excel_projects[excel_index]['title']}")
            st.write(excel_projects[excel_index]['description'])
            # Make image clickable with a link
            st.markdown(
                f"<a href='{excel_projects[excel_index]['url']}' target='_blank'><img src='{excel_projects[excel_index]['image']}' style='width: 100%; border-radius: 10px;'/></a>",
                unsafe_allow_html=True
            )
            time.sleep(3)  # Automatic slide change every 3 seconds
        excel_index = (excel_index + 1) % len(excel_projects)

# CSS for positioning and styling the buttons
st.markdown("""
<style>
    .stButton > button {
        background-color: #0083B8;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-size: 18px;
    }
    .stButton > button:hover {
        background-color: #006491;
    }
    .left-button { position: absolute; left: 10px; }
    .right-button { position: absolute; right: 10px; }
</style>
""", unsafe_allow_html=True)
