number = 42
n = int(input('Guess the number (between 1 and 99):'))
while n != number :
	if n > number and n < 100 and n > 1 :
		print('To high!')
	elif n < number and n < 100 and n > 1:
		print('To low!')
	n = int(input('Guess the number (between 1 and 99):'))
	
if n == number :
	print('Congratulations! You guessed the number')