num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 > num2 and num1 > num3:                           #we have to add num1 > num3 because if we won't it would just consider num3 true as it is non-zero.
	print("num1 is the largest")                          #also if statements check to see if a given condition is true so python will just see num1>num2 true and num3(non-zero) true.
elif num2 > num1 and num2 > num3:                          #we need to write full condition for strong logic.
	print("num2 is the largest")
else:
	print("num3 is the largest")
