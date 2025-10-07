input_num = input("Enter a series of numbers separated by commas:  ")
inputnum_list = input_num.split(",")
nums = []
i = 0

while i < len(inputnum_list):
    nums.append(int(inputnum_list[i]))
    i = i + 1

min_val= nums[0]
i = 1
while i < len(nums):
    if nums[i] < min_val:
        min_val= nums[i]
    i = i + 1

max_val = nums[0]
i = 1
while i < len(nums):
  if nums[i] > max_val:
      max_val = nums[i]
  i = i + 1
i = 0
print("Normalized values: ")
while i < len(nums):
  sum = (nums[i] - min_val) / (max_val - min_val)
  print(f"{sum:.2f}")
  i = i + 1