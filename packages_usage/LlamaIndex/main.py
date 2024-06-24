import os
from dotenv import load_dotenv
from openai import OpenAI

from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage


load_dotenv(".env.llamaindex")

def complete_with_closeai():
    # non-streaming
    resp = OpenAI().complete("Paul Graham is ")
    print(resp)


def chat_with_closeai():
    messages = [
        ChatMessage(
            role="system", content="你是一个编程助手。"
        ),
        ChatMessage(role="user", content="gpt-3.5-turbo-instruct 是什么，和gpt-3.5-turbo什么区别"),
    ]
    resp = OpenAI().chat(messages)
    print(resp)

if __name__ == '__main__':
    complete_with_closeai()