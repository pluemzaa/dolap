#written by proshophonoka est.2025#
#enter price:500 ===> 200baht -> 1 pt
#your points:2.50 pts    1/200*500
price = input("Enter product price:") 
price = float(price)
point = 12.15513794/1 * price
discount = point/500
#print(point)
print("Enter your point: %.2f" % point)
#print("total price %.2f , your point: %.2f point" % (price,point))
print(f"Discount: {discount:.2f}\nTotal: {price-discount:.2f} Baht")