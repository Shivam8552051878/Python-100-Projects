import tkinter

window = tkinter.Tk()
window.title("Miles to kilometer converter")
window.minsize(width=400, height=400)

def calculate():
    km = round(float(user_input.get()) * 1.60934, 2)
    output.config(text=str(km))


is_equal_to = tkinter.Label(text="Is equal to:")
is_equal_to.grid(row=1, column=0)

user_input = tkinter.Entry(width=7)
user_input.grid(row=0, column=1)

output = tkinter.Label(bg="white", width=7)

output.grid(row=1, column=1)

button = tkinter.Button(text="CALCULATE", command=calculate)
button.grid(row=2,column=1)


miles_title = tkinter.Label(text="Miles")
miles_title.grid(row=0, column=2)




kilometer_title = tkinter.Label(text="Kilometer")
kilometer_title.grid(row=1, column=2)


window.mainloop()