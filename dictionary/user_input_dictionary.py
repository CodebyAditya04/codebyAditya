# Take input from the user (a sentence or some text)
text = input()

# Split the text into words (by default split() separates by spaces)
words = text.split()

# Create an empty dictionary to store word frequencies
freq = {}

# Loop through each word in the list 'words'
for word in words:
    # Use .get() to check if the word is already in dictionary
    # If not found, default value = 0, then add +1
    freq[word] = freq.get(word, 0) + 1

# Print the final dictionary showing each word and its frequency
print("Your words and their frequncy in dictionary is:", freq)