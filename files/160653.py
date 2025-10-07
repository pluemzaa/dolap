user_input = input("Enter a series of numbers separated by commas: ")


numbers = [float(x.strip()) for x in user_input.split(",")]


min_val = min(numbers)
max_val = max(numbers)


if max_val == min_val:
    print("All numbers are the same. Normalized values will be 0.00")
    for _ in numbers:
        print("0.00")
else:
    print("Normalized values:")
    
    for x in numbers:
        normalized = (x - min_val) / (max_val - min_val)
        print(f"{normalized:.2f}")