data_input = input("Enter a series of numbers separated by commas: ")
data = [float(x.strip()) for x in data_input.split(',')]
min_val = min(data)
max_val = max(data)
normalized = [(x - min_val) / (max_val - min_val) for x in data]
print("Normalized values:")
for value in normalized:
    print(f"{value:.2f}")