import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizeInterface():
    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = tkinter.Tk()
        self.window.title("Trivia")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        self.score_label = tkinter.Label(text="SCORE: ", background=THEME_COLOR, foreground="white", font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)
        self.canvas = tkinter.Canvas(bg="white", height=250, width=300)
        self.question = self.canvas.create_text(150, 125, text="Hello word", fill="black", font=("Arial", 15, "italic"), width=230)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        image_true = tkinter.PhotoImage(file="images/true.png")
        self.button_true = tkinter.Button(text="True",image=image_true, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.true_button_clic)
        self.button_true.grid(row=2, column=1)
        image_false = tkinter.PhotoImage(file="images/false.png")
        self.button_false = tkinter.Button(text="False", image=image_false, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.false_button_click)
        self.button_false.grid(row=2, column=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            current_question = self.quiz.next_question()
            self.score_label.config(text=f"Score:{self.quiz.score}")
            self.canvas.itemconfig(self.question, text=current_question)
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")


    def true_button_clic(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

    def false_button_click(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)


