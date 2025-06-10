import os
from data import data
import random

def clear_console():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(a,b,ask,score):
    if ask=='a':
      if a['follower_count']>b['follower_count']:
        print('correct!!')
        return score+1,True
      else:
         return score,False
    else:
       if b['follower_count']>a['follower_count']:
        print('correct!!')
        return score+1,True
       else:
         return score,False
         
def highlow(score):
    print(r"""
              __  ___       __                               __                       
             / / / (_)___ _/ /_  ___  _____   ____  _____   / /___ _      _____  _____
            / /_/ / / __ `/ __ \/ _ \/ ___/  / __ \/ ___/  / / __ \ | /| / / _ \/ ___/
           / __  / / /_/ / / / /  __/ /     / /_/ / /     / / /_/ / |/ |/ /  __/ /    
          /_/ /_/_/\__, /_/ /_/\___/_/      \____/_/     /_/\____/|__/|__/\___/_/     
                  /____/                                                              
          """)

    a=random.choice(data)
    print(f"compare A: {a['name']} , a {a['description']} , from {a['country']}")
    print(r"""
            ___  ________
            \  \/ /  ___/
             \   /\___ \ 
              \_//____  >
                      \/ 
           """)
    b = random.choice([item for item in data if item != a])
    print(f"compare B: {b['name']} , a {b['description']} , from {b['country']}")
    ask=input('which one has more followers? type A or B:').lower()
    return compare(a,b,ask,score)

def main():
    score=0
    game=True
    while game:
      score,game=highlow(score)
      clear_console()
      print(f"your score is {score}")
    print(f"game over!!")
    print(f"your final score is {score}")
main()