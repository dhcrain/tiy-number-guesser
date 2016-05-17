import random

low = 1
high = 100
c_guess = 50
turns = 10

print("Trick Skynet Number Game!\nSkynet has {} guesses to "
      "guess your number between 1 and 100.".format(turns))
num = input("Give a number between 1 and 100: ")

for turn in range(turns):
    try:
        num = int(num)
    except ValueError:
        print("You must pick a number!")
        break
    else:
        turns -= 1
        if c_guess > num:
            print("high Skynet's guess was {}".format(c_guess))
            high = c_guess - 1
            c_guess = random.randint(low, high)
        elif c_guess < num:
            print("low Skynet's guess was {}".format(c_guess))
            low = c_guess + 1
            c_guess = random.randint(low, high)
        else:
            print("You Loose!, Skynet's guessed your secret number, {}!".format(num))
            break