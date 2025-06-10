#____________________________blackjack day11__________________________________
 
import random

card=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def blackjack():
    user=random.sample(card,k=2)
    comp=random.sample(card,k=2)
    
    print(f'your cards are {user}')
    print(f"the dealer's first card is {comp[0]}")
    print(f'current score : {user[0]+user[1]}')
    check(user,comp)

def display(user,comp):
    print(f'your cards are{user}')
    print(f'your sum: {sum(user)}')
    print(f"the dealer's cards are {comp}")
    print(f"dealer's sum {sum(comp)}")

def check(user,comp):
    if sum(user)==21:

        if sum(comp)==21:
            print('its a draw')
            display(user,comp)
            return
        
        else:
            print('you win!!')
            display(user,comp)
            return
        
    elif sum(user)>21:

        if sum(comp)>21:
            print('its a draw')
            display(user,comp)
            return
        
        else:
            print('oops you loose!!')
            display(user,comp)
            return
        
    else:
        ask=input('do you want to draw another card? yes or no: ')

        if ask== 'yes':
            user.append(random.choice(card))

            if 11 in user and sum(user) > 21:
                ace_index = user.index(11)
                user[ace_index] = 1
            print(f'your cards are: {user}')
            print(f'yourb sum: {sum(user)}')
            check(user,comp)

        else:

            if sum(comp)<16:
                comp.append(random.choice(card))  

                if 11 in comp and sum(comp) > 21:
                    ace_index = comp.index(11)
                    comp[ace_index] = 1

            if sum(comp)>21:
                display(user,comp)
                print('you win!!!') 
                return
            
            elif sum(comp)==sum(user):
                display(user,comp)
                print('its a draw')
                return
            
            elif sum(comp)>sum(user):
                display(user,comp)
                print('oops you loose!!')
                return
            
            elif sum(comp)<sum(user):
                display(user,comp)
                print('you win!!')
                return

def main():

    print('____________welcome to blackjack_____________\n')
    
    going_on=True

    while going_on:
        blackjack()
        rematch=input('do you want to play again?? yes or no: ')

        if rematch=='no':
            going_on=False
            
    print('thanks for playing')

main()