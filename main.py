from model import generate_text

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.head("/")
@app.get("/")
def index() -> FileResponse:
    return FileResponse(path="static/index.html", media_type="text/html")


@app.get("/essays")
def get_text(question,keywords):
    output = generate_text(question,keywords)
    
    return output
