nums = int(input("Enter number: "))

if nums < 1:
    print("Error number must be 1 or greater")
else:
    for i in range(nums):
        for j in range(nums):
            value = (i + j + 1) % 9
            if value == 0:
                value = 9
            print(value, end=" ")
        print()