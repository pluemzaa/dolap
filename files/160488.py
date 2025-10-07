i = input("Enter a series of numbers separated by commas: ")
nums = i.split(",")
g = len(nums)
for t in range (g):
    nums[t] = int(nums[t])
    
r = min(nums)
q = max(nums)
    
x_scaled = sum(nums) / g
s = 0
print("Normalized values:")
for t in range (g):
    s = (nums[t] - r) / (q - r)
    print(f'{s:.2f}')