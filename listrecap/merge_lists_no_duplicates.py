list1 = [1, 2, 3, 4]                    # First list
list2 = [3, 4, 5, 6]                    # Second list
merged_list = []                        # Create an empty list to hold the merged result

# Merge the two lists using + operator
merged_list = list1 + list2

# Create a new list to store only unique elements
unique_list = []

# Loop through the merged list
for num in merged_list:
    if num not in unique_list:          # If the number is not already in unique_list, add it
        unique_list.append(num)

# Display the final list with duplicates removed
print("Merged list without duplicates:", merged_list)