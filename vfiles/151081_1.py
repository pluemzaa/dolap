pd = input("Enter product price:")
pd = float(pd)
point = int(input("Enter your point:"))
Dis = 1/500*(point)
total = pd-Dis
total = float(total)
print("Discount: %.2f / Total: %.2f Baht"%(Dis,total))