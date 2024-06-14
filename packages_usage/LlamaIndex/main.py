import os
from dotenv import load_dotenv
from openai import OpenAI

from llama_index.llms.openai import OpenAI


load_dotenv(".env.llamaindex")

def chat_with_closeai():
    # non-streaming
    resp = OpenAI().complete("Paul Graham is ")
    print(resp)


if __name__ == '__main__':
    chat_with_closeai()