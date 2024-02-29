import os
# set your OPENAI_API_BASE, OPENAI_API_KEY here!
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1/chat/completions")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sess-f8mdgXPs7GzCop5fKZN0R6GLKmEW4qRAvzS2SBIT")

import openai
openai.api_type = "open_ai" # azure
openai.api_base = OPENAI_API_BASE
# set your own api_version
# openai.api_version = "2023-07-01-preview"
openai.api_key = OPENAI_API_KEY

# MODEL_NAME = 'gpt-4-1106-preview' # 128k 版本
# MODEL_NAME = 'CodeLlama-7b-hf'
# MODEL_NAME = 'gpt-4-32k' # 0613版本
# MODEL_NAME = 'gpt-4' # 0613版本
MODEL_NAME = 'gpt-35-turbo-16k' # 0613版本