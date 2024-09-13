# Problem 04

# Write a program to find whether a given number is prime or not.

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# In other words, a prime number is a number that cannot be formed by multiplying two smaller natural numbers.

num = int(input("Enter a number to check if it is a prime number or not: "))

for i in range(2, num):
    if( num%i == 0 ):
        print(num,"is not prime number")
        break
else:
    print(num,"is Prime Number")


