import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Projects",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Projects ---
st.header("📂 Projects")
st.markdown("## Current Projects")
st.divider()

# --- Scoping Review of Swimming Performance Analysis ---
st.markdown("### 🏊‍♂️ Scoping Review of Swimming Performance Analysis")
st.markdown("##### March 2026 - Present")
st.write("This project is a scoping review of the literature on swimming performance analysis, with a focus on the use of technology and data analysis techniques. The aim is to provide a comprehensive overview of the current state of the field and identify gaps in the literature for future research.")

st.divider()

# Pacing Patterns in Elite Level Swimming
st.markdown("### 🏊‍♂️ Pacing Patterns in Elite Level Swimming")
st.markdown("##### January 2026 - Present")
st.write("This project examines the pacing strategies employed by elite swimmers during competition, focusing on how athletes manage their energy expenditure and maintain performance throughout different segments of a race.")
st.markdown("### 3 main steps:")
st.markdown("##### 1. Data Collection & Preparation")
pacing_1 = [
    "Data collected from elite swimming competitions; this was done by scraping the official results (World Aquatics Database) and extracting race information.",
    "Data was cleaned and prepared for analysis using Python (Pandas).",
    "Race data was categorized (stroke, distance, and gender) and then normalized based on z-scores.",
    "Normalized data was clustered using k-means clustering to identify distinct pacing patterns.",
    "Descriptive statistics were generated to summarize the characteristics of each pacing pattern.",
    "Fisher Information and Random Forest Feature Importance were used to identify the most distictive feature between all pacing profiles."
]
st.markdown("\n".join([f"- {skill}" for skill in pacing_1]))
st.write(" ")
st.markdown("##### 2. Write up and results have not been finalized yet, but the project is ongoing and will be updated as new findings emerge.")

st.divider()

# Ripple Race analysis Program
st.markdown("### 🏊‍♂️ Ripple Race analysis Program")
st.markdown("##### July 2025 - Present")
st.write("This program is a custom software solution designed to analyze race video footage in swimming competitions.")
st.markdown("#### Current Features:")
ripple_1 = [
    "Uses FFMPEG, PySide6, and SQLite to manage video, UI, and flat data",
    "PDF reports can be made for Qualitative and Quantitative analysis of a race",
    "Collected race data can be exported for additional statistical testing",
    "Analysis can be done for both long course (50m) and short course (25m) swimming",
    "Videos can be trimmed within the program to cut down on file sizes",
    "Races data can be validated from internally derived validation files",
    "Performance metrics can be changed to suit the needs of the user, and new metrics can be added (via one line of code)", 
    "Supports a few cloud APIs for file synchronization and sharing (Google Drive, Dropbox, OneDrive)",
    "Supports multiple users (with varying permission levels) can use the program on the same database, and all data is stored using SQLite",
    "Includes team and athlete management features, allowing for easy organization of data and analysis",
]

st.markdown("\n".join([f"- {skill}" for skill in ripple_1]))
st.write(" ")
st.markdown("#### Future Features:")
ripple_2 = [
    "Move to Polars for faster data processing and analysis (currently using Pandas)",
    "Add additional support for cloud APIs (e.g., AWS S3, Box, etc.)",
    "API support for in-house cloud storage solutions (e.g., Nextcloud, ownCloud, etc.)",
    "Enhanced security features (e.g., two-factor authentication, encryption, etc.)",
    "Automated stroke detection and analysis using computer vision and machine learning",
]
st.markdown("\n".join([f"- {skill}" for skill in ripple_2]))
st.write(" ")

# --- Review Assistant Program ---
st.markdown("### 📝 Review Assistant Program")
st.markdown("##### April 2026 - Present")
st.write("This program is a custom software solution designed to assist with the review of your own notes. The goal is to help researchers and students quickly analyze and summarize their notes on academic papers, making it easier to identify key points and findings.")
st.markdown("### Features:")
review_1 = [
    "Has a tablular view of all notes, with the ability to seach and filter content based on column values or global keywords",
    "Dynamically handles column specific widgets based on the data type of the column (e.g., text, number, date, etc.)",
    "Notes can be exported to CSV or Excel for further analysis or sharing",
    "Individual rows can be selected and synthesized into a summary using Googles Gwen model (or other LLMs) to generate a summary of the selected notes or a specific column of the selected notes (e.g. finding similarities in the 'Population' columns)",
    "Supports richtext formatting, Markdown syntax, and spell check for better note-taking",
]
st.markdown("\n".join([f"- {skill}" for skill in review_1]))
st.markdown("#### Status: **Incomplete**")
st.write("The program is still in development, and the current version is a prototype. The goal is to add more features and improve the user experience in future versions. As such, it is not yet available for public use, but I am happy to share the code with anyone who is interested in testing it out and providing feedback.")

st.divider()
# COMPLETED PROJECTS
st.markdown("## Completed Projects")
st.divider()

# --- TAP (Teaching Analysis Program) ---
st.markdown("### 🧑‍🏫 Teaching Analysis Program (TAP)")
st.markdown("##### March 2026 ")
st.write("This program is a custom software solution designed to analyze teaching video footage in physical education and coaching sessions. The goal is to help educators and coaches quickly analyze their teaching sessions and understand the effectiveness of their teaching methods.")
st.markdown("### Features:")
TAP_1 = [
    "**Lesson & subject timers** — A top-level lesson timer runs alongside a per-subject timer. Starting or stopping the lesson timer automatically starts or stops the active subject timer. Switching to a different subject hands the timer off seamlessly.",
    "**Subject navigator** — A collapsible panel lists all subjects in the current lesson. Subjects can be reordered by drag-and-drop, renamed inline, and deleted via right-click.",
    "**Markdown note editor** — Each subject has a rich plain-text editor with live Markdown syntax highlighting, bracket auto-pairing, and spell-check.",
    "**Session types** — Every subject can be tagged with a session type (Lecture, Exercise, Demo, etc.) which is used in the breakdown charts.",
    """**Lesson breakdown charts** — On export, two charts are generated automatically:
        - *Pie chart* — time distribution across subjects (switches to a legend for 5+ subjects).
        - *Bar chart* — total minutes per session type, with each bar a distinct colour.""",
    "**Multiple export formats** — HTML, PDF (via wkhtmltopdf), DOCX (via python-docx), and Markdown. All formats include the breakdown charts in a dedicated section at the start of the document.",
    "**Persistent save/load** — Lessons are stored as .json files, preserving all subject titles, content, session types, and elapsed times.",
    "**Configurable hotkeys** — Key bindings are defined in config.json and can be changed without editing source code.",
]
st.markdown("\n".join([f"- {skill}" for skill in TAP_1]))
st.write(" ")
st.link_button(
    "Download TAP on GitHub",
    "https://github.com/yourusername/tap"
    )
st.divider()

# --- Performance Analysis of Swimming Relays ---
st.markdown("### 🏊‍♂️ From Strokes to Seconds: Principal Components and Predictive Factors of the Men's 4 x 100m Freestyle Relay")
st.markdown("##### May - September 2025")
st.write("""
This M.Sc. research project focused on identifying key performance indicators (KPIs) for the men's 4 x 100m freestyle relay, using principal component analysis (PCA) and stepwise regression to build prediction models for total leg time. Athletes were split into "Starters" (standard dive) and "Non-Starters" (relay takeover) to account for differing start mechanics, enabling targeted, evidence-based training benchmarks for each role.""")
st.markdown("### 3 Main Steps")
st.markdown("#### 1. Data Collection & Preparation")
SW_Relay_1 = [
    "80 elite athletes analysed across 20 relay finals (2023 Worlds, 2024 Olympics, 2025 Worlds) using bespoke video analysis software (NEMO).",
    "12 race variables extracted per swimmer (e.g. stroke rate, distance per stroke, breakout times, turn metrics) via calibrated lane-rope landmarks.",
    "Athletes split into 'Starters' and 'Non-Starters' groups to account for differences between standard starts and relay takeovers.",
    "Intra-analyst reliability assessed via repeated video analysis, averaging 0.55% error across all variables.",
    "Statistical procedures implemented using Python (Pandas, NumPy, SciPy, Scikit-learn).",
]
st.markdown("\n".join([f"- {skill}" for skill in SW_Relay_1]))
st.write(" ")
st.markdown("#### 2. PCA & Stepwise Regression Modelling")
SW_Relay_2 = [
    "Correlation matrix, KMO, and Bartlett's test of sphericity used to assess suitability of the dataset for PCA.",
    "PCA with varimax rotation applied to reduce 12 race variables into 4–5 uncorrelated principal components per group.",
    "Variables with the strongest component loadings carried forward into stepwise multiple linear regression.",
    "Separate regression equations derived for each role: FSS and Rotate (Starters); FSS and Start15 (Non-Starters).",
    "Model stability assessed via k-fold cross-validation; accuracy evaluated using Bland-Altman plots and out-of-sample testing.",
]
st.markdown("\n".join([f"- {skill}" for skill in SW_Relay_2]))
st.write(" ")
st.markdown("#### 3. Insights & Recommendations")
SW_Relay_3 = [
    "Free swimming speed (FSS) emerged as a universal predictor of leg time across both starting roles.",
    "Acyclic-phase metrics (Rotate for Starters, Start15 for Non-Starters) added further predictive value, highlighting the importance of turn and start execution.",
    "Smallest worthwhile change (SWC) calculated to translate KPI improvements into practically meaningful time gains for coaches.",
    "Models recommended as training-support tools rather than definitive competition predictors, given out-of-sample error margins comparable to the SWC.",
]
st.markdown("\n".join([f"- {skill}" for skill in SW_Relay_3]))
st.write(" ")

with open("assets/Performance_prediction_mens_4x100mFR.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Dissertation",
        data=file,
        file_name="Performance_Prediction_Dissertation.pdf",
        mime="application/pdf"
    )
st.divider()

# --- Performance Analysis of Track Cycling ---
st.markdown("### 🚴‍♂️ Exacting Trends and Selecting Kit within Elite Male and Female Track Cyclists in the Team Sprint Event")
st.markdown("##### February - March 2025")
st.write("""
This case study focused on performance modeling for the men’s team sprint squad in elite track cycling, using regression techniques to quantify the effect of kit configurations on performance. The aim was to evaluate how changes in gear selection and cadence influence individual rider splits, enabling evidence-based kit selection.""")
st.markdown("### 3 Main Steps")
st.markdown("#### 1. Data Preparation & Descriptive Statistics")
PA_Cycling_1 = [
    "Medium-large dataset was pivoted and assessed for errors (17,000 x 24 -> 4000 x 44).", 
    "Dataset manipulation and filtering to prepare data for further statistical analysis",
    "Descrisptive statistics and ANOVA were used to compare kit configurations based on athlete position and distance.",
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
with open("assets/Exacting_Trends_and_Selecting_Kit within_Elite_Male_and_Female_Track_Cyclists.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My Case Study",
        data=file,
        file_name="Exacting_Trends_and_Selecting_Kit within_Elite_Male_and_Female_Track_Cyclists.pdf",
        mime="application/pdf"
    )
st.divider()
st.markdown("### 🚴‍♂️ What is the Optimal Starting Technique in Track Cycling?")
st.markdown("##### March - August 2025")
st.write("""
This project, also in collaboration with GB Track Cycling, explores optimal starting techniques using crank data and 2D marker tracking to identify key performance determinants.
The aim is to offer evidence-based recommendations for athletes and coaches in order to improve start performance. The results and details of this research are currently under a non-disclosure agreement and are not available for public viewing.
""")

st.divider()

# --- Database Validation ---
st.markdown("### 📊 Database Validation")
st.markdown("##### February 2025")
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

with open("assets/Database_Validation_Example.pdf", "rb") as file:
    st.download_button(
        label="📄 Download Aquatics Project Summary",
        data=file,
        file_name="Database_Validation_Example.pdf",
        mime="application/pdf"
    )
st.divider()

# ---- Longitudinal Analysis of KO Rates in Amateur Boxing ---
st.markdown("### 🥊 Longitudinal Analysis of KO Rates in Amateur Boxing")
st.markdown("##### November - January 2024")
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

with open("assets/Longitudinal_boxing_KO_Analysis.pbix", "rb") as file:
    st.download_button(
        label="📄 Download Boxing Project",
        data=file,
        file_name="Longitudinal_boxing_KO_Analysis.pbix",
        mime="application/octet-stream"
    )

st.divider()