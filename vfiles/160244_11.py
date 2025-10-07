Z = input("Enter a series of numbers separated by commas: ")

numbers = [float(x) for x in Z.split(",")]
x_min= min(numbers)
x_max = max(numbers)

print("Normalized values:")
for num in numbers:
    normalized = (num - x_min) / (x_max - x_min)
    print(f"{normalized:.2f}")