movies = [
    "Inception", "Interstellar", "Tenet", "Dunkirk", "Memento",
    "The Dark Knight", "Batman Begins", "Oppenheimer", "Prestige"
]

print(" Full Movie List:")
print(movies)

print("\n Top 3 movies:")
print(movies[:3])

print("\n Last 3 movies:")
print(movies[-3:])

print("\n Middle segment (4th to 6th):")
print(movies[3:6])

print("\n Movies in reverse order:")
print(movies[::-1])

n = int(input("\nHow many of your top movies do you want to save? "))
print("\n Your saved favorites:")
print(movies[:n])
