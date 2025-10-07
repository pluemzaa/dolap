correct_username = "admin"
correct_password = "password123"

attempt=0

while attempt != 3:
  username = input("Enter username: ")
  password = input("Enter password: ")
  if username != correct_username or password != correct_password:
    print("Invalid credentials. Try again. ")
    attempt += 1
  elif username == correct_username and password == correct_password:
    break
if attempt == 3:
  print("Maximum login attempts reached. Access denied.")