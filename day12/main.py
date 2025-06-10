#---------------------------day12---------------------------------------
import random

def compare(guess):
    global life,alive
    if guess==number:
        print('you win!!')
        alive=False
    elif guess>number:
        print('too high')
        life-=1
    elif guess<number:
        print('too low!')
        life-=1

number=random.randint(0,100)

mode=input('guessing game!!\nwhich mode you want, type easy or hard:\n').lower()

print('I choose a number between 0 and 100, Try to guess!!')

if mode=="easy":
    life=10

else:
    life=5
alive=True

while alive:
    guess=int(input('enter your guess: '))
    compare(guess)
    print(f'number of remaining guesses: {life}')
    if life==0:
        print('you loose!!')
        alive=False
    


# got to know about global and local of variables and functions
#block scope does not exist in python
# namespaces
# how to access global variable in a local function