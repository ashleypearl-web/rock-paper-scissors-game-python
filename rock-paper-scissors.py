import random
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

game_images = [rock, paper, scissors]

choices = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))
print(f"You chose: \n{game_images[user_input]}")

computer_choice_index = random.randint(0, 2)
print(f"Computer chooses: \n{choices[computer_choice_index]}")
print(game_images[computer_choice_index])

if user_input not in [0, 1, 2]:
    print("Invalid input. Please choose 0, 1, or 2.")
else:
    if (computer_choice_index == 0 and user_input == 2) or \
       (computer_choice_index == 1 and user_input == 0) or \
       (computer_choice_index == 2 and user_input == 1):
        print("You lose!")
    elif (computer_choice_index == 0 and user_input == 1) or \
         (computer_choice_index == 1 and user_input == 2) or \
         (computer_choice_index == 2 and user_input == 0):
        print("You win!")
    else:
        print("It's a draw!")