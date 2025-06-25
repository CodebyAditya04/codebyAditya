password = "secret"
attempts = 0

while attempts < 3:
	guess = input("Enter the password:")

	if guess == password:
		print("Access granted!")
		break
	else:
		print("Invalid password!")
		attempts += 1

if attempts == 3:
	print("Too many attempts. Try again later!")