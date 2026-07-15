from app.gemini_client import generate_text
from app.prompts import SYSTEM_PROMPT, ENGLISH_POST_PROMPT

prompt = f"""
{SYSTEM_PROMPT}

{ENGLISH_POST_PROMPT}
"""

result = generate_text(prompt)

print(result)
