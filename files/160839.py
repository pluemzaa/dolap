i = 0
while i < 3:
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == "admin" and p == "password123":
        print("Login successful.")
        break
    else:
        print("Invalid credentials. Try again.")
        i += 1

if i == 3:
    print("Maximum login attempts reached. Access denied.")