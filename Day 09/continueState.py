# Skips the current iteration and moves to the next one
# The loop does not stop, only the current iteration is skip

# Using continue in for loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Using continue in while loop
x = 15
while x <= 25:
    x = x + 1
    if x == 20:
        continue
    print(x)