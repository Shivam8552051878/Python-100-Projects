import tkinter



window = tkinter.Tk()
window.title("First Project")
window.minsize(width=400, height=300)

label = tkinter.Label(text="tkinter project")
label.grid(row=0, column=0)

def change_label():
    new_text = input_value.get()
    label["text"] = new_text

fred = tkinter.Button(text="Click me", command=change_label)
fred.grid(row=1, column=1)

fred1 = tkinter.Button(text="Click me", command=change_label)
fred1.grid(row=2, column=0)


input_value = tkinter.Entry()
input_value.grid(row=3, column=3)
print(input_value.get())

window.mainloop()
