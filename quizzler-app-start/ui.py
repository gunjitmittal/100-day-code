from faulthandler import disable
from tkinter import *
from quiz_brain import QuizBrain

from pyparsing import col
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.q_text = self.canvas.create_text(150, 125, text="Question text",
                                              font=("Ariel", 20, "italic"),
                                              fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img,
                                   highlightbackground=THEME_COLOR,
                                   command=self.true_button)
        self.right_button.grid(column=0, row=2)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img,
                                   highlightbackground=THEME_COLOR,
                                   command=self.false_button)
        self.wrong_button.grid(column=1, row=2)

        self.label = Label(text=f"Score: {self.quiz.score} ", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="White")
            self.label.config(text=f"Score: {self.quiz.score} ")
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
