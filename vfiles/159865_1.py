a = 42

while True:
    z = int(input("Guess the number (between 1 and 99): "))
    if z < a:
        print("Too low!")
    elif z > a:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break