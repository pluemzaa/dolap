correct_username = "admin"
correct_password = "password123"
type_username = input("Enter username: ")
type_password = input("Enter password: ")
incorrect_username = 0
incorrect_password = 0
attempts = 0
if type_username == correct_username and type_password == correct_password:
  attempts += 1
  print("Login successful!")
elif type_username == correct_username and type_password != correct_password:
  incorrect_password += 1
elif type_username != correct_username and type_password == correct_password:
  incorrect_username += 1
else:
    incorrect_username += 1
    incorrect_password += 1
while attempts == 0:
    print("Invalid credentials. Try again.")
    type_username = input("Enter username: ")
    type_password = input("Enter password: ")
    if type_username == correct_username and type_password == correct_password:
        attempts += 1
        print("Login successful!")
    elif type_username == correct_username and type_password != correct_password:
        incorrect_password += 1
    elif type_username != correct_username and type_password == correct_password:
        incorrect_username += 1
    else:
        incorrect_username += 1
        incorrect_password += 1
    if incorrect_username == 3 and incorrect_password == 3:
        attempts += 1
        print("Invalid credentials. Try again.")
        print("Maximum login attempts reached. Access denied.")