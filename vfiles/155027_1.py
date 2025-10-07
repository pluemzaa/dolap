print('Hello Python!')num = input("Enter a series of numbers separated by commas:").split(",")
num = [int(num[0]),int(num[1]),int(num[2]),int(num[3]),int(num[4])]

print(f"{num[0]:} is the maximum value:{num[0] == max(num)}")
print(f"{num[1]:} is the maximum value:{num[1] == max(num)}")
print(f"{num[2]:} is the maximum value:{num[2] == max(num)}")
print(f"{num[3]:} is the maximum value:{num[3] == max(num)}")
print(f"{num[4]:} is the maximum value:{num[4] == max(num)}")