import time
from google import genai
from google.genai.errors import ServerError
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

MODELS = [
    "gemini-3.5-flash",
    "gemini-2.5-flash"
]

def generate_text(prompt: str):
    last_error = None

    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                return response.text

            except ServerError as e:
                print(f"{model} busy. Retry {attempt+1}/3...")
                last_error = e
                time.sleep(5)

            except Exception as e:
                last_error = e
                break

    raise last_error
