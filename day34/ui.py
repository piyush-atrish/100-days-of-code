from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz : QuizBrain): #---------> specifying data type
        self.window = Tk()
        self.quiz = quiz
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label=Label(text=f"Score : {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1,sticky='e')
        self.canvas = Canvas(width=300,height=250, bg="white")
        self.text=self.canvas.create_text(150,125,width=270,text='Some TEXT',font=('Arial',20,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)
        tick=PhotoImage(file='images/true.png')
        self.right=Button(image=tick,highlightthickness=0,bg=THEME_COLOR,command=self.choose_true)
        self.right.grid(row=2, column=0)
        cross=PhotoImage(file='images/false.png')
        self.wrong=Button(image=cross,highlightthickness=0,bg=THEME_COLOR,command=self.choose_false)
        self.wrong.grid(row=2, column=1)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the quiz.")
            self.right.config(state=DISABLED)
            self.wrong.config(state=DISABLED)


    def choose_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def choose_false(self):
        self.give_feedback(self.quiz.check_answer('false'))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)
