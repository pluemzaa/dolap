randomNo = 42
guess = 0
while True :
    guess = int(input("Guess the number (between 1 and 99):"))
    if guess == randomNo :
        break
    if guess < randomNo :
        print("Too low!")
    else :
        print("Too high")
print("Congratulations! You guessed the number")