import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Portfolio",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded",
)

## Main Page title
st.image("Portfolio/assets/headshot.JPEG", width=200)
st.title("Welcome to My Portfolio")
# --- Projects ---
st.markdown("### About Me")
st.write("""
        Welcome to my portfolio! I am a sports performance analyst with a passion for data analysis and sports performance. 
        I have a strong background in kinesiology, having completed my BA at Vancouver Island University, and have pursued various certifications in strength and conditioning, sports nutrition, and coaching.
        I am currently pursuing a Master's degree in Sports Performance Analytics at the University of Chester, where I am further honing my skills in data analysis and visualization. 
        Recently, I have been working as a performance analyst for AquaticsGB, where I have been involved in notational analysis of swimming competitions and developing custom data management and visualization programs.
        In my own time, I enjoy resistance training, eating good food, and spending time with my family and friends.
         """)
st.write("")
st.write("")

st.markdown("### Interests")
st.write("Recently, I have been focusing on a few key areas of interest: coding, data analysis, and statistics. "
         "The majority of my coding has been done in Python, but I am also learning R and SQL. "
         "I have been using Python for data analysis and visualization, and I am currently working on a few projects that involve scraping data from websites and analyzing it using Python libraries such as Pandas and Matplotlib. "
         "Data visualization programs such as Power BI and Tableau have also been helpful to me as I expand my skills in this area. "
         "At the moment, I am working on my Master's thesis, which involves statistical techniques such as principal component analysis and regression analysis. "
         "I've been using Python for the majority of this project, but I have also been using R for some of the statistical analysis. "
         "I am excited to continue learning and growing in these areas, and I look forward to sharing my projects with you!")