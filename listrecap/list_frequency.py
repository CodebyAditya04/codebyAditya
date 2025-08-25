# Count frequency of elements in a list
elements = [1, 2, 2, 3, 4, 4, 4, 5]
frequency = {}

for item in elements:
    frequency[item] = frequency.get(item, 0) + 1

print("Frequencies:", frequency)