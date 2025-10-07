nums_x = input("Enter a series of numbers separated by commas: ")
nums_x = nums_x.split(",")
x_scaled = 0
for i in range (len(nums_x)):
    nums_x[i] = int(nums_x[i])
    
Max = max(nums_x)
Min = min(nums_x)

print("Normalized values:")
for i in range(len(nums_x)):
    x_scaled = (nums_x[i]-Min)/(Max-Min)
    print(f"{x_scaled:.2f}")