password = input()
password = str(password)
lenght = len(password)
if lenght >= 8:
  print("Password is strong")
else:
  print("Password is weak")