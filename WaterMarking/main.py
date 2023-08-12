import tkinter as tk
from customWindow import HelpFunc
window = tk.Tk()


tk.Label(text="This is the start page").pack(side="top", fill="x", pady=10)
uploaded_image = tk.Button(text="Upload Image", command=HelpFunc().select_multi_images).pack()
print(uploaded_image)
window.mainloop()