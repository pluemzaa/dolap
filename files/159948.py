while True:
    password = input("Enter a password: ")
    length_ok = len(password) > 8
    upper_ok = any(c.isupper() for c in password)
    lower_ok = any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    if length_ok and upper_ok and lower_ok and digit_ok:
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")