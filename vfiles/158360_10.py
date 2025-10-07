password = input("Enter your password: ")
try:
    _ = password[7]
    print("Password is strong")
except IndexError:
    print("Password is weak")