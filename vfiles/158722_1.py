password = input("Enter a password: ")
a = 0
b = 0
c = 0
for i in password:
  if i.isupper():
    a += 1
  elif i.islower():
    b += 1
  else:
    c += 1

if a>=1 and b>=1 and c>= 1 and len(password) > 8:
    print("Password is valid")
else:
    print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
    while a < 1 or b < 1 or c < 1 or len(password) <= 8:
        a = 0
        b = 0
        c = 0
        password = input("Enter a password: ")
        for i in password:
            if i.isupper():
                a += 1
            elif i.islower():
                b += 1
            else:
                c += 1

        if a>=1 and b>=1 and c>= 1 and len(password) > 8:
            print("Password is valid")
        else:
            print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")