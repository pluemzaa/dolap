#lab3

mem = input("Membership (y/n) : ")
total = int(input("Total amount :"))
dis = 0 
if mem == "y" : 
    if total >= 1000 :
        dis =  0.2
    elif total >= 500 and total <= 999 : 
        dis = 0.1
if mem == "n" and total >= 1000 :
    dis = 0.05  
discount = total*dis
final = total - discount 
print(f"Discount : {discount:.2f}")
print(f"Final Amount to Pay : {final:.2f}")