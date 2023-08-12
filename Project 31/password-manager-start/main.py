import tkinter
from tkinter.constants import END
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import create_password
import pyperclip
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = website_lable_input.get()
    email = email_lable_input.get()
    password = password_lable_input.get()
    password_dic = {
        website: {
            "email": email,
            "password": password
        }
    }
    # dialog box
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="OOPS", message="Please don't leave any field empty")
    else:
        try:
            with open("./password.json") as file:
                # Reading data
                data = json.load(file)
        except FileNotFoundError:
            with open("./password.json", "w") as password_data:
                # Writing json data
                json.dump(obj=password_dic, fp=password_data, indent=4)
        else:
            with open("./password.json", "w") as password_data:
                # Updating json file
                data.update(password_dic)
                # Writing json data
                json.dump(data, password_data, indent=4)
        finally:
            pyperclip.copy(password)
            website_lable_input.delete(0, END)
            password_lable_input.delete(0, END)


def set_password():
    password = create_password.PaassworGenerator().random_password()
    password_lable_input.insert(0, password)


def search():
    website = website_lable_input.get()
    try:
        with open("./password.json") as data:
            data = json.load(fp=data)
    except FileNotFoundError:
        messagebox.showinfo("Error", f"No Data File Found!!!")
    else:
        if website not in data:
            messagebox.showinfo("Error", f"No detail for {website} exits.")
        else:
            messagebox.showinfo(website, f"Email:{data[website]['email']}\nPassword:{data[website]['password']}")
            pyperclip.copy(data[website]['password'])

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

photograph = tkinter.PhotoImage(file="./logo.png")
canva_locker = tkinter.Canvas(width=200, height=200)
canva_locker.create_image(100, 100, image=photograph)
canva_locker.grid(row=0, column=1)

# Label
website_lable = tkinter.Label(text="Website")
website_lable.grid(row=1, column=0)

email_lable = tkinter.Label(text="Email/Username")
email_lable.grid(row=2, column=0)

password_lable = tkinter.Label(text="Passoword")
password_lable.grid(row=3, column=0)

# input
website_lable_input = tkinter.Entry(width=25)
website_lable_input.grid(row=1, column=1)
website_lable_input.focus()

email_lable_input = tkinter.Entry(width=50)
email_lable_input.insert(END, "sg9967780426@gmail.com")
email_lable_input.grid(row=2, column=1, columnspan=2)

password_lable_input = tkinter.Entry(width=25)
password_lable_input.grid(row=3, column=1)

# button
website_search_button = tkinter.Button(text="Search", width=21, bg="blue", command=search)
website_search_button.grid(row=1, column=2)

password_generator_button = tkinter.Button(text="Generate Password", padx=21, command=set_password)
password_generator_button.grid(row=3, column=2)

add_button = tkinter.Button(text="ADD", width=43, bg="white")
add_button.grid(row=5, column=1, columnspan=2)

add_button.config(command=save_file)

window.mainloop()
