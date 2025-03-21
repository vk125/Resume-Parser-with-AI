# resume_parser.py

import PyPDF2
import spacy
from transformers import pipeline

# Load NLP model for entity recognition (can be changed to a custom model for skill extraction)
nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to extract skills, experience, etc.
def extract_info_from_text(text):
    doc = nlp(text)
    skills = []
    experience = []
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Assume companies are considered experience
            experience.append(ent.text)
        if ent.label_ == "GPE":  # Assume location-related entities could be experience-related
            experience.append(ent.text)
        # Add logic for skill extraction, you can customize this part with a predefined skill list
    return {"skills": skills, "experience": experience}

def summarize_resume(text):
    # Summarize the resume for a quick overview
    summary = summarizer(text, max_length=100, min_length=25, do_sample=False)
    return summary[0]['summary_text']

# Example usage
if __name__ == "__main__":
    resume_text = extract_text_from_pdf("resume.pdf")
    info = extract_info_from_text(resume_text)
    summary = summarize_resume(resume_text)
    
    print("Extracted Information:", info)
    print("Summary:", summary)
