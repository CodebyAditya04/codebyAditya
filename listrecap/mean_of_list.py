# List of numbers
numbers = [10,20,30,40,50,60,70,80,90,100]

# Variable to store the total sum of numbers
total = 0

# Loop through each number in the list
for num in numbers:
    total += num               # Add each number to total

# Calculate the average by dividing total by the number of items in the list
average = total/len(numbers)

# Print the average
print("The mean of the list is:", average)