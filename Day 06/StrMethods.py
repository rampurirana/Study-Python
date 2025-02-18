# String Methods : Python provides a variety of built-in string mehtods that help manipulating and process strings efficiently

# 1. Case Conversion :
name = "raMpravesH raNa"
print(name.upper()) #converts all character to uppercase
print(name.lower()) #converts all character to lowerrcase
print(name.title()) #capitalizes the first letter of each word
print(name.capitalize()) #capitalizes the first letter of the strings
print(name.swapcase()) #swaps uppercase to lowercase

# 2. Checking String Content :
check = "My age is 20"
print(check.isalpha()) #check if all character are letters
print(check.isdigit()) #check if all character are digits
print(check.isalnum()) #check if all character are letters or numbers
print(check.isspace()) #check if string contains only whitspaces
print(check.isupper()) #check if all character are uppercase
print(check.islower()) #check if all character are lowercase
print(check.istitle()) #check if string follows title case