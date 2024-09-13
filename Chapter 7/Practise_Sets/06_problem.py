# Problem 06

# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter a number to calculate its factorial: "))
fac = 1
for i in range(1 ,num+1):
    fac = fac * i
    print(fac)

print(fac)