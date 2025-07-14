# List of numbers
numbers = [22,11,10,60,20,28,33,99,55]

# Start by assuming the first number is the smallest
min_num = numbers[0]

# Go through each number in the list
for num in numbers:
    if num < min_num:                # If the current number is smaller than min_num
        min_num = num                # Update min_num with the smaller number
 
# After the loop, print the smallest number found
print("The smallest number is:",min_num)