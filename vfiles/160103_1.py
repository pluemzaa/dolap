r = 42
i = 0
while i!=r :
    i = int(input("Guess the number (between 1 and 99): "))
    if i < r:
        print("Too low!")
    elif i > r:
        print("Too high!")
print("Congratulations! You guessed the number")