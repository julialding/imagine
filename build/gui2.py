import sys
import os
import tkinter as tk
import tkinter.messagebox as tk1
import tkinter.filedialog
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import cv2
from datetime import datetime
import geocoder
from geopy.geocoders import Nominatim
import geopy
import csv


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = tk.Tk()
window.title("Natural Disasters Response System")
logo = tk.PhotoImage(file=os.path.join(ASSETS_PATH, "iconbitmap.gif"))
window.call('wm', 'iconphoto', window._w, logo)
window.geometry("862x519")
window.configure(bg="#DDD3BA")

global output_path

image_uploaded = False

latitude = None
longitude = None
timestamp = None


def select_path():
    f_types = [('Image Files', ('*.jpg', '*.jpeg', '*.png')), ('All Files', '*.*')]
    output_path = filedialog.askopenfilename(filetypes=f_types)
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)
    getGPS()

# replace geocode 
# print(str(Nominatim(user_agent="Natural Disaster Response").geocode("192.0.2.1").latitude))

def getGPS():
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get current location
    geolocator = Nominatim(user_agent="Natural Disaster Response")
    location = geocoder.ip("me")
    latitude = location.latlng[0]
    longitude = location.latlng[1]
    # include error handling for no connection
    print(str(latitude))
    print(longitude)

    # Update GUI with GPS information
    entry_2.delete(0, tk.END)
    entry_2.insert(0, str(longitude))
    entry_1.delete(0, tk.END)
    entry_1.insert(0, str(latitude))
    entry_3.delete(0, tk.END)
    entry_3.insert(0, str(timestamp))


def take_snapshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    path = os.path.join(OUTPUT_PATH.parent, "temp/snapshot.jpg")
    cv2.imwrite(str(path), frame)
    global output_path
    output_path = path
    cap.release()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, "Snapshot taken!")
    getGPS()

def get_new_id():
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'r') as file:
        next(file)
        reader = csv.reader(file)
        last_id = 0
        for row in reader:
            last_id = int(row[0])
        new_id = last_id + 1
    return new_id


def upload_image():
    global output_path
    img = Image.open(output_path)
    global latitude, longitude, timestamp
    # store gps info from textboxes into csv
    latitude = entry_1.get()
    longitude = entry_2.get()
    timestamp = entry_3.get()
    # update db here and set status
    path = os.path.join(OUTPUT_PATH.parent, "temp/local_image.png")
    img.save(path)

    # Get the last previous id number in the database.csv file and increase it by one
    new_id = get_new_id()

    image_path = os.path.join(OUTPUT_PATH.parent, f"images/image_{new_id}.png")
    outImg = Image.open(path)
    outImg.save(image_path)
    print(image_path)

    # Create a new line in the database.csv file
    with open(os.path.join(OUTPUT_PATH.parent, "database.csv"), 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([new_id, image_path, latitude, longitude, timestamp, "Pending", " "])

    path_entry.delete(0, tk.END)
    path_entry.insert(0, "Saved! Please close all windows to continue.")
    tk.messagebox.showinfo(
            title="Success!", message="Your image has sucessfully been saved and will be processed. \n\nPlease close all windows to continue")
    global image_uploaded
    image_uploaded = True

def btn_clicked():
    global output_path
    output_path = path_entry.get()
    output_path = output_path.strip()
    
    if not output_path:
        tk.messagebox.showerror(
            title="Invalid Path!", message="Enter a valid output path.")
        return
    
    upload_image()


def image_uploaded_check():
    return image_uploaded


def reset_image_uploaded():
    global image_uploaded
    image_uploaded = False


def image_details():
    return latitude, longitude, timestamp


canvas = tk.Canvas(
    window,
    bg="#DDD3BA",
    height=519,
    width=862,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    431.0,
    0.0,
    862.0,
    519.0,
    fill="#FCFCFC",
    outline="")

button_image_1 = tk.PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = tk.Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat"
)
button_1.place(
    x=557.0,
    y=401.0,
    width=180.0,
    height=55.0
)

button_image_2 = tk.PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = tk.Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=123.0,
    y=401.0,
    width=180.0,
    height=55.0
)

button_image_3 = tk.PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=take_snapshot,
    relief="flat"
)
button_3.place(
    x=123.0,
    y=401.0,
    width=180.0,
    height=55.0
)

canvas.create_text(
    105.0,
    74.0,
    anchor="nw",
    text="Add a diaster image ",
    fill="#5C4E3D",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_text(
    482.0,
    74.0,
    anchor="nw",
    text="Enter the details.",
    fill="#505485",
    font=("Roboto Bold", 24 * -1)
)

entry_image_1 = tk.PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    715.0,
    167.5,
    image=entry_image_1
)
entry_1 = tk.Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=619.0,
    y=137.0,
    width=192.0,
    height=59.0
)

entry_image_2 = tk.PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    715.0,
    248.5,
    image=entry_image_2
)
entry_2 = tk.Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=619.0,
    y=218.0,
    width=192.0,
    height=59.0
)

entry_image_3 = tk.PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    715.0,
    329.5,
    image=entry_image_3
)
entry_3 = tk.Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=619.0,
    y=299.0,
    width=192.0,
    height=59.0
)

canvas.create_text(
    40.0,
    148.0,
    anchor="nw",
    text="Upload a local image",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 20 * -1)
)

canvas.create_text(
    477.0,
    153.0,
    anchor="nw",
    text="Latitude:",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 20 * -1)
)

canvas.create_text(
    477.0,
    236.0,
    anchor="nw",
    text="Longitude:",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 20 * -1)
)

canvas.create_text(
    477.0,
    312.0,
    anchor="nw",
    text="Timestamp:",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 20 * -1)
)

canvas.create_text(
    40.0,
    325.0,
    anchor="nw",
    text="Or, take a snapshot of a connected camera",
    fill="#5C4E3D",
    font=("LibreBaskerville Regular", 16 * -1)
)

entry_image_4 = tk.PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    212.5,
    218.5,
    image=entry_image_4
)
path_entry = tk.Entry(
    bd=0,
    bg="#F1F5FF",
    fg="#000716",
    highlightthickness=0
)
path_entry.place(
    x=52.0,
    y=188.0,
    width=321.0,
    height=59.0
)

button_image_4 = tk.PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = tk.Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=select_path,
    relief="flat"
)
button_4.place(
    x=345.0,
    y=207.0,
    width=24.0,
    height=22.0
)
window.resizable(False, False)
window.mainloop()
