# Linear Search Program

# List of elements
numbers = [10, 20, 30, 40, 50]

# Element to search for
target = int(input("Enter the number to search: "))

# Flag to track if element is found
found = False

# Loop through the list
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Element found at index {i}")
        found = True
        break

# If element not found
if not found:
    print("Element not found in the list.")
