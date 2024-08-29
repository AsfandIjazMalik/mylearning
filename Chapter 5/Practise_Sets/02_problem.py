# Problem 02
# Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set() # Empty set

n1 = int(input("Enter 1st number: "))
s.add(n1)
n2 = int(input("Enter 2nd number: "))
s.add(n2)
n3 = int(input("Enter 3rd number: "))
s.add(n3)
n4 = int(input("Enter 4th number: "))
s.add(n4)
n5 = int(input("Enter 5th number: "))
s.add(n5)
n6 = int(input("Enter 6th number: "))
s.add(n6)
n7 = int(input("Enter 7th number: "))
s.add(n7)
n8 = int(input("Enter 8th number: "))
s.add(n8)

print(s)



# s = {1,2,3,3,4,5,7,8}
# print(s)