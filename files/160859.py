num = int(input("Guess the number (between 1 and 99): "))
if num == 42:
    print("Congratulations! You guessed the number")
elif num > 42:
    print("To high!")
else:
    print("To low!")