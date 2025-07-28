# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to:
# 1. Filter even numbers (x % 2 == 0)
# 2. Square them (x * x)
# 3. Only include squares greater than 10
squares_over_10 = [x * x for x in numbers if x % 2 == 0 and x * x > 10]

# Print the resulting list
print("Squares of even numbers greater than 10:", squares_over_10)
