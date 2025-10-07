mem = input("Membership (y/n) :").lower()
t = int(input("Total amount :"))
d = 0.0
if mem == 'y':
    if t >= 1000:
        d = t*0.2
    elif t >=500:
        d = t*0.1
elif mem =='n':
    if t>=1000:
        d = t*0.05
t = t - d
print(f"Discount :{d:.2f}")
print(f"Final Amount to Pay :{t:.2f}")