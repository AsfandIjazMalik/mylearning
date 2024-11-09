# Lambda Functions
# Lambda Fuctions created by using expressions with lambda keyword

# Without with LAMBDA FUNCTION 
def squ(n):
    return n*n
print('The Square is:',squ(6))

# with LAMBDA FUNCTION of ABOVE FUNCTIONS
print(f'\nWith Lambda Function')
square = lambda a : a*a
print(f'The Square is: {square(5)}')

# more exmaple of lamda function

sum = lambda c , n ,f : c+n+f
print(f'\nThe sum of CNB and F is: {sum(2,3,6)}')