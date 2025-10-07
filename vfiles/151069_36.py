pr = input('Enter poduct price :')
po = input('Enter your point :')
pr = float(pr)
po = int(po)
t = 1/500*po
f = pr-t
print("Discount : %.2f " % t)
print("Total : %.2f Baht " % f)