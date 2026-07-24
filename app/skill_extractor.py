SKILLS = [

    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "FastAPI",
    "Flask",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Docker",
    "Git",
    "GitHub",
    "Pandas",
    "NumPy",
    "Power BI",
    "Excel",
    "AWS",
    "Linux"

]


def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:

        if skill.lower() in text:

            found.append(skill)

    return found