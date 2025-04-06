import streamlit as st
from resume_parser import extract_text_from_pdf
from analyzer import analyze_resume
from job_matcher import suggest_matching_jobs
from gpt_feedback import get_gpt_feedback

st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
st.title("📄 Smart Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.subheader("📃 Extracted Resume Text")
    st.text_area("Resume Text", resume_text, height=250)

    with st.spinner("Analyzing resume..."):
        analysis = analyze_resume(resume_text)
        skills = analysis["skills"]
        strengths = analysis["strengths_summary"]
        weaknesses = analysis["weaknesses_summary"]

        suggested_roles = suggest_matching_jobs(skills, resume_text)


    st.subheader("✅ Skills Detected")
    st.write(skills)

    st.subheader("💪 Strengths")
    st.write(strengths)

    st.subheader("⚠️ Weaknesses")
    st.write(weaknesses)

    st.subheader("🔍 Suggested Job Roles")

    if suggested_roles:
        for role in suggested_roles:
            st.markdown(f"### 🎯 {role['role']}")
            st.markdown(f"**✅ Skills You Have:** {', '.join(role['matched_skills']) or 'None'}")
            st.markdown(f"**❌ Skills You Need:** {', '.join(role['missing_skills']) or 'None'}")
            st.markdown(f"**📊 Match:** `{role['match_percent']}%`")
            st.markdown(f"**💡 Tip:** {role['message']}")
            st.markdown("---")
    else:
        st.warning("No strong job matches found. Try enhancing your resume with more relevant skills or project details.")


    if st.button("🧠 Get GPT Suggestions"):
        feedback = get_gpt_feedback(resume_text)
        st.subheader("📢 GPT Feedback")
        st.write(feedback)