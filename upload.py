import tkinter as tk
from tkinter import filedialog
from PIL import Image
import cv2
import os

def upload_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    img.save('local_image.jpg')
    show_loading_screen()

def take_snapshot():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('snapshot.jpg', frame)
    cap.release()
    show_loading_screen()

def show_loading_screen():
    for widget in root.winfo_children():
        widget.destroy()
    loading_label = tk.Label(root, text="Loading...")
    loading_label.pack()

root = tk.Tk()

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

snapshot_button = tk.Button(root, text="Take Snapshot", command=take_snapshot)
snapshot_button.pack()

root.mainloop()