nums_str = input("Enter numbers separated by commas: ")
nums = []
for num_str_item in nums_str.split(','):
    nums.append(int(num_str_item.strip()))

y = int(input("Enter number to search: "))

found_indices = [] 


for i in range(len(nums)):
    if y == nums[i]:
        found_indices.append(i) 


if found_indices: 
    for index in found_indices:
        print(f"Found {y} at index {index}")
else:
    print(f"No {y} found.")

print("The list of numbers is:", nums)