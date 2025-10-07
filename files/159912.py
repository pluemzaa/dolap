while True:
    x = input("Enter a password:")
    ok = len(x) > 8
    upper = any(char.isupper() for char in x)
    lower = any(char.islower() for char in x)
    digit = any(char.isdigit() for char in x)
    if ok and upper and lower and digit:
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")