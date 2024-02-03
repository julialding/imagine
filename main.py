import os, sys
from pathlib import Path
from build.gui2 import image_uploaded_check, image_details
from image_classifier import image_processed, classify
from image_descriptor import generate_description


CURRENT_PATH = Path(__file__).parent
TEMP_PATH = CURRENT_PATH / Path("temp")

gui_path = CURRENT_PATH / Path("build/gui.py")
gui1_path = CURRENT_PATH / Path("build/gui1.py")
print(gui_path)

os.system(f'python "{gui_path}"')

# Once the image is uploaded, the AI can run on 
temp_image_path = TEMP_PATH / Path("local_image.png")
loop = True
while loop:
    if os.path.exists(temp_image_path):
        print(image_details())
        classify()
        loop = False

    if image_processed():
        os.system(f'python "{gui1_path}"')
        generate_description()





