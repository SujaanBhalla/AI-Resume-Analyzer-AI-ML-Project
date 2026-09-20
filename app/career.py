# =========================================================
# CAREER PREDICTION
# AI Resume Analyzer
# =========================================================


def predict_career(skills):

    # -----------------------------------------------------
    # SAFETY CHECK
    # -----------------------------------------------------

    if not skills:
        return {
            "role": "Not Enough Data",
            "score": 0,
            "all_roles": {}
        }


    # -----------------------------------------------------
    # NORMALIZE SKILLS
    # -----------------------------------------------------

    skills = [
        str(skill).strip().lower()
        for skill in skills
        if skill
    ]


    # Remove duplicates
    skills = list(set(skills))


    # -----------------------------------------------------
    # CAREER ROLES AND REQUIRED SKILLS
    # -----------------------------------------------------

    roles = {

        # -------------------------------------------------
        # DATA SCIENCE
        # -------------------------------------------------

        "Data Scientist": [
            "python",
            "pandas",
            "numpy",
            "scikit-learn",
            "machine learning",
            "statistics",
            "matplotlib",
            "seaborn",
            "sql"
        ],


        # -------------------------------------------------
        # DATA ANALYST
        # -------------------------------------------------

        "Data Analyst": [
            "python",
            "sql",
            "excel",
            "pandas",
            "numpy",
            "power bi",
            "tableau",
            "statistics",
            "data visualization"
        ],


        # -------------------------------------------------
        # MACHINE LEARNING ENGINEER
        # -------------------------------------------------

        "ML Engineer": [
            "python",
            "machine learning",
            "scikit-learn",
            "tensorflow",
            "pytorch",
            "deep learning",
            "numpy",
            "pandas",
            "docker",
            "aws"
        ],


        # -------------------------------------------------
        # AI ENGINEER
        # -------------------------------------------------

        "AI Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "nlp",
            "computer vision",
            "generative ai",
            "llm",
            "artificial intelligence"
        ],


        # -------------------------------------------------
        # SOFTWARE DEVELOPER
        # -------------------------------------------------

        "Software Developer": [
            "java",
            "c++",
            "c",
            "python",
            "data structures",
            "algorithms",
            "git",
            "github",
            "oop"
        ],


        # -------------------------------------------------
        # PYTHON DEVELOPER
        # -------------------------------------------------

        "Python Developer": [
            "python",
            "fastapi",
            "flask",
            "django",
            "sql",
            "git",
            "github",
            "rest api",
            "api"
        ],


        # -------------------------------------------------
        # WEB DEVELOPER
        # -------------------------------------------------

        "Web Developer": [
            "html",
            "css",
            "javascript",
            "react",
            "node.js",
            "bootstrap",
            "git",
            "github",
            "rest api"
        ],


        # -------------------------------------------------
        # BACKEND DEVELOPER
        # -------------------------------------------------

        "Backend Developer": [
            "python",
            "java",
            "node.js",
            "django",
            "flask",
            "fastapi",
            "sql",
            "mongodb",
            "rest api",
            "git"
        ],


        # -------------------------------------------------
        # AI / NLP ENGINEER
        # -------------------------------------------------

        "NLP Engineer": [
            "python",
            "nlp",
            "natural language processing",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "transformers",
            "hugging face",
            "llm"
        ],


        # -------------------------------------------------
        # COMPUTER VISION ENGINEER
        # -------------------------------------------------

        "Computer Vision Engineer": [
            "python",
            "opencv",
            "computer vision",
            "deep learning",
            "tensorflow",
            "pytorch",
            "numpy",
            "image processing",
            "machine learning"
        ],


        # -------------------------------------------------
        # MLOPS ENGINEER
        # -------------------------------------------------

        "MLOps Engineer": [
            "python",
            "machine learning",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "git",
            "github",
            "ci/cd",
            "mlflow"
        ],


        # -------------------------------------------------
        # CLOUD / DEVOPS
        # -------------------------------------------------

        "Cloud / DevOps Engineer": [
            "aws",
            "azure",
            "gcp",
            "docker",
            "kubernetes",
            "linux",
            "git",
            "github",
            "jenkins",
            "ci/cd"
        ],


        # -------------------------------------------------
        # DATABASE DEVELOPER
        # -------------------------------------------------

        "Database Developer": [
            "sql",
            "mysql",
            "postgresql",
            "mongodb",
            "oracle",
            "database",
            "dbms",
            "data warehousing"
        ]

    }


    # -----------------------------------------------------
    # CALCULATE ROLE SCORES
    # -----------------------------------------------------

    result = {}


    for role, required_skills in roles.items():

        match = 0

        for skill in required_skills:

            # Exact match
            if skill in skills:
                match += 1

            # Partial match
            else:

                for user_skill in skills:

                    if (
                        skill in user_skill
                        or user_skill in skill
                    ):
                        match += 1
                        break


        # Calculate percentage
        percentage = int(
            (match / len(required_skills)) * 100
        )

        result[role] = percentage


    # -----------------------------------------------------
    # SORT ROLES BY SCORE
    # -----------------------------------------------------

    sorted_roles = sorted(
        result.items(),
        key=lambda x: x[1],
        reverse=True
    )


    # -----------------------------------------------------
    # BEST CAREER
    # -----------------------------------------------------

    if sorted_roles and sorted_roles[0][1] > 0:

        best_role = sorted_roles[0][0]
        best_score = sorted_roles[0][1]

    else:

        best_role = "Not Enough Data"
        best_score = 0


    # -----------------------------------------------------
    # TOP 5 CAREER OPTIONS
    # -----------------------------------------------------

    top_roles = [
        {
            "role": role,
            "score": score
        }
        for role, score in sorted_roles[:5]
    ]


    # -----------------------------------------------------
    # RETURN RESULT
    # -----------------------------------------------------

    return {

        "role": best_role,

        "score": best_score,

        "all_roles": result,

        "top_roles": top_roles,

        "matched_skills": skills

    }
