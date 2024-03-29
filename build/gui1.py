import sys
import os
import  tkinter as tk
import tkinter.messagebox as tk1
import tkinter.filedialog
from pathlib import Path
# from image_classifier import image_significant

image_significant = True

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets/frame1")

def run_gui():
    gui_path = os.path.join(OUTPUT_PATH, "gui.py")
    print(gui_path)
    os.system(f'python "{gui_path}"')
    window.destroy()
    exit()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Natural Disasters Response System")
logo = tk.PhotoImage(file=os.path.join(ASSETS_PATH, "iconbitmap.gif"))
window.call('wm', 'iconphoto', window._w, logo)
window.geometry("862x519")
window.configure(bg = "#DDD3BA")



canvas = Canvas(
    window,
    bg = "#DDD3BA",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
"""
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_gui,
    relief="flat"
)
button_1.place(
    x=557.0,
    y=401.0,
    width=180.0,
    height=55.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=108.0,
    y=401.0,
    width=180.0,
    height=55.0
)
"""
canvas.create_text(
    178.0,
    43.00000000000001,
    anchor="nw",
    text="Image Classification Successful!",
    fill="#304F49",
    font=("Roboto Bold", 32 * -1)
)
if(image_significant):
    canvas.create_text(
        83.0,
        119.0,
        anchor="nw",
        text="Important image, description generated and saved in the database.",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

else:
    canvas.create_text(
        83.0,
        119.0,
        anchor="nw",
        text="Image is not significant, nothing will be done.",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

canvas.create_text(
    83.0,
    244.0,
    anchor="nw",
    text="Image process was successful, and the appropriate action will be taken. \nOnly significant images are saved in the database to make finding critical locations easier. \n\n\n\nPlease cloase the program to finish. \nIf you want to add more images or search the database, please restart the program.",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
