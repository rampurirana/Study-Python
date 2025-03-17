# Loops : Loops are control structure that allow a block of code to be executed repeatedly based on a condtion

# for loop : Used for iterating over a sequnce (list, tuple, dictionary, string, range)

# Iterating over list :
fruits = ["Apple", "Banana", "Orange", "Mango"]
for fruit in fruits:
    print(fruit)

# Iterating over string :
name = "Rampravesh"
for names in name:
    print(names)

# Iterating over range :
for i in range(10): # the loop is running n-1
    print(i)

# using step in range :
for step in range(1, 15, 3): # where 1 is strting of the loop, 15 is the end of the loop, 3 is the step of the loop that means increase the loop with 3
    print(step)