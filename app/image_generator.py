import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"

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

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("content-type"))
    print("Response Preview:")
    print(response.text[:500])

    response.raise_for_status()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(response.content)

    print("✅ Image generated successfully!")
