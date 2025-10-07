i = input("Enter numbers separated by commas: ")
y = int(input("Enter number to search: "))
nums = i.split(",")

for t in range (len(nums)):
    nums[t] = int(nums[t])
    print(nums)
    if y == nums[t]:
        print('Found ', y ,' at index ', t)
    else:
        print(f"No {y} found.")