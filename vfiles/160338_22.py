num = input("Enter numbers separated by commas:")
nums = nums.split(",")

i = 0

for i in range (len(num)) :
    nun[i] = int(num[i])

    x = int(input("Enter numbber to search: "))
    indx = 0

    for i in range(len(nums)) :
        if num[i] == x :
            print('Found', x , 'at index' , i)
            indx+1
if indx == 0 :
    print(f"No  {x} found.")