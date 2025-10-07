while True:
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")