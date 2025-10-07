nums = input("Enter numbers separated by commas: ")
nums = nums.split(",")
searchnumber = int(input("Enter number to search: "))
for i in range(0,len(nums)):
    nums[i] = int(nums[i])
for i in range(0,len(nums)):
    if searchnumber == nums[i]:
        print("Found", searchnumber ,"at index", i)    
        break
else:
    print("No", searchnumber , "found.")