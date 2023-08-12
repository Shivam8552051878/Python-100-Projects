# import tkinter as tk
#
# def show_page(page_number):
#     # Clear the current content
#     for widget in main_frame.winfo_children():
#         widget.pack_forget()
#
#     # Show the corresponding page
#     if page_number == 1:
#         label1.pack()
#     elif page_number == 2:
#         label2.pack()
#     elif page_number == 3:
#         label3.pack()
#
# # Create the main tkinter window
# root = tk.Tk()
# root.title("Single Window Example")
#
# # Create a frame to hold the dynamic content
# main_frame = tk.Frame(root)
# main_frame.pack(padx=20, pady=20)
#
# # Labels for different "pages"
# label1 = tk.Label(main_frame, text="This is Page 1", font=("Arial", 16))
# label2 = tk.Label(main_frame, text="This is Page 2", font=("Arial", 16))
# label3 = tk.Label(main_frame, text="This is Page 3", font=("Arial", 16))
#
# # Show the initial page (you can change this number to display different pages at start)
# show_page(1)
#
# # Buttons to switch between pages
# button1 = tk.Button(root, text="Page 1", command=lambda: show_page(1))
# button2 = tk.Button(root, text="Page 2", command=lambda: show_page(2))
# button3 = tk.Button(root, text="Page 3", command=lambda: show_page(3))
#
# button1.pack()
# button2.pack()
# button3.pack()
#
# # Run the main tkinter event loop
# root.mainloop()

import tkinter as tk

def show_page(page_number):
    # Clear the current content
    for widget in main_frame.winfo_children():
        widget.pack_forget()

    # Show the corresponding page
    if page_number == 1:
        label1.pack()
    elif page_number == 2:
        label2.pack()
    elif page_number == 3:
        label3.pack()

# Create the main tkinter window
root = tk.Tk()
root.title("Single Window Example")

# Create a frame to hold the dynamic content
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Labels for different "pages"
label1 = tk.Label(main_frame, text="This is Page 1", font=("Arial", 16))
label2 = tk.Label(main_frame, text="This is Page 2", font=("Arial", 16))
label3 = tk.Label(main_frame, text="This is Page 3", font=("Arial", 16))

# Buttons to switch between pages
button1 = tk.Button(root, text="Page 1", command=lambda: show_page(1))
button2 = tk.Button(root, text="Page 2", command=lambda: show_page(2))
button3 = tk.Button(root, text="Page 3", command=lambda: show_page(3))

button1.pack(side=tk.LEFT, padx=5, pady=5)
button2.pack(side=tk.LEFT, padx=5, pady=5)
button3.pack(side=tk.LEFT, padx=5, pady=5)

# Show the initial page (you can change this number to display different pages at start)
show_page(1)

# Run the main tkinter event loop
root.mainloop()
