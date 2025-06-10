#=====================================day26=========================================

#list comprehension:
'''List comprehension offers a shorter syntax when you want to create a new list
based on the values of an existing list.'''
import pandas

list1=[1,2,3,4,5]
# list2=[n+1 for n in list1]
# print(list2)

#can also operate on strings,tuples,arrays,etc

# name='Piyush'
# list=[letter for letter in name]
# print(list)

#can also works for range
#
# double=[2*n for n in range(1,5)]
# print(double)

# conditional comprehension

# names=['piyush','josh','joshi','anjela','altress','max','mathew']
# names1=[name.upper() for name in names if len(name)>5]
# print(names1)

#dictionary comprehension

# import random
#
# student=['piyush','josh','joshi','anjela','altress','max','mathew']
# score={student:random.randint(1,100) for student in student}
# print(score)
#
# passed={student:score for (student,score) in score.items() if score>60 }
# print

# sentence='what is the air speed velocity of an unladen swallow?'
# sentence=sentence.split()
# result={word:len(word) for word in sentence}
# print(result)

# loop through a dict:

# students_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 90,
#     "Ethan": 88,
#     "Fiona": 95,
#     "George": 72,
#     "Hannah": 81,
# }
#
# for(key, value) in students_marks.items():
#     print(key)
#     print(value+10)

# data= {
#     'A': [52, 93, 15, 72, 61],
#     'B': [0.596850, 0.445833, 0.099975, 0.459249, 0.333709],
#     'C': ['Z', 'Y', 'X', 'Y', 'Y'],
#     'D': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
# }
#
# data=pandas.DataFrame(data)
#
# for (index,row) in data.iterrows():
#     print(row.A)


#
import pandas
'''importing pandas to read csv efficiently'''

data=pandas.read_csv('NATO.csv')
'''data frame of NATO letters'''

codes={row.letter:row.code for (index,row) in data.iterrows()}
'''formed a dictionary using dict comprehension'''

word=input('Enter a word: ').upper()

list=[letter for letter in word]

out=[codes[code] for code in list]

print(out)

