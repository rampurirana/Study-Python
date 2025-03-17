# Exits the loops completely
# Used to when need to stop the loop early

# Using break statement in for loop
for i in range(1, 6):
    if i == 3:
        break # stops the loops when i==3
    print(i)

# Uaing break statement in while loop
x = 15
while x <= 25:
    print(x)
    if x == 20:
        break
    x = x + 1