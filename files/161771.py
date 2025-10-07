num = int(input("Enter number: "))
abc = num
nums = 0
if num<1:
    print("Error number must be 1 or greater")

else:
    for a in range(abc):
        
        for c in range(nums,num):
            print((c%9)+1,end=" ")
        nums += 1
        num += 1
        print()