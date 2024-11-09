# Enumerate function 

# enumerate() function Python mein aasan banata hai ke hum list (ya kisi bhi aur iterable)
# mein items ke index (position) ka pata rakh sakain jab hum usay loop mein chalayen.
# Ye hume index aur item dono deta hai.

# Kaise Kaam Karta Hai
# Jab aap enumerate() use karte hain, to ye aapko deta hai:

# Item ka index list mein (default mein 0 se shuru hota hai).
# Aur woh item khud.

names = ['Asfnad Ijaz Malik', 'Faisal Shahzad', 'Tayyab CH', 'Ruksar CH', 'Ibrar Mirza', 'Zain Sheikh']

# Ye loop enumerate() ka use karta hai jo hume index aur item (name) dono deta hai
for index, name in enumerate(names):  # ye ek built-in function hai
    print(f'On Index {index} The Name is {name}')
    
# Index ko kisi aur number se shuru kar sakte hain, jaise 1 ya koi aur number
print(f'\nWE CAN START INDEX FROM ANYWHERE WE WANT\n')
names = ['Asfnad Ijaz Malik', 'Faisal Shahzad', 'Tayyab CH', 'Ruksar CH', 'Ibrar Mirza', 'Zain Sheikh']

# Iss loop mein hum index ko 2 se shuru kar rahe hain using start=2
for index, name in enumerate(names, start=2):
    print(f'On Index {index} The Name is {name}')
    
# IMPORTANT NOTE
# Use enumerate() with: Lists, tuples, strings, sets, and dictionaries (for keys).
# Do not use enumerate() with: Non-iterable objects (like integers, floats, or None).