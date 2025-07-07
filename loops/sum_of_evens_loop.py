# Program to find the sum of even numbers from 1 to N

# Take input from user
n = int(input("Enter a number: "))

# Initialize sum variable
sum_even = 0

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

# Print the result
print("Sum of even numbers from 1 to", n, "is:", sum_even)
