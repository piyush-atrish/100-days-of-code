#----------------------------------day15------------------------------------------

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check(choice):
    """Check if the resources are enough if not returns false else returns true"""
    for item in choice:
        if resources[item]<choice[item]:
            print(f'sorry not enough {item}')
            return False
    return True


def coins():
    """takes coins as input , and calculate total"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def possible(payment,cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if payment>=cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def make(ask,choice):
    """Deduct the required ingredients from the resources."""
    for item in resources:
        resources[item]-=choice[item]
    print(f"Here is your {ask} ☕️. Enjoy!")


def main():

    is_on=True
    while is_on:
        ask=input('what would you like? (espresso/latte/cappuccino):').lower()
        if ask=='off':
            is_on=False
        elif ask == 'report':
            print(f'water:{resources["water"]}')
            print(f"milk:{resources['milk']}")
            print(f'coffee:{resources["coffee"]}')
            print(f'profit:{profit}')
        elif ask == 'espresso' or ask == 'latte' or ask == 'cappuccino':
            choice=MENU[ask]
            if check(choice['ingredients']):
                payment=coins()
                if possible(payment,choice['cost']):
                    make(ask,choice["ingredients"])
           
        else:
            print('wrong input!!')

main()