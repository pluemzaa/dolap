nums=input("Enter numbers separated by commas: ")
nums=nums.split(",")
n=int(input("Enter number to search:  "))
for i in range(len(nums)):
    nums[i]=int(nums[i])
for i in range(len(nums)):
    if n == nums[i]:
        print("Found", n, "at index",i)
    elif n== nums[i]:
        print("Found", n, "at index",i)
        break
print("No",n,"found.")