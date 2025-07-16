# Print numbers greater than average from list
# List of numbers to work with
numbers = [10,20,30,40,50]

# Initialize a variable to hold the sum of all numbers
total = 0

# Loop through the list and add each number to total
for num in numbers:
    total += num        # Adding each number to total

# Calculate the average (mean) of the list
average = total/len(numbers)

# Loop again to find and print numbers greater than the average
for num in numbers:
    if num > average:         # If there's a number bigger than average
        print(num)            # Print it
