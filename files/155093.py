# Enter the x-coordinate of point 1: 2
# Enter the y-coordinate of point 1: 3
# Enter the x-coordinate of point 2: 5
# Enter the y-coordinate of point 2: 7
# The distance between the two points is: 5.00


def calDistance(x1,y1,x2,y2):
    return (((x2-x1)**2)+((y2-y1)**2))**0.5
    
x1 = int(input("Enter the x-coordinate of point 1: "))
y1 = int(input("Enter the y-coordinate of point 1: "))

x2 = int(input("Enter the x-coordinate of point 2: "))
y2 = int(input("Enter the y-coordinate of point 2: "))

print(f"The distance between the two points is: {calDistance(x1,y1,x2,y2):.2f}")