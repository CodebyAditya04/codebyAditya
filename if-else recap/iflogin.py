username = input("Enter the username:")
password = int(input("enter the password:"))

if username == "admin" and password == 2004:
	print("Login successful!")
elif username != "admin" and password == 2004:
	print("Invalid username!")
elif username == "admin" and password != 2004:
	print("Invalid password!")
else:
	print("Invalid credentials!")