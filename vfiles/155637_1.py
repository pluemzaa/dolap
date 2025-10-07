nums = []
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    nums.append(num)

maximum = max(nums)

for n in nums:
    print(f"{n} is maximum: ", n == maximum)