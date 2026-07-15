import json

from app.gemini_client import generate_text
from app.prompts import SYSTEM_PROMPT, CONTENT_PROMPT
from app.topic_manager import get_new_topic


def main():
    # Get a unique topic
    topic = get_new_topic()

    # Build prompt
    prompt = f"""
{SYSTEM_PROMPT}

Today's Science & Technology Topic:
{topic}

{CONTENT_PROMPT}
"""

    # Generate AI response
    response = generate_text(prompt)

    print("\n========== RAW AI OUTPUT ==========\n")
    print(response)

    try:
        # Parse JSON response
        data = json.loads(response)

        print("\n========== GENERATED CONTENT ==========\n")

        print(f"Topic: {data['topic']}")
        print(f"Category: {data['category']}")

        print("\n========== ENGLISH ==========\n")
        print(data["english_title"])
        print()
        print(data["english_post"])

        print("\n========== HINDI ==========\n")
        print(data["hindi_title"])
        print()
        print(data["hindi_post"])

        print("\n========== IMAGE PROMPT ==========\n")
        print(data["image_prompt"])

        print("\n========== HASHTAGS ==========\n")
        print(" ".join(data["hashtags"]))

    except Exception as e:
        print("\n❌ Invalid JSON received from Gemini.")
        print(e)
        print(response)


if __name__ == "__main__":
    main()
