import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    def ask_openai(self, prompt, model):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly and humorous assistant. Your name is Skynet. Respond with warmth and a touch of sarcasm.",
                    "name": "Skynet"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            top_p=0.9,
            max_tokens=300)
        print(response)
        return response.choices[0].message.content.strip()
