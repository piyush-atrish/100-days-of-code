from question_model import Question
from quiz_brain import QuizBrain
import html
from data import question_data
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"]) #--------->

# Some characters are reserved in HTML.
# If you use the less than (<) or greater than (>) signs in your HTML text, the browser might mix them with tags.
# Entity names or entity numbers can be used to display reserved HTML characters.
# Entity names look like this:
#To display a less than sign( <) we must write: & lt; or &#60;

    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# type hints:
# indicate the types of variables, function parameters,
# and return values.They can help other developers understand what types of data
# your function expects and what it will return.
#
# def a_function(a : int) -> str:
#
#     return str(a)
#
# this indicates that the function will take an int argument and return a string.


