num = int(input("Enter a series of numbers separated by commas:"))
numt = num.split(",")

max_x = max(numt)

n0 =  (numt[0] is max(numt) in numt)
n1 =  (numt[1] is max(numt) in numt)
n2 =  (numt[2] is max(numt) in numt)
n3 =  (numt[3] is max(numt) in numt)
n4 =  (numt[4] is max(numt) in numt) 

print(numt0, "is the maximum value:", n0)
print(numt1, "is the maximum value:", n1)
print(numt2, "is the maximum value:", n2)
print(numt3, "is the maximum value:", n3)
print(numt4, "is the maximum value:", n4)