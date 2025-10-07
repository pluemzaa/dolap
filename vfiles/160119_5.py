correct_username = "admin"
correct_password = "password123"
name = input('Enter username: ')
password = input('Enter password: ')
i = 0

while i < 2 :
	if name == correct_username and password == correct_password :
		print('Login successful!')
		i += 3
		
	elif name == correct_username and password != correct_password :
		print('Invalid credentials. Try again.')
		name = input('Enter username: ')
		password = input('Enter password: ')
		i += 1
		
	elif name != correct_username and password == correct_password :
		print('Invalid credentials. Try again.')
		name = input('Enter username: ')
		password = input('Enter password: ')
		i += 1
		
	elif name != correct_username and password != correct_password :
		print('Invalid credentials. Try again.')
		name = input('Enter username: ')
		password = input('Enter password: ')
		i += 1
		
		
	
if i >= 2 and (name != correct_username or password != correct_password) :
	print('Invalid credentials. Try again.')
	print('Maximum login attempts reached. Access denied.')