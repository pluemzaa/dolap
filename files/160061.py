name = input('Enter username:' )
password = input('Enter password:' )
i = 1
while ((name != 'admin') or (password != 'password123')) and (i <= 2):
    print('Invalid credentials. Try again.')
    name = input('Enter username:' )
    password = input('Enter password:' )
    i = i + 1
if (name == 'admin') and (password == 'password123'):
    print('Login successful')
else:
    print('Invalid credentials. Try again.')
    print('Maximum login attempts reached. Access denied.')