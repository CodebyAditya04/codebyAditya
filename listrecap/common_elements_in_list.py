# Define two lists to compare
num1 = [1, 2, 3]
num2 = [2, 3, 4, 5]

# Create an empty list to store common elements
unique_list = []

# Loop through each number in num2
for num in num2:
    if num in num1 and num in num2:           # Check if the number is also in num1
        unique_list.append(num)               # If it is, add it to the unique_list

# Print the results
print("The common elements are:", unique_list)