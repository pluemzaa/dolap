p1 = float(input("Enter product price: "))
p2 = int(input("Enter your point: "))

discount = 2 / 500

if discount > p1 :
    discount = p1
    
total = p1 - discount
    
print("discount %.2f" % discount)
print("Total: %.2f Baht" % total)