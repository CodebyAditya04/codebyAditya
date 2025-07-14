# Manual reverse list program

# Original list of numbers
numbers = [10,20,30,40,50,60,70,80,90,100]

# Empty list to store reversed elements
rev_num = []

# Loop through the list backwards using range
# range(start, stop, step) → step -1 means go in reverse
for i in range(len(numbers) -1, -1, -1):
    rev_num.append(numbers[i])              # Add each element from the end to the new list

# Print the reversed list
print(rev_num)