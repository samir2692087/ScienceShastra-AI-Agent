import time
from google import genai
from google.genai.errors import ServerError
from config import GEMINI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)


def generate_text(prompt: str):

    for attempt in range(5):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            return response.text

        except ServerError:
            print(f"Server busy. Retry {attempt+1}/5")
            time.sleep(10)

    raise Exception("Gemini server busy after 5 retries.")
