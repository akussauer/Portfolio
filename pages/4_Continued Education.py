import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Continued Education",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)
# --- Continued Education ---
st.header("Continued Education")
st.divider()

st.markdown("##### National Strength & Conditioning Association - National Conference 2023")
st.write("**Location:** Las Vegas, NV, USA")
st.markdown("**Date:** July 12–15, 2023")

NSCA_2023_content = {
    "What Do We Know About Menstrual Cycle Effects on Strength & Conditioning Training in Women?": "Kathryn Ackerman, MD, MPH, FACSM",
    "Fueling and Training Considerations for the Postpartum Athlete": "Michelle Arent, MPH, CSCS and Melanie Sulaver, MS, RD, CDN, CISSN",
    "Implementing Eccentric Training: Applications for Improving Hypertrophy, Strength, and Power": "Tim Suchomel, PhD, CSCS,*D, RSCC, USAW-I",
    "Speed and Agility Training for Athletes": "Unknown Speaker",
    "Implementing Eccentric Training: Applications for Improving Hypertrophy, Strength, and Power – Bridge the Gap – Practical": "Tim Suchomel, PhD, CSCS,*D, RSCC, USAW-I",
    "STRENGTH: The Foundation of Performance": "Paul Comfort, PhD, CSCS*D, ASCC",
    "Transfer of Training: Elite Athletes": "William A. Sands, PhD, FACSM",
    "Dancers as Athletes: Recommendations for Enhancing Competitive Performance": "Josh Wludyga, DSc, CSCS*D",
    "REDS: What the What and What Do I Need to Know": "Jana Heitmeyer, MEd, RD, CSSD, LD, CSCS, SCCC",
    "Explosive Power Training: Moving Forward": "James C. Radcliffe, MS",
    "Controlling Chaos? – Implications of Managing Athlete Health and Performance": "Andrea Hudy, MA, MBA, CSCS*D, RSCC*E"
}

for title, speaker in NSCA_2023_content.items():
    st.markdown(f"**{title}**  \n{speaker}")

st.write(" ")
st.write(" ")

st.markdown("##### British Columbia Prosthetics & Orthotics Association - Annual Conference 2019")
st.write("**Location:** Kelowna, BC, Canada")
st.markdown("**Date:** September 26–28, 2019")
st.write(" ")

