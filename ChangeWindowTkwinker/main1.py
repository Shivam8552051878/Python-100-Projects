import tkinter as tk

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("Main Window")

open_window_button = tk.Button(root, text="Open New Window", command=open_new_window)
open_window_button.pack(pady=20)

root.mainloop()
