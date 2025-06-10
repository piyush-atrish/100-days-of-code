# Day 7- Hangman Game - Key Concepts:
# - Random word selection using random.choice()
# - List conversion of strings for letter manipulation
# - While loops with condition ('_' in blank) for game continuation
# - User input handling for letter guesses
# - List indexing and iteration to check/reveal letters
# - Conditional logic for correct/incorrect guesses
# - Game state tracking (remaining lives/mistakes)
# - String/list conversion for display purposes
# - Function definition and parameter passing
# - Variable scope (word, blank, mistake within function)

# Game Design Elements:
# - Visual feedback of guessed letters and blanks
# - Progressive difficulty (limited mistakes)
# - Win/lose condition handling
# - End-game reveal of target word


import random
r=['tree', 'whale', 'river', 'piano', 'zebra', 'fish', 'house', 'lion', 'banana', 
'sun', 'mountain', 'dog', 'ice', 'kangaroo', 'elephant', 'umbrella', 'vase', 
'xylophone', 'notebook', 'jungle', 'giraffe', 'orange', 'cherry', 'apple', 'queen']

word= list(random.choice(r))
blank=['_']* len(word)
mistake=5
def match(word,blank,mistake):
    while '_' in blank:
        letter=input('guess a letter:')
        if letter in word:
            for i in range(0,len(word)):
                if letter==word[i]:
                    blank[i]=letter
            print(blank)
        elif mistake>0:
            mistake-=1
            print(f'oops! remaining lives: {mistake}')
        else:
            print('game over')
            break
    return
print(f'the word is {blank}')
match(word,blank,mistake)
print(f'the word is {word}')
