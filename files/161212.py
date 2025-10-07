input_str = input("Enter a series of numbers separated by commas: ")
x = [float(i.strip()) for i in input_str.split(',')]

min_x = min(x)
max_x = max(x)

print("Normalized values:")

if max_x == min_x:
    for i in x:
        print("0.00")
else:
    for i in x:
        x_scaled = (i - min_x) / (max_x - min_x)
        print("{:.2f}".format(x_scaled))