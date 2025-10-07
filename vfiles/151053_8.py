price = input("Enter prodct price:")
point = input("Enter your point:")
discount = point/500
print("Discount: %.2f" % discount)
print("Total: %.2f Baht" %(price - discount))