import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Projects",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Projects ---
st.header("📂 Projects")
st.write("Below are some of the projects I have worked on in the past year (2024/25).")
st.divider()

st.markdown("### 🥊 Longitudinal Analysis of KO Rates in Amateur Boxing")
st.write("This project involved analyzing the KO/Non-Finish rates in amateur boxing over time, specifically looking at the impact of rule changes and how they affected KO rates across different weight classes and age groups.")

st.markdown("#### 3 main steps:")
st.markdown("##### 1. Cleaning the Dataset")
boxing_1 = [
    "Data was provided by BoxingGB but contained errors and unstandardized formats.",
    "Data was cleaned using Excel and PowerBI.",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_1]))
st.write("")

st.markdown("##### 2. Exploratory Data Analysis via PowerBI")
boxing_2 = [
    "Visuals were created to identify trends in KO/Non-Finish rates across different weight classes, genders, and age groups.",
    "The analysis was conducted using PowerBI.",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_2]))
st.write("")

st.markdown("##### 3. Supplementing the Exploratory Analysis with Additional Longitudinal Data")
boxing_3 = [
    "Longitudinal data was collected from the BoxingGB website to supplement the exploratory analysis.",
    "Data was scraped using Python and BeautifulSoup.",
    "Data was visualized in PowerBI to provide additional insights.",
]
st.markdown("\n".join([f"- {skill}" for skill in boxing_3]))
st.write(" ")

with open("Portfolio/assets/Longitudinal_boxing_KO_Analysis.pbix", "rb") as file:
    st.download_button(
        label="📄 Download Boxing Project",
        data=file,
        file_name="Longitudinal_boxing_KO_Analysis.pbix",
        mime="application/octet-stream"
    )

st.divider()

st.markdown("### 📊 Database Validation")
st.write("This project involved validating the AquaticsGB database, which consists of performance analysis data entered by various analysts over the last two decades. The goal was to ensure the accuracy and consistency of the data by cataloging and removing outliers for review. Additionally, profiling was used to track where errors occur and who has made them.")

st.markdown("#### 3 main steps:")
st.markdown("##### 1. Generating Descriptive Statistics")
DF_1 = [
    "Data provided by AquaticsGB was cleaned, and statistics were generated based on conditional race data (e.g., distance, gender, stroke, etc.).",
    "A reduced dataset (approx. 35,000 rows & 900 columns) was used to generate descriptive statistics.",
    "Descriptive statistics were generated using Python and Pandas.",
    "The program was built with a user-friendly, installable package using a custom Tkinter GUI and Inno Setup Compiler to allow non-technical staff to use it easily.",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_1]))
st.write(" ")

st.markdown("##### 2. Saving Outliers & Generating Error Reports")
DF_2 = [
    "Outliers were identified and removed based on z-scores from the descriptive statistics.",
    "Outliers were added to a separate dataset for review.",
    "Error reports were generated based on the removed outliers.",
    "The program was packaged as a user-friendly GUI using Tkinter and compiled with Inno Setup.",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_2]))
st.write(" ")

st.markdown("##### 3. Profiling of Errors")
DF_3 = [
    "Error profiling was created to identify where and by whom errors occurred.",
    "Profiling was conducted using a custom Python script, though it can also be done using PowerBI or Tableau.",
]
st.markdown("\n".join([f"- {skill}" for skill in DF_3]))
st.write(" ")

with open("Portfolio/assets/Database_Validation_Example.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Aquatics Project Summary",
        data=file,
        file_name="Database_Validation_Example.pdf",
        mime="application/pdf"
    )
st.divider()
st.markdown("### 🚴‍♂️ Exacting Trends and Selecting Kit within Elite Male and Female Track Cyclists in the Team Sprint Event")
st.write("""
This case study focused on performance modeling for the men’s team sprint squad in elite track cycling, using regression techniques to quantify the effect of kit configurations on performance. The aim was to evaluate how changes in gear selection and cadence influence individual rider splits, enabling evidence-based kit selection.""")
st.markdown("### 3 Main Steps")
st.markdown("#### 1. Data Preparation & Descriptive Statistics")
PA_Cycling_1 = [
    "Medium-large dataset was pivoted assessed for errors (17,000 x 24 -> 4000 x 44).", 
    "Dataset manipulation and filtering to prepare data for further statistical analysis",
    "Descrisptive statistics were generated for kit selection based on athlete position and distance.",
    "Statistical procedures are implemented using Python and Scikit-learn.",
]
st.markdown("\n".join([f"- {skill}" for skill in PA_Cycling_1]))
st.write(" ")
st.markdown("#### 2. Regression Modeling")
PA_Cycling_2 = [
    "Regression was performed and fit using either linear, quadratic, or logerithmic calulations.",
    "Separate models built for each lap to reflect position-specific effects (e.g., P1 vs. P2).",
    "Linear regression was used to correlate split distances with race time to inform training benchmark selection.",
    "Model performance evaluated via adjusted R² and AIC (Akaike Information Criterion).",
    "Results visualized using Seaborn and Matplotlib.",
]
st.markdown("\n".join([f"- {skill}" for skill in PA_Cycling_2]))
st.write(" ")
st.markdown("#### 3. Insights & Recommendations")
PA_Cycling_3 = [
    "Descriptive statistics indicated trends associated with specific kit combinations, varying by lap/rider.",
    "Understanding the correlational strength between split distances, especially those that represent the result of a good acceleration phase, provide practical benchmark data for training.",
    "Bespoke program build for evaluating cadence using quadratic regression and custom visuals.",
    "The project demonstrated a repeatable, data-driven process for evaluating equipment interventions in elite sport contexts.",
]
st.markdown("\n".join([f"- {skill}" for skill in PA_Cycling_3]))
st.write(" ")
with open("Portfolio/assets/Exacting_Trends_and_Selecting_Kit within_Elite_Male_and_Female_Track_Cyclists.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Case Study",
        data=file,
        file_name="Exacting_Trends_and_Selecting_Kit within_Elite_Male_and_Female_Track_Cyclists.pdf",
        mime="application/pdf"
    )
st.divider()
st.markdown("### 🚴‍♂️ What is the Optimal Starting Technique in Track Cycling?")
st.write("""
This project, also in collaboration with GB Track Cycling, explores optimal starting techniques using crank data and 2D marker tracking to identify key performance determinants.
The aim is to offer evidence-based recommendations for athletes and coaches. The results of this research are currently under a non-disclosure agreement, so results are not be included for public viewing.
""")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.markdown("## Upcoming Projects")
st.divider()

st.markdown("### 📈 Predictive Analysis of Swimming Performance")
st.write("""
This project involves using multiple regression and machine learning to predict swimming performance based on historical data. 
The goal is to predict swimmer performance in the 100m freestyle relay event based on recent meet data. 
The program is designed to be flexible and compatible with raw outputs from the AquaticsGB database, allowing it to be used for any event. 
This project is currently in development and expected to be completed by August 2025. It aims to help coaches and training staff estimate performance-related metrics and simulate theoretical races.
""")

st.markdown("#### 3 main steps:")
st.markdown("##### 1. Collecting & Analyzing Data")
prediction_1 = [
    "Data will be collected and analyzed from two international meets: the 2023 World Aquatics Championships and the 2024 Olympic Games.",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_1]))
st.write(" ")

st.markdown("##### 2. Building a Predictive Model")
prediction_2 = [
    "A predictive model will be built using Principal Component Analysis, multiple regression, and machine learning techniques.",
    "The program features a user-friendly interface and is designed to be flexible enough for various events.",
    "Statistical procedures are implemented using Python and Scikit-learn.",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_2]))
st.write(" ")

st.markdown("##### 3. Comparing Results")
prediction_3 = [
    "The model’s predictions will be validated using out-of-sample data from the 2025 World Aquatics Championships.",
]
st.markdown("\n".join([f"- {skill}" for skill in prediction_3]))
st.write(" ")

with open("Portfolio/assets/Performance_Prediction_of_the_Mens_100m_Freestyle.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Proposal",
        data=file,
        file_name="Performance_Prediction_Proposal.pdf",
        mime="application/pdf"
    )