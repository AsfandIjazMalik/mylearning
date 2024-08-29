fruits = {
    "red": "Apple",
    "green": "Grapes",
    "yellowish": "Mango"
}

print(fruits) # Printing dictionary

print(fruits["red"]) # provide value of red key is Apple

# we can update and add new item which is present in
# our current dictionary because dictionaries is mutable

fruits.update({"green":"banana", "List": (1,3,4,5,)}) 
print(fruits) # Printing dictionary

# Provide keys of values in list form like this dict_keys (['red', 'green', 'yellowish'])
print(fruits.keys())   

# Provide values of keys in list form like this dict_values(['Apple', 'Grapes', 'Mango'])
print(fruits.values())

# KEY VALUE PAIRS IN TUPLE FORM ([('red', 'Apple'), ('green', 'Grapes'), ('yellowish', 'Mango')])
print(fruits.items()) 

# Print None if yellowish key does not exits in our dictionary 
# If yellowish key exist it provide the value of key yellowish which is Mango
print(fruits.get("yellowish"))  

# it provide same answer like above BUT
# Provide ERROR if yellowish key does not exits in our dictionary
#  If yellowish key exist it provide the value of key yellowish which is Mango
print(fruits["yellowish"]) 

# IMPORTANT NOTE and can be asked for it in Interview 
# But with Square Brakets I serach for the key which is not exit our fruits dictionary it provides error
# But with Round Brakets and get() function I serach for the key which is not exit in our fruits dictionary it provides None
# Mean to say give same answer but not the same 

print(fruits.pop("red"))
print(fruits)