# Given list of numbers
numbers = [10,15,20,22,55,69,78,80,95,100]

# This will store the total sum of odd numbers
total = 0

# Go through each number in the list
for num in numbers:  
    if num % 2 != 0:                                    # Check if the number is odd
        print("The odd numbers are:",num)               # If it is, print it (optional – for visual check)
        total += num                                    # Add the odd number to the total

# After the loop, print the total of all odd numbers
print("The sum of all odd numbers in given list is:",total)