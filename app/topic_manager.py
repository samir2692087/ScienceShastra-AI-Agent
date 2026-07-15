import json
import random
from pathlib import Path

TOPICS_FILE = Path("data/topics.json")
USED_FILE = Path("data/used_topics.json")


def load_topics():
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def load_used():
    with open(USED_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_used(data):
    with open(USED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def get_new_topic():
    topics = load_topics()
    used = load_used()

    available = [t for t in topics if t not in used]

    if not available:
        used = []
        available = topics

    topic = random.choice(available)

    used.append(topic)

    save_used(used)

    return topic
