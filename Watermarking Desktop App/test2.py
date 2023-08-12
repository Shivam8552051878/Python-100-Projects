import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_images():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        for file_path in file_paths:
            display_image(file_path)

def display_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((300, 300))  # Resize the image to fit within a 300x300 box (optional)
    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack()

root = tk.Tk()
root.title("Multiple Image Uploader")
print(root.frame())
# tk.Frame.
upload_button = tk.Button(root, text="Select Images", command=select_images)
upload_button.pack()

root.mainloop()
