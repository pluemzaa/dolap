nums=input("Enter vector: ")
nums=nums.split(",")
print(nums)
#for i in range(len(nums)):
    #nums[i]=int(nums[i])
nums = [int(x) for x in nums]
print(nums)