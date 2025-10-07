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