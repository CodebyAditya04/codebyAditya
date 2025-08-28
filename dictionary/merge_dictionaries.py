dict1 = {"Aman": 88, "Riya": 92}            # first dictionary
dict2 = {"Kabir": 76, "Neha": 95}           # second dictionary

merged_dict = dict1.copy()                  # make a copy of dict1 so original is safe
merged_dict.update(dict2)                   # add all key-value pairs from dict2 into it

print("Merged dictionary:", merged_dict)    # print final merged dictionary