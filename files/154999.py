a = input("Enter a series of numbers separated by commas:")
aList = a.split(",")

aList[0] = int(aList[0])
aList[1] = int(aList[1])
aList[2] = int(aList[2])
aList[3] = int(aList[3])
aList[4] = int(aList[4])

aMin = min(aList)
aMax = max(aList)

print("Normalized values:")
print("%.2f" %((aList[0] - aMin) / (aMax - aMin)))
print("%.2f" %((aList[1] - aMin) / (aMax - aMin)))
print("%.2f" %((aList[2] - aMin) / (aMax - aMin)))
print("%.2f" %((aList[3] - aMin) / (aMax - aMin)))
print("%.2f" %((aList[4] - aMin) / (aMax - aMin)))