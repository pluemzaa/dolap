# รับอินพุตตัวเลขคั่นด้วย ,
input_str = input("Enter a series of numbers separated by commas: ")
numbers = [float(x.strip()) for x in input_str.split(',')]

min_val = min(numbers)
max_val = max(numbers)

print("Normalized values:")
for x in numbers:
    # กรณี max == min ให้ normalized เป็น 0 ทุกค่า (ป้องกันหารศูนย์)
    if max_val == min_val:
        normalized = 0
    else:
        normalized = (x - min_val) / (max_val - min_val)
    print(f"{normalized:.2f}")