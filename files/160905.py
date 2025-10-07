secret = 42
while True:
    guess = int(input("Guess the number (between 1 and 99): "))
      if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break