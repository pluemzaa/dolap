correct_username = "admin"
correct_password = "password123"
for i in range(3):
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username==correct_username and password==correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")
else:
    print("Maximum login attempts reached. Access denied.")