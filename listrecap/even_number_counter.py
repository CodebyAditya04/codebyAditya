numbers = [10,11,14,13,15,16,18,17,23,19]
num = numbers[0]
evennum = 0
for num in numbers:
    if num % 2 == 0:
        evennum += 1
        
print("Total even numbers are:",evennum)