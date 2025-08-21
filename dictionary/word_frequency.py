# Input string
text = "python is fun and python is easy"

# Empty dictionary to store frequencies
freq = {}

# Loop through each character in the string
for char in text:
    # If character already in dictionary, increment count
    # Otherwise, add it with initial value 1
    freq[char] = freq.get(char, 0) + 1

# Print the frequency dictionary
print("Frequency of each character is:", freq)