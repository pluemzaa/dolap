correct_username = "admin"
correct_password = "password123"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")
        attempts += 1

if attempts == 3:
    print("Maximum login attempts reached. Access denied.")