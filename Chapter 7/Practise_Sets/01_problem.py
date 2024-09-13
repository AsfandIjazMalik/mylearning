# Priblem 01

# Write a program to print multiplication table of a given number using for loop.

num_table = int(input("Enter a number for the multiplication table you want to print: "))

for i in range(1, 11):
    print(num_table, "x", i , "=" , num_table *i )
print("\n")


# by using f string
num_table_f_string = int(input("Enter a number for the multiplication table you want to print with F string: "))
for t in range(1, 11):
    # An f-string (formatted string literal) in Python is a way to embed expressions inside string literals,
    # using curly braces {}. Introduced in Python 3.6, f-strings provide a concise and efficient way to format strings.
    print(f"{num_table_f_string} x {t} = {num_table_f_string * t}") #

