a = input('Enter product price :')
p = input('Enter your point :')
a_s = float(a)
p_s = int(p)
t = 1/500*p_s
f = a_s-t
print(f"Discount:%.2f" % t)
print(f"Total :.2f Bath" % f)