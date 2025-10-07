num = int(input("Guess the number (between 1 and 99): "))
while num < 42:
    print('To low!')
    num = int(input("Guess the number (between 1 and 99): "))
    if num > 42:
        print('To high!')
        num = int(input("Guess the number (between 1 and 99): "))
    elif num == 42:
        print('Congratulations! You guessed the number')