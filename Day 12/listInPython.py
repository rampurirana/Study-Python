# A list is a mutable, ordered of collection of items. It can hold elements of different data types.

# Creating List : Create list using square brackets[] or the list() constructor

# list with different data types
myList = [1, 2, 3, "Rampravesh", 6.5, True]
print(myList)

# Accessing elements : Access elements in list using indexing (Starting from 0) or negative indexing
fruits = ["apple", "Banana", "Mango", "Cherry"]
print(fruits[0]) # apple
print(fruits[-2]) # subtract from len of list = 4-2 = Mango

# Modifying Lists : Lists are mutable, that means their elements can be changed
number = [5, 10, 15, 20]
number[1] = 30 # 10 replaced with 30
print(number) # [5, 30, 15, 20]

# Adding elements : append() = Adds an item to the end, insert() = Adds an item at a specific index
num = [1, 2, 3, 4]
num.append(5) # 5 add at the end
num.insert(1, 10) # 10 add at the 1 index
print(num) # [1, 10, 2, 3, 4, 5]

# Removing elements : remove() = Removes a specific value, pop() = Removes an element by index default is last, del = Deletes an element or the entire list
nums = [1, 2, 3, 4, 5, 6, 7]
nums.remove(5)
nums.pop(1)
del nums[3]
print(nums) # [1, 3, 4, 7]