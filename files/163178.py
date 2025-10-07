member = input('Membership (y/n) : ')
total = int(input("Total amount :"))

discount = 0
    
if member == 'y':
    if total >= 1000:
        discount = 0.20
    elif 500 <= total and total < 1000:
        discount = 0.10
else:
    if total >= 1000:
        discount = 0.05
    
discount_amt = total*discount
final = total-discount_amt

print(f'Discount:{discount_amt:.2f}')
print(f'Final Amount to Pay:{final:.2f}')