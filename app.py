import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Load your cleaned Excel file
    return pd.read_excel("cleaned_course_grade.xlsx")

# Load data
df = load_data()

# Streamlit UI
st.title("🎓 Student Grade Lookup")

st.markdown("Enter your roll number to see your course-wise grades.")

roll_input = st.text_input("🔎 Roll Number (e.g., ME211001):")

if roll_input:
    roll_input = roll_input.strip().upper()
    filtered = df[df["Registration No."] == roll_input]

    if not filtered.empty:
        st.success(f"✅ Found {len(filtered)} course(s) for {roll_input}")
        st.dataframe(filtered[["Course Code", "Grade"]].reset_index(drop=True))
    else:
        st.error("❌ Roll number not found. Please check and try again.")
