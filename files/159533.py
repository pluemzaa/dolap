correct_username = "admin"
correct_password = "password123"
connect = 0

while True:
    Username = input("Enter username:")
    Password = input("Enter password:")
    if Username == correct_username and Password == correct_password:
        print("Login successful!")
        break
    elif Username != correct_username or Password != correct_password:
        connect += 1
        print("Invalid credentials. Try again.")
        if connect == 3:
            print("Maximum login attempts reached. Access denied.")
            break