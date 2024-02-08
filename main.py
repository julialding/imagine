import os, sys
from pathlib import Path
# from build.gui2 import image_uploaded_check, image_details
from image_classifier import image_processed, classify
from image_descriptor import generate_description
from database_handler import *


CURRENT_PATH = Path(__file__).parent
TEMP_PATH = CURRENT_PATH / Path("temp")

gui_path = os.path.join(CURRENT_PATH, "build/gui.py")
gui1_path = os.path.join(CURRENT_PATH, "build/gui1.py")
print(gui_path)

os.system(f'python "{gui_path}"')

# Once the image is uploaded, the AI can run on 
temp_image_path = TEMP_PATH / Path("local_image.png")
loop = True
while loop:
    if getLatestStatus() == "Pending":
        # print(image_details()) # replace with db reading
        classify()
        loop = False

    if image_processed():
        os.system(f'python "{gui1_path}"')
        generate_description()
        os.remove(temp_image_path)




