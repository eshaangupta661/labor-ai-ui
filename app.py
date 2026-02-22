import streamlit as st
import requests

API_URL = "https://labour-ai-eshaan-api-exh7c3dhbqheabcf.centralindia-01.azurewebsites.net/predict"

st.set_page_config(page_title="Labour AI", layout="centered")

st.title("💼 Labour Wage Fairness Checker")

state = st.text_input("State")
sector = st.text_input("Sector")
experience = st.number_input("Experience (years)", min_value=0)
skill = st.number_input("Skill Level (1-5)", min_value=1, max_value=5)
wage = st.number_input("Offered Wage (₹)")

if st.button("Check Wage Fairness"):

    payload = {
        "state": state,
        "sector": sector,
        "experience_years": experience,
        "skill_level": skill,
        "offered_wage": wage
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Fair Wage: ₹{result['predicted_wage']}")
            st.info(f"Status: {result['fairness_status']}")
        else:
            st.error("API error. Please try again.")

    except:
        st.error("Could not connect to backend.")
