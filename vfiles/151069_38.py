pr = input('Enter poduct price :')
po = input('Enter your point :')
a_s = float(pr)
p_s = int(po)
t = 1/500*p_s
f = a_s-t
print("Discount : %.2f " % t)
print("Total : %.2f Baht " % f)