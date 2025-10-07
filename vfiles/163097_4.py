m = input('Membership (y/n) :')
ta = int(input("Total amount :"))
d = 0
if (m == 'y') or (m == 'n'):
    if (m == 'y') and (ta >= 1000):
        d = ta*0.2
    elif (m == 'y') and (ta >= 500):
        d = ta*0.1
    elif (m == 'n') and (ta >= 1000):
        d = ta*0.05
        
print(f"Discount : {d:.2f}\nFinal Amount to Pay : {(ta-d):.2f}")