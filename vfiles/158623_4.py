password = input()
password = str(password)
length = len(password)
if length >= 8:
  print("Password is strong")
else:
  print("Password is weak")