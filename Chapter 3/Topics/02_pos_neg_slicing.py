# STRING SLICING IN PYTHON 
# A string in python can be sliced for getting a part of the strings.

# positive slicing
name = "Asfand Ijaz Malik"
print(name[0:3]) # In Python or in other Programming Languages ginti 0 se start o ge 0 1 2 3 ....100000000000000 

#Negative Slicing 
# Not used in PYthon or Can be ask question in Interview

print(name[-8:-2])
print(name[2:8])

# SLICING WITH SKIP VALUE

f = "abcdfghijklmopqrstuvwxyz"
# its mean start from index 2 and end at index 14 
# with skiping the valuse after 3 indexes 3 mean 2 
# value value skip 4 mean 3 value skip 5 mean 4 value skip

skipp = f[2:14:3]   
print(skipp)