inr = input("Enter a password: ")
r_long=False;digit=False;upper=False;lower=False

if len(inr) >= 8:
  r_long=True

for i in range(len(inr)):
  if inr[i].isdigit():
    digit=True
  if inr[i].isupper():
    upper=True
  if inr[i].islower():
    lower=True

if r_long == True and digit == True and upper ==True and lower == True:
  print("Password is valid.")
else:
  print("Password must be at least 8 characters long, contain both uppercase and lowercase letters, and have at least one number.")