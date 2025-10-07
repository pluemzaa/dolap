mem = input("Membership (y/n): ")
total = int(input("Total amount : "))
if mem == 'y' and total >= 1000:
    dis = 20
elif mem == 'y' and total >= 500:
    dis = 10
elif mem == 'n' and total >= 1000:
    dis = 5
else:
    dis = 0

diss = (total/100)*dis
print('Discount : ',f'{diss:.2f}')
final = total-((total/100)*dis)
print('Final Amount to Pay : ',f'{final:.2f}')