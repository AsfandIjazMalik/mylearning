print("SET IN PYTHON")

# SET IS COLLECTION OF WELL DEFINE OBJECTS
# no repetition allowed!

empty_dictionary = {} # Empty Dictionary
# dont use dict = {} it will create empty dictionary

# Empty Set this is the way to make an empty set in Python
empty_set = set() 

print(type(empty_set ))
print(type(empty_dictionary))

non_repitive_set = {1,1,1,2,3,34,4,4}
print("Set is non repetivie or no duplicate data print in Set\n1 and 4 was repetive data\n",non_repitive_set)

empty_set.add(1) # .add only one arguments
print(empty_set)