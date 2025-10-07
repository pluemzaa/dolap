number = 42
guess = 0

while guess != number:
    guess = int(input("Guess the number (between 1 and 99): "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")