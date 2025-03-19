# Functions Arguments : Functions arguments determine how values are passed om into a functions when it is called

# 1. Default Arguments : These have default values and are optional when calling the functions
def greet(name, age = 20):
    print("Name :", name)
    print("Age :", age)
greet("Rampravesh Rana") # uses default age = 20
greet("Ashish Rana", 25) # overrides default age

# 2. Keyword Arguments : Keyword arguments that use parameter names to assign the values rather than order
def details(name, age):
    print("Name :",name)
    print("Age :",age)
details(age = 15, name = "Sagar") # order does not matter

# 3. Required Arguments : Required arguments are functions parameters that must be provided when calling the functions. If is required arguments is missing, Python raises a Type Error
def error(name, age):
    print("Name :", name)
    print("Age :", age)
error("Riya", 16) # work
# error("Riya") # not work

# 4. Arbitrary Arguments : Arbitrary arguments allow a functions to accept multliple variable number of arguments. These arguments are passed into the function as a tuple
def addition(*add): #single star define arbitary arguments
    print(add) #print as tuple
    print(sum(add)) #add all numbers
addition(2, 4, 6, 8)

# Arbitrary Keyword Arguments : Arbitrary keyword arguments allow a function to accept a variable number of named (keyword) arguments. These arguments are passed into the function as a dictionary
def arbiKey(**kid): #double star define arbitrary keyword
    print(kid) #print as dictionary
    for key, value in kid.items(): # key is the argument name, vlaue is the argument vlaues
        print(key, value)

arbiKey(name = "Rampuri Rana", age = 20, rollNum = 1323161)