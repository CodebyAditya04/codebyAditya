keys = ["Aditya", "Aditi", "Rohit", "Kamal"]       # list of keys
values = [100, 98, 99, 96]                         # list of values

# zip() pairs elements from keys and values ->
# dict() then converts these pairs into a dictionary
merged_dict = dict(zip(keys, values))

print("Dictionary created after merging two lists is:", merged_dict)