input_cost = input("Enter product price: ")
input_point = float(input("Enter your point: "))

discount = input_point/500
calculate_total = float(discount) - float(input_cost)

print(f"Total: {calculate_total} Baht")