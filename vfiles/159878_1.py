usernames = "admin"
passwordss = "password123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == usernames and password == passwordss:
        print("Login successful!")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Invalid credentials. Try again.")
        else:
            print("Maximum login attempts reached. Access denied.")