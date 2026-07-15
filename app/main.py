import json

from app.gemini_client import generate_text
from app.prompts import SYSTEM_PROMPT, CONTENT_PROMPT


def main():
    prompt = f"""
{SYSTEM_PROMPT}

{CONTENT_PROMPT}
"""

    response = generate_text(prompt)

    print("\n========== AI OUTPUT ==========\n")
    print(response)

    try:
        data = json.loads(response)

        print("\n========== PARSED ==========\n")
        print("Topic:", data["topic"])
        print("Category:", data["category"])
        print("English Title:", data["english_title"])
        print("Hindi Title:", data["hindi_title"])

    except Exception:
        print("\nResponse is not valid JSON.")


if __name__ == "__main__":
    main()
