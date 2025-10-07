mb = input("Membership (y/n) : ")
tta = float(input("Total amount : "))
dis = 0
if mb == 'y':
    if tta >= 1000:
       dis = tta*0.20
    elif tta >= 500:
       dis = tta*0.10
else:
     tta >= 1000 
     dis = tta*0.05
Final = tta - dis

print(f"Discount : {dis:.2f} ")  
print(f"Final Amount to Pay : {Final:.2f} ")