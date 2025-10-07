num = input('Enter a series of numbers separated by commas:').split(",")
num = [int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4])]

print("Normalized values:")

print((num[0]-min(num))/(max(num)-min(num)))
print((num[1]-min(num))/(max(num)-min(num)))
print((num[2]-min(num))/(max(num)-min(num)))
print((num[3]-min(num))/(max(num)-min(num)))
print((num[4]-min(num))/(max(num)-min(num)))