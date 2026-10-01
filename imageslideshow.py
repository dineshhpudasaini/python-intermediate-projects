from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slider Viewer")

#list of image path
image_path = [
    r"C:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot 2026-10-01 203258.png",
    r"C:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot 2026-10-01 203319.png",
    r"C:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot 2026-10-01 203350.png",
    r"C:\Users\acer\OneDrive\Pictures\Screenshots\Screenshot 2026-10-01 203409.png"
]

#resize the image to 1080x1080
image_size = (1080,1080)
iamges = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(image) for image in iamges]

label = tk.Label(root)
label.pack()

def update_images():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_images()

play_button = tk.Button(root , text = "play slideshow" , command = start_slideshow)
play_button.pack()

root.mainloop()