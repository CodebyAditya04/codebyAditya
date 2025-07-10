# Program to find the largest number in a list

# Create a list of numbers
numbers = [12,15,25,34,56,28,69,16,18,11,10]
max_num = numbers[0]                    # Assume the first number is the largest to start with

for num in numbers:                     # Loop through each number in the list
    if num > max_num:                   # If the current number is greater than max_num, update max_num
        max_num = num                   # Update max_num

# After the loop ends, print the largest number
print("The largest number is:",max_num)
    
