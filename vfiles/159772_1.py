number = 42
n = int(input('Guess the number (between 1 and 99):'))
while n != number :
	if n > number :
		print('To high!')
		n = int(input('Guess the number (between 1 and 99):'))
	else :
		print('To low!')
		n = int(input('Guess the number (between 1 and 99):'))
	
print('Congratulations! You guessed the number')