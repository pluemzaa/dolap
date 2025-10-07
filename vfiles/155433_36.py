num = input("Enter a series of numbers separated by commas:")
numt = num.split(",")

maximum = max(num)

numt0 = int(numt[0])
numt1 = int(numt[1])
numt2 = int(numt[2])
numt3 = int(numt[3])
numt4 = int(numt[4])

numf0 =  (numt[0] is max(num0) in numt)
numf1 =  (numt[1] is max(num1) in numt)
numf2 =  (numt[2] is max(num2) in numt)
numf3 =  (numt[3] is max(num3) in numt)
numf4 =  (numt[4] is max(num4) in numt)

print(numt0, "is the maximum value:", numf0)
print(numt1, "is the maximum value:", numf1)
print(numt2, "is the maximum value:", numf2)
print(numt3, "is the maximum value:", numf3)
print(numt4, "is the maximum value:", numf4)