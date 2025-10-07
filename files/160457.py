num = input("Enter numbers separated by commas: ")
num = num.split(',')
numsearch = int(input("Enter number to search: "))
for i in range(len(num)):
    num[i] = int(num[i])
if numsearch in num:
    for i in range(len(num)):
        if numsearch == num[i]:
            print('Found',numsearch ,'at index',i)     
else:
    print("No",numsearch,"found.")