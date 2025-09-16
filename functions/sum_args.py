nums = ()

# Define a function that can take any number of arguments
def add_numbers(*nums):        # *nums collects all numbers into a tuple
    total = 0                  # Temporary variable to store the running total
    for num in nums:           # Loop through each number in nums
        total += num           # Add the current number to total
    return total               # Return the final sum to the caller

# Call the function with 3 numbers and print the returned value
print(add_numbers(10, 20, 30))

# Call the function with 2 numbers and print the returned value
print(add_numbers(5, 15))