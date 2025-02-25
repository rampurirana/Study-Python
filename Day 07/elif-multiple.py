# elif is used for checking multiple conditions

marks = int(input("Please enter your obtained marks : "))

if marks >= 80:
    print("You have obtained A Grade")
elif marks >= 60:
    print("Yuo have obtained B Grade")
elif marks >= 33:
    print("You have obtained C Grade")
else:
    print("You have failed")