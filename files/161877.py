nums = int(input("Enter number: "))
if nums < 1:
    print("Error number must be 1 or greater")
for i in range(nums):
    for j in range(nums):
        print(((i+j)%9)+1, end=' ')
    print()