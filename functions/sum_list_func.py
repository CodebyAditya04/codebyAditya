# Given list of numbers
numbers = [10, 20, 30, 5]

# Define a function called sum_list which takes a list of numbers as parameter
def sum_list(numbers):
    total = 0                 # Variable to store the total
    for num in numbers:       # loop through each number
        total += num          # add it to total
        print("total of all numbers in list is:", total)

# Calling the function to run the code
sum_list(numbers)