passw = input("Enter a password: ")
ap = len(passw)
big = False
small = False
num = False
if ap >= 8 :
    for c in passw:
        if c.isupper():
            big = True
        elif c.islower():
            small = True
        elif c.isdigit():
            num = True
        
    if big and small and num:
        print("Password is valid.")  
    else:
        print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
else :    
    print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")