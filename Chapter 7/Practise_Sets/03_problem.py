# Write a program to print multiplication table of a given number using while loop

num_table = int(input("Enter a number for the multiplication table you want to print: "))

a = 1

while(a <= 10):
    print(f"{num_table} x {a} = { num_table * a} ")
    a += 1