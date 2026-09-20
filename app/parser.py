import re
import pdfplumber

from app.skill_extractor import extract_skills


def extract_email(text):
    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email[0] if email else "Not Found"


def extract_phone(text):
    phone = re.findall(
        r"(?:\+91[\s-]?)?[6-9]\d{9}",
        text
    )

    if phone:
        return phone[0]

    return "Not Found"


def extract_name(text):
    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Skip common headings
        if line.lower() in [
            "resume",
            "curriculum vitae",
            "cv",
            "profile",
            "contact",
            "summary"
        ]:
            continue

        # Name usually appears near the top
        if (
            len(line) > 3
            and len(line.split()) <= 4
            and not "@" in line
            and not any(char.isdigit() for char in line)
        ):
            return line

    return "Not Found"


def extract_text_from_pdf(file_path):

    text = ""

    try:

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as e:

        raise Exception(
            f"Unable to read PDF: {str(e)}"
        )

    return text


def parse_resume(file_path):

    # =====================================================
    # EXTRACT TEXT FROM PDF
    # =====================================================

    text = extract_text_from_pdf(file_path)

    if not text.strip():

        raise Exception(
            "No readable text found in the PDF."
        )


    # =====================================================
    # EXTRACT RESUME INFORMATION
    # =====================================================

    skills = extract_skills(text)


    result = {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "Skills": skills,

        "Raw_Text": text

    }

    return result


if __name__ == "__main__":
    print("Resume parser is ready.")