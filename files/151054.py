money=input("Enter product price:")
point=input("Enter your point:")
money= float(money)
point= int(point)
Discount=1/500*point
Discount=float(Discount)
Total=money-Discount
print(f"Discount: %.2f \nTotal: %.2f Baht"%(Discount,Total))