nums_input = input("Enter a series of numbers separated by commas: ")
nums =[int(x.strip()) for x in nums_input.split(",")]

min_val = min (nums)
max_val = max (nums)

print("Normalized values:")

if max_val == min_val:
    for _ in nums:
        print (f"{0.00:.2f}")
        
else:
    for x in nums:
        normolized = (x - min_val) / (max_val - min_val)
        print (f"{normolized:.2f}")