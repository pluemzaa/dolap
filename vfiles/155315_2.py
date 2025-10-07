print('Hello Python!')import math
def calculae_distance():
"""calculates the distance between two points given their coordinates."""
print("Enter the x-coordinate of point 1: ", end="")
x1=float(input())
print("Enter the y-coordinate of point 1: ", end="")
y1=float(input())

print("Enter the x-coordinate of point 2: ", end="") #corrected prompt for point 2
x2=float(input())
print("Enter the y-coordinate of point 2: ", end="")#corrected prompt for point 2
y2=float(input())
distance = math.sqrt((x2) - x1**2 + (y2 - y1)**2)
print(f"Thedisance between the two point is {distance:.2f}")
if __name__ == "__main__":
calculae_distance()