# nested if else used for checking if-else conditions inside the conditions

age = int(input("Please enter your current age : "))
weight = int(input("Please enter your current age : "))

if age >= 18:
    if weight >= 60:
        print("You are eligible for donatting blood")
    else:
        print("You are not eligible for donatting blood, because your weight is not met our requirement")
else:
    print("You are not eligible for donatting blood, because your age is not met our requirement")