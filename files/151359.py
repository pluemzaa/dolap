input_cost = input("Enter product price: ")
input_point = float(input("Enter your point: "))

discount = input_point/500
calculate_total = float(input_cost)-float(discount) 

print(f"Discount: {discount:.2f}")
print(f"Total: {calculate_total:.2f} Baht")