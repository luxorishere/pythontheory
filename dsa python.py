# Python List
# Built-in methods of list in Python
# List has many built-in methods which can be used to perform various operations on the list.
# Here are some commonly used built-in methods:
# Use of extend in list

# 1. append(item):
#    Appends an item to the end of the list.
# Extend method
# Extend method is used to append elements of one list to another list.
# It takes an iterable as an argument and appends all the elements of the iterable to the list.

# 2. count(item):
#    Returns the count of an item in the list.
# Output: [1, 2, 3, 4, 5, 6]

# 3. extend(iterable):
#    Extends the list by appending all the items from the iterable.

# 4. index(item):
#    Returns the index of the first occurrence of an item in the list.

# 5. insert(index, item):
#    Inserts an item at the specified index.

# 6. pop([index]):
#    Removes an item at the specified index and returns it.
#    If no index is specified, pop removes and returns the last item.

# 7. remove(item):
#    Removes the first occurrence of an item from the list.

# 8. reverse():
#    Reverses the order of the elements in the list.

# 9. sort([key]):
#    Sorts the elements of the list in ascending order.
#    It is stable, meaning it preserves the relative order of elements with equal values.

# 10. clear():
#     Removes all the elements from the list.

# 11. copy():
#     Returns a shallow copy of the list.

# 12. print(list):
#     Prints the list.

# You can find more built-in methods in the Python documentation.
# The extend method changes the original list.
# It does not return a new list.
import random
AZ_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
az_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "'", "\"", "<", ">", ",", ".", "?"]

total_list = [AZ_list, az_list, number_list, symbol_list]

password = ""

limit = int(input("Enter the length of the password: "))

for i in range(limit):
    char_list = random.choice(total_list)
    char = random.choice(char_list)
    password += char
print(password)


