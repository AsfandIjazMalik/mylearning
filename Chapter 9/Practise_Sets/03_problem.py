# 03_Problem 

# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

entr_num = int(input('Enter the number to of which you want to print table: '))
table = [entr_num*i for i in range(1 ,11)]
print(table)
    