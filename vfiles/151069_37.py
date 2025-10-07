pr = input('Enter poduct price :')
po = input('Enter your point :')
p_a = float(pr)
p_s = int(po)
t = 1/500*po
f = p_a-t
print("Discount : %.2f " % t)
print("Total : %.2f Baht " % f)