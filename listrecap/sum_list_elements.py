num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))
num5 = int(input("Enter the fifth number:"))

numbers = [num1, num2, num3, num4, num5]
total = 0

for num in numbers:
    total += num

print("The total is:",total)