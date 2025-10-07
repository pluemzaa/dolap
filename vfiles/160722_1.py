secret = random(99)+1
guess = int(input(""))
if guess>secret:
    print("Too high!")
elif guess<secret:
    print("Too low!")
else:
    print("Congratulations! You guessed the number")