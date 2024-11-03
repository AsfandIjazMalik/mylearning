# Warlus Operator introduceed in 3.8 version of Python
# Convience method to do 2 work in one line one of code 
# := is symbol of warlus operator

# Example of Warlar operator
if (n := len([1,2,34])) >= 3:
    print("Yes Lenght is equal to 3")
else:
    print("NO")


# Without Warlus Operator 
friend_names_list = []

while True:
    friends_name = input("Enter the Name of the friends how many you want: ")
    friend_names_list.append(friends_name)
    if friends_name == 'quit':
        print(friend_names_list)
        break

# Above example With Warlus Operator

new_friend_names_list = []
while (name := input("Enter the Name of the friends how many you want: ")) != 'quit':
    new_friend_names_list.append(name)

