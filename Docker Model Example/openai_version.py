from openai import OpenAI
import os


BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

client = OpenAI(
    base_url=BASE_URL,
    api_key="anything")

MODEl_NAME = "ai/smollm2:latest"

PROMPT = "Explain how transformers work."

messages = [
    {
        "role": "user",
        "content": PROMPT
    }
]

response = client.chat.completions.create(
    model=MODEl_NAME,
    messages=messages
)
print(response.choices[0].message.content)  # Print the response content