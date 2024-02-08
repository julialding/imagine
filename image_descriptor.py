# AI Code that will run on the image to generate a description
from openai import OpenAI
import os
from database_handler import *
import base64

global descriptioned
os.environ['OPENAI_API_KEY'] = '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'
OUTPUT_PATH = Path(__file__)
# Microsoft code here

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def generate_description():
    print("Classifying image")
    # global descriptioneds
    descriptioned = True
    base64_image = encode_image(os.path.join(OUTPUT_PATH.parent, "temp\local_image.png"))
    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "You are genrating text decriptions for scences in natural disasters. Anwer the question: What’s in this image? Your response should usefull to a responder trying to find relevant information about the dangers presented. Look for any people, anmals, fires, flood/ water, or any other significant details and dangers. Please, do not use any commas and write all the information in text block"},
            {
            "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    print(response.choices[0])
    text_response = response.choices[0].message.content
    print(text_response)
    updateLatestData("Processed", text_response)
    # save to db


# generate_description()
# returns if image has a description ready
def image_decriptioned():
    return descriptioned

def reset():
    global descriptioned
    descriptioned = False