from typing import Union,List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str
    keywords: List[str]

class Essay(BaseModel):
    body: str
    

@app.get("/")
def read_root():
    return {"msg": "Hello, World!"}

# Questions
@app.get("/questions/")
def read_all_questions():
    return "all articles"

@app.get("/questions/{question_id}")
def read_question(question_id:int):
    return {"question_id": question_id}

@app.post("/questions/")
async def create_question(question: Question):
    return question

# Essays
@app.get("/essays/")
def read_all_essays():
    return "all articles"

@app.get("/essays/{essay_id}")
def read_essay(question_id:int):
    return {"essay_id": essay_id}

@app.post("/essays/")
async def create_essay(essay: Essay):
    return essay
