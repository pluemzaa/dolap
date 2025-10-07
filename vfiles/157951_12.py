while True:
    password = input("Enter a password: ")

    if len(password) > 8:
        has_upper = False
        has_lower = False
        has_digit = False

        for ch in password:
            if ch.isupper():
                has_upper = True
            if ch.islower():
                has_lower = True
            if ch.isdigit():
                has_digit = True

        if has_upper and has_lower and has_digit:
            print("Password is valid.")
            break

    print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")