import tkinter as tk

import Helper.customWindow


class UploadFrame(tk.Frame):
    def __init__(self, master, on_registration, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.on_registration = on_registration
        self.label_upload = tk.Label(text="Watermarking Desktop Application", font=("roman", 30, "bold"),
                                     fg="lightblue")
        self.label_upload.pack(side=tk.LEFT)
        self.list_images = tk.Button(width=20, height=5, text="Upload Images",
                                     command=Helper.customWindow.HelpFunc().select_multi_images, bg="blue")
        self.list_images.pack(side=tk.LEFT)
        self.next_btn = tk.Button(width=20, height=5, text="NEXT",
                                     command=self.next, bg="blue")
        self.next_btn.pack(side=tk.LEFT)

    def next(self):
        if self.on_registration != None:
            self.on_registration(self.list_images)




class OptionFrame(tk.Frame):
    def __init__(self, master, image_path, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        print("hello")
        self.welocme = tk.Label(text="Hello World")
        self.welocme.pack(side=tk.LEFT)



def on_registration(image_path):
        uploadImage.pack_forget()  # Hide the registration form
        welcome_frame = OptionFrame(root, image_path)
        welcome_frame.pack()


root = tk.Tk()
root.title("Watermarking Desktop Application")
root.minsize(width=600, height=600)
root.config(bg="blue")
uploadImage = UploadFrame(root, on_registration=on_registration)
root.mainloop()
