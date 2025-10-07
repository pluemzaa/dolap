x = input()
i = 0
for _ in x:
    i += 1
    if i >= 8:
        break
if i >= 8:
    print("Password is strong")
else:
    print("Password is weak")