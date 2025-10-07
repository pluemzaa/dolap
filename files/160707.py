while 1 :
    num = int(input('Guess the number (between 1 and 99): '))
    if num < 42 :
        print("To low!")
    elif num > 42 :
        print('To high!')
    elif num == 42 :
        print('Congratulations! You guessed the number')
        break