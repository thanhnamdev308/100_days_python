from hangman_arts import stages as hangman_stages
from hangman_arts import logo as hangman_logo
from hangman_words import words as hangman_words
import random
from os import system


def clear():
    system('cls')


def gen_word():
    """
    Generate random word from library
    """

    return random.choice(hangman_words)


def gen_blank(word: str):
    """
    Generate blank from given word
    """

    word_length = len(word)
    blank = []

    for character in range(word_length):
        blank += "_"

    return blank


def draw_start_screen():
    """
    Draw the start screen
    """

    clear()
    print(hangman_logo)
    print()
    input("Press enter to start the game... ")
    clear()


def get_player_guess():
    """
    Get player guess
    """

    player_guess = ""
    while (True):
        player_input = input("\nGuess a letter: ")
        # Verify input
        if (len(player_input) == 1):
            player_guess = player_input
            break
        print("Invalid input, please type again!")

    return player_guess


WIN = "You win!"
LOSE = "You lose..."


def game():
    """
    Game loop
    """

    word = gen_word()
    blanks = gen_blank(word)
    word_length = len(word)
    current_stage = -1
    player_life = len(hangman_stages) - 1
    game_end = False
    result = ""
    char_guessed = []

    while (not game_end):
        clear()
        print("You have guessed: ")
        for char in char_guessed:
            print(char, end=" ")

        print(hangman_stages[current_stage])
        print()
        print("".join(blanks))
        print()
        
        if (player_life == 0):
            game_end = True
            result = LOSE
            break

        # Let player guess
        player_guess = ""
        while (True):
            player_guess = get_player_guess()
            if player_guess not in char_guessed:
                char_guessed.append(player_guess)
                break
            else:
                print("You have guessed this already, choose another one!")

        # Check if player choose correct
        player_wrong = True
        for index in range(word_length):
            if player_guess == word[index]:
                player_wrong = False
                blanks[index] = word[index]

        if (player_wrong):
            player_life -= 1
            current_stage -= 1

        if "_" not in blanks:
            game_end = True
            result = WIN

    print(result)
    if (result == LOSE):
        print(f"The word is: {word}")


def main():
    """
    Main function
    """

    draw_start_screen()
    while (True):
        game()
        again = input("\nPlay again? y/n ")
        if (again == "y"):
            pass
        else:
            break


if __name__ == "__main__":
    main()
