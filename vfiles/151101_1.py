prc = input('Enter product price:')
pnt = input('Enter your point:')
prc = float(prc)
pnt = int(pnt)
dis = 1/500*pnt
tt = prc-dis
print('Discount: %.2f' %dis)
print('Total: %.2f Bath ' %tt)