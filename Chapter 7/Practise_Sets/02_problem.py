# Problem 02

# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.


lst = ["Asfand" , "Saima" , "Sadaf", "Shahzad" , "Shahbaz"]

for name in lst:
    if(name.startswith("S")):
        print("Hi how are you",name)

print("\nWith F sting\n")

for nme in lst:
    if(nme.startswith("A")): # startwith() is not a standalone built-in function in Python; it is a method that belongs to string objects (i.e., it is a method of the str class).
        print(f"Your are Python Specilist {nme}") # by using f string