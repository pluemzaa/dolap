# enter number:10,20,30
# enter number: 10,20,30,40,50<=59ตัว

nums = input("Enter numbers separated by commas:")
nums = nums.split(",")
# # cast str -> int
# nums[0] = int(nums[0])
# nums[1] = int(nums[1])
# nums[2] = int(nums[2])
i = 0
y=int(input("Enter number to search:"))
for i in range(len(nums)):
    nums[i] = int(nums[i])
    i = i+1

# print(nums)
i = 0
while i in range(len(nums)):
    if y==nums[i]:
        print("found",y, "at index", i)
    i = i+1
else:
    print("No" ,y, "found.")