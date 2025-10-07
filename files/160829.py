password = input("Enter a password: ")
if len(password) < 8:
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
elif not any(char.isupper() for char in password):
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
elif not any(char.islower() for char in password):
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
elif not any(char.isdigit() for char in password):
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")
else:
  print("Password is valid.")