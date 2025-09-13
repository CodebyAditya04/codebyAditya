# Define a function 'greet' with a default parameter 'name' set to "Guest"
def greet(name="Guest"):
    # Print a greeting message using the provided name
    print("Hello,", name)

# Call the function with "Aditya" as input
greet("Aditya")

# Call the function without input, so it uses the default value "Guest"
greet()