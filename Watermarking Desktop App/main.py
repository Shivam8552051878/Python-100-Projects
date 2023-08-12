import tkinter as tk

from Helper.customWindow import HelpFunc


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            # print("!stdojen")
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Add Text Image",
                  command=lambda: master.switch_frame(AddText)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(AddLogo)).pack()


class AddText(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add text Image.").pack(side="top", fill="x", pady=10)
        self.upload = tk.Button(self, text="upload image", command=HelpFunc().select_multi_images).pack()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

    def data(self):
        print(self.upload_images)


class AddLogo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Add Logo Image.").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
