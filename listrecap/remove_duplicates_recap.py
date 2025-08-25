# Remove duplicates from a list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("List without duplicates:", unique_items)