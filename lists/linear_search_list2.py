# My own Linear Search program 🙂

# Taking list from user
numbers = [5, 12, 7, 9, 20, 15]

# Ask user what number to find
search = int(input("Enter number to search: "))

# Check each number one by one
index = 0
while index < len(numbers):
    if numbers[index] == search:
        print("Found at position", index)
        break
    index += 1
else:
    print("Number not found in the list.")
