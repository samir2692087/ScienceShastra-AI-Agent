import os
import time
import fal_client

FAL_KEY = os.getenv("FAL_KEY")

os.environ["FAL_KEY"] = FAL_KEY


def generate_image(prompt: str, output_path="output/image.png"):

    os.makedirs("output", exist_ok=True)

    result = fal_client.subscribe(
        "fal-ai/flux/dev",
        arguments={
            "prompt": prompt,
            "image_size": "landscape_4_3",
            "num_images": 1,
            "enable_safety_checker": True
        }
    )

    image_url = result["images"][0]["url"]

    import requests

    img = requests.get(image_url, timeout=300)

    img.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(img.content)

    return output_path
