from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizGUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)
        score_label_text = self.score_label = Label(text=f"Score: {self.score}", font=("Arial", 12, "normal"),
                                                    fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=2, row=1, padx=20, pady=20)
        canvas_bg = self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=(20, 20), ipadx=20, ipady=20, )

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(column=2, row=3, padx=20, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(column=1, row=3, padx=20, pady=20)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(command=self.true_pressed)
            self.false_button.config(command=self.false_pressed)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.true_button.config(command="")
            self.false_button.config(command="")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.window.after(1000, self.answer_feedback)

        elif not is_right:
            self.true_button.config(command="")
            self.false_button.config(command="")
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
            self.window.after(1000, self.answer_feedback)

    def answer_feedback(self):
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.canvas.config(bg="white")
        self.get_next_question()

