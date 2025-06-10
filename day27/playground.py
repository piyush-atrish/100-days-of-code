def add(*n):
    sum=0
    for x in n:
        sum+=x
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))

def calc(n,**kwargs):   # Advanced keyword arguments, takes arguments as a dictionary
                        # with keys and values

     n += kwargs['add']
     n *= kwargs['multiply']

     return n

print(calc(2,add=2,multiply=5))

class Car:
    def __init__(self,**kwargs):
        self.model = kwargs.get('model')  # works same as ["key"] but won't give
        self.color = kwargs.get('color')  # error if argument missing
        self.year = kwargs.get('year')
        self.make = kwargs['make']

car=Car(model='volks wagon',make=True)
print(car.model)
print(car.color)
print(car.year)
