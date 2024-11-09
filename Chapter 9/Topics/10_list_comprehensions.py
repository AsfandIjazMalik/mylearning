# List Comprehension

# Without List Comprehension

list_item = [2, 3, 4, 5, 6]
# squarelist = []
# for item in list_item:
#     squarelist.append(item*item)
    
# print(squarelist)

# With list List Comprehension

# Example 1
# list is an elegent way to create a new list based on existing list.

squrelist = [i*i for i in list_item]
print(squrelist)

# List comprehension in Python is a quick way to create lists. Instead of using loops,
# you can write a single line to make a new list by defining a pattern or rule.
# Example 2
squares = [x**2 for x in range(2, 11)]
print(squares)
