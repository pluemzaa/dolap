correct_username = "admin"
correct_password = "password123"

attempt = 0
while attempt < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")
        attempt += 1
else:
    print("Too many failed attempts. Access denied.")