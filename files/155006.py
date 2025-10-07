num = input('Enter a series of numbers separated by commas:').split(",")
num = [int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4])]


x1 = (num[0]-min(num))/(max(num)-min(num))
x2 = (num[1]-min(num))/(max(num)-min(num))
x3 = (num[2]-min(num))/(max(num)-min(num))
x4 = (num[3]-min(num))/(max(num)-min(num))
x5 = (num[4]-min(num))/(max(num)-min(num))



print("Normalized values:")
print(f"{x1:.2f}")
print(f"{x2:.2f}")
print(f"{x3:.2f}")
print(f"{x4:.2f}")
print(f"{x5:.2f}")