while True:
    pwd = input("Enter a password: ")

    if (len(pwd) > 8 and
        any(c.isupper() for c in pwd) and
        any(c.islower() for c in pwd) and
        any(c.isdigit() for c in pwd)):
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")