import re

p = input("Enter your password:")

x = True

while x:  
    
    if (len(p) < 8):
        break

    elif not re.search("[a-z]", p):
        break

    elif not re.search("[0-9]", p):
        break

    elif not re.search("[A-Z]", p):
        break
    else:
        print("Password is Valid")
        x = False
        break
if x:
    print("Password must be at least 8 characters long, contain both uppercase lowercase letters, and have at least one number.")