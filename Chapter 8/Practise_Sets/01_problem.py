# Problem 01

# Write a program using functions to find greatest of three numbers.

a = 10
b = 12
c = 45

def greatest_num(a , b ,c):
    
    if (a>b and a>c):
        print("A is greatest number")

    elif (b>a and b>c):
        print("B is greatest number")

    else:
        print("C is greatest number")
        return(a , b , c)
    

gtmun = greatest_num(a , b , c)
print(gtmun)
