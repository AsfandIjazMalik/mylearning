# LOCAL AND GLOBAL VARIABLES

# Local Variable: Yeh wo variable hai jo sirf function ke andar kaam karta hai; function ke bahar access nahi ho sakta.
# Global Variable: Yeh wo variable hai jo program ke kisi bhi hissen mein kaam karta hai; kisi bhi function se access ho sakta hai.
# Global aur local variables ka use code ko organized rakhta hai aur naming conflicts se bachata hai 
# (conflict hota hai jab do alag jagon par same naam ke variables hon aur unka use confused ho sakta hai).

a = 3
print(f'The Global Variable is {a}')

def local_variable():
    # Yeh line error degi kyunki "a" naam ka variable is function mein pehle hi define hai (as a local variable).
    # Agar "a" pehle define na hota, to hum global variable "a" ko access kar sakte they.
    # print(f'The Global Variable is {a}')
    
    # Local variable woh hota hai jo sirf function ke andar define aur use hota hai.
    # Isay function ke bahar access nahi kar sakte.
    a = 1 
    print(f'Local variable is {a}')
    
local_variable()
print(f'Again\nThe Global Variable is {a}')

# Global Variable ko hum function ke andar bhi use kar sakte hain "global" keyword ki madad se
# Agar hume function ke bahar se us variable ko access karna ho aur uska value change karna ho, 
# to "global" keyword use karte hain.

def global_variable_inside_fun():
    print(f'\nGlobal Variable Inside a Function')
    global a  # Yeh "global" keyword variable ko globally accessible banata hai
    a = 10  # Ab humne global variable "a" ka value function ke andar change kar diya hai.
    
    # Is "global" keyword ka matlab hai ke ab "a" variable global scope mein hai,
    # isliye hum function ke andar se iska value change kar sakte hain aur yeh change
    # poore program mein (global scope mein) nazar aayega.
   
# Function ko call karte hain    
global_variable_inside_fun()
print(a)  # Function ke bahar se global variable ko access karna