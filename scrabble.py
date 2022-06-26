letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#using a list comprehension i assigned the keys and values to this dictionary
letters_to_points = {key:value for key,value in zip(letters, points)}

#this will add a value to our letters_to_points dictionary
letters_to_points[' '] = 0

#this functino will score our words!
def score_word(word):
  point_total = 0
  #here we loop through every letter and then use the get function to assign the points. the second argument is a default incase the letter does not exist in our dictionary for points
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total

#current leaderboard
player_to_words = {'player1':['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'LexiCon': ['ERASER', 'BELLY', 'HUSKY'], 'ProfReader': ['ZAP', 'COMA', 'PERIOD']}
#print(player_to_words)

#this function takes in an existing players word and adds it to their word bank.
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  elif player not in player_to_words:
    print('Player is invalid. Please try again')

#this will keep track of scoring
player_to_points = {}

for key, value in player_to_words.items():
  player = key
  words = value
  player_points = 0
  for word in words:
    player_points += score_word(word)
    #this assigns the 'Player' with the updated points they have
  player_to_points[player] = player_points


'''
TO DOS:
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well
'''

print(player_to_points)

#print(player_to_words)