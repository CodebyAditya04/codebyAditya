# Program to find and print all factors of a number

# Ask the user to enter a number
n = int(input("Enter the number:"))

# Loop from 1 to n (inclusive)
for i in range(1,n+1):            
    if n % i == 0:             # Check if 'i' is a factor of 'n'
        print(i)               # If yes print the factor