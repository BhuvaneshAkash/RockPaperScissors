rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
#user choice 
game_choice = [rock , paper , scissors]
user_choice = int(input("choose 0 for rock for paper 1 for scissors 2 :"))
print(game_choice[user_choice])
#opponent choice (coumpter's choice)
computer_choice = random.randint(0,2)
print(game_choice[computer_choice])
if user_choice>=3 or user_choice<0:
  print("You are typed an Wrong number\n \n YOU LOSE \n ")
elif computer_choice ==0 and user_choice ==2:
  print("You Lose")
elif user_choice==0 and computer_choice ==2:
  print("you win")
elif user_choice == 0  and computer_choice ==1 :
  print("You win")
elif computer_choice == 0 and user_choice == 1:
  print("you lose")
elif user_choice ==1 and computer_choice == 2:
  print("you lose")
elif computer_choice ==1 and user_choice ==2:
  print("you win")
else :
  print("draw")  