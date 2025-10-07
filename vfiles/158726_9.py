correct_username = "admin"
correct_password = "password123"
type_username = input("Enter username: ")
type_password = input("Enter password: ")
a = 0
b = 0
c = 0
if type_username == correct_username and type_password == correct_password:
    c += 1
    print("Login successful!")
else:
    a += 1
    b += 1
while c == 0:
    a += 1
    b += 1
    print("Invalid credentials. Try again.")
    type_username = input("Enter username: ")
    type_password = input("Enter password: ")
    if type_username == correct_username and type_password == correct_password:
        c += 1
        print("Login successful!")
    elif a == 3 or b == 3:
        c += 1
        print("Maximum login attempts reached. Access denied.")