x = input("Enter a series of numbers separated by commas:").split(',')
x_list =[int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4])]
x_min = min(x_list)
x_max = max(x_list)
x1 = x_list[0] == x_max
x2 = x_list[1] == x_max
x3 = x_list[2] == x_max
x4 = x_list[3] == x_max
x5 = x_list[4] == x_max
print(x_list[0],"is the maximum value:", x1 )
print(x_list[1],"is the maximum value:", x2)
print(x_list[2],"is the maximum value:", x3)
print(x_list[3],"is the maximum value:", x4)
print(x_list[4],"is the maximum value:", x5)