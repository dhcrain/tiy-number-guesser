import random

rand_num = random.randint(1, 100)
turns = 5

print("Guess the number Game!\nYou have {} guesses to "
      "guess the random number between 1 and 100.".format(turns))
print(rand_num)
for turn in range(turns):
    guess = input("What is your guess? ")
    turns -= 1
    try:
        guess = int(guess)
    except ValueError:
        print("You must pick and number!")
    else:
        if guess > rand_num:
            print("Too High, you have {} guesses left.".format(turns))
        elif guess < rand_num:
            print("Too Low, you have {} guesses left.".format(turns))
        else:
            print("You Win!, {} was the secret number!".format(rand_num))
            break

        if turns == 0:
            print("You Loose!, {} was the secret number!".format(rand_num))
            break

        if abs((guess - rand_num)) <= 10:
            print("You are within 10 of the Secret Number!")