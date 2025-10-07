i = 42
a = int(input("Guess the number (between 1 and 99): "))
while a != 42:
    if a < 42:
        print("Too low!")
    else:
        print("Too high!")
    a = int(input("Guess the number (between 1 and 99): "))
print("Congratulations! You guessed the number")