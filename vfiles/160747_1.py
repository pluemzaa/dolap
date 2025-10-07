input_data = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in 
min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")

if max_val == min_val:
    for num in numbers:
        print("0.00")
else:
    for num in numbers:
        normalized = (num - min_val) / (max_val - min_val)
        print(f"{normalized:.2f}")