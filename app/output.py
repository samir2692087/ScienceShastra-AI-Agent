from pathlib import Path
import json

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_output(english, hindi, image_prompt, hashtags, topic):
    (OUTPUT_DIR / "english_post.md").write_text(
        english,
        encoding="utf-8"
    )

    (OUTPUT_DIR / "hindi_post.md").write_text(
        hindi,
        encoding="utf-8"
    )

    (OUTPUT_DIR / "image_prompt.txt").write_text(
        image_prompt,
        encoding="utf-8"
    )

    (OUTPUT_DIR / "hashtags.txt").write_text(
        hashtags,
        encoding="utf-8"
    )

    metadata = {
        "topic": topic
    }

    with open(
        OUTPUT_DIR / "metadata.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)

    print("✅ Output files saved.")
