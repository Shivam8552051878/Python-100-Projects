BACKGROUND_COLOR = "#B1DDC6"
import tkinter
import pandas
import random
try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dic = data.to_dict(orient="records")

current_card = {}

def learn_word():
    data_dic.remove(current_card)
    print(len(data_dic))
    data = pandas.DataFrame(data_dic)
    data.to_csv("./data/word_to_learn.csv", index=False)
    next_card()


# Fun
def next_card():
    global current_card
    current_card = random.choice(data_dic)
    image.config(file="images/card_front.png")
    card_front_canva.itemconfig(tagOrId=language_text, text="French", fill="black")
    card_front_canva.itemconfig(tagOrId=words_text, text=current_card["French"], fill="black")
    window.after(3000, flip_card)
def flip_card():
    image.config(file="images/card_back.png")
    card_front_canva.itemconfig(tagOrId=language_text, text="English", fill="white")
    card_front_canva.itemconfig(tagOrId=words_text, text=current_card["English"], fill="white")


window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# window.after(3000, func=flip_card)

# front card
card_front_canva = tkinter.Canvas(height=550, width=850)
card_front_canva.config(height=550, width=850, bg=BACKGROUND_COLOR, highlightthickness=0)
image = tkinter.PhotoImage(file="./images/card_front.png")
card_front_canva.create_image(425, 275, image=image)
language_text = card_front_canva.create_text(400, 150, text="English", font=("Helvetica", 40, "bold"), fill="black")
words_text = card_front_canva.create_text(400, 263, text="", font=("Helvetica", 60, "normal"), fill="black")

card_front_canva.grid(row=1, column=1, columnspan=3)
# image.config(file="./images/card_back.png")
# wrong
image_wrong = tkinter.PhotoImage(file="./images/wrong.png")
button_wrong = tkinter.Button(image=image_wrong, highlightthickness=0, padx=50, pady=50, borderwidth=0, command=next_card)
button_wrong.grid(row=3, column=1)
# right
image_right = tkinter.PhotoImage(file="./images/right.png")
button_right = tkinter.Button(image=image_right, highlightthickness=0, padx=50, pady=50, borderwidth=0, command=learn_word)
button_right.grid(row=3, column=3)




next_card()
window.mainloop()

