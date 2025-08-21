# Input string
text = "python is fun and python is easy"

# Split the string into words (default split is on spaces)
words = text.split()

# Empty dictionary to store word frequencies
freq = {}
# Loop through each word in the list
for word in words:
    # If word already in dictionary, increment its count
    # Otherwise, add it with initial value 1
    freq[word] = freq.get(word, 0) + 1

# Print the frequency of words
print("Frequency of words is:", freq)