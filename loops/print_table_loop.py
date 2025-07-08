#program to print the multiplication table of a given number

#ask the user to enter a number
num = int(input("Enter the number to print it's multiplication table:"))

for i in range(1,11):                               #loop from 1 to 10
    print(f"{num} x {i} = {num * i}")