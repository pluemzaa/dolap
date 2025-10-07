password = input("Enter a password:")
capital = False
number = False
long = False

while not capital or not number :

    if len(password) < 8 :
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number. ")
        password = input("Enter a password:")
        continue
    for c in password :
        if(not capital):
            capital = c.isupper()
        if(not number):
            number = c.isdigit()
        if(capital and number) :
            break
    if(capital and number) :
        break
    else :
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number. ")
    password = input("Enter a password:")
print("Password is valid.")