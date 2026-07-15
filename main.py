import json

from app.gemini_client import generate_text
from app.output import save_output


with open("data/topics.json", "r", encoding="utf-8") as f:
    topics = json.load(f)

topic = topics[0]

english_prompt = f"""
Write a Facebook post in English about:

{topic}

Requirements:
- 120-180 words
- Beginner friendly
- Scientifically accurate
- End with a question
- Include 5 hashtags
"""

hindi_prompt = f"""
'{topic}' पर प्राकृतिक हिन्दी में Facebook पोस्ट लिखिए।

आवश्यकताएँ:
- 120-180 शब्द
- सरल भाषा
- वैज्ञानिक रूप से सही
- अंत में प्रश्न
- 5 हैशटैग
"""

image_prompt = f"""
Create a premium realistic science illustration about:

{topic}

Ultra detailed
Professional lighting
Educational style
High quality
"""

english = generate_text(english_prompt)
hindi = generate_text(hindi_prompt)

hashtags = """#Science
#Technology
#Education
#Learning
#ScienceShastra"""

save_output(
    english=english,
    hindi=hindi,
    image_prompt=image_prompt,
    hashtags=hashtags,
    topic=topic
)

print("✅ All files generated successfully.")
