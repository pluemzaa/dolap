price = float(input("Enter product price:"))
point_cal= price * 500
print ("Enter your point:", int(point_cal))
discount = float(input("Discount:"))
total = price-discount
print (f"Total:{total:.2f}")