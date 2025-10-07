import random
rd = random.randint(1,99)
Num = int(input('Guess the number (between 1 and 99):'))
while True:
    if Num == rd:
        print('Congratulations! You guessed the number')
        break
    elif Num < rd:
        print('Too low!')
    elif Num > rd:
        print('To hight!')
    Num = int(input('Guess the number (between 1 and 99):'))