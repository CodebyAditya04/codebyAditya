# Count even and odd numbers in a list
# List of numbers to check
numbers = [10, 15, 22, 33, 42, 55, 100]

# Variables to store the value of even and odd number counts
count_even = 0
count_odd = 0

# Loop through the list
for num in numbers:
    if num % 2 == 0:                   # If the number is even
        count_even += 1                # Add 1 to count_even
    elif num % 2 != 0:                 # If the number is odd
        count_odd += 1                 # Add 1 to count_odd 

# Print the results
print("Total number of even numbers is:", count_even)
print("Total number of odd numbers is:", count_odd)