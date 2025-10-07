mem = input("Membership (y/n) :")
total = float(input("Total amount :"))
dis1 = (total*20)/100
dis2 = (total*10)/100
dis3 = (total*5)/100
if mem == "y":
    if total >= 1000 :
        print(f"Discount :{dis1:.2f}")
        print(f"Final Amount to Pay :{total-dis1:.2f}")
    elif total >= 500 and total <= 999:
        print(f"Discount :{dis2:.2f}")
        print(f"Final Amount to Pay :{total-dis2:.2f}")
    else :
        print(f"Discount :0.00")
        print(f"Final Amount to Pay :{total:.2f}")
elif total >= 1000:
        print(f"Discount :{dis3:.2f}")
        print(f"Final Amount to Pay :{total-dis3:.2f}")
else :
        print(f"Discount :0.00")
        print(f"Final Amount to Pay :{total:.2f}")