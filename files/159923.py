secret_number = 42
while True:
    guess = int(input("Guess the number (between 1 and 99): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break