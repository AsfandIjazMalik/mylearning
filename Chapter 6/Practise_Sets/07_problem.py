# Problem 7

# Write a program which finds out whether a given name is present in a list or not.

name = input("Enter your name: ")

li = ["Asfand", 123, None, True, 2j]

if("Asfand".lower() in li):
    print("Yes given name is in the list")

else:
    print("No")