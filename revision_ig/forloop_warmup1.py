numbers = []                                   # Empty list
n = int(input("How many numbers?"))            # Python needs to know how many times to repeat asking for numbers.

for i in range(n):                             # Loop n times to take user input, n is a value decided at runtime
    value = int(input("Enter the numbers:"))   # Letting the user decide what to enter
    numbers.append(value)                      # Adding user-input to the empty list

for num in numbers:                            # Loop through each element
    print(num * 2)                             # Print the result of each element multiplied by 2