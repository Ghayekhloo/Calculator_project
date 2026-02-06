
def my_sum(a, b):
    result = a + b
    print (f"result = {result}")
def my_minus(a, b):
    result = a - b
    print (f"result = {result}")
def my_plus(a, b):
    result = a * b
    print (f"result = {result}")
def my_div(a, b):
    result = a / b
    print (f"result = {result}")    
    
    
def my_calculation():
    a  = int(input(" enter the first number \n"))
    b = int(input(" enter the second number \n"))

    operator = input("type of operation is \n")

    if operator == "+":
            my_sum(a, b)
    elif operator == "-":
            my_minus(a, b)
    elif operator == "*":
            my_plus(a, b)
    elif operator == "/":
            my_div(a, b)
    else: 
        print("My calculate no sufficent for compute this numbers") 
my_calculation()               