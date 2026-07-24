def calculate_ats_score(data):

    score = 0

    # Contact details (20 marks)
    if data["Name"] != "Not Found":
        score += 5

    if data["Email"] != "Not Found":
        score += 5

    if data["Phone"] != "Not Found":
        score += 5


    # Skills (40 marks)
    skills = data["Skills"]

    if len(skills) >= 5:
        score += 40
    elif len(skills) >= 3:
        score += 25
    elif len(skills) > 0:
        score += 15


    # Resume sections keyword check (40 marks)
    text = str(data).lower()

    sections = [
        "education",
        "project",
        "experience",
        "certificate"
    ]

    for section in sections:
        if section in text:
            score += 10


    return min(score, 100)