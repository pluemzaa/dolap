num = input ("Enter numbers separated by commas: ")
num = num.split (",")
y = int(input("Enter number to search: "))
for i in range(len(num)):
  num[i]=int(num[i])
if y in num:
    for i in range(len(num)):
        if y == num[i]:
            print('Found', y ,'at index', i)
else:
    print('No' ,y, 'found.')