# Problem 03

# Can we have a set with 18 (int) and '18' (str) as a value in it?
# Answer : yes we can have 18 as an integer and 18 a string

s = set()
s.add(18)
s.add("18")
print(len(s),s)

