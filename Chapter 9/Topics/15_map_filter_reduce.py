from functools import reduce
# Map Function
# Map applies a function to all the items in an input_list.

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

square = lambda a: a*a
square_list = map(square, lst)
print('Example of Map Function\n',list(square_list))

# Filter Function
# Filter creates a list of items for which the function returns true.

def filer_fun(m):
    if m % 3 == 0:
        return True
    return False

dev_by_three = filter(filer_fun, lst)
print('\nExample of Filter Function\n',list(dev_by_three))

# Reduce Function 
# Reduce applies a rolling computation to sequential pair of elements.

sum = lambda a, b: a+b
print('\nExample of Reduce Function\n',reduce(sum, lst))
