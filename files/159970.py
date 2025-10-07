number = int(input("Guess the number (between 1 and 99):"))
random = 42
while number < 100 :
    if number > random :
        print("Too high!")
    elif number < random :
        print("Too low!")
    elif number == random :
        print("Congratulations! You guessed the number")
        break
    number = int(input("Guess the number (between 1 and 99): "))