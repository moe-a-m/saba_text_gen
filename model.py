'''
https://huggingface.co/gpt2
https://huggingface.co/deepset/roberta-base-squad2
'''
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, set_seed

# settings.py
import os
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import unicodedata

load_dotenv(find_dotenv())
seed = int(os.environ.get("SEED"))
set_seed(seed)


def get_answer(question: str, keywords: str):
    model_name = "deepset/roberta-base-squad2"

    # a) Get predictions
    nlp = pipeline('question-answering',
                   model=model_name, tokenizer=model_name)
    QA_input = {
        'question': question,
        'context': keywords
    }
    res = nlp(QA_input)

    # b) Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return res


def get_prediction(text: str):
    essay_length = int(os.environ.get("ESSAY_LENGTH"))
    generator = pipeline('text-generation', model='gpt2')
    return generator(text, max_length=essay_length, num_return_sequences=1)[0]


def generate_text(question: str, keywords: str):
    answer = get_answer(question, keywords)
    get_score(question, answer['score'])
    genText = get_prediction(answer['answer'])
    save_txt(question, genText)
    return genText


def clean_filename(filename):

    forbidden_chars = '"*\\/\'.|?:<>'
    filename = ''.join(
        [x if x not in forbidden_chars else '#' for x in filename])
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename


def save_txt(title, txt):
    dirName = 'answers'
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")
    else:
        print("Directory ", dirName,  " already exists")

    title = clean_filename(title)
    current_dateTime = datetime.now()
    current_time = "{:%B %d, %Y}".format(current_dateTime)
    name = dirName+'/'+current_time+title+'.txt'
    with open(name, 'w', encoding='utf-8') as f:

        f.write(txt['generated_text'])


def get_score(question, score):
    dirName = 'score'
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName,  " Created ")
    else:
        print("Directory ", dirName,  " already exists")
        
    question = clean_filename(question)
    current_dateTime = datetime.now()
    current_time= "{:%B %d, %Y}".format(current_dateTime)
    name = dirName+'/'+current_time+question+'.txt'
    
    txt = question +', '+os.environ.get("ESSAY_LENGTH")+ ','+ str(score)
    with open(name, 'w', encoding='utf-8') as f:

        f.write(txt)