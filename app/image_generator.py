import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-dev"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def generate_image(prompt, output_path="output/image.png"):
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt
        },
        timeout=300
    )

    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print("✅ Image generated successfully!")
