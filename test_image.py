from app.image_client import generate_image

def main():
    prompt = """
Create a premium educational science illustration.

Topic:
How do rockets work?

Style:
Modern 3D educational infographic

Background:
Deep blue space

Include:
Rocket
Earth
Stars
Orange exhaust flames
Educational labels

Ultra realistic
8K
High quality
"""

    response = generate_image(prompt)

    print(response)


if __name__ == "__main__":
    main()
