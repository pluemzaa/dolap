input_nums = input("Enter numbers separated by commas: ")
nums = input_nums.split(",")

for i in range (len(nums)):
    nums[i] = int(nums[i])

search = input("Enter number to search: ")

found = False
for i in range(len(nums)):
    if nums[i] == search:
        print("Found",search ,"at index : ",i)
        found = True
if not found:
    print('No',search,'found')