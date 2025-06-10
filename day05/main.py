# Day 5- Password Generator - Key Concepts:
# - Using Python's string module for character sets (letters, symbols, digits)
# - List operations (creation, concatenation, shuffling)
# - User input handling and type conversion (int())
# - Controlled randomization with random.choice() for character selection
# - Conditional logic for building password components
# - List shuffling with random.shuffle() for better security
# - String joining to convert list to final password string
# - Modular design separating character types and quantitiesimport string


import random
letters = list(string.ascii_lowercase + string.ascii_uppercase)
symbols = list(string.punctuation)
numbers = list(string.digits)

lc=int(input('how many letters do you want in your passcode?'))
sc=int(input('how many symbols do you want in your passcode?'))
nc=int(input('how many numbers do you want in your passcode?'))
total=lc+sc+nc
passcode=[]
for i in range(total):
    if i<lc:
        passcode.append(random.choice(letters))
    elif i<sc+lc:
        passcode.append(random.choice(symbols))
    else:
        passcode.append(random.choice(numbers))

random.shuffle(passcode)
passcode=''.join(passcode)
print(passcode)

