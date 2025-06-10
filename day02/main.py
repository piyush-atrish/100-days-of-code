# Day 2 - Tip Calculator  
# Concepts learned:  
# - Type conversion (float(), int()) for numerical input  
# - Arithmetic operations (+, /) and assignment operator (+=)  
# - Rounding numbers using round()  
# - String formatting ('{:.2f}'.format()) to enforce 2 decimal places  
# - f-strings (formatted strings) for cleaner output  

print('Welcome to the Tip Calculator')  
bill = float(input('What is your bill? '))  
tip = int(input('What percentage would you like to give?\n10, 12, or 15: '))  
bill += bill * (tip / 100)  # Adds tip to total bill  
split = int(input('How many people are splitting the bill? '))  
bill = round(bill / split, 2)  # Splits and rounds to 2 decimal places  
bill = '{:.2f}'.format(bill)  # Ensures trailing zero (e.g., 5.00)  
print(f'Every person should pay: ${bill}\nThank you!!')  
