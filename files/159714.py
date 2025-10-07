password = input()
if len(password) >= 8:
    print("Password is strong")
elif len(password) <8:
    print("Password is weak")