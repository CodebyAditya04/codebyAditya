while True:                                                             # Start an infinite loop to allow multiple calculations
    num1 = float(input("Enter the first number:"))                      # Ask the user to enter the first number
    num2 = float(input("Enter the second number:"))                     # Ask the user to enter the second number
    operator = input("Enter the operator(+,-,*,/):")                    # Ask the user to choose an operator
# Check which operator was entered and perform the correct operation
    if operator == "+":                                                 
        print(num1 + num2)          #Addition
    elif operator == "-":
        print(num1 - num2)          #Subtraction
    elif operator == "*":
        print(num1 * num2)          #Multiplication
    elif operator == "/":
        if num2 != 0:
            print(num1/num2)                                  # Division (only if second number is not zero)
        else:
            print("Not divisible by zero!")                   # If user tries dividing by zero print this message
    else:
        print("Invalid operator!")                            # If the operator is'nt recognized

    again = input("Do you want to go again?(yes/no):")        # Ask the user if they want to calculate again
    if again != "yes":                                        # If the user enters anything other than 'yes', break the loop and stop
        break