numbers = input("Enter a series of numbers separated by commas: ")
num_list = [float(x.strip()) for x in numbers.split(",")]

min_val = min(num_list)
max_val = max(num_list)

print("Normalized values:")

for x in num_list:
    if max_val != min_val:
        x_scaled = (x - min_val) / (max_val - min_val)
    else:
        x_scaled = 0  # หรืออื่น ๆ ตามต้องการกรณี min = max
    print(f"{x_scaled:.2f}")