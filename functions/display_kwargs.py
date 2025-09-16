# display_kwargs.py

# Function that accepts any number of named arguments
def display_info(**info):               # **info collects all keyword arguments into a dictionary
    for key, value in info.items():     # Loop through each key-value pair in the dictionary
        print(key, ":", value)         # Print the key and its corresponding value

# Call the function with 3 keyword arguments
display_info(name="Aditya", age=21, grade="A")  

# Call the function with 2 keyword arguments
display_info(name="Aditi", city="Delhi")