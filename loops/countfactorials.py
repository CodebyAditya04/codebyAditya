#write a program to count the number of factors for a given number
num = int(input("Enter the number:"))                  #taking input from user
i = 1                                                  #starting from 1
factors = 0                                            #variable for factors
while i <= num:                                        #start the loop from 1 to the number
	if num % i == 0:                                   #if num and i are divisible and reminder is 0, it's a factor
		print(i)
		factors += 1                                   #increase the factor count by 1
	i += 1                                             #increase i count by 1

print("The total number of factors:", factors)         #print the total number of factors