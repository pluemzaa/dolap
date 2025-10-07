while True:
  password =input("Enter a password:")
  l1 = len(password) >8
  L2 = any(ch.isupper() for ch in password)
  L3 = any(ch.islower() for ch in password)
  L4 = any(ch.isdigit() for ch in password)
  if l1 and L2 and L3 and L4:
    print("Password is valid.")
  break
  else:
      print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")