from functools import reduce
# 09 Problem
# Write a program to find the maximum of the numbers in a list using the reduce function.

lst = [4, 5, 9, 10, 14, 15, 19, 20]

def greter_num(a, b):
    if a>b:
        return a
    return b

print('The grater number is:',reduce(greter_num, lst))