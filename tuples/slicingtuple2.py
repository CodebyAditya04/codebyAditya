days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("All days of the week:")
print(days)

n = int(input("how many days from the start do you want to see? "))

print(f"\n the first {n} days are:")
print(days[:n])

print("the weekend days are:")
print(days[-2:])

print("the workingdays are:")
print(days[:-2])