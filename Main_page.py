import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Portfolio",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

## Main Page title
st.image("assets/headshot.JPEG", width=200)
st.title("Welcome to My Portfolio")
# --- Projects ---
st.markdown("### About Me")
st.write("""
        Welcome to my portfolio! I am a sports data analyst with a passion for machine learning and sports performance. 
        I have a strong background in sport and exercise science, having completed my BA at Vancouver Island University and my master's degree in Sports Performance Analytics at the University of Chester. 
        Currently, I am pursuing a PhD in Data Analysis in Sport at Heriot-Watt University, where I am focusing on the application of machine learning techniques to swimming data.
        Recently, I have been working as a performance analyst for AquaticsGB on an ad hoc basis, where I have been involved in notational analysis of swimming competitions and developing custom data management and visualization programs.
        In my own time, I enjoy resistance training, golfing, eating good food, and spending time with my family and friends.
         """)
st.write("")
st.write("")

st.markdown("### Interests")
st.write("Recently, I have been focusing on a few key areas of interest: coding, data analysis, and statistics. "
         "The majority of my coding has been done in Python, but I am also building my skills in R and SQL. "
         "I have been using Python for data analysis and visualization, and I am currently working on a few projects that involve custom solutions for data collection, management, and visualization. "
         "Data visualization programs such as Power BI and Tableau have also been helpful to me as I expand my skills in this area. "
         "I am excited to continue learning and growing in these areas, and I look forward to sharing my projects with you!")