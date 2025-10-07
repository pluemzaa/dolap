uusername = input("Enter username: ")
password = input("Enter password: ")
correct_username = "admin"
correct_password = "password123"
if username == correct_username and password == correct_password:
    print("Login successful!")
elif username != correct_username or password != correct_password:
    print('Invalid credentials. Try again')
    for i in range(2):
        i = input("Enter username: ")
        i = input("Enter password: ")
        print('Invalid credentials. Try again')
    print("Maximum login attempts reached. Access denied.")