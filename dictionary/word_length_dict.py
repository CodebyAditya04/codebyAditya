text = "I love coding"

# Split the text into a list of words
words = text.split()

# Create an empty dictionary to store word lengths
length = {}

# Loop through each word in the list
for word in words:
    # Get the length of the current word using len()
    # Assign it as the value in the dictionary with the word as key
    length[word] = len(word)

# Print the final dictionary showing each word and its length
print("Length of each word in dictionary is:", length)