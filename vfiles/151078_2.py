price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
discout = point/500
Total = price-discout
print( "Discount: ", discout)
print("Total: %.2f Baht"% Total)