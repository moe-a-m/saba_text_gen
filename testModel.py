from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(7)
val = generator("Hello, I'm a language model,", max_length=500, num_return_sequences=1)
print(val)