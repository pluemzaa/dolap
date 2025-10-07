nums = [int(input(f"Enter number #{i+1}: ")) for i in range(5)]

# หาค่าสูงสุด
maximum = max(nums)

# แสดงผลว่าแต่ละตัวเป็นค่าสูงสุดหรือไม่
[print(f"{n} is the maximum value: {n == maximum}") for n in nums]