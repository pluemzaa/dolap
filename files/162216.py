correct_username = "admin"
correct_password = "password123"
for i in range(3):
    user = input("Enter username: ")
    password = input("Enter password: ")
    if user == correct_username and password == correct_password:
      print("Login successful!")
      break
    else:
      print("Invalid credentials. Try again.")
else:
   print("Maximum login attempts reached. Access denied.")