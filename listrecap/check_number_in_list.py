numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

guess = int(input("Enter your number:"))

if guess in numbers:
    print("the number is in the list!")

else:
    print("the number is not in the list!")