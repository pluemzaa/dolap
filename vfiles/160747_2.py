user_input = input("Enter a series of numbers separated by commas: ")


numbers = [float(num.strip()) for num in 
min_value = min(numbers)
max_value = max(numbers)


scaled_numbers = [(num - min_value) / (max_value - min_value) for num in 
print("Normalized values:")
for num in scaled_numbers:
   print(f"{num:.2f}")