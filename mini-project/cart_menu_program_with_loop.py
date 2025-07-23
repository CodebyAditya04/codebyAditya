# Initialize an empty list to act as the shopping cart
cart = []

# Loop indefinitely until the user chooses to exit
while True:
    # Display the shopping cart menu
    print("\nShopping cart menu")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")
    
    # Ask the user for their choice
    choice = input("Enter your choice (1-4): ")

    # Option 1: Add an item to the cart
    if choice == "1":
        item = input("Enter the item name: ")
        cart.append(item)  # Add the item to the cart
        print(f"'{item}' has been added to your cart!")

    # Option 2: Remove an item from the cart
    elif choice == "2":
        item = input("Enter item name to remove: ")
        if item in cart:
            cart.remove(item)  # Remove item if it exists
            print(f"'{item}' has been removed from your cart!")
        else:
            print("Couldn't find the item in the cart!")

    # Option 3: View all items currently in the cart
    elif choice == "3":
        if cart:
            print("Your cart contains:")
            for item in cart:
                print("-", item)  # Display each item
        else:
            print("Your cart is empty!")

    # Option 4: Exit the program
    elif choice == "4":
        print("Goodbye! Please visit again :)")
        break  # Exit the loop

    # Handle invalid menu options
    else:
        print("Invalid option! Please choose from 1-4")
