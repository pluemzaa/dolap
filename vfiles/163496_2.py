enter_i1=input("Enter item 1 :")
enter_w1=float(input("Enter weight 1 :"))

enter_i2=input("Enter item 2 :")
enter_w2=float(input("Enter weight 2 :"))

enter_i3=input("Enter item 3 :")
enter_w3=float(input("Enter weight 3 :"))

enter_i4=input("Enter item 4 :")
enter_w4=float(input("Enter weight 4 :"))

print(enter_i1,"%.2f"%enter_w1)
print(enter_i2,"%.2f"%enter_w2)
print(enter_i3,"%.2f"%enter_w3)
print(enter_i4,"%.2f"%enter_w4)

print("---------------------------")
print(f"total:{enter_w1+enter_w2+enter_w3+enter_w4:.2f}")