# https://platform.openai.com/docs/quickstart

import os
from dotenv import load_dotenv
from openai import OpenAI

# os.eviron['MODEL'] = 
os.eviron['OPENAI_API_BASE'] = http://localhost:8080/v1/chat/completions
os.eviron['OPENAI_BASE_URL'] = http://localhost:8080/v1/chat/completions

client = OpenAI()

def chat_with_openai():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    print(completion.choices[0].message.content)

def response_with_json():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    )
    print(response.choices[0].message.content)

if __name__ == '__main__':
    chat_with_openai()