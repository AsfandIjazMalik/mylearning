# fatorial of any num With Recursion

def fact_of_num(h):
    if h == 1 or h == 0:  # Base case for recursion
        return 1
    return fact_of_num(h - 1) * h  # Recursive call

result = fact_of_num(3)  # Call the function
print(result)  # Output: 6