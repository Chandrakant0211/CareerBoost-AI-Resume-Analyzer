import sys
import os
import streamlit as st

# 1. PATH FIX
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# 2. LOCAL IMPORTS
try:
    from utils import extract_text_from_pdf, extract_skills, calculate_match_score, skill_gap_analysis, ats_score
    from skills_db import SKILLS_DATABASE
except ImportError as e:
    st.error(f"Error: Could not find project files. Details: {e}")
    st.stop()

# 3. PAGE SETUP
st.set_page_config(page_title="CareerBoost AI", layout="wide")
st.title("🚀 CareerBoost AI - Advanced Resume Analyzer")

# 4. USER INPUTS
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description Here", height=200)

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        # Processing with safety checks
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_skills = extract_skills(resume_text) or []  # Fallback to empty list

        match_score = calculate_match_score(resume_text, job_description)
        missing_skills = skill_gap_analysis(resume_skills, job_description)
        ats = ats_score(resume_skills)

        # ---------------- Dashboard ----------------
        st.subheader("📊 Analysis Dashboard")
        col1, col2, col3 = st.columns(3)
        col1.metric("Match Score", f"{match_score}%")
        col2.metric("ATS Score", f"{ats}/100")
        col3.metric("Skills Found", len(resume_skills))

        # ---------------- Skills ----------------
        st.divider()
        st.subheader("✅ Detected Skills")
        st.write(", ".join(resume_skills).title() if resume_skills else "No skills detected.")

        st.subheader("❌ Missing Skills (Required by JD)")
        if missing_skills:
            st.error(", ".join(missing_skills).title())
        else:
            st.success("No major skill gaps found!")

        # ---------------- Suggestions ----------------
        st.divider()
        st.subheader("💡 Improvement Suggestions")
        if match_score < 50:
            st.warning("Low Match: Add more relevant keywords from the Job Description.")
        elif match_score < 75:
            st.info("Good: Consider adding quantifiable achievements related to missing skills.")
        else:
            st.success("Excellent Match!")
