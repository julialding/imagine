import os, sys
from pathlib import Path
# from build.gui2 import image_uploaded_check, image_details
import tkinter.messagebox as tk1
from image_classifier import image_processed, classify
from image_descriptor import generate_description
from database_handler import *
import tkinter as tk
import psutil

def guiNotRunning():
    for process in psutil.process_iter():
        guiStatus = True
        restStatus = True
        if process.name() == "gui1.py" or process.name() == "gui2.py" or process.name() == "gui3.py":
            restStatus =  False
        if process.name() == "gui.py":
            guiStatus = False
    return guiStatus, restStatus

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
    status  = getLatestStatus()

    if status == "Pending":
        generate_description()
        os.system(f'python "{gui1_path}"')
        loop = True

    guiStatus, restStatus = guiNotRunning()
    if status == "Processed":
        if(not restStatus):
            os.system(f'python "{gui_path}"')
        if not guiStatus and restStatus:
            continue
        else:
            exit()

