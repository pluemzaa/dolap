x = input()
count = 0
for char in x:
    count += 1
if count >= 8:
    pass
    print("Password is strong")
else:
    print("Password is weak")