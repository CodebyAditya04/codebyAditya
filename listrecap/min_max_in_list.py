# Find smallest and largest number in list without using built-in functions
# List of numbers to check
numbers = [25, 10, 40, 5, 60]

# Start by assuming the first number is both the smallest and the largest
max_num = numbers[0]                  # Variable for the largest
min_num = numbers[0]                  # Variable for the smallest

# Loop through each number in the list
for num in numbers:
    if num < min_num:                  # If the current number is smaller than min_num
        min_num = num                  # Update min_num
    elif num > max_num:                # If the current number is larger than max_num
        max_num = num                  # Update max_num

# Print the results
print("The smallest number is:", min_num)
print("The largest number is:", max_num)
