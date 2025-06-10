#-----------------------day 10-------------------------------------

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():

  num1 = float(input("enter a number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    if operation_symbol not in operations:
        print("invalid operation")
        break
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    ask=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation"
             f"\ntype 'e' to exit: ").lower()
    if ask == "y":
      num1 = answer
    elif ask == "n":
        calculator()
    elif ask == "e":
        should_continue = False
    else:
      print("Invalid input")
      should_continue = False

  print("Goodbye")

calculator()
