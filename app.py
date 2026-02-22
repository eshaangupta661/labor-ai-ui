import streamlit as st
import requests

st.set_page_config(page_title="AI Wage Fairness Engine", layout="centered")

API_URL = "https://labour-ai-eshaan-api-exh7c3dhbqheabcf.centralindia-01.azurewebsites.net/predict"

st.title("🇮🇳 AI-Powered Wage Fairness Checker")
st.markdown("Check if a worker is being underpaid under MGNREGS conditions.")

# State list (must match training data exactly)
states = [
    "ANDHRA PRADESH","ARUNACHAL PRADESH","ASSAM","BIHAR",
    "CHHATTISGARH","GOA","GUJARAT","HARYANA","HIMACHAL PRADESH",
    "JAMMU AND KASHMIR","JHARKHAND","KARNATAKA","KERALA",
    "LADAKH","MADHYA PRADESH","MAHARASHTRA","MANIPUR",
    "MEGHALAYA","MIZORAM","NAGALAND","ODISHA","PUNJAB",
    "RAJASTHAN","SIKKIM","TAMIL NADU","TELANGANA",
    "TRIPURA","UTTAR PRADESH","UTTARAKHAND","WEST BENGAL",
    "ANDAMAN AND NICOBAR","DN HAVELI AND DD","LAKSHADWEEP","PUDUCHERRY"
]

sectors = ["construction", "agriculture", "manual_labor"]

state = st.selectbox("Select State", states)
sector = st.selectbox("Select Sector", sectors)
experience = st.slider("Experience (Years)", 0, 15, 3)
skill = st.slider("Skill Level (1-5)", 1, 5, 2)
offered_wage = st.number_input("Offered Daily Wage", min_value=0.0)

if st.button("Check Fairness"):

    payload = {
        "state": state,
        "sector": sector,
        "experience_years": experience,
        "skill_level": skill,
        "offered_wage": offered_wage
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            st.success(f"Predicted Fair Wage: ₹ {result['predicted_wage']}")

            if result["fairness_status"] == "Underpaid":
                st.error("⚠ Worker is UNDERPAID")
            else:
                st.success("✅ Wage is FAIR")
        else:
            st.error("Backend error.")

    except:
        st.error("Could not connect to backend.")
