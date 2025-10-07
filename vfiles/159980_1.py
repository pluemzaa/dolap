password = input("Enter a password: ")

if len(password) >= 8 :
  print("Password is valid.")
else :
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")