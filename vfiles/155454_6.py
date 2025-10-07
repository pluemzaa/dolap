x1 = int(input("Enter the x ceordinate of peint 1:"))
y1 = int(input("Enter the y ceordinate of peint 1:"))
x2 = int(input("Enter the x ceordinate of peint 2:"))
y2 = int(input("Enter the y ceordinate of peint 2:"))

import math

slope = (x2-x1)**2+(y2-y1)**2
slope = (math.sqrt(slope))

print("The dlstance between the two points is:%.2f" %slope**0.5)