# 3. A list contains the multiplication table of 10. write a program to convert it to vertical string of same numbers.
# 10
# 20
# 30
# .
# .
# .

lst_of_table_of_10 = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
vertical_string = '\n'.join(lst_of_table_of_10) # join funtion only take list of stringtype
print(vertical_string)
print(type(vertical_string))