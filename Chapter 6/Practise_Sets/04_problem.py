# Problem 04
 
# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
# Write a program to detect these spams.

c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

comment = input("Enter your commnt: ")

if( c1 in comment or c2 in comment or c3 in comment or c4 in comment):
    print("This is spam ")

else:
    print("This is not spam")