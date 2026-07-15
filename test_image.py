from app.image_client import generate_image

prompt = """
A premium educational science illustration of a futuristic space rocket launching
into space with Earth in the background, highly detailed, cinematic lighting,
photorealistic, 8K, science education poster.
"""

image_path = generate_image(prompt)

print(f"Image saved to: {image_path}")
print("Status:", response.status_code)
print("Content-Type:", response.headers.get("content-type"))
print("Size:", len(response.content))
