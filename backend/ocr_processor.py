import base64
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()
def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
def extract_text_from_image(image_path):
    # Convert image to Base64
    base64_image = encode_image(image_path)

    # OpenAI API request for OCR
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract the text from this image.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            }
        ],
    )

    # Extract and print the detected text
    return (response.choices[0].message.content)
