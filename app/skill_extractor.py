import re


# =========================================================
# SKILLS DATABASE
# =========================================================

SKILLS = [

    # Programming Languages
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "R",

    # Web Development
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "Express.js",
    "FastAPI",
    "Flask",
    "Django",

    # Database
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "SQLite",
    "Oracle",
    "Redis",

    # Data Science
    "Data Science",
    "Data Analysis",
    "Data Visualization",
    "Statistics",
    "Exploratory Data Analysis",
    "EDA",

    # Machine Learning
    "Machine Learning",
    "Deep Learning",
    "Supervised Learning",
    "Unsupervised Learning",
    "Natural Language Processing",
    "NLP",
    "Computer Vision",
    "Reinforcement Learning",

    # ML Libraries
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "XGBoost",

    # Data Libraries
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "SciPy",

    # AI
    "Artificial Intelligence",
    "Generative AI",
    "Large Language Models",
    "LLM",
    "ChatGPT",
    "OpenAI",
    "Hugging Face",

    # Cloud
    "AWS",
    "Microsoft Azure",
    "Azure",
    "Google Cloud",
    "GCP",

    # DevOps
    "Docker",
    "Kubernetes",
    "Jenkins",
    "CI/CD",
    "Git",
    "GitHub",
    "GitLab",
    "Linux",

    # Tools
    "Jupyter",
    "Jupyter Notebook",
    "VS Code",
    "Postman",

    # Business / Analytics
    "Power BI",
    "Tableau",
    "Excel",
    "Microsoft Excel",

    # Backend / APIs
    "REST API",
    "RESTful API",
    "API Development",

    # Other
    "OOP",
    "Object Oriented Programming",
    "Data Structures",
    "Algorithms",
    "Problem Solving"
]


# =========================================================
# EXTRACT SKILLS
# =========================================================

def extract_skills(text):

    found = []

    if not text:
        return found

    text = text.lower()

    for skill in SKILLS:

        skill_lower = skill.lower()

        # -------------------------------------------------
        # Special handling for short skills
        # -------------------------------------------------

        if skill in ["C", "R", "C++", "C#"]:

            pattern = r"(?<![a-zA-Z])" + re.escape(
                skill_lower
            ) + r"(?![a-zA-Z])"

        else:

            pattern = r"(?<![a-zA-Z0-9])" + re.escape(
                skill_lower
            ) + r"(?![a-zA-Z0-9])"

        if re.search(pattern, text):

            found.append(skill)


    # =====================================================
    # REMOVE DUPLICATES
    # =====================================================

    unique_skills = []

    for skill in found:

        if skill not in unique_skills:

            unique_skills.append(skill)


    return unique_skills


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":

    sample_text = """
    I am a Data Scientist with experience in Python,
    SQL, Machine Learning, Pandas, NumPy, TensorFlow,
    Power BI, Git and AWS.
    """

    skills = extract_skills(sample_text)

    print("Detected Skills:")
    print(skills)