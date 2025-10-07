M = input("Membership (y/n) : ")
n = int(input("Total amount : "))
total = 0
D = 0
if M=='y':
    if n >= 1000:
        D = n*0.2
        total = n - D
    elif 500 <= n and n <= 999:
        D = n*0.1
        total = n - D
    else:
        total = n 
if M=='n':
    if n >= 1000:
        D = n*0.05
        total = n - D  
        
print(f"Discount : {D:.2f}")
print(f"Final Amount to Pay : {total:.2f}")