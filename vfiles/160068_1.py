password = input("Enter a password:")
i = []
for x in password:
  if x.isupper():
    i.append(1)
  elif x.islower():
    i.append(2)
  elif x.isnumeric():
    i.append(3)
if  1 in i and 2 in i and 3 in i:
  print("Password is valid.")
elif len(password) < 8:
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
else:
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")