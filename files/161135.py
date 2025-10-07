user_input = input("Enter a series of numbers separated by commas: ")

numbers = [float(num) for num in user_input.split(',')]

min_num = min(numbers)
max_num = max(numbers)

if max_num - min_num == 0:
    normalized = [0.00 for _ in numbers]
else:
    normalized = [(num - min_num) / (max_num - min_num) for num in numbers]

print("Normalized values :")
for n in normalized:
    print(f"{n:.2f}")