# operattors in python

number1 = int(input("Enter Your First Numbers: "))
number2 = int(input("Enter Your Second Number: "))
print("\n")

# Arithmatic Operators
print("The Addition of two number",number1+number2)
print("The Substation of two number",number1-number2)
print("The Multiplication of two number",number1*number2)
print("The Division of two number",number1/number2)
print("The Modulus of two number",number1%number2)
'''Exponential will give power 10**3 will be 10x10x10 = 1000'''
print("The Exponential of two number",number1**number2)
'''Provide without point digits like 3.55 Floor Division will provide only 3'''
print("The Floor Division of two number",number1//number2)

# Assignment operator
a = 3
# a +=2 increment of value a by 2 and asign it to a 
# a -=2
# a /=2 # a/2 = 1.5
# a //=2 a/2 = 1 without point digit
# a **=2  3 into the power 2 is 9
# a %=2 a/2 will provide remainder 1
b = 4 # assign 4 to b with = is assignment operator
print(a,b)

# Comparison operators
# it always provides answer in BOLEAN TYPE LIKE true or false
# It is wildly used in if-Else Statements
u = 3
p = 2
print("COMPARISON OPERATORS")
print(u>p) # GREATER THAN
print(u<p) # LESS THAN
print(u!=p) # NOT EQUAL TO
print(u==p) # IS EQUAL TO
print(u>=p) #GREATER OR EQUAL TO
print(u<=p) #LESS THAN OT EQUAL
print("\n")

# LOGICAL OPERATORS
print("LOGICAL OPERATORS\n")
w = 7
q = 100
print(w==q and w!=q)
print(w < q or p < w)
print("OR Is a logical operator and atleat one condition is true")
print("TRUTH TABLE OF 'OR' OPERATOR")
print("True or False is:", True or False)
print("True or True is:", True or True)
print("False or True is:", False or True)
print("False or False is:", False or False)
print("\n")

print("AND Is a logical operator and both will match its return true otherwise its return false")
print("TRUTH TABLE OF AND OPERATOR")
print("True and False is:", True and False)
print("True and True is:", True and True)
print("False and True is:", False and True)
print("False and False is:", False and False)
print("\n")

print("jo true ko false or false ko true bna de usko NOT OPERATOR khty hain")
print(not (False)) # reverse
print(not (True)) # reverse



# BITWISE OPERATORS IS ADVANCE OPERATORS NOT COVERED IN  THIS 3 HOURS VIDEO