import random
import hangman_words
import hangman_art
import os

word_list = hangman_words.word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
chances = 6
end_of_game = False

print(" ".join(display))
print(hangman_art.stages[chances])
while not end_of_game and "_" in display:

    guess = (input("Guess a letter : ")).lower()

    for index, char in enumerate(chosen_word):
        if char == guess:
            display[index] = guess

    if guess in display:
        print(f"You've already guessed {guess}")
    elif guess not in chosen_word:
        print("You guessed a letter that's not in the word. You lose a life.")
        chances -= 1

    print(" ".join(display))
    if chances <= 0:
        end_of_game = True
    print(hangman_art.stages[chances])

if "_" in display:
    print(f"Sorry but you lost !, the correct answer was {chosen_word}")
else:
    print("You win !")
    end_of_game = True
