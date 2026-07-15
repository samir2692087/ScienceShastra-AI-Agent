from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_text(prompt: str):
    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
