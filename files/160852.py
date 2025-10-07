correct_username = "admin"
correct_password = "password123"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        attempts += 1
        if attempts == max_attempts:
            print("Invalid credentials. Try again.