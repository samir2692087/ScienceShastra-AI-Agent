import json
import os

def export_markdown():
    with open("output/post.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    md = f"""# {data['english_title']}

## Topic
{data['topic']}

## Category
{data['category']}

---

# English Post

{data['english_post']}

---

# Hindi Title

{data['hindi_title']}

# Hindi Post

{data['hindi_post']}

---

# Image Prompt

{data['image_prompt']}

---

# Hashtags

{' '.join('#'+h for h in data['hashtags'])}
"""

    with open("output/post.md", "w", encoding="utf-8") as f:
        f.write(md)

    print("✅ Markdown exported.")

if __name__ == "__main__":
    export_markdown()
