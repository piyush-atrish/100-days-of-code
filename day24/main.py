# file=open('my_file.txt') ------> opens a file and saves it in variable file
# content = file.read()  --------> returns the content of the file as string
# print(content)
# file.close() -------> essential to return the resources of your computer

# with open('my_file.txt') as file: -------> closes the file automatically
#     content = file.read()
#     print(content)

# with open('my_file.txt', 'w') as file: ------------> default 'r'(read mode), 'w'(write mode)
#     file.write('Hello World')  ----------> deletes the previous data and rewrites the input provided

# with open('my_file.txt','a') as file:
#     file.write('\nThis is piyush') ---------> adds input to previous data

# with the 'w' write mode if the file do not exist beforehand , it will create the file with the name we opened it with
#


# absolute file path----> the complete address of a file or directory in a computer system,
#                         starting from the root directory
#  example- /user/deckstop/100dbc/day24/main.py (starts with / )

# relative file path ------>  a way to specify a file or directory's location in
#                             relation to the current working directory

# example - ./my_file.txt (./ represent current working folder)
#           ./file1/file2 ( to access children directory)
#           ../file0 ( to access parent folder)


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Letters/starting_letter.txt') as file:
    letter=file.read()
with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

for name in names:
    stripped_name = name.strip()
    with open(f'./Output/ReadyToSend/{stripped_name}.txt', 'w') as f:
        f.write(letter.replace('[name]', stripped_name))