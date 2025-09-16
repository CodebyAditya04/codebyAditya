# Ask the user to enter a number and store it in 'num'
num = int(input("Enter the number to find the square:"))

# Define a function that takes one number as input and returns its square
def square(num):
    return num * num         # multiply the number by itself and return the result

# Call the function and print the returned value
print("The square of the number is:", square(num))