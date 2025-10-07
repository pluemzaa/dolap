correct_username = "admin"
correct_password = "password123"
a = 1

for x in range(1,4) :
    user = input("Enter username: ")
    passw = input("Enter password: ")
    
    if a == 3 :
        print("Maximum login attempts reached. Access denied.")

    elif user == correct_username and passw == correct_password :
        print("Login successful!")
        break
    
    else :
        a = a + 1
        print("Invalid credentials. Try again.")