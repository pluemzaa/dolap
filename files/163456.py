member = input("Membership (y/n) :")
total = float(input("Total amount :"))


d =0

if member == "y":  
    if total >= 1000:
        d = total * 0.20
    elif 500 <= total < 1000:
        d = total * 0.10
else:  
    if total >= 1000:
        d = total * 0.05


final = total - d

print(f"Discount :{d:.2f}")
print(f"Final Amount to Pay :{final:.2f}")