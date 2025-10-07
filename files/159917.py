while True:
    p = input("Enter a password: ")
    u = 0
    d = 0
    n = 0
    for i in p:
        if i.isupper():
            u +=1
        elif i.islower():
            d += 1
        elif i.isdigit():
            n +=1
    if len(p) >= 8 and u > 0 and d > 0 and n > 0:
        print("Password is valid.")
        break
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")