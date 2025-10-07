mem = input("Membership (y/n) : ")
amt = int(input("Total amount : "))
dis = 0
if mem == 'y':
    sub = True
else :
    sub = False
if amt >=1000:
    if sub == True:
        dis = amt*0.2
    else:
        dis = amt*0.05
elif amt in range(500,1000) and sub == True:
    dis = amt*0.1
else:
    dis = 0
print(f'Discount : {dis:.2f}')
print(f"Final Amount to Pay : {amt-dis:.2f}")