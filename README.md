# Resume Classifier and Parser App Project
This project involves classifying resumes into various designations and parsing important information from PDF resumes. It uses machine learning techniques for classification and spaCy for natural language processing

# Table of Contents
* Overview
* Steps Followed
* Performance Metrics
* Resume Parser App

# Overview
The Resume Classifier utilizes machine learning techniques to classify resumes into different categories. It employs eight different classification models initially, but through evaluation, XGBoost demonstrates the best performance in terms of accuracy, precision, recall, and F1-score.

# Steps Followed
1. Data Collection and Conversion:
     * DE, DS, JD, MDE: Original CV files downloaded from Google.
     * Data Engineer, Data Scientist, Java Developer, Mechanical Design Engineer: CV files converted from PDF to DOCX.
2. Resume Classifier Program:
     * Demonstrates how to convert PDF to DOCX, extract text from DOCX files, and save it as a CSV file.
3. Classification Models:
     * Compares various models for classification and selects the best-performing one.
4. Model Performance:
     * Shares the accuracy of the models built (refer to Accuracy.xlsx file).
  
# Performance Metrics

## Accuracy
* Measures the proportion of correctly classified instances out of the total instances.
* Accuracy of 0.96 means that 96% of the resumes were correctly classified into their respective categories by the model.

# Precision

* Ratio of correctly predicted positive observations to the total predicted positives.
* Class 0: Precision of 1.00
* Class 1: Precision of 0.90
* Class 2: Precision of 0.96
* Class 3: Precision of 0.97

# Recall

* Ratio of correctly predicted positive observations to all observations in the actual class.
* Class 0: Recall of 0.95
* Class 1: Recall of 0.95
* Class 2: Recall of 0.96
* Class 3: Recall of 0.97

# F1-score

* Harmonic mean of precision and recall.
* Class 0: F1-score of 0.97
* Class 1: F1-score of 0.93
* Class 2: F1-score of 0.96
* Class 3: F1-score of 0.97

# Resume Parser App

The Resume Parser App is a tool for extracting important information from uploaded PDF resumes. This application uses spaCy, a powerful natural language processing library, to identify and obtain crucial details from PDF resumes, including name, contact number, email address, talents, and education. Simply update the necessary skills list in the code and search for relevant skills for the job position in the submitted resume.

## Files Included

 *  main.py: Source code for the Resume Parser App.
 *  requirements.txt: List of dependencies required for the project.
  
## Business objective:
The document classification solution should significantly reduce the manual human effort in the HRM. 
It should achieve a higher level of accuracy and automation with minimal human intervention

## Deployed in streamlit and the link is given below
https://chandan101989-nlp-resume-classification-main-buhvf6.streamlit.app/
