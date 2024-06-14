import os
from dotenv import load_dotenv
from openai import OpenAI

def check_env():
    # 加载环境变量
    load_dotenv(".env.closeai")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    print(OPENAI_API_KEY)


# closeAI 是一个 openai 中转商：https://doc.closeai-asia.com/
def chat_with_closeai():
    load_dotenv(".env.closeai")
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "你是谁"}
        ]
    )
    print(completion.choices[0].message)


if __name__ == '__main__':
    chat_with_closeai()