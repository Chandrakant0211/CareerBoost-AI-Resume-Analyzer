# 🚀 CareerBoost AI - Advanced Resume Analyzer

An AI-powered tool built with **Streamlit** and **Python** to help job seekers optimize their resumes for Applicant Tracking Systems (ATS).

---

## 📌 Problem Statement

Many qualified candidates are filtered out by ATS because of missing keywords or poor formatting. This project helps bridge that gap by providing real-time analysis and skill recommendations.

---

## ✨ Key Features

- **PDF Text Extraction:** High-speed parsing using PyMuPDF.  
- **ATS Scoring:** Real-time compatibility score (0-100).  
- **Skill Gap Analysis:** Identifies missing technical and soft skills.  
- **Interactive Dashboard:** Visual feedback for better resume optimization.

---

## 🛠️ Technology Stack

- **Language:** Python 3.x  
- **Framework:** Streamlit  
- **Libraries:** PyMuPDF (fitz), Regex, NLTK  
- **Database:** Custom `skills_db` module

---

## 🚀 How to Run (Windows)

1. **Repository Clone करें:**

   **hugu**


**git clone https://github.com/Chandrakant0211/CareerBoost-AI-Resume-Analyzer.git
cd CareerBoost-AI-Resume-Analyzer**


 ## 2.Virtual Environment बनाएं:
python -m venv .venv

## 3.Virtual Environment Activate करें (CMD):
**.venv\Scripts\activate**

## 4. Required Libraries Install करें:
  **pip install -r requirements.txt**
  
## अगर requirements.txt नहीं है, तो manually install करें:
**pip install streamlit PyMuPDF nltk**

## 5.Streamlit App Run करें
**streamlit run carrierBoostAi.py**
## 6. Optional: NLTK Resources Download करें (अगर app text processing error दे):
**import nltk**
**nltk.download('punkt')**
**nltk.download('stopwords')**


## 📂 Project Structure
**CareerBoost-AI-Resume-Analyzer/**
**│
├── carrierBoostAi.py        # Main Streamlit app
├── skills_db.py             # Custom skills database module
├── requirements.txt         # Python dependencies
├── README.md
└── images/**                  # Screenshots or images
