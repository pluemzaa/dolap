nums = int(input("Enter number:"))
i = j = 0
if nums > 0:
    while i < nums:
        j = 0
        while j < nums:
            num = (i + j + 1) % 9
            if num == 0:
                num = 9
            print(num, end=' ')
            j=j+1
        i = i+1
        print()
else:
    print("Error number must be 1 or greater")