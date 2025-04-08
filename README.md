A Streamlit app that analyzes resumes using NLP and AI. It detects skills, highlights strengths and weaknesses, and recommends suitable job roles.

Deployed on streamlit : "https://resume-analyser-suraj-suryaansh.streamlit.app/"

## Features
- 📄 Resume upload (PDF)
- 🧠 NLP-based analysis
- 💼 Job role suggestion
- 🤖 GPT-powered feedback (optional)

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py
```

## Optional
Set your OpenAI key:
```bash
export OPENAI_API_KEY=your_key_here
```
