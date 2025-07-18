# Empty list
cart = []

# Display the shopping cart menu
print("Shopping cart menu")
print("1. Add item")
print("2. Remove item")
print("3. View items")
print("4. Exit")

# Ask the user to enter their choice
choice = input("Enter your choice(1-4):")

# Option 1: Add item to the cart
if choice == "1":
    item == input("Enter the item name:")                 # Get the item name from the user
    cart.append(item)                                     # Add the item to the cart
    print(f"'{item}' has been added to your cart!")

# Option 2: Remove item from the cart
elif choice == "2":
    item == input("Enter item name to remove item:")      # Get the item name to remove
    if item in cart:
        cart.remove(item)                                 # Remove the item if it exists
        print(f"'{item}' has been removed from your cart!")
    else:
        print("Couldn't find the item in the cart!")      # Item not found

# Option 3: View items in the cart
elif choice == "3":
    if cart:
        print("Your cart contains:")
        for item in cart:
            print("-",item)                           # List each item
    else:
        print("Your cart is empty!")

# Option 4: Exit the program
elif choice == "4":
    print("Goodbye! Please visit again :)")

# Handle invalid inputs
else:
    print("Invalid option! Please choose from 1-4")
    