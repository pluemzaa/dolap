input_str = input(”Enter a series of numbers separated by commas: “)
numbers = [float(x.strip()) for x in input_str.split(’,‘)]

min_val = min(numbers)
max_val = max(numbers)

print(”Normalized values:“)
for x in numbers:
    
    if max_val == min_val:
        normalized = 0
    else:
        normalized = (x - min_val) / (max_val - min_val)
    print(f”{normalized:.2f}“)