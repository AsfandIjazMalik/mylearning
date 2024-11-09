# Exception Handling
# It is a way to manage errors without stopping the program, allowing a message to be displayed instead.
# Instead of crashing, a message will be shown if an error occurs, keeping the program running.

# An error might occur if the user enters something other than a number.
try:
    num_table = int(input("Enter the number corresponding to the table you wish to execute: "))
    
    # Using a loop to print the multiplication table
    for i in range(1, 11):
        print(f"{num_table} x {i} = {num_table * i}")
    
# IN except we can handling any Spicific error whcih can be occur during program execution
except ValueError: # specific error
    print("Please enter a valid number in range 1 to any number.")
    
print("\nDone")

# Imp NOTE: I can also handle specific error with exception handling lik...
# 1. ValueError 2. TypeError 3. ZeroDivisionError
# 4. IndexError
# 5. KeyError
# 6. FileNotFoundError
# 7. IOError
# 8. AttributeError
# 9. ImportError
# 10. OverflowError
# 11. RuntimeError
# 12. AssertionError
# 13. MemoryError
# 14. NameError
# 15. IndentationError
# 16. SyntaxError
# 17. StopIteration
# 18. KeyboardInterrupt
# 19. NotImplementedError
# 20. EnvironmentError
# 21. PermissionError
# 22. EOFErro
# And many more other error can hadle 