xp = input("Enter a series of numbers separated by commas: ")

x = xp.split(",")

x[0] = int(x[0])
x[1] = int(x[1])
x[2] = int(x[2])
x[3] = int(x[3])
x[4] = int(x[4])
# print(xp)

x_min = min(x)
x_max = max(x)
# print(x)


# print(max(x))
# print(min(x))

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])


x0 = ((x[0] - (x_min)) / ((x_max)-(x_min)))
x1 = ((x[1] - (x_min)) / ((x_max)-(x_min)))
x2 = ((x[2] - (x_min)) / ((x_max)-(x_min)))
x3 = ((x[3] - (x_min)) / ((x_max)-(x_min)))
x4 = ((x[4] - (x_min)) / ((x_max)-(x_min)))


print("Normalized values:")
print("%.2f"%x0)
print("%.2f"%x1)
print("%.2f"%x2)
print("%.2f"%x3)
print("%.2f"%x4)