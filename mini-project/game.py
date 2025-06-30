secret = 7                                                             #variable for the right number
attempts = 0                                                           #variable for attempts

while attempts < 3:                                                    #loop 3 times
	guess = int(input("Enter the number:"))                            #using guess as variable for user input
	if guess == secret:                                                #checking if guessed number is equal to secret number
		print("Your guess was correct!")                               #if the guess was correct print this message
		break                                                          #break the loop if guess correct
	else:                                                              #if incase the guess was incorrect
		print("Your guess was incorrect, Please try again!")           #print this message if the guess was incorrect
		attempts += 1                                                  #increase the attempts by one each time the user inputs a number

	if attempts >= 3:                                                  #condition to check if the attempts exceed the limit
		print("Game over!")                                            #print this message incase the attempts exceed limit