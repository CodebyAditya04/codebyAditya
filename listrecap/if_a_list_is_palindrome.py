# Given list of numbers
numbers = [1, 2, 3, 2, 1]

# Check if the list is equal to its reverse
if numbers == numbers[::-1]:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")