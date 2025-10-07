n = int(input("Enter number:"))
if n < 1 :
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            nums = (i+j+1)
            if nums > 9:
                nums = (nums-1) % 9 + 1
            print(nums,end=" ")
        print()