cart = []

cart.append("milk")
cart.append("bread")
cart.append("eggs")

print("Items in cart:")
for item in cart:
    print("-", item)

cart.remove("bread")
print("\nAfter removing 'bread':")
print(cart)