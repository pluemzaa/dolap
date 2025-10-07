price=input("Enter product price:")
price=float(price)
point=input("Enter your point:")
point=float(point)
point=1/500*point
price=price-point
print("Discount:%.2f"%point)
print("Total:%.2f Bath"%price)