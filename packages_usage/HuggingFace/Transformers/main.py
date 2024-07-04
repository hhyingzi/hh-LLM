from dotenv import load_dotenv
import os

# 环境变量
load_dotenv("transformers.env")
print('HF_HOME=' + os.getenv('HF_HOME'))
print('HF_HUB_CACHE=' + os.getenv('HF_HUB_CACHE'))


from transformers import pipeline

# 文本生成推理任务演示。默认模型 “openai-community/gpt2”
prompt = "Hugging Face is a community-based open-source platform for machine learning."
generator = pipeline(task="text-generation", device_map="auto")
response = generator(prompt)  # doctest: +SKIP
print(response[0]['generated_text'])