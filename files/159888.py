c = 42
while True:
    a = int(input("Guess the number (between 1 and 99):"))
    if a > c:
        print("Too high!")
    elif a < c:
        print("Too low!")
    else:
        print("Congratulations! You guessed the number")
        break