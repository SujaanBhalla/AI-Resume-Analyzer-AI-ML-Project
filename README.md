🤖 AI Resume Analyzer

An AI-powered resume analysis application that helps users understand their resume through ATS score evaluation, skill extraction, career prediction, and resume improvement suggestions.

🌐 Live Demo

🚀 Try AI Resume Analyzer

🚧 Deployment platform may be updated as the project moves to Streamlit deployment.

📂 GitHub Repository

GitHub – AI Resume Analyzer

✨ Features
📄 Upload and analyze PDF resumes
⭐ ATS score analysis
🧠 Automatic technical skill extraction
💼 AI-based career prediction
📊 Top career recommendations
📈 Resume improvement suggestions
🔍 Resume information extraction
🎨 Modern and responsive Streamlit interface
⚡ Fast and simple resume analysis workflow
🛠️ Technologies Used
Python
Streamlit
Natural Language Processing (NLP)
Machine Learning
PDFPlumber
Regex-based Text Processing
Pandas / NumPy
Git & GitHub
📁 Project Structure
AI-Resume-Analyzer-AI-ML-Project/
│
├── app/
│   ├── parser.py
│   ├── ats.py
│   ├── career.py
│   └── skill_extractor.py
│
├── models/
│
├── uploads/
│
├── streamlit_app.py
├── main.py
│
├── requirements.txt
├── README.md
└── .gitignore

uploads/, virtual environments, Python cache files, and other local files are excluded from GitHub using .gitignore.

🔄 How It Works
Upload Resume (PDF)
        ↓
   PDF Text Extraction
        ↓
Resume Information Extraction
        ↓
   Skill Extraction
        ↓
   ATS Score Analysis
        ↓
   Career Prediction
        ↓
Resume Improvement Suggestions
        ↓
      Results
🧠 Core Modules
📄 Resume Parser

Extracts readable text from uploaded PDF resumes and identifies:

Name
Email
Phone number
Technical skills
Resume text
⭐ ATS Score

Evaluates the resume using predefined resume-quality and keyword-based criteria to generate an ATS compatibility score.

🧠 Skill Extractor

Automatically identifies technical and professional skills from resume content using pattern-based text matching.

💼 Career Prediction

Matches extracted skills with predefined career profiles and provides:

Predicted career role
Career match score
Top career options
Matched skills
📈 Resume Suggestions

Provides suggestions based on the extracted resume information and analysis results.

🚀 Run Locally
1. Clone the repository
git clone https://github.com/SujaanBhalla/AI-Resume-Analyzer-AI-ML-Project.git
2. Open the project
cd AI-Resume-Analyzer-AI-ML-Project
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Run the Streamlit application
streamlit run streamlit_app.py
7. Open in browser

Streamlit will provide a local URL similar to:

http://localhost:8501
☁️ Deployment

The application is designed for deployment using Streamlit Community Cloud.

Deployment Steps
Push the project to GitHub.
Open Streamlit Community Cloud.
Connect the GitHub repository.
Select streamlit_app.py as the main application file.
Deploy the application.
🎯 Project Objective

The objective of this project is to develop an intelligent resume analysis system that helps users:

Understand the quality of their resume
Identify relevant technical skills
Estimate ATS compatibility
Discover suitable career paths
Improve their resume presentation

The project combines Python, NLP, text processing, and machine-learning concepts into a practical AI-based application.

🔮 Future Improvements

Improve ATS scoring accuracy

Add job-description matching

Add semantic similarity using NLP models

Improve career prediction using a trained ML model

Add more career categories

Add personalized resume recommendations

Support DOCX resumes

Improve resume section detection

Add downloadable analysis reports

Enhance UI/UX

Add resume keyword optimization

Add real-time job-role matching

📌 Project Status

🚧 Actively Developed

The core resume analysis workflow is implemented, including PDF parsing, skill extraction, ATS analysis, career prediction, and Streamlit-based frontend functionality.

👩‍💻 Author

Sujaan Bhalla

B.Tech – Artificial Intelligence & Data Science

⭐ If You Find This Project Useful

Feel free to ⭐ star the repository and explore the project.

Built with Python, AI, NLP, and Machine Learning.
