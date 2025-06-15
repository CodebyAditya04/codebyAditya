cart = []

def show_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("\nYour cart:")
        for i, item in enumerate(cart, 1):
            print(f"{i}. {item}")

def add_item():
    item = input("Enter the item to add: ")
    cart.append(item)
    print(f"'{item}' added to cart.")

def remove_item():
    show_cart()
    item = input("Enter the item to remove: ")
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from cart.")
    else:
        print(f"'{item}' not found in cart.")

def main():
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Show cart")
        print("2. Add item")
        print("3. Remove item")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_cart()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Thanks for using the shopping cart. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()