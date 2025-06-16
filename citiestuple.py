cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Dehradun", "Bangalore")

letter = input("Enter a starting letter: ").lower()

print(f"Cities starting with '{letter}':")
found = False

for city in cities:
    if city.lower().startswith(letter):
        print(city)
        found = True

if not found:
    print("No city found with that letter.")
