# Original string containing key-value pairs separated by commas and colons
text = "name:Aditya,age:21,language:Python"

# Split the text at commas to separate each key-value pair
pairs = text.split(",")

# Loop through each key-value pair
for item in list:
    # Split each pair at the colon to separate the key and value
    key_value = item.split(":")
    # Print the key and value with clear labeling
    print("key:", key_value[0], "| value:", key_value[1])