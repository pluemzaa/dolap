nums = int(input("Enter number:"))
rows = col = nums
i = j  = 0

if nums < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(1, nums+1):
        for j in range(nums):
            n = ((i - 1 + j) % 9 + 1)
            print(n, end=" ") 
        print()