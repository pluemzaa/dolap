mem = input("Membership (y/n) : ")
total = float(input("Total amount : "))
dis = 0
if mem == "y":
    if total >= 1000:
        dis = total * 0.2
    elif 500 <= total and total < 1000:
        dis = total * 0.1
elif mem == "n":
    if total >= 1000:
        dis = total * 0.05

print(f"Discount : {dis:.2f}")
print(f"Final Amount to Pay : {total - dis:.2f}")