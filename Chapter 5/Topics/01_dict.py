print("DICTIONARY DATA TYPE IN PYTHON")

# Dictionary is a collection of keys-value pairs.

mrk = {} # Empty Dictionary

marks = {
    "Asfand": 95,   # associated with key = value pair 
    "Saima": 85,
    "Sadaf": 80
}

print(marks,type(marks))
print(marks["Asfand"])

word_meaning = {
    "love" : "Pyar",
    "hate" : "Nafrat",
    "loyal" : "Wafadar",
    "lier" : "Jhota"
}

print(word_meaning)
print(word_meaning["love"])
print(word_meaning.update({"lier" : "JHOTA", "Lawyer": "Wakeel"}))
print("Updated Dictionary", word_meaning)

# if you want to know the marks of anyone you can use their key 
# unlike STRINGS, LIST, TUPLE Which used indexing for check value

# if there are 1000 student with their marks we can't get marks by using index thats why
# dictionaries made in Python to check out marks any other key values pair of thousads 
# we just used key to check their value at once from thousads of data 

# Dictionaries in Python are versatile
# and powerful data structures used for
# storing and managing data in key-value pairs. 

# allowing for fast retrieval of data.
