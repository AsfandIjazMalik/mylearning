# Finally Keyword 

# The finally keyword in Python is used in exception handling to define a block of
# code that will always run, no matter what. Whether an error happens or not, the
# finally block will execute after the try and except blocks.

def fun():
    # Inform the user that indexing starts from 0.
    print('You can enter 0 because indexing starts from 0 to n-1')
    
    try:
        lst = [1, 2, 'Asfand Ijaz Malik', False, 3.6, True]
        # Get user input for the index number
        numindex = int(input("Enter the index number of the value you wish to retrieve: "))
        # Retrieve and print the value at the specified index
        print(f'At index {numindex} the value is:\n{lst[numindex]}')
        return 1  # Return from the function if successful
        
    except IndexError:  # Handle the specific error for out-of-range indices
        print("Index Out Of Range Error")
        return 0  # Return from the function if an error occurs
        
    finally:
        # This block runs regardless of what happened in try or except
        print("IMPORTANT NOTE:\nThe finally block always executes, whether the try or except blocks were run.")
        
    # This print statement will NOT run because the function returns from the try or
    # except block and white dashed underline is highlighing this will not execute 
    print("This will not run, regardless of whether try or except executed, because the function returns from try or except.")

# Call the function to execute the code
fun()

# NOTE : Function exit after return 