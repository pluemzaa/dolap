data = [] #[[10,20,30] , [1,2,3]]
item = [] # [cat, dog]

lab = input('Enter item 1 :')
item.append(lab)

nums = float(input('Enter weight 1 :'))
data.append(nums)

lab = str(input('Enter item 2 :'))
item.append(lab)

nums = float(input('Enter weight 2 :'))
data.append(nums)

lab = input('Enter item 3 :')
item.append(lab)

nums = float(input('Enter weight 3 :'))
data.append(nums)

lab = input('Enter item 4 :')
item.append(lab)

nums = float(input('Enter weight 4 :'))
data.append(nums)

data[0] = float(data[0])
data[1] = float(data[1])
data[2] = float(data[2])
data[3] = float(data[3])

r0 = data[0]
r1 = data[1]
r2 = data[2]
r3 = data[3]

print (item[0],"           " ,"%.2f" %r0)
print (item[1],"           " ,"%.2f" %r1)
print (item[2],"           " ,"%.2f" %r2)
print (item[3],"           " ,"%.2f" %r3)
print ("--------------------------- ")
print ("total","           ", "%.2f" %(data[0]+data[1]+data[2]+data[3]))