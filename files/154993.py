x = input("Enter a series of numbers separated by commas: ").split(',')
x_list = [int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),]
xmin = min(x_list)
xmax = max(x_list)
x0 = x_list[0] == xmax
x1 = x_list[1] == xmax
x2 = x_list[2] == xmax
x3 = x_list[3] == xmax
x4 = x_list[4] == xmax
print(x_list[0],"is the maximum value: ",x0)
print(x_list[1],"is the maximum value: ",x1)
print(x_list[2],"is the maximum value: ",x2)
print(x_list[3],"is the maximum value: ",x3)
print(x_list[4],"is the maximum value: ",x4)