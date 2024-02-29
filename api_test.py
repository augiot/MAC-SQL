import os
import openai

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "http://10.20.216.187:8020/v1")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "xxx")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sess-f8mdgXPs7GzCop5fKZN0R6GLKmEW4qRAvzS2SBIT")

# openai.api_type = "azure"
openai.api_base = OPENAI_API_BASE
openai.api_key = OPENAI_API_KEY
openai.api_type = "open_ai" # azure

MODEL_NAME = "/mnt/user2/workspace/model/Qwen-7B-Chat"
MODEL_NAME = "gpt-3.5-turbo"

def api_func(prompt:str):
    # global MODEL_NAME
    print(f"\nUse OpenAI model: {MODEL_NAME}\n")
    if MODEL_NAME.startswith('CodeLlama'):
        openai.api_base = 'http://0.0.0.0:8000/v1'
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        stop = ["<|im_end|>","<|endoftext|>"]
    )
    text = response['choices'][0]['message']['content'].strip()
    prompt_token = response['usage']['prompt_tokens']
    response_token = response['usage']['completion_tokens']
    return text, prompt_token, response_token

print(api_func("你好"))