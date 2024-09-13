# Recursion

def show_five_to_one(n): # function definition

     # ye agr na o to ye infinitily chaly ga or ek asa point ay ga jaha puri
     # memory accupy jay ge or program crash kr jay ga es leay zruri hoti
    if(n == 0):
        return # jb return k sth kch nae likhty to wo control ko return kr rha hota hai not valuse
    print(n)
    show_five_to_one(n-1) # The function will keep calling itself until the value of n becomes 0

show_five_to_one(10) # calling function