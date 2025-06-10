# DAY 8 - Caesar Cipher Project
# ----------------------------------
# CORE CONCEPTS PRACTICED:
# 1. String Manipulation
#    - Concatenation
#    - Case conversion (.lower())
#    - Index checking (.index())
#    - f-strings for output

# 2. List Operations
#    - Creating character sets
#    - List indexing
#    - Modulo wrapping (%26)

# 3. Function Implementation
#    - Parameter passing
#    - Return values
#    - Recursive calls
#    - Encapsulation

# 4. Program Flow Control
#    - While/for loops
#    - Conditional branching
#    - User input handling
#    - Type conversion

# 5. Python Features Used:
#    - ASCII art in triple quotes
#    - Negative indices
#    - Method chaining
#    - Interactive console I/O

# 6. Cryptographic Principles:
#    - Substitution cipher
#    - Symmetric encryption
#    - Shift operations
#    - Character preservation

# Note: This implements a classic Caesar cipher
# with support for both encoding and decoding.


alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=[' ','0','1','2','3','4','5','6','7','8','9']
def cypher(message,shift):
    code=""
    for i in message:
        if i in number:
            code+=i
        else:
            code+=(alpha[(alpha.index(i)+shift)%26])
    return code
def ceaser():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction=='encode':
        code=cypher(text,shift)
        print(f'the encryption is is {code}\n')
    elif direction=='decode':
        code=cypher(text,-shift)
        print(f'the message is {code}\n')
    end=input('do you want to continue?\ntype yes or no:\n')
    if end == 'yes':
        ceaser()
    else:
        print('Thank you!')

print("""   _____                                  _       _               
  / ____|                                (_)     | |              
 | |     __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    """)
ceaser()
