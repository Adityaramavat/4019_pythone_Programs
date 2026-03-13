#12.Write a program to display the use of local, global and nonlocal variables


# This variable is accessible everywhere in the file
message = "Global Value"

def outer_function():

    
    # This variable is only alive inside 'outer_function'
    message = "Local Value"
    
    def inner_function():
        
        # 3. NONLOCAL VARIABLE
        # 'nonlocal' tells Python to use the 'message' variable 
        # from the function directly outside this one (outer_function),
        # NOT the global one.
        
        nonlocal message
        message = "Nonlocal Value"
        print(f"Inside inner_function: {message}")

    print(f"Before calling inner:  {message}")
    inner_function()
    print(f"After calling inner:   {message}")


print(f"Start of program:      {message}")
outer_function()
print(f"End of program:        {message}")
