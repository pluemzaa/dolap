price=input("Enter product price:")
point=input("Enter product point:")
price=float(price)
point=int(point)
Discount=1/500*point
Total=price-Discount
print(f"Discount:%2f,Total:%2f Bath"%(Discount,Total))