import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

def generate_image(prompt: str, output_path="output/image.png"):
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt
        },
        timeout=300
    )

    if response.status_code != 200:
        raise Exception(
            f"Hugging Face Error {response.status_code}: {response.text}"
        )

    os.makedirs("output", exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(response.content)

    return output_path
