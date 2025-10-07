T1 = input("Enter item 1 :")
W1 = float(input("Enter weight 1 :"))
T2 = input("Enter item 2 :")
W2 = float(input("Enter weight 2 :"))
T3 = input("Enter item 3 :")
W3 = float(input("Enter weight 3 :"))
T4 = input("Enter item 4 :")
W4 = float(input("Enter weight 4 :"))

_total = W1+W2+W3+W4

print(T1,f"{W1:.2f}",sep="                   ")
print(T2,f"{W2:.2f}",sep="                   ")
print(T3,f"{W3:.2f}",sep="                   ")
print(T4,f"{W4:.2f}",sep="                   ")
print("---------------------------")
print(f"total                     {_total:.2f}")