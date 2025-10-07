price = input("Enter product price: " )
point =input("Enter your point: ")
price = float(price)
point = int(point)
d = point / 500
Total = price - d
print("Discount:%.2f"%d)
print("Total: %.2f "%Total,("Baht"))