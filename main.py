import re
from pdfminer.high_level import extract_text
import docx2txt
import spacy
from spacy.matcher import Matcher
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np



def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)


def extract_contact_number_from_resume(text):
    contact_number = None
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    return contact_number


def extract_email_from_resume(text):
    email = None
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email


def extract_skills_from_resume(text, skills_list):
    skills = []
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)
    return skills


def extract_education_from_resume(text):
    education = []
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())
    return education


def extract_name(resume_text):
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)
    patterns = [
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}],
        [{'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}, {'POS': 'PROPN'}]
    ]
    for pattern in patterns:
        matcher.add('NAME', patterns=[pattern])
    doc = nlp(resume_text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        return span.text
    return None


def calculate_ats_score(skills_list, extracted_skills):
    total_skills = len(skills_list)
    matched_skills = len(extracted_skills)
    score = (matched_skills / total_skills) * 100
    return score


def main():
    st.set_page_config(
        page_title="Resume Information Extractor",
        page_icon=":page_facing_up:",
        layout="centered",
        initial_sidebar_state="expanded")
    
    st.title("Resume Information Extractor")
    st.markdown("""
        <style>
            .css-18e3th9 { 
                padding-top: 2rem; 
                padding-bottom: 2rem; 
                padding-left: 2rem; 
                padding-right: 2rem; 
            }
            .css-1d391kg {
                padding: 1rem 1rem 1rem 1rem;
            }
            .stButton > button {
                color: white;
                background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%);
                border: none;
                padding: 0.5rem 1rem;
                border-radius: 5px;
                font-size: 1rem;
            }
            .stFileUploader > div {
                padding: 0.5rem 1rem;
                border: 2px dashed #00C9FF;
                border-radius: 5px;
                text-align: center;
            }
        </style>
        """, unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a resume (PDF or DOCX format)", type=["pdf", "docx"])


    if uploaded_file is not None:
        with st.spinner("Extracting information..."):
            if uploaded_file.type == "application/pdf":
               text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(uploaded_file)
            else:
                st.error("Unsupported file format. Please upload a PDF or DOCX file.")
                return

        st.header("Extracted Information")

        name = extract_name(text)
        st.subheader("👤 Name")
        st.write(name if name else "Name not found")

        contact_number = extract_contact_number_from_resume(text)
        st.subheader("📞 Contact Number")
        st.write(contact_number if contact_number else "Contact Number not found")

        email = extract_email_from_resume(text)
        st.subheader("📧 Email")
        st.write(email if email else "Email not found")

        skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'AWS', 'Time Series Analysis',
                       'Deep Learning', 'SQL', 'Natural Language Processing', 'Descriptive Statistics',
                       'Inferential Statistics', 'Docker']
        extracted_skills = extract_skills_from_resume(text, skills_list)
        st.subheader("💼 Skills")
        st.write(extracted_skills if extracted_skills else "No skills found")

        extracted_education = extract_education_from_resume(text)
        st.subheader("🎓 Education")
        st.write(extracted_education if extracted_education else "No education information found")

        ats_score = calculate_ats_score(skills_list, extracted_skills)
        st.subheader("📊 ATS Score")
        st.write(f"Total Score: {ats_score:.2f}%")

        # Plotting donut chart
        labels = ['Matched Skills', 'Remaining Skills']
        sizes = [ats_score, 100 - ats_score]
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['Lightgreen', 'lightgrey'])
        center_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(center_circle)
        ax.axis('equal')
        ax.set_title('ATS Score')
        st.pyplot(fig) 

        # Calculate and display remaining skills
        remaining_skills = set(skills_list) - set(extracted_skills)
        st.subheader("🚀 Skills to Develop")
        st.write(list(remaining_skills) if remaining_skills else "No additional skills to develop")


if __name__ == '__main__':
    main()