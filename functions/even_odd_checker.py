# even_or_odd.py
# This program checks if a number entered by the user is even or odd using a function.

# Variable to store the value given by the user
num = int(input("Enter the number to check:"))

# Defined a fucntion called check_even that takes one number as parameter
def check_even(num):
    # Checks if the number is even 
    if num % 2 == 0:
        print("The number is even!")
    # if the number is not even then print this
    else:
        print("The number is odd!")

# Calling the function to run the code
check_even(num)