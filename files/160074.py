correct_username = "admin"
correct_password = "password123"
count = 0
max = 3
logged_in = False
while count < max and not logged_in:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        logged_in = True
    else:
        count = count + 1
        if count <= max:
            print("Invalid credentials. Try again.")
if not logged_in and count == max:
    print("Maximum login attempts reached. Access denied.")