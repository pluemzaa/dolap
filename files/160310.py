num = input("Enter numbers separated by commas: ")
num = num.split (",")

find = int(input("Enter number to search:"))

for i in range (0,len(num)) :
    num[i] = int(num[i])

for i in range (0,len(num)) :
    if find == num[i] :
        print ("Found", find , 'at index', i)
        continue
    elif find not in num :
        print ("No", find , "found.")
        break