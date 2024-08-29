print("LIST IN PYTHON ")

# Python lists are containers to store a set of values of any data type.


friend = ["Apple", 77 , None, True, 8.55, "Asfand"] # in this list "strind" , Int , Float , None, Bolean data types stored
print(friend)
friend.append("Ijaz Malik") # adding Ijaz Malik list added at the end of the list

# in List data type we can change the string in place but in strings data type we can't change inplace 
friend[0] = "Peach" # List are mutable unlike Strings
print(type(friend[2])) 
print(friend)


