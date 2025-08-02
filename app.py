import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_excel("All_RollNumbers_CGPA.xlsx")

df = load_data()

st.title("🎓 CGPA Lookup - DHA Suffa University")

roll_input = st.text_input("Enter your Roll Number (e.g., ME211001):")

if roll_input:
    roll_input = roll_input.strip().upper()
    result = df[df["Registration No."] == roll_input]
    if not result.empty:
        cgpa = result.iloc[0]["CGPA"]
        st.success(f"🎯 Your CGPA is: {cgpa}")
    else:
        st.error("❌ Roll number not found. Please check and try again.")
