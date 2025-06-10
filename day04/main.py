# Day 4 - Rock Paper Scissors Game
# Concepts Learned:
# - Using random.randint() for computer opponent choices
# - Multi-line strings (triple quotes) for ASCII art
# - Storing options in a list for programmatic access
# - Converting user input to integers for logic comparison
# - Basic game logic with if/elif/else conditions
# - String interpolation with f-strings to display choices
# - Simple win/lose/draw condition checking
# - Index-based comparison between user and computer selections

import random

print('welcome to rock paper scissors!!')
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game=[rock,paper,scissors]
m=random.randint(0,2)
n=int(input('type 0 for rock,1 for paper and 2 for scissors: '))
print(f'your choice is:\n{game[n]}')
print(f'computer choice is:\n{game[m]}')

if m==n:
    print('it is a draw!!')
elif game[m]==game[n-2]:
    print('you lost!!')
else:
    print('you won!!')