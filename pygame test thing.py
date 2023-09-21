import pygame as py
import array
from array import *
import threading
import time

n = 0

# arrays
# https://www.freecodecamp.org/news/python-array-tutorial-define-index-methods/

# file = open("test.txt")
# info = file.readlines()


# numbers = array('i', [])

# try:
#     while True:
#         numbers.append(int(info[n].strip()))
#         n += 1
# except: pass
# print(numbers)
# print("")



# numbers = numbers[1:5]

# for number in numbers:
#     print(number)
# print("")



# numbers.append(11)
# print(numbers)
# print("")



# numbers.extend([12, 13, 14])
# print(numbers)
# print("")



# numbers.insert(0, 1)
# numbers.insert(5, 6)
# numbers.insert(6, 7)
# numbers.insert(7, 8)
# numbers.insert(8, 9)
# numbers.insert(9, 10)
# print(numbers)
# print("")



# numbers.remove(1)
# print(numbers)
# print("")



# numbers.pop(3)
# print(numbers)
# print("")
# print("")
# print("")



# lists
# https://www.freecodecamp.org/news/how-to-make-a-list-in-python-declare-lists-in-python-example/

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
print("")



numbers.append(11)
print(numbers)
print("")



numbers.insert(0, 0.5)
print(numbers)
print("")



for number in numbers:
    print(number)
print("")



numbers[0] = 2
print(numbers)
print("")



numbers.remove(2)
print(numbers)
print("")



numbers.pop(10)
print(numbers)
print("")



del numbers[9]
print(numbers)
print("")


numbers.clear()
print(numbers)
print("")


numbers = [1, 2]
print(len(numbers))