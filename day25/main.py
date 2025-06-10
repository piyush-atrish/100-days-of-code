# CSV-----> comma separated values
# import csv
# with open('226 weather-data.csv') as file:
#     data=csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         else:
#             temp=int(row[1])
#             temperatures.append(temp)
# print(temperatures)

# # we have to do so much to just get hold of one data therefor we can use pandas:

# import pandas
'''Pandas is a Python library used for working with data sets. It has functions for 
analyzing, cleaning, exploring, and manipulating data.'''

# data=pandas.read_csv('226 weather-data.csv') #----------> we get a dataframe from panda
# # print(data['temp']) #---------> we get a series(a 1D structure) from panda
#
# temperature=data['temp'].tolist()
# print(temperature)
# print(f'the average temperature is {data["temp"].mean()}')
# print(f'the highest temperature is {data["temp"].max()}')
# max=data[data.temp==data.temp.max()]
# print(f'it was {max.day} and the conditions were {max.condition}')

#create a dataframe from scratch:
# data_dict={
#     'students':['amy','james','anjela','piyush'],
#     'scores':[70,77,90,100]
# }
# data=pandas.DataFrame(data_dict)
# print(data)
# data.to_csv('data.csv')

# import pandas
#
# data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
#
# '''red=0
# black=0
# gray=0
# for _ in data['Primary Fur Color']:
#     if _=='Cinnamon':
#         red+=1
#     elif _=="Gray":
#         gray+=1
#     elif _=="Black":
#         black+=1'''
#
# red=len(data[data['Primary Fur Color']=='Cinnamon'])
# black=len(data[data['Primary Fur Color']=='Black'])
# gray=len(data[data['Primary Fur Color']=='Gray'])
#
# count={
#     'fur color' : ['gray','red','black'],
#     'count' : [gray,red,black]
# }
#
# count=pandas.DataFrame(count)
# print(count)
# count.to_csv('squirrel_count.csv')


import turtle
import pandas

data=pandas.read_csv('50_states.csv')

def match(word):
    word=word.title()
    if word in data['state'].values:
            return data[data['state']==word].iloc[0]
    return None

class State(turtle.Turtle):
    def __init__(self,state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(state['x'],state['y'])
        self.write(state['state'],move=False,align='center',font=('Arial',12,'bold'))

screen = turtle.Screen()
screen.title('U.S state games')
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
score=0
guessed =[]

while score<50:

    guess=screen.textinput(title=f'Guess State {score}/50', prompt="enter name of a state")
    state=match(guess)
    if guess == 'exit':
        break
    if state is not None and guess not in guessed:
        new_state= State(state)
        score+=1
        guessed.append(guess)

screen.textinput('Game over',"press enter to quit")
screen.bye()