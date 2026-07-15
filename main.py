from gemini import generate_post

prompt = """
Write a short Science & Technology Facebook post in English.
Keep it factual, engaging, and under 150 words.
"""

print(generate_post(prompt))
