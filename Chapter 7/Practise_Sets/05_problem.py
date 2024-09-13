# Program 05

# Write a program to find the sum of first n natural numbers using while loop.

number = int(input("enter a number from 1 to n that you want to add: "))

i = 1
sum = 0

while (i <= number):
    sum += i
    i += 1
    print(sum)

print("\n")
print(sum)
