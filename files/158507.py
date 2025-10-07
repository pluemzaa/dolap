password = input()
ypass = len(password)
if ypass >= 8:
  print("Password is strong")
else:
  print("Password is weak")