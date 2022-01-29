from tkinter import *

THEME_COLOR = "#375362"


class QuizGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("QuizGame")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)
        self.score_label = Label(text=f"Score: 0", font=("Arial", 12, "normal"), fg="white", bg=THEME_COLOR,
                                 highlightthickness=0)
        self.score_label.grid(column=2, row=1, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question goes here",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=(20, 20), ipadx=20, ipady=20, )

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0)
        self.false_button.grid(column=2, row=3, padx=20, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0)
        self.true_button.grid(column=1, row=3, padx=20, pady=20)

        self.window.mainloop()
