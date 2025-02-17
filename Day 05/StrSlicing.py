# String Slicing : String slicing is the process of extracting a spicific poriton of a string using indexing

#1. Basic syntax of slicing : String[start:end:step(optional)]
fullName = "Rampravesh Rana"

# print single character of string
print(fullName[0])
print(fullName[12])

# print specific portion of string
print(fullName[0:3])
print(fullName[3:11])

# slicing with default vlaues
print(fullName[:4]) # blank is specifies the default vlaue 0
print(fullName[3:]) # blank is specifies the ending of the character
print(fullName[:]) # entire string

# using negative indexing
print(fullName[-3:15])
print(fullName[0:-2])
# jidhar bhi negative value ho usko total length of string se subtract kar deta hai aur subtract value ko indexing specifies hota hai