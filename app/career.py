def predict_career(skills):

    skills = [skill.lower() for skill in skills]


    roles = {

        "Data Scientist": [
            "python",
            "pandas",
            "numpy",
            "machine learning"
        ],

        "Data Analyst": [
            "python",
            "sql",
            "excel",
            "pandas"
        ],

        "ML Engineer": [
            "python",
            "tensorflow",
            "aws",
            "machine learning"
        ],

        "Software Developer": [
            "java",
            "c++",
            "git"
        ]

    }


    result = {}


    for role, required in roles.items():

        match = 0

        for skill in required:

            if skill in skills:
                match += 1


        percentage = int((match / len(required)) * 100)

        result[role] = percentage


    best_role = max(
        result,
        key=result.get
    )


    return {
        "role": best_role,
        "score": result[best_role],
        "all_roles": result
    }