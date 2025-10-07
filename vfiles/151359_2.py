input_cost = input("Enter product price: ")
input_point = float(input("Enter your point: "))

discount = input_point/500
calculate_total = float(input_cost)-float(discount) 

print(f"discount is: {discount}")
print(f"Total: {calculate_total} Baht")