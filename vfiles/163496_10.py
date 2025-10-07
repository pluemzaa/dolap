enter_i1=input("Enter item 1 : ")
enter_w1=float(input("Enter weight 1 : "))

enter_i2=input("Enter item 2 : ")
enter_w2=float(input("Enter weight 2 : "))

enter_i3=input("Enter item 3 : ")
enter_w3=float(input("Enter weight 3 : "))

enter_i4=input("Enter item 4 : ")
enter_w4=float(input("Enter weight 4 : "))

num=enter_w1+enter_w2+enter_w3+enter_w4

print(f"{enter_i1} {enter_w1:.2f}")
print(f"{enter_i2} {enter_w2:.2f}")
print(f"{enter_i3} {enter_w3:.2f}")
print(f"{enter_i4} {enter_w4:.2f}")
print("---------------------------")
print(f"total: {num:.2f}")