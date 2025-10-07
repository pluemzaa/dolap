num = int(input("Guess the number (between 1 and 99): "))
while num != 42:
    if num < 42 :
        print("Too low!")
    elif num > 42:
        print("Too high!")
    num = int(input("Guess the number (between 1 and 99): "))
if num == 42:
        print("Congratulations! You guessed the number")