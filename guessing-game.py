import random
rand_num = random.randint(1, 100)
turns = 5
print(rand_num)
print("Guess the number Game!\nYou have 5 guesses to "
      "guess the random number between 1 and 100.")

for turn in range(turns):
    guess = int(input("What is your guess? "))
    turns -= 1
    if guess > rand_num:
        print("Too High, you have {} guesses left.".format(turns))
    elif guess < rand_num:
        print("Too Low, you have {} guesses left.".format(turns))
    else:
        print("You Win!, {} was the secret number".format(rand_num))
        break

    if (guess - rand_num) <= 10:
        print("You are with in 10 of the Secret Number!")