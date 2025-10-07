mn = input("Enter product price:")
mn = float(mn)
point = int(input("Enter your point:"))
Ds = 1/500*(point)
totle = mn-Ds
totle = float(totle)
print("Discount: %.2f \ntotle: %.2f Baht"%(Ds,totle))