"""
Forth day learning Python
This is a simple rock_scissors_paper game
"""

from random import randint
from enum import Enum

# declare game images
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

Choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}


def image_from_choice(choice: str):
    """ Return images from choice """

    return Choices[choice]


def choice_from_number(number: int):
    """ Return choice string from number """

    choice = ""
    match number:
        case 1:
            choice = "rock"
        case 2:
            choice = "scissors"
        case 3:
            choice = "paper"
    return choice


WIN = "You win!"
DRAW = "It's a draw"
LOSE = "You lose.."


def game_result(user_choice: str, computer_choice: str):
    """ Game logic function """

    result = ""
    if (user_choice == computer_choice):
        result = DRAW
    elif (user_choice == "rock") and (computer_choice == "scissors"):
        result = WIN
    elif (user_choice == "scissors") and (computer_choice == "paper"):
        result = WIN
    elif (user_choice == "paper") and (computer_choice == "rock"):
        result = WIN
    else:
        result = LOSE
    return result


def main():
    """ Main function """

    while (True):
        while (True):
            user_input = input(
                "\nChoose 1 for rock, 2 for scissors, 3 for paper: ")
            if (user_input == "1") or (user_input == "2") or (user_input == "3"):
                break
            print("Invalid input, please type again!")

        user_choice = choice_from_number(int(user_input))
        computer_choice = choice_from_number(randint(1, 3))

        print("\nYou choose:")
        print(image_from_choice(user_choice))
        print("\nComputer choose:")
        print(image_from_choice(computer_choice))
        print()
        print(game_result(user_choice, computer_choice))

        again = input("\nPlay again? y/n ")
        if (again == "y"):
            pass
        else:
            break


if __name__ == "__main__":
    main()
