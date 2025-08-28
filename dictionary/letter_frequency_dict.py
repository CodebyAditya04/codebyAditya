text = "banana"

# Create an empty dictionary to store letter counts
length = {}

# Loop through each character in the string
for letter in text:
    if letter in length:            # If letter already exists in dictionary
        length[letter] += 1         # Increase its count by 1
    else:
        length[letter] = 1          # If it's the first time, set count as 1

# Print the dictionary containing each letter and its frequency
print("Number of times each letter has been repeated is:", length)