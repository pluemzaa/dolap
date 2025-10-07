A = input("Enter your name:")
B = input("Enter your email:")
C = input("Enter your GPA:")
num = float(C)

list = [A, B, num]
tuple = (A, B, num)
dict = {"name": A, "email":B, "GPA":num}

print(list)
print(tuple)
print(dict)