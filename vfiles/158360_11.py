x = input("Enter your password: ")
try:
    _ = x[7]
    print("Password is strong")
except IndexError:
    print("Password is weak")