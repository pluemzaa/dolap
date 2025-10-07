nums = input("Enter a series of numbers separated by commas: ")

numbers = nums.split(',')
for i in range(len(numbers)):
    numbers[i] = float(numbers[i]) 

min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")
for x in numbers:
    if max_val != min_val:
        normalized = (x - min_val) / (max_val - min_val)
    else:
        normalized = 0.0  
    print(f"{normalized:.2f}")