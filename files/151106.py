a = input("Enter product price :")
p = input("Enter your point :")
a_s = float(a)
p_s = float(p)
t = 1/500*p_s
f = a_s-t
print("Discount: %.2f "% t)
print("Total : %.2f Baht " % f)