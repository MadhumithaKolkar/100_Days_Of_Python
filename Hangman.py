import random
import time

# start = time.time()
word_list = ["advark","baboon","camel"]

chosen_word = random.choice(word_list)
length = len(chosen_word)
chances = length
word = ['_']*length

# while chances>=1:
#
#     print("".join(word))
#     guess = input("Guess a letter : ")
#     guess = guess.lower()
#
#     letters = {}
#     if guess in chosen_word:
#         count = 0
#         for index,ch in enumerate(chosen_word):
#
#             if ch == guess:
#                 count += 1
#                 letters[index] = ch
#         chances -= count
#         print("---",chances)
#         print("Correct")
#
#         for index in letters:
#             word[index] = letters[index]
#
#
#     else:
#
#         chances -= 1
#         print("Wrong")
#         print(chances)
#
# if "_" in word:
#     print("Game Over")
# else:
#     print("Win")
# print(chosen_word)
# # print("Time taken : ",(time.time()-start)*1000)

guess = (input("Guess a letter : ")).lower()
display = ['_']*len(chosen_word)
print("The chosen word is : ", chosen_word)
for index,char in enumerate(chosen_word):
    if char == guess:
        display[index] = guess
print(display)