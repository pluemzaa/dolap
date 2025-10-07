while True:
    password = input("Enter a password: ")
    
    length_ok = len(password) > 8
    has_upper = False
    has_lower = False
    has_digit = False
    
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
    
    if length_ok and has_upper and has_lower and has_digit:
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")