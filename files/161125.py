resalt=[]
while True :
    password=list(input("Enter a password:"))
    for i in range(len(password)):
        if password[i].isupper():
            resalt.append(1)
        elif password[i].islower():
            resalt.append(2)
        elif password[i].isdigit():
            resalt.append(3)
    print(resalt)
    if 1 in resalt and 2 in resalt and 3 in resalt :
        print("Password is valid.")
        break
    else :
        print("Password must be at least 8 characters long, contain