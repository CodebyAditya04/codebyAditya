# List of numbers to search through
numbers = [10,20,20,30,40,100,50,60,69,66,65]

# Start by assuming the first number is both the largest and second largest
max_num = numbers[0]             
sec_num = numbers[0]

# Go through each number in the list
for num in numbers:
    if num > max_num:                     # If the current number is bigger than the current max,
        sec_num = max_num                 # update second largest to be the old max,
        max_num = num                     # and update max to be the new number

# If the number is not the max, but bigger than current second largest,
    elif num > sec_num and num != max_num:
        sec_num = num                       # update the second largest

# Print the final result
print("The second largest number is:", sec_num)