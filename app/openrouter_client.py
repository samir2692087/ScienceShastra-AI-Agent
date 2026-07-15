import requests

from config import OPENROUTER_API_KEY, MODEL

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_text(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.8
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data,
        timeout=120
    )

    print(response.status_code)
    print(response.text)
    return response.text

    return response.json()["choices"][0]["message"]["content"]
