M = input("Membership (y/n) : ")
n = int(input("Total amount : "))
D = 0
if M=='y':
    if n >= 1000:
        D = n*0.2
    elif 500 <= n and n < 1000:
        D = n*0.1
    else:
        total = n 
elif M == "n":
    if n >= 1000:
        D = n*0.05
        
print(f"Discount : {D:.2f}")
print(f"Final Amount to Pay : {n-D:.2f}")