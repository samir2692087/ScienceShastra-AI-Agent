import json
import os

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

    print("\n=========== RAW AI OUTPUT ===========\n")
    print(response)

    try:
        # Parse JSON response
        data = json.loads(response)

        # Create output folder
        os.makedirs("output", exist_ok=True)

        # Save complete JSON
        with open("output/post.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Save individual files
        with open("output/english_post.txt", "w", encoding="utf-8") as f:
            f.write(data["english_post"])

        with open("output/hindi_post.txt", "w", encoding="utf-8") as f:
            f.write(data["hindi_post"])

        with open("output/image_prompt.txt", "w", encoding="utf-8") as f:
            f.write(data["image_prompt"])

        with open("output/youtube_title.txt", "w", encoding="utf-8") as f:
            f.write(data["youtube_title"])

        with open("output/youtube_description.txt", "w", encoding="utf-8") as f:
            f.write(data["youtube_description"])

        with open("output/facebook_caption.txt", "w", encoding="utf-8") as f:
            f.write(data["facebook_caption"])

        with open("output/instagram_caption.txt", "w", encoding="utf-8") as f:
            f.write(data["instagram_caption"])

        with open("output/x_post.txt", "w", encoding="utf-8") as f:
            f.write(data["x_post"])

        with open("output/hashtags.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(data["hashtags"]))

        print("\n✅ All files saved successfully!")

        print("\n=========== GENERATED CONTENT ===========\n")
        print(f"Topic: {data['topic']}")
        print(f"Category: {data['category']}")

        print("\n=========== ENGLISH ===========\n")
        print(data["english_title"])
        print()
        print(data["english_post"])

        print("\n=========== HINDI ===========\n")
        print(data["hindi_title"])
        print()
        print(data["hindi_post"])

        print("\n=========== IMAGE PROMPT ===========\n")
        print(data["image_prompt"])

        print("\n=========== HASHTAGS ===========\n")
        print(" ".join(data["hashtags"]))

    except Exception as e:
        print("\n❌ Invalid JSON received from AI.\n")
        print(e)
        print(response)


if __name__ == "__main__":
    main()
