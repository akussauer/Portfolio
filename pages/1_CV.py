import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - CV",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("📄 Curriculum Vitae")
st.markdown("#### Alex Kussauer")

# --- Skills and Abilities ---
st.header("🛠️ Skills and Abilities")
skills = [
    "Experienced in working in teams and with the public",
    "Knowledgeable in the field of sports performance analysis",
    "Skilled in data analysis and interpretation",
    "Familiar with procedures and workflow of large teams and organizations",  # Changed to North American spelling for consistency
    "Good time management skills",
    "Experienced at coding in Python",
    "Skilled in Power BI and Tableau",  # Added space in "Power BI"
    "Technical skills unique to prosthetics and orthotics",
    "Trained in first aid"
]
st.markdown("\n".join([f"- {skill}" for skill in skills]))

# --- Education and Training ---
st.header("🎓 Education and Training")
edu = {
    "MSc Sports Performance Analytics (Sept 2025 - Present)": "University of Chester, Chester, England",  # Removed period after MSc
    "NSCA Certified Strength & Conditioning Specialist (June 2024)": "National Strength & Conditioning Association, Victoria, Canada",
    "Anti-Racism in Sport (Jan 2024)": "National Coaching Certification Program, Vancouver, BC",  # Fixed "Programe" typo
    "Weightlifting Competition Introduction Workshop (Nov 2023)": "National Coaching Certification Program, Vancouver, BC",
    "CPR-C and AED (2023)": "City of Nanaimo, Nanaimo, Canada",
    "National Lifeguard Certification (2022)": "City of Nanaimo, Nanaimo, Canada",
    "Indigenous Canada (Jan 2022)": "University of Alberta",
    "Sports Nutrition Coach Certification (June 2021)": "National Academy of Sports Medicine",
    "Deep Tissue Massage: Myofascial Release Certificate (Dec 2021)": "Michael Eric Everson",
    "Group Fitness Instructor Certification (Oct 2021)": "British Columbia Recreation & Parks Association",
    "BA Kinesiology (2019)": "Vancouver Island University, Nanaimo, Canada",  # Replaced colon with comma
    "Coaching Athletes with Disabilities (2018)": "National Coaching Certification Program, Nanaimo, Canada",
    "Tri-City Policy Statement: Ethical Conduct for Research Involving Humans (2017)": "Vancouver Island University, Nanaimo, Canada",  # Fixed "Reseach"
    "Fundamental Movement Skills (2015)": "National Coaching Certification Program, Nanaimo, Canada",
}
for title, org in edu.items():
    st.markdown(f"**{title}**  \n{org}")

# --- Work Experience ---
st.header("💼 Work Experience")
work_experience = {
    "Performance Analyst (Jan 2025 - Present)": "Aquatics GB, Manchester, England",
    "Skills Coach and Support Worker (Nov 2021 - Sept 2024)": "Canucks Autism Network, Nanaimo and Victoria, Canada",
    "Sports Field Maintenance & Machine Operator (2021 - 2024)": "City of Nanaimo, Nanaimo, Canada",
    "Lifeguard & Swim Instructor (2015 - 2021)": "City of Nanaimo, Nanaimo, Canada",
    "Parks Ambassador (April - July 2020)": "City of Nanaimo, Nanaimo, Canada",
    "Camp Leader III (July - August 2020)": "City of Nanaimo, Nanaimo, Canada",
    "Clinical Assistant & Technician (2019 - 2021)": "B.D. Mitchell Prosthetics & Orthotics, Nanaimo, Canada",
}
for role, location in work_experience.items():
    st.markdown(f"**{role}**  \n{location}")