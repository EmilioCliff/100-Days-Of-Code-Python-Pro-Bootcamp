"""
Instructions
Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.
"""
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
temp = a
a = b
b = temp
print("a: " + a)
print("b: " + b)
