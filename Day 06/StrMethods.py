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

# 3. Searching and Finding
find = "Rampravesh Rana"
print(find.find("ravesh")) #returns the index of first occurance of the substring
print(find.count("a")) #counts the number of the same [a = 4] character in the stirng

# 4. Modifying String
mod = " Thank You "
print(mod.replace("Thank", "Hello")) #replace the subtring
print(mod.strip()) #removes the leading and trailing spaces
print(mod.lstrip()) #removes the leading spaces
print(mod.rstrip()) #removes the trailing spaces

# 5. Spliting and Joining
strignFruits = "mango, banana, apple"
print(strignFruits.split()) #split a string into lists

listFruits = ["mango", "banana", "apple"]
print(",".join(listFruits)) #join a list into strings

# 6. String Alignment
alig = "Ram"
print(alig.center(10, "-")) #center the string within a given width
print(alig.ljust(10, "-")) #align the string in the left
print(alig.rjust(10, "-")) #align the string in the right
print(alig.zfill(5)) #fill the remaining letter with 0

# 7. Encoding and Decoding
en_de = "hello"
print(en_de.encode()) #encode the string into bytes

byte_text = b"hello"
print(byte_text.decode()) #deocde the bytes into normal string

# Formatting String
name = "Rampravesh Rana"
age = 20
print("My name is {} and i am {} years old.".format(name, age)) #format a string using placeholder
print(f"My name is {name} and in am {age} years old.") #Moderan way to format string