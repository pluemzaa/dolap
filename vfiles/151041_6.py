price = input("Enter product price: ")
point = input("Enter your point: ")
price =float(price)
point =float(point)
dis = point/500
dis =float(dis)
total=price-dis
print("Discount: %.2f\nTotal: : %.2f Bath"% (dis,total))