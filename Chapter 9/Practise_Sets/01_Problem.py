# 01_Problem
# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files
# are not present, a message without exiting the program must be printed prompting the same.

try:
    with open('1.txt', 'r') as f:
        print(f.read())
        
except:
    print("File not Found")
try:
    with open('2.txt', 'r') as f:
        print(f.read())
        
except:
    print("File not Found")        
try:
    with open('3.txt', 'r') as f:
        print(f.read())
        
except:
    print("File not Found")
    
    
print('Thank You No Error Occur due to Try Except')