games = ['gta', 'black myth wukong', 'witcher 3', 'elden ring']

print("my games:")
print(games)

game = input("enter a game name to check:")

if games in games:
  print(game,"is in the list")
else:
  print(game,"is not in the list")