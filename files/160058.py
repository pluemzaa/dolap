key=42
while True:
    N=int(input("Guess the number (between 1 and 99): "))
    if N<key:
        print("Too low!")
    elif N>key:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number")
        break