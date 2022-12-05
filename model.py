from transformers import pipeline, set_seed
set_seed(7)


def get_prediction(text : str):
    generator = pipeline('text-generation', model='gpt2')

    return generator(text, max_length=10, num_return_sequences=1)[0]