price =input("Enter product price:")
price =float(price)
point =input("Enter your point:")
point=float(point)
discount = point/500
val= price - discount

print(f'discount:{discount:.2f}')
print(f'total:{val:.2f} Baht')