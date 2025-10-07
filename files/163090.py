Mem = input("Membership (y/n) : ")
total = int(input("Total amount : "))
if Mem =='y':
    discount = 0
    if total >=1000:
        discount = total * 0.20
    elif total >=500 :
        discount = total *0.10    
if Mem == 'n':
    discount = total * 0.05
    if total >= 1000:
        discount = total *0.05
    elif total <1000:
        discount = 0   
print(f"Discount : {discount:.2f}")    
print(f"Final Amount to Pay : {(total - discount):.2f}")