guess = int(input("Guess the number (between 1 and 99):"))
while guess != 42 :
    if guess > 42:
        print ("Too high!")
    else :
        print ("Too low!")
    guess = (int(input("Guess the number (between 1 and 99):")))
print ("Congratulations! You guessed the number")