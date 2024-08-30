# Problem 05

# Write a program to find whether a given username contains less than 10 characters or not.

user_name = input("Enter user user_name here: ")

if(len(user_name) <= 10):
    print("Your user name is right")
    print("User Name is", user_name)

else:
    print("Please enter user_name in range of 10 characters\nCurrently your user is", user_name)