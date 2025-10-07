correct_username = "admin"
correct_password = "password123"
C = 0
while C <= 3:
  X = input('Enter username:')
  Y = input('Enter password:')
  if X == correct_username and Y == correct_password:
    print('Login successful!')
    break
  elif X != correct_username or Y != correct_password:
    C += 1
    print('Invalid credentials. Try again.')
  if C == 3:
    print('Maximum login attempts reached. Access denied.')
    break