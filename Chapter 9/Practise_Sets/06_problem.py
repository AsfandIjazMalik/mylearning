# 06 Problem
# Write a program to input name, marks and phone number of aN Employee
# and format it using the format function like below:
# “The name of the Employee is Asfand Ijaz Malik, his Salary is 200000 and phone number is 99999888”

name = input("Enter your name: ")
salary = int(input("Enter your Salary: "))
phone_number = int(input("Enter your Phone Number: "))

info = 'The name of Person is {} his Slary is {} and his Phone Number is {}'.format(name, salary,phone_number)
print(' The Employess Info are below\n',info)

