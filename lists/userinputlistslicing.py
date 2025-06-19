games = ["Chess", "Ludo", "Carrom", "Snakes", "Monopoly", "Scrabble", "Uno"]

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

print(f"\nGames from index {start} to {end - 1}:")
print(games[start:end])
