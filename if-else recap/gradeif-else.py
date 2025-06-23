marks = int(input("Enter the grades:"))

if marks >= 90 and marks <= 100:
	print("Grade A+")
elif marks >= 80 and marks <= 89:
	print("Grade A")
elif marks >= 70 and marks <= 79:
	print("Grade B")
elif marks >= 60 and marks <= 69:
	print("Grade C")
elif marks >= 50 and marks <= 59:
	print("Grade D")
else:
	print("Fail")