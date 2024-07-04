import os
from dotenv import load_dotenv
from openai import OpenAI

def check_env():
    # 加载环境变量
    load_dotenv("zhipuai.env")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    print(OPENAI_API_KEY)


def chat_with_closeai():
    load_dotenv("zhipuai.env")
    client = OpenAI()
    completion = client.chat.completions.create(
        model="glm-4",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "你是谁"}
        ]
    )
    print(completion.choices[0].message)


if __name__ == '__main__':
    chat_with_closeai()