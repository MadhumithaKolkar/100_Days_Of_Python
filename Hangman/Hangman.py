import random
import time

# start = time.time()
word_list = ["advark","baboon","camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
display = ['_']*len(chosen_word)
chances = 6
end_of_game = False

print(f"Chances = {chances}")
print(stages[chances])
while not end_of_game and "_" in display:

    guess = (input("Guess a letter : ")).lower()
    same_char = 0

    for index,char in enumerate(chosen_word):
        if char == guess:
            display[index] = guess

    if guess not in chosen_word:
        chances -= 1

    print(f"Chances left = {chances}")
    print("".join(display))
    if chances <= 0: end_of_game = True
    print(stages[chances])

if "_" in display:
    print("Sorry but you lost !")
else:
    print("You win !")
    end_of_game = True