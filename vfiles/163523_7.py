import sys
member = input("Membership(y/n) : ")
price = int(input("Total amount : "))
price_dis = 0
total = 0
if member == "y":
    if price >= 1000:
        price_dis = price * 0.20
        print(f"Discount : {price_dis:.2f}")    
        print(f"Final Amount to Pay : {price - price_dis:.2f}")
        sys.exit()
    if price >= 500:
        price_dis = price * 0.10
        print(f"Discount : {price_dis:.2f}")
        print(f"Final Amount to Pay : {price-price_dis:.2f}")
        sys.exit()
    if price > 0 :
        price_dis = 0
        print(f"Discount {price_dis:.2f}")
        print(f"Final Amount to Pay : {price - price_dis:.2f}")
        sys.exit()
        
        
if member == "n":
    if price >= 1000:
        price_dis = price * 0.05
        print(f"Discount : {price_dis:.2f}")    
        print(f"Final Amount to Pay : {price-price_dis:.2f}")
        sys.exit()