password = 42

while True:
    guess = int(input("Guess the number (between 1 and 99): "))
    if guess < password :
        print("Too low!")
    elif guess > password:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break