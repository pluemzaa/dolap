nums = input("Enter a series of numbers separated by commas: ")
nums = nums.split(",")                     # แยกตัวเลขด้วย comma
nums = [int(n) for n in nums]             # แปลงเป็นจำนวนเต็ม

_min = min(nums)                          # หาค่าต่ำสุด
_max = max(nums)                          # หาค่าสูงสุด

print("Normalized values:")
for n in nums:
    x_scaled = (n - _min) / (_max - _min) if _max != _min else 0.0
    print(f"{x_scaled:.2f}")