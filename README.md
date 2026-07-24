

# 🤖 AI Resume Analyzer

An AI-powered Resume Analysis System that analyzes resumes, extracts important information, evaluates ATS compatibility, identifies technical skills, and predicts suitable career roles.

The project is built using **FastAPI, NLP, and Machine Learning concepts** to help users understand and improve their resumes.

---

## 🚀 Features

### 📄 Resume Upload
- Upload resume in PDF format
- Extract resume content automatically
- Process resume using NLP techniques

### 👤 Resume Information Extraction
Automatically extracts:

- Name
- Email
- Phone Number
- Technical Skills

### 🛠 Skill Analysis
Detects important technical skills such as:

- Python
- Java
- C/C++
- SQL
- Git & GitHub
- Pandas
- NumPy
- Excel
- AWS
- Linux

### ⭐ ATS Score Analysis
Evaluates resume compatibility based on:

- Resume information completeness
- Technical skills
- Important keywords
- Resume structure

### 💼 Career Prediction
Predicts suitable career roles based on detected skills.

Example:

- Data Analyst
- Data Scientist
- ML Engineer
- Software Developer

### 🤖 AI Resume Suggestions
Provides improvement suggestions such as:

- Add more project details
- Mention measurable achievements
- Update skills according to job roles

---

# 🏗️ Project Architecture

AI-Resume-Analyzer

│ ├── main.py
│ ├── app
│   ├── parser.py
│   ├── skill_extractor.py 
│   ├── ats.py 
│   └── career.py 
│ ├── templates 
│   ├── index.html 
│   └── result.html 
│ ├── static │   
├── css │   
│   └── style.css 
│   │ │   └── js 
│       └── script.js 
│ 
├── requirements.txt 
│ └── README.md

---

# ⚙️ Technologies Used

## Backend
- Python
- FastAPI

## Frontend
- HTML
- CSS
- JavaScript

## Libraries
- pdfplumber
- Jinja2
- NLP techniques
- Regular Expressions

## Tools
- Git
- GitHub
- VS Code

---

# 🔄 Working Flow

Upload Resume (PDF)

↓

PDF Text Extraction

↓

Resume Parsing

↓

Skill Extraction

↓

ATS Score Calculation

↓

Career Prediction

↓

AI Suggestions

↓

Resume Analysis Report

---

# 📦 Installation & Setup

### 1. Clone Repository

git clone https://github.com/SujaanBhalla/AI-Resume-Analyzer.git

2. Move into Project Folder

cd AI-Resume-Analyzer

3. Create Virtual Environment

python -m venv venv

4. Activate Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

6. Run Application

uvicorn main:app --reload


---

🌐 Open Application

Visit:

http://127.0.0.1:8000


---

📸 Application Output

The system provides:

Resume Details

Extracted Skills

ATS Score

Career Prediction

Resume Improvement Suggestions



---

🔮 Future Improvements

Planned features:

Job Description Matching

AI Resume Chatbot

LLM-based Resume Feedback

Advanced ATS Algorithm

Resume Ranking System

Cloud Deployment



---

👨‍💻 Author

Sujaan Bhalla

B.Tech Artificial Intelligence & Data Science Student

Interested in:

Artificial Intelligence

Machine Learning

Data Science

MLOps
