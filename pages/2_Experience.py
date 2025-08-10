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

st.markdown("##### Performance Analyst")
st.markdown("AquaticsGB: Jan 2025 - Present")  # Removed space around colon
aquatics_gb = [
    "Perform notational analysis of swimming competitions",  # Fixed "Performan"
    "Develop and implement custom data management programs",  # Fixed "managment"
    "Create custom visuals and reports for coaches and athletes", 
]
st.markdown("\n".join([f"- {skill}" for skill in aquatics_gb]))
st.write("")

st.markdown("##### Skills Coach and Support Worker")
st.markdown("Canucks Autism Network: Nov 2021 - Sept 2024")  # Removed space around colon
CAN = [
    "Support children and adults with autism in sports and recreation",
    "Teach swimming and water safety to children with autism",
    "Teach motor skills and sports to children with autism",  
]
st.markdown("\n".join([f"- {skill}" for skill in CAN]))
st.write("")

st.markdown("##### Sports Field Maintenance & Machine Operator")
st.markdown("City of Nanaimo: 2021 - 2024")  # Removed space around colon
city_of_nanaimo = [
    "Maintain and repair sports fields and parks in Nanaimo",
    "Operate and maintain heavy machinery for field maintenance",
    "Assist with the organization of community sports events", 
    "Fertilize, aerate, and seed sports fields",
    "Build and maintain baseball diamonds to a high standard",  # Fixed "Built" to "Build", "Baseball" capitalization
    "Groom and maintain artificial turf fields",
]
st.markdown("\n".join([f"- {skill}" for skill in city_of_nanaimo]))
st.write("")

st.markdown("##### Clinical Assistant & Technician")
st.markdown("B.D. Mitchell Prosthetics & Orthotics: 2019 - 2021")  # Removed space around colon
bd_mitchell = [
    "Assist with the fabrication and fitting of prosthetics and orthotics",
    "Maintain and repair prosthetics and orthotics",
    "Assist with patient care and education", 
]
st.markdown("\n".join([f"- {skill}" for skill in bd_mitchell]))
st.write("")

st.markdown("##### Lifeguard & Swim Instructor")
st.markdown("City of Nanaimo: 2015 - 2021")  # Removed space around colon
lifeguard = [
    "Supervise and ensure the safety of swimmers in the pool",
    "Teach swimming lessons to children and adults",
    "Maintain pool cleanliness and safety standards", 
]
st.markdown("\n".join([f"- {skill}" for skill in lifeguard]))
st.write("")

st.markdown("##### Parks Ambassador")
st.markdown("City of Nanaimo: April - July 2020")  # Removed space around colon
parks_ambassador = [
    "Promote and educate the public about parks and recreation",
    "Maintain and clean parks and recreation facilities",
    "Provide information and assistance to park visitors", 
]
st.markdown("\n".join([f"- {skill}" for skill in parks_ambassador]))
st.write("")

st.markdown("##### Camp Leader III")
st.markdown("City of Nanaimo: July - August 2020")  # Removed space around colon
camp_leader = [
    "Lead and supervise children in summer camp activities",
    "Plan and organize camp activities and events",
    "Ensure the safety and well-being of campers", 
]
st.markdown("\n".join([f"- {skill}" for skill in camp_leader]))
st.write("")