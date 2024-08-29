print("If Elif Else Ladder")

# Taking user input
age = int(input("Enter your age :")) 

# Check the entered age by user if it is greater or equal to 18
if (age>=18):
    print("You Enter your ages is:", age)
    print("You are Eligible")

# Checking age if it is less than 0
elif(age<0):
    print("Your are entering invalid age please enter age above 0")

# Checking age if it is equal to 0
elif(age==0):
    print("0 is not Valid Age")

# iF above condition is not match else block will print
else:
    print("You Enter your ages is:", age)
    print("You are not Eligible")

# It will Execute after if-Else Block
print("THANK YOU!!!") # it is connected with if statement

# All these connected with each other cheching one by one which
