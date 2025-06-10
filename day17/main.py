#----------------------------------------day17--------------------------------------------

# class FirstLetterOfEachWordIsCapital: ----------PascalCase, other are --- camelCase , snake_case
#     def __init__(self, parameter1, parameter2): ------------------constructor(__init__)
#         self.attribute1 = parameter1
#         self.attribute2 = parameter2
#         def method1():
#             pass
#
# object1 = FirstLetterOfEachWordIsCapital("argument1","argument2")
# print(object1.attribute1)
# print(object1.attribute2)

from zdata import question_data

class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer


question_bank=[]
for items in question_data:
    question_bank.append(Question(items["text"],items["answer"]))


class Quizbrain:

    def __init__(self,qlist):
        self.qlist = qlist
        self.number=0
        self.points=0

    def check(self,choice,current):
        if current.answer.lower() == choice:
            self.points+=1
            print('you got it right!!')
            print(f'your score is: {self.points}/{self.number}')
        else:
            print('sorry, you got it wrong!')
            print(f'the correct answer is {current.answer}')
            print(f'your score is: {self.points}/{self.number}')

    def ask(self):
        current=self.qlist[self.number]
        self.number+=1
        choice=input(f'Q{self.number}. {current.text}? True/False: ').lower()
        self.check(choice,current)

    def still_has_questions(self):
       return self.number < len(self.qlist)


def main():
    quiz=Quizbrain(question_bank)
    while quiz.still_has_questions():
        quiz.ask()

main()