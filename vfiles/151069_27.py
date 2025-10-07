pr = input('Enter poduct price :')
po = input('Enter your point :')
pr = float(pr)
po = int(po)
D = 1/500*po
t = pr-D
print(" Discount : %.2f " % D)
print("total : %.2f Baht " %t)