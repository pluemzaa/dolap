pd = input('Enter product price: ')
p = input('Enter your point: ')
pd = float(pd)
p = int(p)
Discount = 1/500 * p
print('Discoun: %.2f' %Discount)
Total = pd - Discount
print("Total: %.2f " %Total ,'Baht')