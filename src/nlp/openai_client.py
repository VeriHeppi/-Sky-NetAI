import os
from dotenv import load_dotenv
from openai import OpenAI

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.cache = {}

    def ask_openai(self, prompt, model):
        if prompt in self.cache:
            return self.cache[prompt]

        response = self.client.chat.completions.create(
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
        result = response.choices[0].message.content.strip()
        self.cache[prompt] = result
        return result
