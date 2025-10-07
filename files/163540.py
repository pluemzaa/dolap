mem=input("Membership (y/n) :")
total=float(input("Total amount :"))
dis=0
if mem == "y":
    if total >=1000:
        dis=total*0.20
    elif total>=500:
        dis=total*0.10
else:
    if  total>=1000:
        dis=total*0.05
ftotal = total - dis
print("Discount :",f"{dis:.2f}")
print("Final Amount to Pay :",f"{ftotal:.2f}")