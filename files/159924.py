correct_username = "admin"
correct_password = "password123"

for i in range(3):
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == correct_username and p == correct_password:
        print("Login successful!")
        break
    elif i != 2: print("Invalid credentials. Try again.")
    else: print("Invalid credentials. Try again.");print("Maximum login attempts reached. Access denied.")