price = input("Enter product price: ")
price =float(price)
point = input("Enter your point: ")
point =float(point)
dis = point/500
dis =float(dis)
total=price-dis
print("Discount: %.2f\nTotal: %.2f Baht"% (dis,total))