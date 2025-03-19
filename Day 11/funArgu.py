# Functions Arguments : Functions arguments determine how values are passed om into a functions when it is called

# 1. Default Arguments : These have default values and are optional when calling the functions
def greet(name, age = 20):
    print("Name :", name)
    print("Age :", age)
greet("Rampravesh Rana") # uses default age = 20
greet("Ashish Rana", 25) # overrides default age

# 2. Keeyword Arguments : Keyword arguments that use parameter names to assign the values rather than order
def details(name, age):
    print("Name :",name)
    print("Age :",age)
details(age = 15, name = "Sagar") # order does not matter