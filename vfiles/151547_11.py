price = float(input("Enter product price" ))
point = int(input("Enter your point"))

Discount = point/500
Total = price - Discount

print("Discount:%.2f   \nTotalt: %.2f Baht" % (Discount,Total))