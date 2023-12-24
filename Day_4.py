#Merssen Twister Pseudo Randomisation
#
# import random
#
# random_integer = random.randint(1,1000000)
# print(random_integer)
# line1 = ["⬜️","️⬜","️⬜"]
# line2 = ["⬜️","⬜️","️⬜"]
# line3 = ["⬜️","⬜️","⬜️"]
# map = (line1,line2,line3)
# print(map)
# name = "Madhumitha.Kolkar"
# name = name.split('.')
# print(name)
# name = ''.join(name)
# print(name)

#Rock,Paper,Scissor Game

import random

rock_paper_scissors = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

x=0
wiz_points = 0
user_points = 0
for x in range(10):
    user_choice = int(input("""Choose:
1--> Rock
2--> Paper
3--> Scissors
"""))
    user_choice = user_choice-1

    wiz_choice = random.randint(0,2)
    hMap = {0:"Rock",1:"Paper",2:"Scissors"}
    print(f"You chose: {hMap[user_choice]}{rock_paper_scissors[user_choice]}")
    print(f"Wiz chose: {hMap[wiz_choice]}{rock_paper_scissors[wiz_choice]}")

    if (user_choice==1 and wiz_choice==0) or (user_choice==0 and wiz_choice==2) or (user_choice==2 and wiz_choice==1):
        print("You win")
        user_points+=1
    elif (user_choice==0 and wiz_choice==1) or (user_choice==2 and wiz_choice==0) or (user_choice==1 and wiz_choice==2):
        print("Wiz wins")
        wiz_points+=1
    else:
        print("Draw")
print(f"You scored : {user_points}, Wiz scored : {wiz_points}")
if user_points>wiz_points:
    print("You win")
elif wiz_points>user_points:
    print("Wiz won")
else:
    print("You and wiz both scored equally.")