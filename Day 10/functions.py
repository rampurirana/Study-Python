# Functions : A functions is a block of code that performs a specific task whenever it is called.
# functions is defined using the def keyword

def greet(name): # greet is the name of functions, name is the parameter
    print(f"Hello, {name}") # functions body

greet("Rampravesh Rana") # functions call

# 1. Built-in functions : These are functions that come pre defined in python and can be used directly without defining them
numbers = [1, 2, 3, 4, 5]
print(len(numbers)) #5
print(sum(numbers)) #15

# 2. User defined functions : These are the functions created by user to perform specific tasks. Define using the def keyword
def isdivide(a, b):
    if(a % b == 0):
        print("Divisible by two")
    else:
        print("Not divisible by two")

a = 25
b = 8
isdivide(a, b) # not divisible

isdivide(10, 5) # divisible