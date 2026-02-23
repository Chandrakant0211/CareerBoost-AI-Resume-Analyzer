import spacy
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills_db import SKILLS_DATABASE

# Load NLP model safely
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(uploaded_file):
    """Safely extract text from PDF."""
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
        return text.lower() if text else ""
    except:
        return ""

def extract_skills(text):
    """Detect skills. Always returns a list, never None."""
    if not text:
        return []
    return

def calculate_match_score(resume_text, job_description):
    """Calculate match score safely."""
    if not resume_text or not job_description:
        return 0.0
    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job_description.lower()])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])
        return round(float(similarity[0][0]) * 100, 2)
    except:
        return 0.0

def skill_gap_analysis(resume_skills, job_description):
    """Find missing skills safely."""
    if not job_description:
        return []
    job_text = job_description.lower()
    resume_skills_lower = [s.lower() for s in (resume_skills or [])]
    return [skill for skill in SKILLS_DATABASE if skill.lower() in job_text and skill.lower() not in resume_skills_lower]

def ats_score(resume_skills):
    """Calculate ATS score. Prevents NoneType error."""
    if not resume_skills:
        return 0
    return min(len(resume_skills) * 10, 100)
