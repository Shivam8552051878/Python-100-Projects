import tkinter as tk
import Helper.customWindow


class UploadFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.label_upload = tk.Label(text="Watermarking Desktop Application", font=("roman", 30, "bold"),
                                     fg="lightblue")
        self.label_upload.grid()
        self.list_images = tk.Button(text="Upload Images", command=Helper.customWindow.HelpFunc().select_multi_images)
        self.list_images.grid()


class CustomFrame(tk.Frame):
    def __init__(self, master , on_registration = None, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        self.on_registration = on_registration

        self.label_upload = tk.Label(text="Watermarking Desktop Application", font=("roman", 30, "bold"),
                                  fg="lightblue", bg="blue")
        self.label_upload.grid(row=10, column=2)
        self.list_images = tk.Button(width=20, height=5, text="Upload Images",
                                     command=Helper.customWindow.HelpFunc().select_multi_images, bg="blue")
        self.list_images.grid(row=12, column=2)
        self.next_button = tk.Button(width=20, height=5, text="NEXT",
                                     command=self.submit_form, bg="blue")
        self.next_button.grid(row=12, column=2)

    def submit_form(self):
        if self.on_registration is not None:
            self.on_registration(self.list_images)
class OptionFrame(tk.Frame):
    def __init__(self, master, image_path, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        print("hello")
        self.welcome = tk.Label(text="Hello World")
        self.welcome.grid(row=0, column=0)



if __name__ == "__main__":
    root = tk.Tk()

    root.title("Watermarking Desktop Application")
    def on_registration(image_list):
        uploadImage.pack_forget()  # Hide the registration form
        welcome_frame = OptionFrame(root, image_path=image_list)
        welcome_frame.pack()
    root.minsize(width=600, height=600)
    root.config(bg="blue")
    uploadImage = CustomFrame(root, on_registration=on_registration)
    root.mainloop()
