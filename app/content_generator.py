import os

HISTORY_FILE = "history/topics.txt"


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_topic(topic):
    os.makedirs("history", exist_ok=True)

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(topic + "\n")


def build_prompt():
    history = load_history()

    history_text = "\n".join(history[-100:])

    prompt = f"""
You are ScienceShastra AI.

Generate ONE completely NEW science topic.

Rules:
- Never repeat any topic from the history below.
- Topic must be interesting.
- Suitable for YouTube Shorts.
- Suitable for Facebook, Instagram and X.
- Biology, Physics, Chemistry, Space, AI, Technology, Earth Science or Medical Science.

Previously used topics:
{history_text}

Return ONLY the topic title.
"""

    return prompt
