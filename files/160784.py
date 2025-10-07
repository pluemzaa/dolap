secret_number = 42  

while True:
    guess = int(input("Guess the number (between 1 and 99): "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")