import os
from dotenv import load_dotenv
from openai import OpenAI

from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage


load_dotenv(os.path.dirname(__file__)+"/llamaindex.env", override=True)
client = OpenAI()

def complete_with_closeai():
    # non-streaming
    resp = OpenAI().complete("香蕉是什么颜色的？")
    print(resp)


def chat_with_closeai():
    messages = [
        ChatMessage(
            role="system", content="你是一个编程助手。"
        ),
        ChatMessage(role="user", content="香蕉是什么颜色的？"),
    ]
    resp = OpenAI().chat(messages)
    print(resp)

if __name__ == '__main__':
    complete_with_closeai()