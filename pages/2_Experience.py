import streamlit as st

st.set_page_config(
    page_title="Alex Kussauer - Experience",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Work Experience ---
st.header("💼 Work Experience")
st.write("")

st.markdown("##### Biomechanics and Data Support (ad hoc)")
st.markdown("GB Cycling: Aug 2025 - Sept 2025")
gb_cycling = [
    "Provided project support for the biomechanics team at British Cycling in Manchester, England",
    "Assisted with data collection and statistical analysis for cycling performance",
    "Analyzed Track cycling starts and performance indicators within the team sprint event"
]
st.markdown("\n".join([f"- {skill}" for skill in gb_cycling]))
st.write("")

st.markdown("##### Performance Analyst (ad hoc)")
st.markdown("AquaticsGB: Jan 2025 - Present")
aquatics_gb = [
    "Perform notational analysis of swimming competitions",
    "Develop custom programs for performance prediction and data visualization", 
]
st.markdown("\n".join([f"- {skill}" for skill in aquatics_gb]))
st.write("")

st.markdown("##### Skills Coach and Support Worker")
st.markdown("Canucks Autism Network: Nov 2021 - Sept 2024") 
CAN = [
    "Support children and adults with autism in sports and recreation",
    "Teach swimming and water safety to children with autism",
    "Teach motor skills and sports to children with autism",  
]
st.markdown("\n".join([f"- {skill}" for skill in CAN]))
st.write("")

st.markdown("##### Sports Field Maintenance & Machine Operator")
st.markdown("City of Nanaimo: 2021 - 2024")
city_of_nanaimo = [
    "Maintain and repair sports fields and parks in Nanaimo",
    "Operate and maintain heavy machinery for field maintenance",
    "Assist with the organization of community sports events", 
    "Fertilize, aerate, and seed sports fields",
    "Build and maintain baseball diamonds to a high standard", 
    "Groom and maintain artificial turf fields",
]
st.markdown("\n".join([f"- {skill}" for skill in city_of_nanaimo]))
st.write("")

st.markdown("##### Clinical Assistant & Technician")
st.markdown("B.D. Mitchell Prosthetics & Orthotics: 2019 - 2021") 
bd_mitchell = [
    "Assist with the fabrication and fitting of prosthetics and orthotics",
    "Maintain and repair prosthetics and orthotics",
    "Assist with patient care and education", 
]
st.markdown("\n".join([f"- {skill}" for skill in bd_mitchell]))
st.write("")

st.markdown("##### Lifeguard & Swim Instructor")
st.markdown("City of Nanaimo: 2015 - 2021") 
lifeguard = [
    "Supervise and ensure the safety of swimmers in the pool",
    "Teach swimming lessons to children and adults",
    "Maintain pool cleanliness and safety standards", 
]
st.markdown("\n".join([f"- {skill}" for skill in lifeguard]))
st.write("")

st.markdown("##### Parks Ambassador")
st.markdown("City of Nanaimo: April - July 2020")
parks_ambassador = [
    "Promote and educate the public about parks and recreation",
    "Maintain and clean parks and recreation facilities",
    "Provide information and assistance to park visitors", 
]
st.markdown("\n".join([f"- {skill}" for skill in parks_ambassador]))
st.write("")

st.markdown("##### Camp Leader III")
st.markdown("City of Nanaimo: July - August 2020")
camp_leader = [
    "Lead and supervise children in summer camp activities",
    "Plan and organize camp activities and events",
    "Ensure the safety and well-being of campers", 
]
st.markdown("\n".join([f"- {skill}" for skill in camp_leader]))
st.write("")