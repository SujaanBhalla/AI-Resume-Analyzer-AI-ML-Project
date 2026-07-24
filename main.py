from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.staticfiles import StaticFiles

from app.parser import parse_resume
from app.ats import calculate_ats_score
from app.career import predict_career

import pdfplumber
import os


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(
    directory="templates"
)


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    context = {
        "request": request
    }


    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )




@app.post("/upload")
async def upload_resume(
    request: Request,
    file: UploadFile = File(...)
):


    filepath = os.path.join(
        UPLOAD_DIR,
        file.filename
    )


    with open(filepath, "wb") as f:

        f.write(await file.read())



    text = ""


    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:

                text += extracted



    parsed_data = parse_resume(text)



    ats_score = calculate_ats_score(
        parsed_data
    )



    career_prediction = predict_career(
        parsed_data["Skills"]
    )



    return templates.TemplateResponse(

        request=request,

        name="result.html",

        context={

            "request": request,

            "data": parsed_data,

            "ats_score": ats_score,

            "career": career_prediction

        }

    )