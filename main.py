```python
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.parser import parse_resume
from app.ats import calculate_ats_score
from app.career import predict_career

import os
import shutil
import uuid


# ---------------------------------------------------------
# CREATE FASTAPI APP
# ---------------------------------------------------------

app = FastAPI(
    title="AI Resume Analyzer",
    description="Analyze resumes, calculate ATS scores, and predict suitable careers.",
    version="1.0.0"
)


# ---------------------------------------------------------
# DIRECTORIES
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")


# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------

if os.path.exists(STATIC_DIR):
    app.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static"
    )


# ---------------------------------------------------------
# JINJA2 TEMPLATES
# ---------------------------------------------------------

templates = Jinja2Templates(
    directory=TEMPLATE_DIR
)


# ---------------------------------------------------------
# HOME PAGE
# ---------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Display the resume analyzer home page.
    """

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


# ---------------------------------------------------------
# RESUME ANALYZER
# ---------------------------------------------------------

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_resume(
    request: Request,
    file: UploadFile = File(...)
):
    """
    Upload a PDF resume and analyze it.

    Steps:
    1. Validate uploaded file
    2. Save the PDF
    3. Parse resume
    4. Calculate ATS score
    5. Predict career
    6. Display results
    """

    # -----------------------------------------------------
    # CHECK FILE
    # -----------------------------------------------------

    if not file.filename:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Please select a resume file."
            }
        )


    # -----------------------------------------------------
    # CHECK PDF FORMAT
    # -----------------------------------------------------

    file_extension = os.path.splitext(file.filename)[1].lower()

    if file_extension != ".pdf":
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": "Please upload your resume in PDF format."
            }
        )


    # -----------------------------------------------------
    # CREATE UNIQUE FILE NAME
    # -----------------------------------------------------

    unique_filename = f"{uuid.uuid4().hex}.pdf"

    file_path = os.path.join(
        UPLOAD_DIR,
        unique_filename
    )


    # -----------------------------------------------------
    # SAVE UPLOADED FILE
    # -----------------------------------------------------

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Unable to save the uploaded file: {str(e)}"
            }
        )


    # -----------------------------------------------------
    # PARSE RESUME
    # -----------------------------------------------------

    try:

        resume_data = parse_resume(file_path)

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Unable to analyze the resume: {str(e)}"
            }
        )


        # -----------------------------------------------------
    # CALCULATE ATS SCORE
    # -----------------------------------------------------

    try:

        ats_result = calculate_ats_score(
            resume_data
        )

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"ATS score calculation failed: {str(e)}"
            }
        )


    # -----------------------------------------------------
    # PREDICT CAREER
    # -----------------------------------------------------

    try:

        career_result = predict_career(
            resume_data
        )

    except Exception as e:

        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Career prediction failed: {str(e)}"
            }
        )


    # -----------------------------------------------------
    # DISPLAY RESULTS
    # -----------------------------------------------------

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "resume": resume_data,
            "ats": ats_result,
            "career": career_result
        }
    )


# ---------------------------------------------------------
# HEALTH CHECK
# ---------------------------------------------------------

@app.get("/health")
async def health_check():

    return {
        "status": "success",
        "message": "AI Resume Analyzer is running."
    }


# ---------------------------------------------------------
# RUN APPLICATION
# ---------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )