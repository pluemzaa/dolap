Membership=str(input("Membership (y/n) : "))
Amount=int(input("Total amount : "))
Discount=0
if Membership =="y":
    if Amount >= 1000:
        Discount=Amount/5
        print("Discount:","%.2f"%Discount)
    elif 500 <= Amount <= 999:
        Discount=Amount/10
        print("Discount:","%.2f"%Discount)
    else:
        print(Amount)
else:
    if Amount >= 1000:
        Discount=Amount/20
        print("Discount:","%.2f"%Discount)
    else:
        print(Amount)
Final =Amount-Discount
print(f"Final Amount to Pay: ","%.2f"%Final)