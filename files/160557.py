nums1 = input("Enter numbers separated by commas: ")
nums = nums1.split(",")
y = input("Enter number to search: ")

    
for i in range(len(nums)):
        if y ==nums[i]:
         print("Found ", y , " at index ", i )
       
       
else :
  print ("No ", y ," found." )