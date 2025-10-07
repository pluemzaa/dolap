x = input("Enter a series of numbers separated by commas:")
x = x.split(",")
x = int(x)


print(x[0],"is the maximum value:",x[0] is max(x))
print(x[1],"is the maximum value:",x[1] is max(x))
print(x[2],"is the maximum value:",x[2] is max(x))
print(x[3],"is the maximum value:",x[3] is max(x))
print(x[4],"is the maximum value:",x[4] is max(x))