orrect_username = "admin"
correct_password = "password123"

a = input('Enter username: ')
b = input('Enter password: ')
i = 0
while (a != correct_username and b != correct_password) and i < 2 :
	print('Invalid credentials. Try again.')
	i += 1
	a = input('Enter username: ')
	b = input('Enter password: ')
if 	a != correct_username and b != correct_password and i == 2 :
	print('Invalid credentials. Try again.')
	print('Maximum login attempts reached.')
	print('Access denied.')
if a == correct_username and b == correct_password:
	print('Login successful!')