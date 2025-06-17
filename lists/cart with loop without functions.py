cart = []

print("\nShopping Cart Menu")
print("1. Add item")
print("2. Remove item")
print("3. View cart")
print("4. Exit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    item = input("Enter the item name: ")
    cart.append(item)
    print(f"'{item}' has been added to your cart.")

elif choice == "2":
    item = input("Enter the item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"'{item}' has been removed.")
    else:
        print("Item is not in the cart.")

elif choice == "3":
    print("\nYour cart contains:")
    if not cart:
        print("Your cart is empty.")
    else:
        for i, item in enumerate(cart, start=1):
            print(f"{i}. {item}")

elif choice == "4":
    print("Thank you for shopping. Goodbye!")

else:
    print("Please select from options (1-4).")

