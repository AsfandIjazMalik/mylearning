# 08 Problem
# Write a program to filter a list of numbers which are divisible by 5.

lst = [4, 5, 9, 10, 14, 15, 19, 20]

div_by_five = lambda a : a%5 == 0
div_five = filter(div_by_five, lst)
print('The number divion by 5 in lst are',list(div_five))
