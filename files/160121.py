correct_username = 'admin'
correct_password = 'password123'

tries = 0
max_tries = 3

while tries < max_tries :
    username_input = input("Enter username:")
    password_input = input("Enter password:")
    
    if username_input==correct_username and password_input==correct_password :
        break
    else :
        print("Invalid credentials. Try again.")
        tries +=1
    if tries == 3 :
        print("Maximum login attempts reached. Access denied.")
        exit()

print("Login successful!")