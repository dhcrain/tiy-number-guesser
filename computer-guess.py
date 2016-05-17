import random

c_guess = random.randint(1, 100)
turns = 5

print("Trick the computer number Game!\nThe computer has {} guesses to "
      "guess your number between 1 and 100.".format(turns))
num = input("Give a number between 1 and 100: ")

for turn in range(turns):
    try:
        num = int(num)
    except ValueError:
        print("You must pick and number!")
    else:
        turns -= 1
        if c_guess > num:
            print("The Computer's guess was {}".format(c_guess))
            c_guess = random.randint(1, c_guess)
        elif c_guess < num:
            print("The Computer's guess was {}".format(c_guess))
            c_guess = random.randint(c_guess, 100)
        else:
            print("You Loose!, The computer guessed your secret number, {}!".format(num))
            break

        if abs((c_guess - num)) <= 10:
            print("The Computer is within 10 of your Secret Number!")