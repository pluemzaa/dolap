x = 42
while True:
    guess = int(input("Guess the number (between 1 and 99):"))
    if guess < x:
        print("Too low!")
    elif guess > x:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break