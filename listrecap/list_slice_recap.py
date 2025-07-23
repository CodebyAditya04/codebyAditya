numbers = [1,2,3,4,5,6,7,8,9,10]

# Print the first six elements (indexes 0 to 5)
print("The first five elements are:")
print(numbers[0:5])                 # This gets the first five element by saying start at index 0 and stop at 4(excluding 5)

# Print the last three elements of the list
print("The last three elements are:")
print(numbers[-3:])                 # Negative indexing gets the last 3 elements: 8, 9, 10

# Print every second element from the list
print("Every second element from the list:")
print(numbers[::2])                 # Step of 2 skips every second number: 1, 3, 5, 7, 9

# Print the reversed list
print("The reversed list is:")
print(numbers[::-1])                # Slicing with a step of -1 reverses the list

# Print items from index 3 to 7 (inclusive of index 3 and exclusive of index 8)
print("Items from index 3 to 7 are:")
print(numbers[3:8])                 # Outputs: 4, 5, 6, 7, 8