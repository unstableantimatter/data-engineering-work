letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {l : p for l, p in zip(letters, points)}

# Handling space tiles
letter_to_points[" "] = 0

print(letter_to_points)

# Function to score a word played
def score_word(word):
  point_total = 0
  for char in word:
    point_total += letter_to_points.get(char, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

# Dictionary of players with corresponding list of words they have played
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],	"wordNerd":["EARTH", "EYES", "MACHINE"],	"Lexi Con":["ERASER", "BELLY", "HUSKY"],	"Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

# Scoring the words that have been played already
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points

# Create callable function to handle scoring when a new word is played
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
      player_to_points[player] = player_points

# Handling new words played and new players
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

# Print the current game score
print(player_to_points)





