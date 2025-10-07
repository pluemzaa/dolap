i=42
N=int(input("Guess the number (between 1 and 99): "))
while N!=i:
    if N>i:
        print("Too high!")
    else:
        print("Too low!")
    N=int(input("Guess the number (between 1 and 99): "))
print("Congratulations! You guessed the number")