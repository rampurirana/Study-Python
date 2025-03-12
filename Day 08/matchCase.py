# The match-case statement is a similar to the switch-case statement in other language. It provides a clean way to handle multiple conditions

number = int(input("Please enter the number (0-5) : "))
match number:
    case 0:
        print("This is the zero")
    case 1:
        print("This is the one")
    case 2:
        print("This is the two")
    case 3:
        print("This is the three")
    case 4:
        print("This is the four")
    case 5:
        print("This is the five")
    case _:
        print("Please enter valid number")