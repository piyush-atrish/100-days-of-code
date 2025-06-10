#------------------------------------day16-------------------------------------------------
#____________________________________OOPS__________________________________________________

#Classes,objects,instances,attributes,methods

# from turtle import Turtle,Screen
# turtle = Turtle()
# screen = Screen()
# screen.bgcolor("white")
# screen.setup(width=500, height=300)
# turtle.color("cyan")
# turtle.shape("turtle")
# turtle.forward(100)
# screen.exitonclick()

# from prettytable import PrettyTable
#
# table=PrettyTable()
# table.add_column('pokemon',['pikachu',"squirtle","charmendar"])
# table.add_column('type',['electric','water','fire'])
# table.align='l'
# print(table)


# from coffee_maker import CoffeeMaker
# from menu import Menu
# from money_machine import MoneyMachine


# def main():
#     is_on=True
#     menu=Menu()
#     machine=MoneyMachine()
#     coffee_maker=CoffeeMaker()
#     while is_on:
#         ask=input(f'What would you like? {menu.get_items()}').lower()
#         if ask=='off':
#             is_on=False
#         elif ask=='report':
#             coffee_maker.report()
#             machine.report()
#         elif ask == 'espresso' or ask == 'latte' or ask == 'cappuccino':
#             drink=menu.find_drink(ask)
#             if coffee_maker.is_resource_sufficient(drink):
#                 if machine.make_payment(drink.cost):
#                     coffee_maker.make_coffee(drink)
#         else:
#             print('Please enter a valid option')

# main()

# https://repl.it/@appbrewery/oop-coffee-machine-start




