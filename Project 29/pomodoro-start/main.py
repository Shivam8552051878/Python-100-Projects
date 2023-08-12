import math
import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
countdown = 5 * 300
num = 1
check_symbol = "✔"
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    global check_symbol, num, timer
    window.after_cancel(timer)
    canva.itemconfig(canvas_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="", foreground=GREEN)
    check_symbol = "✔"
    num = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def run():
    global SHORT_BREAK_MIN, LONG_BREAK_MIN, WORK_MIN, num
    if num % 8 == 0:
       count_down(LONG_BREAK_MIN)
       title_label.config(text="Break", foreground=RED)
    elif num % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break", foreground=PINK)
    else:
        count_down(WORK_MIN)
        title_label.config(text="Work", foreground=GREEN)

    num += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global check_symbol, timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:

        count_sec = f"0{count_sec}"

    canva.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        run()
        if num % 2 == 0:
            check_label.config(text=check_symbol)
            check_symbol = check_symbol + check_symbol





# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)
photo_image = tkinter.PhotoImage(file="./tomato.png")

canva = tkinter.Canvas(width=210, height=223, bg=YELLOW, highlightthickness=0)
canva.create_image(105, 112, image=photo_image)
canvas_text = canva.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canva.grid(row=6, column=3)

start_button = tkinter.Button(text="Start", highlightthickness=0, width=7, command=run)
start_button.grid(row=9, column=2)

restart_button = tkinter.Button(text="Restart", highlightthickness=0, width=7, command=reset_time)
restart_button.grid(row=9, column=4)


check_label = tkinter.Label(text="", bg=YELLOW, fg=GREEN)
check_label.grid(row=9, column=3)

title_label = tkinter.Label(text="Timer", width=7, background=YELLOW, foreground=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=2, column=3)

# print(time.localtime())
window.mainloop()