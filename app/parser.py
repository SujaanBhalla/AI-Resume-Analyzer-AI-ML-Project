import re

from app.skill_extractor import extract_skills


def extract_email(text):

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email[0] if email else "Not Found"


def extract_phone(text):

    phone = re.findall(
        r"\+?\d[\d\s\-]{8,15}",
        text
    )

    return phone[0] if phone else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 3 and len(line.split()) <= 4:

            return line

    return "Not Found"


def parse_resume(text):

    result = {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "Skills": extract_skills(text)

    }

    return result