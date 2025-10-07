numin = input("Enter a series of numbers separated by commas: ")
nums = numin.split(',')
nums[0] = int(nums[0])
nums[1] = int(nums[1])
nums[2] = int(nums[2])
nums[3] = int(nums[3])


hun = min(nums)
hui = max(nums)
print(hun,hui)

marum = (nums[0] - hun) / (hui - hun)
marum1 = (nums[1] - hun) / (hui - hun)
marum2 = (nums[2] - hun) / (hui - hun)
marum3 = (nums[3] - hun) / (hui - hun)
marum4 = (nums[4] - hun) / (hui - hun)

print("Normalized values:")
print(f"{marum:.2f}")
print(f"{marum1:.2f}")
print(f"{marum2:.2f}")
print(f"{marum3:.2f}")
print(f"{marum4:.2f}")