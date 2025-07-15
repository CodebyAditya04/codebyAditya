# Original list with some duplicate numbers
numbers = [10, 20, 30, 20, 40, 30, 50, 10, 60]

# Empty list to store only unique numbers (no duplicates)
num_2 = []

# Go through each number in the original list
for num in numbers:
    if num not in num_2:            # If the number is not already in the new list, add it
       num_2.append(num)            # Adding the number in the new list

print("list with duplicates:", numbers)               # Print the original list (with duplicates)
print("list without the duplicates:", num_2)          # Print the new list with duplicates removed