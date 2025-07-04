# Program to calculate the sum of even numbers from 1 to N

N = int(input("Enter a number: "))               # Ask the user to enter a number (N)

total = 0                                        # Variable to store the total sum of even numbers

for i in range(1, N + 1):                                  # Loop through all numbers from 1 to N (inclusive)
    if i % 2 == 0:  # Check if the number is even
        total += i  # Add the even number to the total

print("The sum of even numbers from 1 to", N, "is:", total)      # After the loop ends, print the total sum