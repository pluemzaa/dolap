x = 42
while True:
    num = int(input("Guess the number (between 1 and 99):"))
    if num > 42:
        print("Too high!")
    elif num < 42:
        print("Too low!")
    else:
        print("Congratulations! You guessed the number")