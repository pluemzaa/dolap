a = input("Enter a series of numbers separated by commas:")
aList = a.split(",")

aList[0] = int(aList[0])
aList[1] = int(aList[1])
aList[2] = int(aList[2])
aList[3] = int(aList[3])
aList[4] = int(aList[4])

aMax = max(aList)

print(aList[0],"is the maximum value",aList[0] == aMax)
print(aList[1],"is the maximum value",aList[1] == aMax)
print(aList[2],"is the maximum value",aList[2] == aMax)
print(aList[3],"is the maximum value",aList[3] == aMax)
print(aList[4],"is the maximum value",aList[4] == aMax)