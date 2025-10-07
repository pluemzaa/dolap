mem = input("Membership (y/n) : ")
money = int(input("Total amount : "))
dis = 0
if mem == "y":
    if money >= 1000:
        dis = (money*0.2)
        total = money - (money*0.2)
        
    elif 500 <= money < 1000:
        dis = (money*0.1)
        total = money - (money*0.1)
    else:
        total = money
else:
    if money >= 1000:
        dis = (money*0.05)
        total = money - (money*0.05)
    else:
        total = money

print(f"Discount : {dis:.2f}")
print(f"Final Amount to Pay : {total:.2f}")