n = int(input("Enter number:"))
if n <= 0:
    print("Error number must be 1 or greater")
else:
    for i in range(n):
        for j in range(n):
            nums = (i + j + 1) % 9
            if nums == 0:
                nums = 9
            print(nums,end="")
        print()