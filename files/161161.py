a = 42
b = 0
while b != a:
    b = int(input("Guess the number (between 1 and 99): "))
    if b < a:
        print("Too low!")
    elif b > a:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")