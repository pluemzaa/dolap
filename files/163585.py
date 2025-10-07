m = input("Membership (y/n) : ") 
t = int(input("Total amount : "))

if m=='y':
    if t>=1000:
        a = t*0.2
    elif t>=500 and t<=999:
        a = t*0.1
    else:
        a = 0.00
        
if m=='n':
   if t>=1000:
       a = t*0.05
   else:
       a = 0.00
    
print(f"Discount :{a:.2f}")
o = t-a
print(f"Final Amount to Pay :{o:.2f}")