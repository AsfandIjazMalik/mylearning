# Problem 06 

# Write a program to find out whether a given post is talking about “Asfand” or not.

post = input("Enter Post: ")

if("Asfand".lower() in post.lower()):
    print("Yes, post is talking about Asfand\nAnd post is",post)

else:
    print("No, post is not talking about Asfand\nAnd post is",post)