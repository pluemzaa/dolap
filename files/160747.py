user_input = input("Enter a series of numbers separated by commas: ")

num_list = [float(num) for num in user_input.split(',')]


min_val = min(num_list)
max_val = max(num_list)


normalized_values = [(x - min_val) / (max_val - min_val) for x in num_list]
print("Normalized values:")
for value in normalized_values:
    print(f"{value:.2f}")