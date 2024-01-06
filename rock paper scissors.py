import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_img = [rock, paper, scissors]

user_choice = input("What do you choose, Rock Paper or Scissors?\n").lower()

valid_choice = ["rock", "paper", "scissors"]


if user_choice in valid_choice:
    print("Your Choice:", user_choice)
    print(game_img[valid_choice.index(user_choice)])
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")


computer_choice = random.choice(valid_choice)
print("Computer chose:", computer_choice)
print(game_img[valid_choice.index(computer_choice)])

if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("Congratulations! You win!")
else:
    print("Computer wins! Better luck next time.")
