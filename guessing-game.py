import random
import os

low_num = -5
high_num = 5
max_turns = 5
close_range = 2 # for giving hints


class colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[94m'
    PINK = '\033[38;5;206m'
    PURPLE = '\033[38;5;57m'
    ORANGE = '\033[38;5;202m'
    CYAN ='\033[36m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

rand_num = random.randint(low_num, high_num)
os.system("clear")

print(f"""
{colors.PINK}Guess the number Game!{colors.ENDC}
You have {max_turns} guesses to guess the random number between {colors.ORANGE}{low_num} and {high_num}{colors.ENDC}.""")

# print(rand_num)

turns = max_turns
while turns <= max_turns:

    guess = input(f"{colors.BOLD}{colors.PURPLE}What is your guess? {colors.ENDC}")
    try:
        guess = int(guess)
        if guess < low_num or guess > high_num:
            raise IndexError
    except ValueError:
        print("You must pick and number!")
    except IndexError:
        print("Number out of range, pick again")
    else:
        turns -= 1
        if guess > rand_num:
            print(f"{colors.RED}Too High{colors.ENDC}, you have {colors.BLUE}{turns}{colors.ENDC} guesses left.")
        elif guess < rand_num:
            print(f"{colors.YELLOW}Too Low{colors.ENDC}, you have {colors.BLUE}{turns}{colors.ENDC} guesses left.")
        else:
            print(f" ✔ {colors.YELLOW}You Win!, {rand_num} was the secret number!{colors.ENDC} ✔ ")
            break

        if turns == 0:
            print(f"{colors.RED} ✘ You Lose!, {rand_num} was the secret number!{colors.ENDC}")
            break

        if abs((guess - rand_num)) <= close_range:
            print(f"{colors.GREEN}You are within {close_range} of the Secret Number!{colors.ENDC}")
