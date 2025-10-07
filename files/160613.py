input_str  = input("Enter a series of numbers separated by commas:") 

str_list =  input_str.split(',')

numbers = []
for item in str_list:
    numbers.append(float(item))
    
min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")

value_range = max_val - min_val

if value_range == 0:
    for x in numbers:
        print("0.00")
else:
    for x in numbers:
        scaled_value = (x - min_val) / value_range
        print(f"{scaled_value:.2f}")