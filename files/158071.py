x = int(input("Guess the number (between 1 and 99): "))
while x != 42:
    if x < 42:
        print("Too low!")
    elif x > 42:
        print("Too High!")
    x = int(input("Guess the number (between 1 and 99): "))
print("Congratulations! You guessed the number")