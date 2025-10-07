correct_username = "admin"
correct_password = "password123"
i = 1
while i <= 3:
  username = input("Enter username: ")
  password = input("Enter password: ")
  if username == correct_username and password == correct_password :
    print("Login successful!")
    break
  else:
      print("Invalid credentials. Try again.")
      i += 1
if i > 3:
  print("Maximum login attempts reached. Access denied.")