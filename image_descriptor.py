# AI Code that will run on the image to generate a description
from openai import OpenAI
import os
global descriptioned
# os.environ['OPENAI_API_KEY'] = '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'
# Microsoft code here
def generate_description():
    print("Classifying image")
    # global descriptioneds
    descriptioned = True
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s in this image?"},
            {
            "type": "image_url",
            "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0])
    # save to db


generate_description()
# returns if image has a description ready
def image_decriptioned():
    return descriptioned

def reset():
    global descriptioned
    descriptioned = False