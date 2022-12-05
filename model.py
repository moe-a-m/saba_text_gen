from transformers import pipeline, set_seed
# settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# config = dotenv_values(".env")
seed = int(os.environ.get("SEED"))
set_seed(seed)


def get_prediction(text: str):
    essay_length = int(os.environ.get("ESSAY_LENGTH"))
    generator = pipeline('text-generation', model='gpt2')
    return generator(text, max_length=essay_length, num_return_sequences=1)[0]
