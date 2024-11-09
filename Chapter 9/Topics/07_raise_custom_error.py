# Raise Custom Error 
# Es me Hud se error raise krty hain
# Why we raise error Intentially?
# Ta k program ruky jay or kch unexpeted na o jay.
num = int(input('Enter Number between 1 and 10: '))

if ( num < 1 or num > 10):
    raise ValueError("Number is not Between 1 and 10")
else:
    print(f"Good Number is {num} which Between 1 and 10")
    
# > Clear Communication: They let you explain specific problems in your code more clearly.
# > Better Control: You can manage different types of errors separately.
# > Easier to Read: It makes your code easier to understand for someone else reading it.
# > In short, custom errors help you handle problems in your code in a way that makes sense for your situation!